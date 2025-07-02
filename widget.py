# This Python file uses the following encoding: utf-8
import sys
import serial
import time
import struct
import csv

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtGui import QFont
from PySide6.QtCore import QObject, QThread, Signal, Slot


class FileSendWorker(QObject):
    line_processed = Signal(str)
    finished = Signal()

    def __init__(self, ser, file_path):
        super().__init__()
        self.ser = ser
        self.file_path = file_path

    @Slot()
    def run(self):
        try:
            with open(self.file_path, 'r') as infile:
                reader = csv.reader(infile)
                for line_num, row in enumerate(reader, start=1):
                    if len(row) < 140:
                        self.line_processed.emit(f"[WARN] Line {line_num}: Too few values. Skipping.")
                        continue

                    float_values = [float(val) for val in row[:140]]
                    for val in float_values:
                        packet = struct.pack('<f', val)
                        self.ser.write(packet)
                        time.sleep(0.001)

                    self.ser.flush()
                    response = self.ser.readline().decode(errors='ignore').strip()
                    self.line_processed.emit(f"[RX] Line {line_num}: {response}")
                    time.sleep(0.05)
        except Exception as ex:
            self.line_processed.emit(f"[ERROR] Failed: {ex}")
        self.finished.emit()


class ReadWorker(QObject):
    line_received = Signal(str)
    finished = Signal()

    def __init__(self, ser):
        super().__init__()
        self.ser = ser
        self._running = True

    @Slot()
    def run(self):
        buffer = ""
        try:
            while self._running:
                if self.ser.in_waiting:
                    data = self.ser.read(self.ser.in_waiting)
                    buffer += data.decode(errors='ignore')

                    lines = buffer.replace('\r\n', '\n').replace('\r', '\n').split('\n')

                    for line in lines[:-1]:
                        self.line_received.emit(line.strip())
                    buffer = lines[-1]  # partial line remains

                time.sleep(0.05)
        except Exception as ex:
            self.line_received.emit(f"[ERROR] ReadWorker exception: {ex}")
        self.finished.emit()

    def stop(self):
        self._running = False


class SendBinaryWorker(QObject):
    finished = Signal()
    error = Signal(str)
    success = Signal(str)

    def __init__(self, ser, byte_values):
        super().__init__()
        self.ser = ser
        self.byte_values = byte_values

    @Slot()
    def run(self):
        try:
            # Validate values
            for b in self.byte_values:
                if not 0 <= b <= 255:
                    raise ValueError(f"Value {b} out of uint8_t range")

            byte_array = bytes(self.byte_values)
            self.ser.write(byte_array)
            self.success.emit(f"[TX] Sent {len(byte_array)} bytes (uint8_t) from GUI input")
        except Exception as ex:
            self.error.emit(f"[ERROR] Invalid uint8_t input: {ex}")
        self.finished.emit()


# You need to run this command beforehand to generate ui_form.py from your .ui file:
# pyside6-uic form.ui -o ui_form.py
from ui_form import Ui_Widget


