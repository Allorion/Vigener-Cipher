public class GenerateArray {
    // Метод создания масива с порядковыми номерами букв в алфавите
    int[] generateArray(String text, String[] alphabet) {
        String[] arrayText = text.split(""); // Создаем масив из исходного текста
        int[] positionArray = new int[text.length()]; // Создаем массив позиций букв в алфавите
        for (int i = 0; i < arrayText.length; i++) { // С помощью цикла получаем символ строки
            for (int j = 0; j < alphabet.length; j++) { // С помощью цикла получаем символ алфавита
                if (arrayText[i].equals(alphabet[j])) { // Сравниваем букву текста и букву алфавита
                    positionArray[i] = j; // Добавляем букву к масиву
                }
            }
        }
        return positionArray; // Возвращаем масив
    }
}
