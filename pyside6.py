import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QMessageBox
from PySide6.QtGui import QFont
from PySide6.QtCore import QSize

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Masukkan detail Anda:")
        self.label.setFont(QFont('Arial'))

        self.input_nama = QLineEdit()
        self.input_nama.setFont(QFont('Arial'))
        self.input_nama.setPlaceholderText("Nama")

        self.input_nim = QLineEdit()
        self.input_nim.setFont(QFont('Arial'))
        self.input_nim.setPlaceholderText("NIM")

        self.input_hobi = QLineEdit()
        self.input_hobi.setFont(QFont('Arial'))
        self.input_hobi.setPlaceholderText("Hobi")

        self.button = QPushButton("Kirim")
        self.button.setFont(QFont('Arial'))

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input_nama)
        self.layout.addWidget(self.input_nim)
        self.layout.addWidget(self.input_hobi)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.display_data)
        self.button.setStyleSheet("background-color: #82E0AA ;")

    def display_data(self):
        nama = self.input_nama.text()
        nim = self.input_nim.text()
        hobi = self.input_hobi.text()

        self.label.setText(f"Halo, {nama}!\nNIM Anda adalah {nim}\ndan hobi Anda adalah {hobi}.")
   
    def reset_data(self):
        self.input_nama.clear()
        self.input_nim.clear()
        self.input_hobiclear()
        self.label.setText("Masukkan detail Anda:")
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikasi Input Detail")
        
        self.widget = CustomWidget()
        self.setCentralWidget(self.widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

