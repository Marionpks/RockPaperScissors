const buttons = document.querySelectorAll('.choice');
const playerChoiceDisplay = document.getElementById('player-choice');
const computerChoiceDisplay = document.getElementById('computer-choice');
const message = document.getElementById('message');
const score = document.getElementById('score');

let playerScore = 0;
let computerScore = 0;

function getComputerChoice() {
    const choices = ['Rock', 'Paper', 'Scissors'];
    return choices[Math.floor(Math.random() * 3)];
}

function playRound(playerChoice) {
    const computerChoice = getComputerChoice();
    playerChoiceDisplay.textContent = playerChoice;
    computerChoiceDisplay.textContent = computerChoice;

    if (playerChoice === computerChoice) {
        return `It's a tie! You both chose ${playerChoice}.`;
    } else if (
        (playerChoice === 'Rock' && computerChoice === 'Scissors') ||
        (playerChoice === 'Paper' && computerChoice === 'Rock') ||
        (playerChoice === 'Scissors' && computerChoice === 'Paper')
    ) {
        playerScore++;
        return `You win! ${playerChoice} beats ${computerChoice}.`;
    } else {
        computerScore++;
        return `You lose! ${computerChoice} beats ${playerChoice}.`;
    }
}

buttons.forEach(button => {
    button.addEventListener('click', () => {
        const playerChoice = button.id.charAt(0).toUpperCase() + button.id.slice(1);
        const resultMessage = playRound(playerChoice);
        message.textContent = resultMessage;
        score.textContent = `Player: ${playerScore} | Computer: ${computerScore}`;
    });
});
