import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
from PyQt6.QtCore import QUrl
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt6.QtGui import QFont

class QtClient(QWidget):
    def __init__(self):
        super().__init__()

        self.network_manager = QNetworkAccessManager()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Qt Client")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Add modern font
        self.response_text = QTextEdit()
        self.response_text.setReadOnly(True)
        self.response_text.setFont(QFont("Arial", 14))
        layout.addWidget(self.response_text)

        # Use a modern-looking button
        btn_fetch = QPushButton('Fetch Data')
        btn_fetch.setFont(QFont("Arial", 12))
        btn_fetch.clicked.connect(self.fetch_data)
        layout.addWidget(btn_fetch)

        self.setLayout(layout)

    def fetch_data(self):
        url = QUrl("http://127.0.0.1:8000/api/endpoint/")  # Replace with your actual Django API URL
        request = QNetworkRequest(url)
        reply = self.network_manager.get(request)
        reply.finished.connect(self.handle_response)

    def handle_response(self):
        reply = self.sender()
        if reply.error() == QNetworkReply.NetworkError.NoError:
            response = reply.readAll().data().decode()
            self.response_text.setText(response)
        else:
            self.response_text.setText("Error: " + reply.errorString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = QtClient()
    client.show()
    sys.exit(app.exec())