class COMPort(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.port, self.baudrate = self.get_serial_params()

        self.ser = None
        self.read_thread = None
        self.read_worker = None
        self.send_thread = None
        self.send_worker = None

        font = QFont("Consolas", 18, QFont.Bold)
        self.ui.plainTextEditReport.setFont(font)
        self.ui.plainTextEditReport.setStyleSheet("background-color: black; color: white;")

        self.ui.sendStart.clicked.connect(self.start)
        self.ui.sendStop.clicked.connect(self.stop)
        self.ui.pushClear.clicked.connect(self.clear)
        self.ui.sendBinary.clicked.connect(self.send_binary)
        self.ui.sendFileButton.clicked.connect(self.on_sendFileButton_clicked)
        self.ui.pushEcho.clicked.connect(self.echo)
        self.ui.pushSave.clicked.connect(self.save)

    def get_serial_params(self):
        port = self.ui.comboPortNumber.currentText().strip()
        baud = int(self.ui.comboBaud.currentText().strip())
        return port, baud

    def open_serial_port(self):
        if self.ser and self.ser.is_open:
            return  # already open
        try:
            self.port, self.baudrate = self.get_serial_params()
            self.ser = serial.Serial(self.port, self.baudrate, timeout=0.1)
            time.sleep(2)  # wait for port stabilization
            self.ser.reset_input_buffer()
            self.ui.plainTextEditReport.appendPlainText(f"[OK] Serial port {self.port} opened at {self.baudrate} baud.")
        except Exception as ex:
            self.ui.plainTextEditReport.appendPlainText(f"[ERROR] Failed to open serial port: {ex}")
            self.ser = None

    def close_serial_port(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            self.ui.plainTextEditReport.appendPlainText("[INFO] Serial port closed.")
            self.ser = None

    def start(self):
        if self.read_worker is not None:
            self.ui.plainTextEditReport.appendPlainText("[INFO] Already reading.")
            return

        self.open_serial_port()
        if not self.ser:
            return

        self.read_worker = ReadWorker(self.ser)
        self.read_thread = QThread()
        self.read_worker.moveToThread(self.read_thread)

        self.read_worker.line_received.connect(self.ui.plainTextEditReport.appendPlainText)
        self.read_worker.finished.connect(self.read_thread.quit)
        self.read_worker.finished.connect(self.read_worker.deleteLater)
        self.read_thread.finished.connect(self.read_thread.deleteLater)

        self.read_thread.started.connect(self.read_worker.run)
        self.read_thread.start()

        self.ui.plainTextEditReport.appendPlainText("[OK] Started reading...")

    def stop(self):
        if self.read_worker:
            self.read_worker.stop()
            self.read_worker = None
            self.ui.plainTextEditReport.appendPlainText("[OK] Reading stopped.")
        else:
            self.ui.plainTextEditReport.appendPlainText("[INFO] Not currently reading.")

        # Note: do NOT close the serial port here so you can keep sending!

    def clear(self):
        self.ui.plainTextEditReport.clear()

    def send_binary(self):
        text = self.ui.lineEdit.text()
        str_values = text.strip().split()

        try:
            byte_values = [int(val) for val in str_values]
        except Exception as ex:
            self.ui.plainTextEditReport.appendPlainText(f"[ERROR] Invalid input: {ex}")
            return

        self.open_serial_port()
        if not self.ser:
            return

        # If a send is already running, ignore or notify user
        if self.send_worker is not None:
            self.ui.plainTextEditReport.appendPlainText("[INFO] Send in progress, please wait.")
            return

        self.send_worker = SendBinaryWorker(self.ser, byte_values)
        self.send_thread = QThread()
        self.send_worker.moveToThread(self.send_thread)

        self.send_worker.success.connect(self.ui.plainTextEditReport.appendPlainText)
        self.send_worker.error.connect(self.ui.plainTextEditReport.appendPlainText)
        self.send_worker.finished.connect(self.send_thread.quit)
        self.send_worker.finished.connect(self.send_worker.deleteLater)
        self.send_thread.finished.connect(self.send_thread.deleteLater)

        def cleanup():
            self.send_worker = None
            self.send_thread = None

        self.send_thread.finished.connect(cleanup)
        self.send_thread.started.connect(self.send_worker.run)
        self.send_thread.start()

    def on_sendFileButton_clicked(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Input File",
            "",
            "CSV Files (*.csv);;Text Files (*.txt);;All Files (*)"
        )

        if not file_path:
            return

        self.open_serial_port()
        if not self.ser:
            self.ui.plainTextEditReport.appendPlainText("[ERROR] Serial port not open.")
            return

        self.worker = FileSendWorker(self.ser, file_path)
        self.thread = QThread()
        self.worker.moveToThread(self.thread)

        self.worker.line_processed.connect(self.ui.plainTextEditReport.appendPlainText)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.started.connect(self.worker.run)
        self.thread.start()

    def echo(self):
        self.open_serial_port()
        if not self.ser:
            return

        try:
            report_text = self.ui.plainTextEditReport.toPlainText()
            lines = report_text.splitlines()
            for line in lines:
                line_bytes = (line + '\r\n').encode('utf-8')
                self.ser.write(line_bytes)
                time.sleep(0.01)

            self.ui.plainTextEditReport.appendPlainText(f"[TX] Echoed {len(lines)} lines.")

        except Exception as ex:
            self.ui.plainTextEditReport.appendPlainText(f"[ERROR] Failed to echo: {ex}")

    def save(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Report",
            "",
            "Text Files (*.txt);;All Files (*)"
        )

        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.ui.plainTextEditReport.toPlainText())
                self.ui.plainTextEditReport.appendPlainText(f"[OK] Report saved to: {file_path}")
            except Exception as e:
                self.ui.plainTextEditReport.appendPlainText(f"[ERROR] Failed to save: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = COMPort()
    widget.show()
    sys.exit(app.exec())
