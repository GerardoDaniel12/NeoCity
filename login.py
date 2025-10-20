import sys
import json
import os
from PyQt5 import QtWidgets, QtGui, QtCore

USERS_FILE = "neocity_users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

class AnimatedButton(QtWidgets.QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.default_style = """border-radius:8px; padding:6px; font-weight:600; background: rgba(0,255,234,0.95); color: #000; transition: 0.3s;"""
        self.hover_style = """border-radius:8px; padding:6px; font-weight:600; background: #00ffe5; color: #000; box-shadow: 0 0 10px #00ffe5;"""
        self.setStyleSheet(self.default_style)

    def enterEvent(self, event):
        self.setStyleSheet(self.hover_style)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet(self.default_style)
        super().leaveEvent(event)

class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Neocity – Iniciar sesión / Registro")
        self.setFixedSize(500, 350)
        self.users = load_users()
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                    stop:0 #0f0c29, stop:0.5 #302b63, stop:1 #24243e
                );
            }
            QLabel {
                color: white;
                font-weight: bold;
            }
        """)
        layout = QtWidgets.QVBoxLayout()
        title = QtWidgets.QLabel("NEOCITY")
        title.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont("Daydream", 32, QtGui.QFont.Bold)
        title.setFont(font)
        title.setStyleSheet("color: #00ffea;")
        layout.addWidget(title)

        form_widget = QtWidgets.QWidget()
        form_layout = QtWidgets.QFormLayout()
        form_layout.setLabelAlignment(QtCore.Qt.AlignRight)

        self.email_input = QtWidgets.QLineEdit()
        self.email_input.setPlaceholderText("Correo electrónico")
        self.email_input.setFixedHeight(30)
        self.email_input.setStyleSheet("border-radius:6px; padding:6px; background: rgba(255,255,255,0.9);")

        self.pass_input = QtWidgets.QLineEdit()
        self.pass_input.setPlaceholderText("Contraseña")
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_input.setFixedHeight(30)
        self.pass_input.setStyleSheet("border-radius:6px; padding:6px; background: rgba(255,255,255,0.9);")

        self.role_combo = QtWidgets.QComboBox()
        self.role_combo.addItems(["Usuario", "Administrador"])
        self.role_combo.setFixedHeight(30)
        self.role_combo.setStyleSheet("border-radius:6px; padding:6px; background: rgba(255,255,255,0.9);")

        form_layout.addRow(QtWidgets.QLabel("Correo:"), self.email_input)
        form_layout.addRow(QtWidgets.QLabel("Contraseña:"), self.pass_input)
        form_layout.addRow(QtWidgets.QLabel("Rol:"), self.role_combo)
        form_widget.setLayout(form_layout)
        layout.addWidget(form_widget)

        btn_layout = QtWidgets.QHBoxLayout()
        self.login_btn = AnimatedButton("Iniciar sesión")
        self.register_btn = AnimatedButton("Registrarse")
        for btn in (self.login_btn, self.register_btn):
            btn.setFixedHeight(36)
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        btn_layout.addStretch()
        btn_layout.addWidget(self.login_btn)
        btn_layout.addWidget(self.register_btn)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        self.setLayout(layout)
        self.login_btn.clicked.connect(self.check_login)
        self.register_btn.clicked.connect(self.register_account)

    def check_login(self):
        email = self.email_input.text().strip()
        password = self.pass_input.text()
        role = self.role_combo.currentText()
        if not email:
            QtWidgets.QMessageBox.warning(self, "Error", "Ingresa un correo electrónico")
            return
        if email not in self.users:
            QtWidgets.QMessageBox.critical(self, "Error", "Correo no registrado")
            return
        entry = self.users[email]
        if entry["password"] != password or entry["role"] != role:
            QtWidgets.QMessageBox.critical(self, "Error", "Credenciales incorrectas o rol no coincide")
            return
        QtWidgets.QMessageBox.information(self, "Bienvenido", f"Bienvenido {role} a Neocity, {email}")

    def register_account(self):
        email = self.email_input.text().strip()
        password = self.pass_input.text()
        role = self.role_combo.currentText()
        if not email or not password:
            QtWidgets.QMessageBox.warning(self, "Error", "Correo y contraseña son requeridos para registrarse")
            return
        if email in self.users:
            QtWidgets.QMessageBox.critical(self, "Error", "El correo ya está registrado")
            return
        self.users[email] = {"password": password, "role": role}
        save_users(self.users)
        QtWidgets.QMessageBox.information(self, "Registro exitoso", f"Se ha registrado el {role} {email}")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
