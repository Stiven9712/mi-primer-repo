import java.util.Scanner;

public class EstacionesDelAnio {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el número del mes (1 al 12): ");
        int mes = scanner.nextInt();

        switch (mes) {
            case 3:
            case 4:
            case 5:
                System.out.println("Primavera");
                break;
            case 6:
            case 7:
            case 8:
                System.out.println("Verano");
                break;
            case 9:
            case 10:
            case 11:
                System.out.println("Otoño");
                break;
            case 12:
            case 1:
            case 2:
                System.out.println("Invierno");
                break;
            default:
                System.out.println("Mes no válido");
        }

        scanner.close();
    }
}

