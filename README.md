# Описание
Программа реализует шифр Плейфера с использованием заданного ключа.

# Запуск программы
Скачиваем файлы с  кодом.

Запускаем программу:

python playfair_cipher.py

# Тестирование программы
Для запуска юнит-тестов выполняем следующую команду:

python -m unittest test_playfair_cipher.py

# Примечание
В файле playfair_cipher.py можно изменить значение переменной key и текст для шифрования.

cipher = PlayfairCipher("YOUR_KEY")
encrypted_text = cipher.encrypt("YOUR_TEXT")
print(f"Encrypted: {encrypted_text}")
decrypted_text = cipher.decrypt(encrypted_text)
print(f"Decrypted: {decrypted_text}")