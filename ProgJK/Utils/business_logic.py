import sqlite3
import os
#from Gui.gui1 import Ui_MainWindow
import string

class DatabaseManager:
    def __init__(self):
        # Путь к файлу базы данных
        self.db_name = 'Database\\practic.db'

        # Проверяем существование файла базы данных
        if not os.path.exists(self.db_name):
            raise FileNotFoundError(f"Database file '{self.db_name}' not found")

        # Подключаемся к базе данных
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def get_tasks_count(self, section):
        self.cursor.execute("SELECT COUNT(*) FROM your_table WHERE section = ?", (section,))
        return self.cursor.fetchone()[0]

    def close(self):
        self.connection.close()

class logicButton:
    class logicButtonCreator:
        def deleteBatton(self, N):
            N+=1
        def createButton(self, N):
            N+=1
    class logicButtonCD:
        def varitblC(self, class1):
            if class1 == 1:
                return fCkriptograf.Chesary.encrypt()

        def varitblD(self, class1):
            if class1 == 1:
                return fCkriptograf.Chesary.decrypt()
            if class1 == 2:
                return fCkriptograf.SloganCipher.decrypt()



class fCkriptograf:
    def __init__(self, section):
        self.section = section

    class Chesary:
        @staticmethod
        def encrypt(text, shift):
            shift = int(shift)
            step_by_step = []
            encrypted_text = ""

            for index, char in enumerate(text):
                if char.isalpha():
                    shifted = ord(char) + shift
                    if char.islower():
                        if shifted > ord('z'):
                            shifted -= 26
                        elif shifted < ord('a'):
                            shifted += 26
                    elif char.isupper():
                        if shifted > ord('Z'):
                            shifted -= 26
                        elif shifted < ord('A'):
                            shifted += 26
                    encrypted_text += chr(shifted)
                    step_by_step.append(
                        f"{char} ({ord(char) - ord('a') + 1}) + {shift} -> {chr(shifted)} ({shifted - ord('a') + 1})")
                else:
                    encrypted_text += char
                    step_by_step.append(
                        f"{char} (буква {index + 1}) -> {char} (буква {index + 1})")

            return encrypted_text, step_by_step

        @staticmethod
        def decrypt(text, shift):
            decrypted_text, step_by_step = fCkriptograf.Chesary.encrypt(text, -int(shift))
            return decrypted_text, step_by_step[::-1]

    class SloganCipher:
        def __init__(self, slogan):
            self.slogan = slogan.upper().replace(" ", "")
            self.original_alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        def _shift_alphabet(self):
            shifted_alphabet = []
            seen = set()

            # Добавляем символы из слогана
            for char in self.slogan:
                if char not in seen:
                    shifted_alphabet.append(char)
                    seen.add(char)

            # Добавляем оставшиеся символы алфавита
            for char in self.original_alphabet:
                if char not in seen:
                    shifted_alphabet.append(char)

            return self.original_alphabet, shifted_alphabet

        def _char_position(self, char, alphabet):
            return alphabet.index(char.upper())

        def encrypt(self, text):
            encrypted_text = ""
            slogan_index = 0
            encryption_steps = []
            original_alphabet, shifted_alphabet = self._shift_alphabet()

            for char in text:
                if char.isalpha():
                    base = ord('a') if char.islower() else ord('A')
                    index = original_alphabet.index(char.upper())
                    encrypted_char = shifted_alphabet[index]

                    if char.islower():
                        encrypted_char = encrypted_char.lower()

                    encrypted_text += encrypted_char
                    original_pos = self._char_position(char, original_alphabet)
                    shifted_pos = self._char_position(encrypted_char, original_alphabet)
                    encryption_steps.append(
                        f"{char} (позиция {original_pos}) -> {encrypted_char} (позиция {original_pos})")
                else:
                    encrypted_text += char
                    encryption_steps.append(f"{char} (не изменено)")

            return encrypted_text, encryption_steps, original_alphabet, shifted_alphabet

        def decrypt(self, text):
            decrypted_text = ""
            slogan_index = 0
            decryption_steps = []
            original_alphabet, shifted_alphabet = self._shift_alphabet()

            for char in text:
                if char.isalpha():
                    base = ord('a') if char.islower() else ord('A')
                    index = shifted_alphabet.index(char.upper())
                    decrypted_char = original_alphabet[index]

                    if char.islower():
                        decrypted_char = decrypted_char.lower()

                    decrypted_text += decrypted_char
                    original_pos = self._char_position(char, shifted_alphabet)
                    shifted_pos = self._char_position(decrypted_char, shifted_alphabet)
                    decryption_steps.append(
                        f"{char} (позиция {original_pos}) -> {decrypted_char} (позиция {original_pos})")
                else:
                    decrypted_text += char
                    decryption_steps.append(f"{char} (не изменено)")

            return decrypted_text, decryption_steps, original_alphabet, shifted_alphabet

    class KeywordSubstitutionCipher:
        def __init__(self, key):
            self.key = key.upper()
            self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            self.cipher_alphabet = self.create_cipher_alphabet()

        def create_cipher_alphabet(self):
            """Создает зашифрованный алфавит на основе ключа."""
            key_upper = ''.join(sorted(set(self.key.upper()), key=lambda x: self.key.index(x)))
            remaining_chars = [char for char in self.alphabet if char not in key_upper]
            cipher_alphabet = key_upper + ''.join(remaining_chars)
            return cipher_alphabet

        def encrypt(self, message):
            """Шифрует сообщение."""
            encrypted_message = ''
            steps = []

            for char in message.upper():
                if char in self.alphabet:
                    index = self.alphabet.index(char)
                    new_char = self.cipher_alphabet[index]
                    encrypted_message += new_char
                    steps.append(f"{char} (id: {index}) -> {new_char} (id: {self.cipher_alphabet.index(new_char)})")
                else:
                    encrypted_message += char
                    steps.append(f"{char} (не изменился)")

            return encrypted_message, steps, self.cipher_alphabet

        def decrypt(self, encrypted_message):
            """Расшифровывает сообщение."""
            decrypted_message = ''
            steps = []

            for char in encrypted_message.upper():
                if char in self.cipher_alphabet:
                    index = self.cipher_alphabet.index(char)
                    new_char = self.alphabet[index]
                    decrypted_message += new_char
                    steps.append(f"{char} (id: {index}) -> {new_char} (id: {self.alphabet.index(new_char)})")
                else:
                    decrypted_message += char
                    steps.append(f"{char} (не изменился)")

            return decrypted_message, steps, self.cipher_alphabet
        

    class TrisemusCipher:
        def __init__(self, key):
            self.key = key
            self.alphabet = string.ascii_lowercase.replace('j', '')  # Alphabet without 'j'
            self.trisemus_table = self._create_trisemus_table()

        def _create_trisemus_table(self):
            # Remove duplicates from key while preserving order
            seen = set()
            key_unique = ''.join([ch for ch in self.key if not (ch in seen or seen.add(ch))])

            # Create the table using key and remaining letters of the alphabet
            combined = key_unique + ''.join([ch for ch in self.alphabet if ch not in key_unique])

            # Create 5x5 table
            table = [combined[i:i + 5] for i in range(0, len(combined), 5)]
            return table

        def _find_position(self, char):
            for row_idx, row in enumerate(self.trisemus_table):
                if char in row:
                    col_idx = row.index(char)
                    return (row_idx, col_idx)
            return None

        def encrypt(self, plaintext):
            plaintext = plaintext.replace('j', 'i')  # Replace 'j' with 'i'
            encrypted_text = ''
            encryption_steps = []
            for char in plaintext:
                pos = self._find_position(char)
                if pos:
                    row, col = pos
                    new_char = self.trisemus_table[(row + 1) % 5][col]  # Shift down in the table
                    encrypted_text += new_char
                    encryption_steps.append(f'{char} -> {new_char}')
                else:
                    encrypted_text += char  # Non-alphabet characters remain unchanged
                    encryption_steps.append(f'{char} (unchanged)')
            return encrypted_text, encryption_steps, self.trisemus_table

        def decrypt(self, ciphertext):
            decrypted_text = ''
            decryption_steps = []
            for char in ciphertext:
                pos = self._find_position(char)
                if pos:
                    row, col = pos
                    new_char = self.trisemus_table[(row - 1) % 5][col]  # Shift up in the table
                    decrypted_text += new_char
                    decryption_steps.append(f'{char} -> {new_char}')
                else:
                    decrypted_text += char  # Non-alphabet characters remain unchanged
                    decryption_steps.append(f'{char} (unchanged)')
            return decrypted_text, decryption_steps, self.trisemus_table

