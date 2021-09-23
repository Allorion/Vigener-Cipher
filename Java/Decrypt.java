public class Decrypt {
    String[] alphabet;

    Decrypt(String[] importAlphabet) {
        alphabet = importAlphabet;
    }

    // Дешифровка текста
    void decrypt(String key, String decryptText){
        // Передаем переменные классу обработки текста и ключа
        ArrayPositionLetter classArrayPositionLetter = new ArrayPositionLetter(decryptText, alphabet, key);
        int[][] arrayPositionLetter = classArrayPositionLetter.startArrayPositionLetter(); // Получаем масивы ключ. текст
        int[] arrayPositionLetterDecryptText = arrayPositionLetter[0]; // Получаем масив номеров букв текста
        int[] arrayPositionLetterKey = arrayPositionLetter[1]; // Получаем масив номеров букв ключа

        StringBuilder unencryptedText = new StringBuilder(); // Создаем переменную для зашифр. текста
        for (int i = 0; i < arrayPositionLetterDecryptText.length; i++) { // Создаем цикл создания шифр. текста
            int p = arrayPositionLetterDecryptText[i] - arrayPositionLetterKey[i]; // Используя формулу с
            // порядковыми номерами букв C = P + K, где С - зашифрованная буква, P - исходная буква, K - буква ключа
            if (p < 0) { // Создаем условие, если число расшифрованной буквы меньше 0
                p += alphabet.length; // Прибавляем количество символов алфавита
            }
            unencryptedText.append(alphabet[p]); // Добавляем букву в конец строки зашифрованного тектса
        }
        System.out.println("Расшифрованный текст: " + unencryptedText); // Выводим зашифрованный текст

    }
}
