
import java.util.Scanner;

public class CalculadoraBasica {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el primer número: ");
        double numero1 = scanner.nextDouble();

        System.out.print("Ingrese el segundo número: ");
        double numero2 = scanner.nextDouble();

        System.out.print("Ingrese la operación (+, -, *, /): ");
        String operacion = scanner.next();

        switch (operacion) {
            case "+":
                System.out.println("Resultado: " + (numero1 + numero2));
                break;
            case "-":
                System.out.println("Resultado: " + (numero1 - numero2));
                break;
            case "*":
                System.out.println("Resultado: " + (numero1 * numero2));
                break;
            case "/":
                if (numero2 == 0) {
                    System.out.println("Error: División por cero");
                } else {
                    System.out.println("Resultado: " + (numero1 / numero2));
                }
                break;
            default:
                System.out.println("Operación no válida.");
        }

        scanner.close();
    }
}
