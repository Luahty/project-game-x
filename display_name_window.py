import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton, QVBoxLayout, QWidget, QWidget, QColorDialog, QFontDialog

class WidgetPropertiesApp (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hiển thị tên")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.edit = QLineEdit()
        self.button = QPushButton("Hiển thị")
        self.label = QLabel()
    
        layout = QVBoxLayout()
    
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
    
        central_widget.setLayout(layout)
    
        self.button.clicked.connect(self.display_text)

    def display_text(self):
        text = self.edit.text()
        self.label.setText(f'Tên của bạn là: {text}')
        
def main():

    app = QApplication(sys.argv)
    window = WidgetPropertiesApp()
    window.show()
    sys.exit(app.exec_())
    
if __name__=="__main__":
    main()