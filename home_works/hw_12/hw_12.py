import string
from collections import Counter


class CaesarsCipher:
    """Класс, реализующий шифр Цезаря."""

    def __init__(self):
        self.alphabet = string.ascii_letters + string.digits + " !?. "

    def encrypt(self, message: str, key: int) -> str:
        """Шифрует сообщение с помощью шифра Цезаря."""
        if key == 0:
            return message
        encrypted_message = ""
        for char in message:
            if char in self.alphabet:
                index = self.alphabet.index(char)
                shifted_index = (index + key) % len(self.alphabet)
                encrypted_message += self.alphabet[shifted_index]
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt(self, message: str, key: int) -> str:
        """Расшифровывает сообщение, зашифрованное шифром Цезаря."""
        return self.encrypt(message, -key)


def find_key(ciphertext: str) -> int:
    """Находит ключ шифра Цезаря с помощью частотного анализа."""
    cipher = CaesarsCipher()
    alphabet = cipher.alphabet
    letter_counts = Counter(c for c in ciphertext.lower() if c.isalpha())

    if not letter_counts:
        return 0

    most_common = letter_counts.most_common(1)[0][0]
    most_common_index = alphabet.lower().find(most_common)

    best_key = None
    best_score = 0
    for common_letter in "eoaинт":
        index_common = alphabet.lower().find(common_letter)
        key = (index_common - most_common_index) % len(alphabet)
        decrypted = cipher.decrypt(ciphertext, key)
        score = sum(1 for c in decrypted if c.isalpha())
        if score > best_score:
            best_score = score
            best_key = key

    return best_key if best_key is not None else 0


def main():
    ciphertext = "o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D"
    cipher = CaesarsCipher()
    key = find_key(ciphertext)
    decrypted_message = cipher.decrypt(ciphertext, key)

    print(f"Ключ: {key}, расшифровка: {decrypted_message}")
    print(f"Возможно ваш пароль: ['{decrypted_message}']")


if __name__ == "__main__":
    main()
