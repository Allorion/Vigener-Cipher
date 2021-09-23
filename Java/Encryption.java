public class Encryption {
    String[] alphabet;

    Encryption(String[] importAlphabet) {
        alphabet = importAlphabet;
    }

    // Шифрование текста
    void encryption(String key, String unencryptedText) {
        // Передаем переменные классу обработки текста и ключа
        ArrayPositionLetter classArrayPositionLetter = new ArrayPositionLetter(unencryptedText, alphabet, key);
        int[][] arrayPositionLetter = classArrayPositionLetter.startArrayPositionLetter(); // Получаем масивы ключ. текст
        int[] arrayPositionLetterUnencryptedText = arrayPositionLetter[0]; // Получаем масив номеров букв текста
        int[] arrayPositionLetterKey = arrayPositionLetter[1]; // Получаем масив номеров букв ключа

        StringBuilder encryptedText = new StringBuilder(); // Создаем переменную для зашифр. текста
        for (int i = 0; i < arrayPositionLetterUnencryptedText.length; i++) { // Создаем цикл создания шифр. текста
            int c = arrayPositionLetterUnencryptedText[i] + arrayPositionLetterKey[i]; // Используя формулу с
                // порядковыми номерами букв C = P + K, где С - зашифрованная буква, P - исходная буква, K - буква ключа
            if (c >= alphabet.length) { // Если число превышает количество букв в алфавите
                c -= alphabet.length; // Отнимаем от получившегося числа зашифрованной буквы количество букв алфавита
            }
            encryptedText.append(alphabet[c]); // Добавляем букву в конец строки зашифрованного тектса
        }
        System.out.println("Зашифрованный текст: " + encryptedText + " - ключ " + key); // Выводим зашифрованный текст
    }
}
