import java.util.Scanner;

public class Start {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        String[] alphabet = {"А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р",
                "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"};

        Encryption encryption = new Encryption(alphabet);
        Decrypt decrypt = new Decrypt(alphabet);

        while (true) {
            printMenu();
            int answer = scanner.nextInt();
            scanner.nextLine();
            if (answer == 1) {
                System.out.println("Введите желаемое слово ключ: ");
                String key = scanner.nextLine();

                System.out.println("Введите текст для зашифровки: ");
                String unencryptedText = scanner.nextLine();

                encryption.encryption(key, unencryptedText);
            }else if (answer == 2) {
                System.out.println("Введите ключ: ");
                String key = scanner.nextLine();

                System.out.println("Введите зашифрованный ключ: ");
                String decryptText = scanner.nextLine();

                decrypt.decrypt(key, decryptText);
            }else if (answer == 0) {
                System.out.println("Программа завершила работу!");
                break;
            }
        }
    }

    public static void printMenu() {
        System.out.println("Выберите действие:");
        System.out.println("1 - Зашифровать текст");
        System.out.println("2 - Расшифровать текст");
        System.out.println("0 - Завершить работу");
    }
}