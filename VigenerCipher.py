######################################################################################################
# Title: Vigener Cipher                                                                              #
# Author: Allori(Влад)                                                                               #
# Github : https://github.com/Allorion                                                               #
######################################################################################################

class VisionEncryption:

    def __init__(self):
        # Создаем русский алфавит
        self.alphabet = {
            "А": 0,
            "Б": 1,
            "В": 2,
            "Г": 3,
            "Д": 4,
            "Е": 5,
            "Ё": 6,
            "Ж": 7,
            "З": 8,
            "И": 9,
            "Й": 10,
            "К": 11,
            "Л": 12,
            "М": 13,
            "Н": 14,
            "О": 15,
            "П": 16,
            "Р": 17,
            "С": 18,
            "Т": 19,
            "У": 20,
            "Ф": 21,
            "Х": 22,
            "Ц": 23,
            "Ч": 24,
            "Ш": 25,
            "Щ": 26,
            "Ъ": 27,
            "Ы": 28,
            "Ь": 29,
            "Э": 30,
            "Ю": 31,
            "Я": 32,
        }

    # Шифрование текста
    def encryption(self, key, originalMessage):
        keyQuantity = int((len(originalMessage) / len(key)) + 1)  # Получаем количество удлинений ключа
        key = (key * keyQuantity)  # Удлиняем ключ
        encryptedText = ''  # Создаем переменную для зашифрованного текста
        for i in range(len(originalMessage)):  # Создаем цикл для зашифровки каждой буквы
            # Обрабатываем наличие символов не входящих в алфавит
            if originalMessage[i] == ' ' or originalMessage[i] == ',' or originalMessage[i] == '.' or originalMessage[
                i] == '-':
                encryptedText += originalMessage[i]  # Добавляем символ в текст
            else:
                c = self.alphabet[originalMessage[i]] + self.alphabet[
                    key[i]]  # Используя формулу с порядковыми номерами
                # букв C = P + K, где С - зашифрованная буква, P - исходная буква, K - буква ключа
                if c >= len(self.alphabet):  # Если число превышает количество букв в алфавите
                    c -= len(
                        self.alphabet)  # Отнимаем от получившегося числа зашифрованной буквы количество букв алфавита
                for key2, values in self.alphabet.items():  # Получаем ключ и значение алфавита
                    if values == c:  # Проверяем на соответствие значения алфавита (числа), значение совпадает идем дальше
                        encryptedText = encryptedText + key2  # Получаем его ключ (букву) прибавляем ее к строке шифр.текста
        return encryptedText  # Возвращаем зашифрованный текст

    # Расшифровка текста
    def decryption(self, key, encryptedText):
        keyQuantity = int((len(encryptedText) / len(key)) + 1)  # Получаем количество удлинений ключа
        key = (key * keyQuantity)  # Удлиняем ключ
        originalMessage = ''  # Создаем переменную для расшифрованного текста
        for i in range(len(encryptedText)):  # Создаем цикл для расшифровки каждой буквы
            # Обрабатываем наличие символов не входящих в алфавит
            if encryptedText[i] == ' ' or encryptedText[i] == ',' or encryptedText[i] == '.' or encryptedText[i] == '-':
                originalMessage += encryptedText[i]  # Добавляем символ в текст
            else:
                p = self.alphabet[encryptedText[i]] - self.alphabet[key[i]]  # Используя формулу с порядковыми номерами
                # букв P = (C - K + A), где P - расшифрованная буква, K - буква ключа, А - количество букв в алфавите
                if p < 0:  # Создаем условие, если число расшифрованной буквы меньше 0
                    p += len(self.alphabet)  # Прибавляем количество символов алфавита
                for key2, values in self.alphabet.items():  # Получаем ключ и значение алфавита
                    if values == p:  # Проверяем на соответствие значения алфавита (числа), значение совпадает идем дальше
                        originalMessage = originalMessage + key2  # Получаем его ключ (букву) прибавляем ее к строке текста
        return originalMessage  # Возвращаем расшифрованный текст


if __name__ == "__main__":
    try:  # Обработка ошибок (если ошибки нет)
        print('''
            ██╗░░░██╗██╗░██████╗░███████╗███╗░░██╗███████╗██████╗░  ░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
            ██║░░░██║██║██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗  ██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
            ╚██╗░██╔╝██║██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝  ██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
            ░╚████╔╝░██║██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗  ██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
            ░░╚██╔╝░░██║╚██████╔╝███████╗██║░╚███║███████╗██║░░██║  ╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
            ░░░╚═╝░░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝  ░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

            ██████╗░██╗░░░██╗  ░█████╗░██╗░░░░░██╗░░░░░░█████╗░██████╗░██╗
            ██╔══██╗╚██╗░██╔╝  ██╔══██╗██║░░░░░██║░░░░░██╔══██╗██╔══██╗██║
            ██████╦╝░╚████╔╝░  ███████║██║░░░░░██║░░░░░██║░░██║██████╔╝██║
            ██╔══██╗░░╚██╔╝░░  ██╔══██║██║░░░░░██║░░░░░██║░░██║██╔══██╗██║
            ██████╦╝░░░██║░░░  ██║░░██║███████╗███████╗╚█████╔╝██║░░██║██║
            ╚═════╝░░░░╚═╝░░░  ╚═╝░░╚═╝╚══════╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝
        ''')
        c = VisionEncryption()  # Вызываем класс программы
        while True:  # Создаем бесконечный цикл, чтобы программа не закрывалась после выполнения
            choiceUser = int(input('Выберите действие:'
                                   '\n1. Зашифровать текст\n'
                                   '2. Дешифровка текста\n'))
            if choiceUser == 1:  # Зашифровка текста
                key = input('Введите ключ: ').upper()
                originalMessage = input('Введите текст для зашифровки: ').upper()
                print(f'Зашифрованный текст: {c.encryption(key, originalMessage)} : ключ: {key}')
            elif choiceUser == 2:  # Расшифровка текста
                key = input('Введите ключ: ').upper()
                encryptedText = input('Введите зашифрованный текст: ').upper()
                print(f"Расшифрованный текст: {c.decryption(key, encryptedText)}")
            else:  # Если ввели не верные данные
                print('Вы ввели не верный выбор')
    except:  # Если ошибка
        print('Вы сделали что-то не то, попробуйте заново')
