# Welcome to Nate's rock-em-sock-em-Paper game!

Please read the below instructions to set up and configure your game.
_Please also refer to the requirements.txt file for additional details_

## Set-up

### Environment Setup 
Follow the below instructions to set up your python environment for the game:
_NB - instructions sourced from https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md_ 

```sh
conda create -n my-game-env python=3.8 # (first time only)
conda activate my-game-env
```

## Customizing player name
This program allows the user to customize their displayed name within the game for better enjoyment

In order to customize their name the user needs to set up a local .env file. 
Please follow the instructions below to complete this process:

_NB - instructions sourced from https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/dotenv.md_

### Installation

First install the package, if necessary:

```sh
pip install python-dotenv # note: NOT just "dotenv"
```

### Usage


To setup this example, create a new directory on your Desktop named "my-secure-project". Then navigate there from the command-line:

```sh
cd Desktop/my-secure-project/
```

Create two files in the "my-secure-project" directory named ".env" and "my_script.py", respectively, and place inside the following contents:

```sh
# my-secure-project/.env

SECRET_MESSAGE="Hello World"
```

```py
# my-secure-project/my_script.py

import os
from dotenv import load_dotenv

load_dotenv() #> loads contents of the .env file into the script's environment

print(os.getenv("SECRET_MESSAGE")) # reads the variable from the environment
#> "Hello World"
```

And run the script to see the output:

```sh
python my_script.py
```

## Playing the game
Once your environment is set up, navigate to the code in your command line program of choice and
enter "python game.py" to begin the game. Have fun!
