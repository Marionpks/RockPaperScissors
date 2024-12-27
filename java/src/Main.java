package rpsgame;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        GameLogic game = new GameLogic();
        boolean playAgain = true;

        System.out.println("Welcome to Rock-Paper-Scissors!");

        while (playAgain) {
            System.out.println("Enter your choice (rock, paper, scissors):");
            String userChoice = scanner.nextLine().toLowerCase();

            while (!game.isValidChoice(userChoice)) {
                System.out.println("Invalid choice. Please enter rock, paper, or scissors:");
                userChoice = scanner.nextLine().toLowerCase();
            }

            String computerChoice = game.getComputerChoice();
            System.out.println("Computer chose: " + computerChoice);

            String result = game.determineWinner(userChoice, computerChoice);
            System.out.println(result);

            // Ask the user if they want to play again
            System.out.println("Do you want to play again? (y/n):");
            String playAgainResponse = scanner.nextLine().toLowerCase();
            if (!playAgainResponse.equals("y")) {
                playAgain = false;
                System.out.println("Thanks for playing! Goodbye.");
            }
        }

        scanner.close();
    }
}
