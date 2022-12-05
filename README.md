# Hangman

This is Portfolio Project 3 called Hangman
<br>
<br>
<img src="documentation/amiresponsive.png" alt="amIresponsive?"/>
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
- I want user to be able to put there nickname in game.
- I want user to be able to see rules of the game.
- I want user to be able to save their score if they guess the word correctly if they decide to finish.
- I want user to be able to guess the words letters replaced with _ and if guessed correctly to replace them with correct letter.
- I want user to display highscore of top 3 scores(they are filled in with placeholders to display).
- I want user to have 7 lives and if you use all of them to be displayed with Game Over text.
- I want user to be able to play game again if they lost all of their lives by playing game again.

## Project Goal

- Projects goal is to play Hangman game, check if provided input is correct or not, save the score and display highscores.

## Requirements and Expectations

- Easy to understand game what to do as a player.
- Run the game through browser.
- Expect website to save score.
- Expect game to provide random word.
- Expect game to check if provided input is correct.
- Expect game to have highscore system displayed at begining.

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

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - Sorting data in google sheets descending order on changes in file.
    <img src="documentation/game-word-guess-google-sheet-js.png" alt="App scripts google sheets">

## Dependencies and Frameworks

- [Lucid Charts](https://www.lucidchart.com/)
    - Used for logic charts

- [Gspread](https://docs.gspread.org/en/v5.7.0/)
    - Used to access google sheets to manipulate, save and read data of it.

- [Time Library](https://docs.python.org/3/library/time.html)
    - Used to time code execution.

- [Random Library](https://docs.python.org/3/library/random.html)
    - Used to randomize words if API is down giving status code 503.

- [OS](https://docs.python.org/3/library/os.html)
    - Used to clear terminal before new word is being displayed.

- [Art](https://pypi.org/project/art/)
    - Used to make ASCII art from words used in function center_text.

- [PEP8 Code Institute](https://pep8ci.herokuapp.com/#)
    - Used to linter Python code and see if any mistakes or issues come up.

- [Random word API](https://random-word-api.herokuapp.com/home)
    - Used to display random word, was down for a while and had to develop defensive code for that.

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

1. I have tested my game so many times in gitpod terminal itself having issues and bugs thrown left and right. Big issue was when API would pass you a string of words that would include "" and []. I had to get rid of those and then take the words and put in new list of words and then pass it on to another function to accept lower case letters.

2. Another issue i came up was same word being assigned more than once, function wouldnt roll another word from list or API.
I had to reasign variable again before function was called again to pick another word.
    <details><summary>Picture</summary>
    <img src="documentation/bug-same-word-more-than-once.png" alt="words displayed more than once">
    </details>
<br>

3. I have encountered bug where if I have checked if input user provides is Yes or No it would always be Yes or True.
I had to redo the checking instead of **user_input == "yes" or "no"** made it as **user_input in ["yes", "no"]** that solved my issue and changed all if statements checking users input.

4. I have encountered issue with putting capital letters or lower case letters in guessing or users input where it would throw errors that its invalid input, as I assigned in defensive code. I had to make **user_input.lower()** in every input check so even if its capital letter in guessed letter it would adjust it and not throw error for invalid input.

5. Biggest issue I have encountered was when API died, I had to develop function that checks if its responding giving error 200 or not responding giving error 503. I have made a function that checks the status code and if its 503 to use txt file with words in it, and if its responding to use the API. After all API was brought back to live and it proved that my Function works, I have ran my game one of the times and saw weird word looked up in txt file and it wasnt there. Opened [Random word API](https://random-word-api.herokuapp.com/home) and website was back live!.

6. I had one issue with indentation as well that wouldnt check if all letters are correct and if so to finish the game.
    <details><summary>Picture</summary>
    <img src="documentation/bug-finish-indentation.png" alt="indentation error">
    </details>
<br>

7. I found issue where hangman ascii wouldnt print, had to reasign variable with lives to be as with starting the game!
    <details><summary>Picture</summary>
    <img src="documentation/hangman-new-game.png" alt="hangman wouldnt print ascii art">
    </details>
<br>

## PEP8 Linter from Code Institute

- run.py ran through pep8 linter and found no errors
    <details><summary>Picture</summary>
    <img src="documentation/linter_1.png" alt="no errors">
    </details>
<br>

- utils.py ran through pep8 linter and found no errors
    <details><summary>Picture</summary>
    <img src="documentation/linter_2.png" alt="no errors">
    </details>
<br>

- ascii_art.py ran through pep8 linter and errors are found, they are justified to print ascii art for hangman.
    <details><summary>Picture</summary>
    <img src="documentation/linter_3_hangman.png" alt="error for ascii art">
    </details>
<br>

- game.py ran through pep8 linter and no errors found.
    <details><summary>Picture</summary>
    <img src="documentation/linter_4.png" alt="no errors">
    </details>
<br>

- api.py ran through pep8 linter and no errors found.
    <details><summary>Picture</summary>
    <img src="documentation/linter_5.png" alt="no errors found">
    </details>
<br>

- settings.py ran through pep8 linter and no errors found.
    <details><summary>Picture</summary>
    <img src="documentation/linter_6.png" alt="no errors found">
    </details>
<br>



## Testing User Stories

| **Feature**                     | **Action**                          | **Expected Result**                                                                  | **Result** |
|---------------------------------|-------------------------------------|--------------------------------------------------------------------------------------|-------------------|
| I want user to be able to run and play the game in their browser | You need to run link in my github or open link to heroku I provide| heroku link opens and game starts | PASS              |
<details><summary>Picture</summary>
<img src="documentation/user-story-1.png" alt="Link to game"/>
<img src="documentation/user-story-2.png" alt="Link open in browser"/>
</details>
<br>


| **Feature**                     | **Action**                          | **Expected Result**                                                                  | **Result** |
|---------------------------------|-------------------------------------|--------------------------------------------------------------------------------------|-------------------|
| I want user to be able to put there nickname in game | When you run game and type in start game will start and prompt to input your nickname and then display it | game start and displays nick provided | PASS              |
<details><summary>Picture</summary>
<img src="documentation/user-story-3.png" alt="prompt for nickname"/>
<img src="documentation/user-story-4.png" alt="nickname displayed"/>
</details>
<br>

| **Feature**                     | **Action**                          | **Expected Result**                                                                  | **Result** |
|---------------------------------|-------------------------------------|--------------------------------------------------------------------------------------|-------------------|
| I want user to be able to see rules of the game. | start the game, rules will display on its own | rules to be displayed | PASS              |
<details><summary>Picture</summary>
<img src="documentation/game-word-guess-rules.png" alt="rules being displayed"/>
</details>
<br>

| **Feature**                     | **Action**                          | **Expected Result**                                                                  | **Result** |
|---------------------------------|-------------------------------------|--------------------------------------------------------------------------------------|-------------------|
| I want user to be able to save their score if they guess the word correctly if they decide to finish | When you guessed word or words correctly and want to finish your score will be saved | Score being saved after user inputs finish after guessing word correctly | PASS              |
<details><summary>Picture</summary>
<img src="documentation/game-word-guess-finished.png" alt="prompt for nickname"/>
</details>
<br>

| **Feature**                     | **Action**                          | **Expected Result**                                                                  | **Result** |
|---------------------------------|-------------------------------------|--------------------------------------------------------------------------------------|-------------------|
| I want user to be able to guess the words letters replaced with _ and if guessed correctly to replace them with correct letter | when game starts and rules are displayed game start printing word to guess | guess correct letter from word | PASS              |
<details><summary>Picture</summary>
<img src="documentation/game-word-guess-correct-word.png" alt="word was guessed right"/>
</details>
<br>

| **Feature**                     | **Action**                          | **Expected Result**                                                                  | **Result** |
|---------------------------------|-------------------------------------|--------------------------------------------------------------------------------------|-------------------|
| I want user to display highscore of top 3 scores(they are filled in with placeholders to display) | at beginning you type in highscore/h or 2 to display highscores | top3 highscores will be displayed | PASS              |
<details><summary>Picture</summary>
<img src="documentation/game-highscore.png" alt="highscore displayed"/>
</details>
<br>


| **Feature**                     | **Action**                          | **Expected Result**                                                                  | **Result** |
|---------------------------------|-------------------------------------|--------------------------------------------------------------------------------------|-------------------|
| I want user to have 7 lives and if you use all of them to be displayed with Game Over text | User needs to play game, you have 7 lives each game | 7 lives corresponding to hangman parts | PASS              |
<details><summary>Picture</summary>
<img src="documentation/game-word-guess-game-over.png" alt="highscore displayed"/>
</details>
<br>

| **Feature**                     | **Action**                          | **Expected Result**                                                                  | **Result** |
|---------------------------------|-------------------------------------|--------------------------------------------------------------------------------------|-------------------|
| I want user to be able to play game again if they lost all of their lives by playing game again | Type in at game over yes to play again | If you lose all of your lives you can choose to pick to play again | PASS              |
<details><summary>Picture</summary>
<img src="documentation/game-word-guess-new-game.png" alt="highscore displayed"/>
</details>
<br>

# Bugs

1. Nickname can be space, tried to figure it out but failed so far.
2. Numbers are taken in as input, made error pop up saying letters only allowed.
3. Letters or numbers used again throw an error but keep getting added to list of GUESSES.
4. If API is down, txt file will give words in defensive code but there is chance of same word coming up more than once.

# Deployment

## Google sheets deployment
<br>
1. Go to [Google Sheets](https://www.google.com/sheets/about/) or google a "Google Sheets" and press first link saying **Google Sheets: Online Spreadsheet Editor**.
2. Login with your email.
3. Press Blank same as on image below.
    <details><summary>Picture</summary>
    <img src="documentation/google-sheets-create.png" alt="google sheets"/>
    </details>
    <br>

4. Rename file to whatever you like! we will call it **hangman**.
    <details><summary>Picture</summary>
    <img src="documentation/google-sheets-1.png" alt="rename google sheets"/>
    </details>
    <br>

5. Open another tab and open [Google Cloud](https://cloud.google.com/) or google **Google Cloud Platform** and press link saying **Google Cloud: Cloud Computing Services**.

6. Press on Console top right beside Icon of your email.
    <details><summary>Picture</summary>
    <img src="documentation/google-sheets-2.png" alt="google cloud"/>
    </details>
    <br>

7. Press **My First Project** and click **NEW PROJECT** and name your new project to **hangman** and press **Create**.
    <details><summary>Picture</summary>
    <img src="documentation/google-sheets-6.png" alt="google cloud"/>
    <img src="documentation/google-sheets-7.png" alt="google cloud"/>
    <img src="documentation/google-sheets-8.png" alt="google cloud"/>
    </details>
    <br>

8. Type in **Google Drive API** and press **Enable**
    <details><summary>Picture</summary>
    <img src="documentation/google-sheets-3.png" alt="google cloud"/>
    <img src="documentation/google-sheets-4.png" alt="google cloud"/>
    <img src="documentation/google-sheets-5.png" alt="google cloud"/>
    </details>
    <br>

9. Press **CREATE CREDENTIALS** next page should open and drop down menu should be selected on **Google Drive API** if its not look for it there, then press **Aplication data** and **No, I'm not using them**
    <details><summary>Picture</summary>
    <img src="documentation/google-sheets-9.png" alt="google cloud"/>
    <img src="documentation/google-sheets-10.png" alt="google cloud"/>
    </details>
    <br>

10. Type in in first row **hangman** or whatever you like and press **CREATE AND CONTINUE**, after that select **Basic** and then select **Editor**, menu will hide and press **CONTINUE**. Next leave those two rows empty and press **DONE**
    <details><summary>Picture</summary>
    <img src="documentation/google-sheets-11.png" alt="google cloud"/>
    <img src="documentation/google-sheets-12.png" alt="google cloud"/>
    <img src="documentation/google-sheets-13.png" alt="google cloud"/>
    <img src="documentation/google-sheets-14.png" alt="google cloud"/>
    </details>
    <br>

11. Press **Credentials** and press on the email shown on the picture below, next press **KEYS** and press button **ADD KEY**, another little menu will come out and press **Create new key**.
    <details><summary>Picture</summary>
    <img src="documentation/google-sheets-15.png" alt="google cloud"/>
    <img src="documentation/google-sheets-16.png" alt="google cloud"/>
    <img src="documentation/google-sheets-17.png" alt="google cloud"/>
    <img src="documentation/google-sheets-18.png" alt="google cloud"/>
    </details>
    <br>

12. Menu will pop out and press **JSON** and **CREATE**. File will start to download, keep it safe dont show to anyone. Press **SHOW ALL** on right hand side on download panel. Keep in mind where that JSON file is saved, you will need it later on.
    <details><summary>Picture</summary>
    <img src="documentation/google-sheets-19.png" alt="google cloud"/>
    <img src="documentation/google-sheets-20.png" alt="google cloud"/>
    </details>
    <br>

13. On top in search bar type in **Google Sheets API**, scroll down until you find it. Press **Enable**
    <details><summary>Picture</summary>
    <img src="documentation/google-sheets-21.png" alt="google cloud"/>
    <img src="documentation/google-sheets-22.png" alt="google cloud"/>
    <img src="documentation/google-sheets-23.png" alt="google cloud"/>
    </details>
    <br>

## GitHub/GitPod
<br>

14. Go to [GitHub](https://github.com/) and login if you arent, then go to [this link](https://github.com/aboczek/hangman-cli). My repository will open, press **< CODE >** and press **Local** then press Copy to clipboard button.
    <details><summary>Picture</summary>
    <img src="documentation/github-repo-1.png" alt="github"/>
    </details>
    <br>

15. Go to your github repositories and create new repo, call it whatever you like. Press **Create Repository** it will lead you to another page, and press **Gitpod** it should open workspace for you.
    <details><summary>Picture</summary>
    <img src="documentation/github-repo-2.png" alt="github"/>
    <img src="documentation/github-repo-3.png" alt="github"/>
    <img src="documentation/github-repo-4.png" alt="github"/>
    </details>
    <br>

16. When Gitpod is open, type in git bash following "**git clone https://github.com/aboczek/hangman-cli.git**" without quotation marks, and press enter. It will clone my repository.
    <details><summary>Picture</summary>
    <img src="documentation/github-repo-5.png" alt="github"/>
    <img src="documentation/github-repo-6.png" alt="github"/>
    </details>
    <br>

17. When everything is ready, type in **cd hangman-cli** it should change directory to it. Now you need to download libraries I'm using in my project list is as following.
    - pip install art
    - pip install gspread

18. Now we need to copy our JSON file into the hangman-cli directory, open your **Downloads** or where your downloads go to and copy file by dragging it in into main folder, When its done right click on file and rename it to **creds.json**. Make sure its in the right place otherwise game wont run throwing an errors.
    <details><summary>Picture</summary>
    <img src="documentation/github-repo-7.png" alt="github"/>
    </details>
    <br>

19. Now go back to Google sheets and open your [worksheet](https://docs.google.com/spreadsheets/u/0/?tgif=d), in row/column B1 write in **Name** and C1 write in **Score**, next rename your working sheet to **hangman_sheet**
    <details><summary>Picture</summary>
    <img src="documentation/github-repo-8.png" alt="github"/>
    </details>
    <br>

20. Go back to your gitpod and left click on creds.json and copy **client email** then go back to your worksheet and press **Share** then copy in the **client email**, next step is to uncheck notify people as on picture below.
    <details><summary>Picture</summary>
    <img src="documentation/github-repo-9.png" alt="github"/>
    <img src="documentation/github-repo-10.png" alt="github"/>
    <img src="documentation/github-repo-11.png" alt="github"/>
    <img src="documentation/github-repo-12.png" alt="github"/>
    </details>
    <br>

21. Congratulations, if you have done everything as said above your game should run and should look like this.
    <details><summary>Picture</summary>
    <img src="documentation/github-repo-13.png" alt="github"/>
    </details>
    <br>

22. In your workspace type in **cd hangman-cli** and then **git remote rename origin upstream** that should create your own version of project. Next type in **git remote add origin http://github.com/YOU/YOUR_REPO**(do not open the link leads to nowhere just drag text and copy it) if you are confused you can follow this [link](https://stackoverflow.com/questions/18200248/cloning-a-repo-from-someone-elses-github-and-pushing-it-to-a-repo-on-my-github). I have used it myself.

23. Check if your repo has assigned new repo address by typing in **git remote -v** origin should reach to your github upstream should reach to mine.

24. If everything is alright type in **git add .**, then **git commit -m "write whatever u wnt"** and then **git push origin main --force** We use force to push the files we have cloned otherwise it will try to fetch new files from my repository.

25. Check your github repo if all the files are pushed correctly.

26. Open your google sheets, now we can add JavaScript code to sort scores from highest to lowest. You will need to add Dummy data into the worksheet otherwise it will throw errors, next click **extensions** and **App Script**.
    <details><summary>Picture</summary>
    <img src="documentation/github-repo-14.png" alt="github"/>
    </details>
    <br>

27. Copy in this code down below.
    ```
    function dataSorting() {
    const ss = SpreadsheetApp.getActiveSpreadsheet()
    const sheet = ss.getSheetByName("hangman_sheet")
    const lastRow = sheet.getRange(2,2,sheet.getLastRow()-1,3)
    lastRow.sort({column:3,ascending: false});
    }
    ```

28. Press **Run** and it will ask you for permissions. You need to review privilages and allow them like on pictures below. 
    <details><summary>Picture</summary>
    <img src="documentation/github-repo-15.png" alt="github"/>
    <img src="documentation/gitpod-repo-16.png" alt="github"/>
    <img src="documentation/google-sheets-authorise.png" alt="github"/>
    </details>
    <br>

29. When you have that done go back to your **App Script** and press **Run** two yellow boxes should appear on the bottom saying about Notice that execution started and completed, that means code is working.
    <details><summary>Picture</summary>
    <img src="documentation/gitpod-repo-17.png" alt="github"/>
    </details>
    <br>

30. Now we need to add event listener, press clock logo on left side, and then press **create new trigger** then window will pop up. We chose which function to run like on picture below, and select event type we choose **On change** and save. You can go back to **< >** code section of App Script and Save the code if you havent by now. Nothing needs to be done more than it is now and it will run when there is any change done into the google sheets.
    <details><summary>Picture</summary>
    <img src="documentation/gitpod-repo-event.png" alt="github"/>
    <img src="documentation/gitpod-repo-18.png" alt="github">
    <img src="documentation/gitpod-repo-19.png" alt="github">
    </details>
    <br>
## Heroku 

31. Go to [Heroku](https://id.heroku.com/login) and login to your account.

32. On top right corner you have **New** press it and **Create new app**, next (1)name your app whatever you like then (2)pick server: europe, and (3) press **Create app**
    <details><summary>Picture</summary>
    <img src="documentation/heroku-1.png" alt="heroku"/>
    <img src="documentation/heroku-2.png" alt="heroku"/>
    </details>
    <br>

33. Go to **Settings** and press **Reveal Config Vars**. Now go to your workspace and copy entire **creds.json** content, and in **KEY** type in **CREDS** in **VALUE** Copy content of **creds.json** and **press ADD** then again in **KEY** type in **PORT** and **VALUE** type in **8000**.
    <details><summary>Picture</summary>
    <img src="documentation/heroku-3.png" alt="heroku"/>
    <img src="documentation/heroku-4.png" alt="heroku"/>
    <img src="documentation/heroku-5.png" alt="heroku"/>
    </details>
    <br>

34. Now scroll down until you see **Buildpacks**, press **Add buildpack** and pick **python** and **save change** then again **Add buildpack** but this time pick **nodejs** and **save change**. heroku/python should be above nodejs if its not put it as on image below you can drag it by hamburger menu on left side of it or remove with x and add again in correct order.
    <details><summary>Picture</summary>
    <img src="documentation/heroku-6.png" alt="heroku"/>
    <img src="documentation/heroku-7.png" alt="heroku"/>
    <img src="documentation/heroku-8.png" alt="heroku"/>
    <img src="documentation/heroku-9.png" alt="heroku"/>
    </details>
    <br>

35. Go back to top of the page and click **Deploy**, and click on **GitHub** and connect to it. Next below type in name of your repo and press search, it should automaticaly find the repo.
    <details><summary>Picture</summary>
    <img src="documentation/heroku-10.png" alt="heroku"/>
    <img src="documentation/heroku-11.png" alt="heroku"/>
    </details>
    <br>

36. Scroll down and press **Enable Automatic Deploys** then **Deploy Branch** it will deploy the branch.
    <details><summary>Picture</summary>
    <img src="documentation/heroku-12.png" alt="heroku"/>
    </details>
    <br>

37. Go to the top of the page and press **Open app** it will open new tab with your game in it.
    <details><summary>Picture</summary>
    <img src="documentation/heroku-13.png" alt="heroku"/>
    <img src="documentation/heroku-14.png" alt="heroku"/>
    </details>
    <br>
# Credits 
- Slack Community and my Mentor!
- Tutor Support, [Scott](https://github.com/ShavingSeagull) and [Joshua](https://github.com/LordButley)
- [Simen Daehlin](https://github.com/Eventyret) My Mentor very Helpfull!.
- [AmIresponsive](https://ui.dev/amiresponsive) for responsive look of my website.
- [Officedemy](https://www.officedemy.com/how-to-automatically-sort-in-google-sheets/) JS code to sort score highest to lowest.
- [GeeksforGeeks](https://www.geeksforgeeks.org/clear-screen-python/) for clear function to clear terminal.
- [PEP8 by CI](https://pep8ci.herokuapp.com/#) Used to linter python code.
- [Youtube](https://www.youtube.com/watch?v=5x6iAKdJB6U) Getting the idea how it should look.
- [Stackoverflow](https://stackoverflow.com/questions/18200248/cloning-a-repo-from-someone-elses-github-and-pushing-it-to-a-repo-on-my-github) Cloning and how to push into your own github repo.
- [Random word API](https://random-word-api.herokuapp.com/home) Used to pull random words for game.
    Ps: love and hate with this API it died on me and had to develop defensive code for it if its responding or not.