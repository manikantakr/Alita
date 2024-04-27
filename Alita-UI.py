import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit
from ai_functions import speak, takecommand, wish, play_youtube, search_google, send_whatsapp_message
from PyQt5.QtCore import Qt

class AIAssistantUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('AI Assistant')
        self.setGeometry(100, 100, 400, 400)

        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("Ask me something...")
        self.text_edit.setReadOnly(True)

        self.btn_listen = QPushButton('Listen', self)
        self.btn_listen.clicked.connect(self.listen)

        # Set button properties
        self.btn_listen.setStyleSheet("""
            QPushButton {
                background-color: blue;
                color: white;
                border-radius: 50px;
                font-size: 18px;
                padding: 20px;
                width: 200px;
                height: 200px;
            }
            QPushButton:hover {
                background-color: darkblue;
            }
        """)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.btn_listen, alignment=Qt.AlignCenter)  # Align button to center

        self.setLayout(layout)

    def listen(self):
        wish()
        while True:
            query = takecommand()
            self.text_edit.append(f"User: {query}")

            if "open notepad" in query:
                speak("Opening Notepad")

            elif "open vs code" in query:
                speak("Opening VS Code")

            elif "open command prompt" in query:
                speak("Opening Command Prompt")

            elif "open camera" in query:
                speak("Opening Camera")

            elif "open youtube" in query:
                speak("What would you like to play?")
                song_query = takecommand()
                speak(f"Playing {song_query} on YouTube")
                play_youtube(song_query)

            elif "search google" in query:
                speak("What would you like to search for?")
                search_query = takecommand()
                search_google(search_query)

            elif "send whatsapp message" in query:
                speak("Say the message you'd like to send")
                message = takecommand()
                send_whatsapp_message(message)

            elif "exit" in query:
                speak("Goodbye Master")
                break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AIAssistantUI()
    window.show()
    sys.exit(app.exec_())