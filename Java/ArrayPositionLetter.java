public class ArrayPositionLetter {
    String text;
    String[] alphabet;
    String key;

    ArrayPositionLetter(String importText, String[] importAlphabet, String importKey) {
        text = importText;
        alphabet = importAlphabet;
        key = importKey;
    }

    GenerateArray generate = new GenerateArray();

    int[][] startArrayPositionLetter() {
        int keyQuantity = (text.length() / key.length()) + 1; // Получаем количество удлинений ключа
        for (int i = 1; i < keyQuantity; i++) { // Удлинняем ключ с помощью цикла
            key += key;
        }

        int[] arrayPositionLetterText = generate.generateArray(text, alphabet); // Масив позиций букв текста в алфавите
        key = key.substring(0, arrayPositionLetterText.length); // Обрезаем ключ по колич. символов текста
        int[] arrayPositionLetterKey = generate.generateArray(key, alphabet); // Масив позиций букв ключа в алфавите

        return new int[][]{arrayPositionLetterText, arrayPositionLetterKey};
    }
}
