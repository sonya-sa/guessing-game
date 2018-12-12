#Guessing-Game

Guessing-Game is a word guessing game, which can be played by a user "against" the computer. This is a game where the secret-keeper (in this case, the computer) thinks of a word, and the guesser (the user) tries to guess it one letter at a time. The guesser has six guesses (incorrect guesses). If the guesser guesses a letter which is part of the word, the secret-keeper will reveal all occurrences of that letter in the word. If the guesser guesses a correct letter such that all letters are now revealed, the game is over and the user has won. The user begins the game by selecting a difficulty from 1-10. A terminal-based game was also created, for which the application was logically modeled after.

#Contents

* [Tech Stack](#technologies)
* [Installation](#install)
* [Version 2.0](#version)
* [About Me](#aboutme)

## <a name="technologies"></a>Technologies
Backend: Python, Flask <br/>
Frontend: Bootstrap, HTML, CSS<br/>
APIs: LinkedIn URL <br/>

## <a name="install"></a>Installation

To run Guessing-Game:

Clone or fork repo:

```
https://github/sonya-salimy/guessing-game
```

Create and activate a virtual environment inside your guessing-game directory:

```
virtualenv venv
source env/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run app:

```
python server.py
```
To run terminal based game:

```
python game.py
```

Navigate to 'localhost:5000/' to access Guessing-Game

##<a name='version'></a>Version 2.0
*Create database to store user information and scores
*Add Javascript and AJAX to increase efficiency 
*Cache results to avoid multiple API calls
*Deploy application

##<a name="aboutme"></a>About Me
Sonya Salimy is a software engineer, interested in the use of science, technology, policy and community engagement to tackle the world's most pressing problems.
Connect with Sonya on [LinkedIn][http://www.linkedin.com/in/sonya-salimy].

