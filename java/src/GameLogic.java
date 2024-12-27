package rpsgame;

import java.util.Random;

public class GameLogic {
    private String[] choices = {"rock", "paper", "scissors"};

    public boolean isValidChoice(String choice) {
        for (String validChoice : choices) {
            if (validChoice.equals(choice)) {
                return true;
            }
        }
        return false;
    }

    public String getComputerChoice() {
        Random random = new Random();
        int index = random.nextInt(choices.length);
        return choices[index];
    }

    public String determineWinner(String userChoice, String computerChoice) {
        if (userChoice.equals(computerChoice)) {
            return "It's a tie!";
        } else if ((userChoice.equals("rock") && computerChoice.equals("scissors")) ||
                   (userChoice.equals("scissors") && computerChoice.equals("paper")) ||
                   (userChoice.equals("paper") && computerChoice.equals("rock"))) {
            return "You win!";
        } else {
            return "Computer wins!";
        }
    }
}
