# Hangman

This is Portfolio Project 3 called Hangman
<br>
<br>
***placeholder for picutre***
<br>
<br>

- [Motivation](#)
- [User Experience](#)
    - [User Stories](#user-stories)
    - [Project Goal](#project-goal)
    - [Requirements and Expectations](#requirements-and-expectations)
    - [AppFlow](#appflow)
- [Technology, Frameworks and Programs used](#d)
    - [Languages](#languages)
    - [Dependencies and Programs used](#dependencies-and-frameworks)
- [Features](#features)
- [Testing](#testing)
- [Testing user stories](#testing-user-stories)
- [Deployment](#deployment)
- [Credits](#credits)

# Motivation

Portfolio Project 3 is about Hangman game. I have picked it to challenge myself and see how far I can go.
Main Purpose of this website is to play the game in CLI(Command Line Interface)

# User Experience(UX)

## User Stories
- I want user to be able to run and play the game in their browser.
- I want user to be able to input data into the game.
- I want user to see if they got the word correctly or not.
- I want user to be able to save the score.
- ***placeholder for more data***

## Project Goal

- Projects goal is to play Hangman game, check if provided input is correct or not and save the score.

## Requirements and Expectations

- Easy to understand game what to do as a player.
- Run the game through browser.
- Expect website to save score.
- Expect game to provide random word.
- Expect game to check if provided input is correct.

## Appflow

- Starting logic containing Start and Highscore.
<br>

<img src="documentation/PP3-start-logic.png" alt="App flow for start logic">

- Game logic containing everything else that happens in game from printing the word to checking it and saving score.
<br>

<img src="documentation/PP3-game-logic.png" alt="App flow for game logic">

[Back to top](#hangman)


# Technology, Frameworks and Programs used.

## Languages

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Dependencies and Frameworks

- [Lucid Charts](https://www.lucidchart.com/)
    -  Used for logic charts

# Features

### Main menu where you Type "start" to start the game or "highscore" to display top 3 scores(filled in with placeholders)
<details><summary>Picture</summary>
<img src="documentation/game_start.png" alt="main menu"/>
</details>
<br>

### Highscore, if you press 'Enter' it will return to the main menu above^
<details><summary>Picture</summary>
<img src="documentation/game-highscore.png" alt="highscore"/>
</details>
<br>

### starting game asks for nickname, if nickname empty throws an error!
<details><summary>Picture</summary>
<img src="documentation/game-nickname.png" alt="nickname"/>
<img src="documentation/game-nickname-error.png" alt="throw an error!"/>
</details>
<br>

### Rules, displays Rules in Ascii and prints out rules
<details><summary>Picture</summary>
<img src="documentation/game-word-guess-rules.png" alt="rules ascii"/>
</details>
<br>

### Word being displayed!
<details><summary>Picture</summary>
<img src="documentation/game-guess-word.png" alt="word displayed"/>
<img src="documentation/game-word-guess-correct-letter.png" alt="correct letter"/>
<img src="documentation/game-word-guess-wrong-letter.png" alt="error"/>
</details>
<br>

### Guessed the word!
<details><summary>Picture</summary>
<img src="documentation/game-word-guess-correct-word.png" alt="correct word"/>
</details>
<br>

### Continue/New word printed
<details><summary>Picture</summary>
<img src="documentation/game-word-guess-new-word.png" alt="new word printed"/>
</details>
<br>

### Game over you are out of lives!
<details><summary>Picture</summary>
<img src="documentation/game-word-guess-game-over.png" alt="game over"/>
</details>
<br>

### When game over do you want to play again?
<details><summary>Picture</summary>
<img src="documentation/game-word-guess-new-game.png" alt="new game"/>
</details>
<br>

### Finish/Saving score and finishing
<details><summary>Picture</summary>
<img src="documentation/game-word-guess-finished.png" alt="finishing game"/>
</details>
<br>

### Finished game saves to Google Sheets and sorts it descending/from highest to lowest
<details><summary>Picture</summary>
<img src="documentation/game-word-guess-google-sheet.png" alt="google sheets">
<img src="documentation/game-word-guess-google-sheet-js.png" alt="JavaScript in app scripts for google sheets">
</details>
<br>

# Testing

***loads of placeholders***

## Testing User Stories

- ***Placeholder***

# Bugs

1. Nickname can be space, tried to figure it out but failed so far.
2. Numbers are taken in as input, made error pop up saying letters only allowed.
3. Letters or numbers used again throw an error but keep getting added to list of GUESSES.

# Deployment

    ***Placeholder***

# Credits 
- Slack Community and my Mentor!
- Tutor Support, [Scott](https://github.com/ShavingSeagull) and [Joshua](https://github.com/LordButley)
- [Simen Daehlin](https://github.com/Eventyret) My Mentor very Helpfull!.
- [The W3C Markup Validation Service](https://validator.w3.org/) Validation of HTML.
- [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) Validation of CSS.
- [AmIresponsive](https://ui.dev/amiresponsive) for responsive look of my website.
