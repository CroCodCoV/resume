import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Gui.gui2 import Ui_MainWindow
from Utils.business_logic import *

# cipher = fCkriptograf.Chesary
# encrypted_text, encryption_steps = cipher.encrypt("Hello, World!", 7)
# print("Зашифрованный текст:", encrypted_text)
# print("Шаги шифрования:")
# for step in encryption_steps:
#     print(step)
#
# cipher = fCkriptograf.SloganPrimesusCipher("PYTHON")
# encrypted_text, encryption_steps = cipher.encrypt("Hello, World!")
# print("Зашифрованный текст:", encrypted_text)
# print("Шаги шифрования:")
# for step in encryption_steps:
#     print(step)
#
# decrypted_text, decryption_steps = cipher.decrypt(encrypted_text)
# print("\nРасшифрованный текст:", decrypted_text)
# print("Шаги дешифрования:")
# for step in decryption_steps:
#     print(step)
#
# cipher = fCkriptograf.KeywordSubstitutionCipher("PYTHON")
# encrypted_text, encryption_steps = cipher.encrypt("Hello, World!")
# print("Зашифрованный текст:", encrypted_text)
# print("Шаги шифрования:")
# for step in encryption_steps:
#     print(step)
#
# decrypted_text, decryption_steps = cipher.decrypt(encrypted_text)
# print("\nРасшифрованный текст:", decrypted_text)
# print("Шаги дешифрования:")
# for step in decryption_steps:
#     print(step)
#
# cipher = fCkriptograf.SloganCipher("PYTHON")
# encrypted_text, encryption_steps = cipher.encrypt("Hello, World!")
# print("Зашифрованный текст:", encrypted_text)
# print("Шаги шифрования:")
# for step in encryption_steps:
#     print(step)
#
# decrypted_text, decryption_steps = cipher.decrypt(encrypted_text)
# print("\nРасшифрованный текст:", decrypted_text)
# print("Шаги дешифрования:")
# for step in decryption_steps:
#     print(step)
# print(fCkriptograf.SloganCipher_EN("marmint").encrypt("qwertyuiopasdfghjklzxcvbnm"))
# print(fCkriptograf.SloganCipher_EN("marmint").decrypt(fCkriptograf.SloganCipher_EN("marmint").encrypt("qwertyuiopasdfghjklzxcvbnm")))
#
# print(fCkriptograf.SloganCipher_Ru("ткде").encrypt("Привет мир"))
# print(fCkriptograf.SloganCipher_Ru("ткде").decrypt(fCkriptograf.SloganCipher_Ru("ткде").encrypt("Привет мир")))
#
# cipher = fCkriptograf.KeywordSubstitutionCipher("asdfsdfe", 1)
# message = "1234567890qwertyuiopasdfghjklzxcvbnm=-+/.,"
# encrypted_message1 = cipher.encrypt(message)
# print(encrypted_message1)
#
# decrypted_message = cipher.decrypt(encrypted_message1)
# print(decrypted_message)
#
# cipher = fCkriptograf.KeywordSubstitutionCipher("vfrf", 1)
# message = "dfghjklp[ASDFGHJK][][["
# encrypted_message = cipher.encrypt(message)
# print(encrypted_message)
#
# decrypted_message = cipher.decrypt(encrypted_message)
# print(decrypted_message)
#
# print(list(ord(i) for i in decrypted_message))

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow(self)
        #self.ui.setupUi(self)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())


