# Python Digital Clock
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 400, 200)  # Adjusted dimensions for better spacing

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        # Load and apply a digital font
        font_id = QFontDatabase.addApplicationFont("digital-7.ttf")  # Add your digital font file here
        if font_id == -1:
            print("Error loading digital font. Falling back to default font.")
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            digital_font = QFont(font_family, 100)  # Set font size to 100
            self.time_label.setFont(digital_font)

        # Set style
        self.time_label.setStyleSheet("color: hsl(111, 100%, 50%);")  # Green color
        self.setStyleSheet("background-color: black;")

        # Timer for updating the clock
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second

        # Initial time update
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")  # Format for time
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
