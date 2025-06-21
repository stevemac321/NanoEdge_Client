# This Python file uses the following encoding: utf-8
import sys
import json
import requests
import pandas as pd
import numpy as np
import random
import serial
import struct
import time

from PySide6.QtWidgets import QApplication, QWidget

# You need to run this command beforehand to generate ui_form.py from your .ui file:
# pyside6-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class EKGSimulator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.port = "COM4"
        self.baudrate = 115200

        # Connect buttons to functions
        self.ui.sendNormal.clicked.connect(self.send_ekg_normal_data)
        self.ui.sendAnom.clicked.connect(self.send_ekg_anom_data)
        self.ui.pushClear.clicked.connect(self.clear)

        # Load ECG data once
        self.load_data()

    def clear(self):
         self.ui.plainTextEditReport.clear()

    def load_data(self):
        regular_df = pd.read_csv('c:/repos/EKG/signals/regular.csv', header=None)
        anomaly_df = pd.read_csv('c:/repos/EKG/signals/anomaly.csv', header=None)

        self.normal_signals = regular_df.values.astype(np.float32)
        self.anomaly_signals = anomaly_df.values.astype(np.float32)

        print("Loaded", self.normal_signals.shape[0], "normal signals.")
        print("Loaded", self.anomaly_signals.shape[0], "anomaly signals.")

    def send_ekg_normal_data(self):
        if len(self.normal_signals) == 0:
            print("No normal signals loaded.")
            return
        sample = random.choice(self.normal_signals).tolist()
        self.send_sample(sample)

    def send_ekg_anom_data(self):
        if len(self.anomaly_signals) == 0:
            print("No anomaly signals loaded.")
            return
        sample = random.choice(self.anomaly_signals).tolist()
        self.send_sample(sample)

    def send_sample(self, sample):

        self.port = self.ui.comboPortNumber.currentText()
        self.baudrate = self.ui.comboBaud.currentText()
        self.send_and_hold_open(sample)

    #------------------------------------------------------------------
    def send_and_hold_open(self, sample):

        ser = serial.Serial(self.port, self.baudrate, timeout=None)
        time.sleep(2)  # Let MCU settle

        ser.reset_input_buffer()
        ser.reset_output_buffer()

        # Send one float at a time (4 bytes each)
        for i, val in enumerate(sample):
            b = struct.pack('<f', val)
            ser.write(b)
            ser.flush()
            time.sleep(0.001)  # slight delay (1ms) to help MCU keep up

        try:
            while True:
                if ser.in_waiting >= 2:
                    response = ser.read(2)
                    self.ui.plainTextEditReport.appendPlainText("[OK] All floats sent. Port is held open.")
                    self.ui.plainTextEditReport.appendPlainText(f"Report bytes: {response[0]:02X} {response[1]:02X}")
                    self.ui.plainTextEditReport.appendPlainText(f"Status: {response[0]}")
                    self.ui.plainTextEditReport.appendPlainText(f"Similarity: {response[1]}")
                    break
                time.sleep(0.05)

        except KeyboardInterrupt:
            print("[ERROR] Interrupted.")

        finally:
            ser.close()
            print("[OK]Port closed.")

        lines = []
        line = ""
        for i, val in enumerate(sample):
            line += f"{val:8.3f} "
            if (i + 1) % 6 == 0:
               lines.append(line.rstrip())
               line = ""
        if line:
            lines.append(line.rstrip())

        self.ui.plainTextEditReport.appendPlainText("\n".join(lines))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = EKGSimulator()
    widget.show()
    sys.exit(app.exec())
