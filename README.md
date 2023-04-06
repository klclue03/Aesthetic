<img src="https://i.ibb.co/vxhtYVh/aesthetic.png">

# Aesthetic
**Aesthetic is a multipurpose Discord bot. Features include moderation, games, music, roles, and utilities. Run /help for information on commands Contact positive#9872 on Discord for any questions.**

## Features
- **Moderation**: Kicking, Banning, Unbanning, Ban List
- **Games**: Coin Fliping, Rock Paper Scissors, Unscrambling Words, Wordle
- **Generation**: Joke Generator, Memes, Animal Pictures
- **Music**: Youtube Video Supported
- **Roles**: Adding or Removing Roles, Changing Nicknames, User Information
- **Utilities**: Language Translator, Calculator, Polls, Timers, Reminders

## General Setup
- If you have Git, clone/download the repository using the command `git clone`
- Create a discord bot in the [Discord Developer Portal](https://discord.com/developers/applications)
- Get your bot token
- Create a file called config.py which includes the following items:
```
BOT_TOKEN # Your bot token generated from your Discord Developer Portal

REDDIT_CLIENT_ID # Create a reddit client to generate this variable
REDDIT_CLIENT_SECRET # Create a reddit client to generate this variable
REDDIT_PASSWORD # Your Reddit

# NOTE: IT IS ALSO IMPORTANT TO CHANGE THE REDDIT USERNAME IN Generator.py IN BOTH THE MEME AND ANIMAL COMMANDS

PFP # Profile picture of the bot
BANNER # Image to show when the bot joins a server

wordle_list # List of 5 letter words for the wordle command
words # List of words for the scramble command

COMMANDS = ['+join', '+disconnect', '+play', '+pause', '+resume', '+role',
            '+user', '+nick', '+translate', '+help disconnect', '+help pause', '+help resume', '+help role',
            '+help calculator', '+help poll', '+calculator', '+poll', '+timer', '+reminder', '+coin', '+toss',
            '+k', '+b', '+help timer', '+help reminder', '+ct', '+scram', '+j', '+m', '+a', '+an', '+hi',
            '+bye', '+dc', '+p', '+r', '+n', '+u', '+trans', '+calc', '+c', '+stop', '+help', '+wordle', '+ban_list',
            '+bl', '+unban', '+remind', '+wd', '+t', '+time']

banned_words # List of banned words that you want in your server

country_dict # Dictionary of countries you want the bot to react with a flag emoji when the country is said in a message
```
- Run the code using your IDE or application that you opened the repository with, or create a server to host the repository
- Aesthetic is now running on your Discord server!

## Issues or Questions
If you have any questions, contact me on Discord at positive#9872. If you have any issues, post them [here](https://github.com/klclue03/Aesthetic/issues). Or, you can submit a pull request. I may make a few patches or updates for this project, but plan for it to be finalized soon.

**Other Information**:
- Built with Python 3.9.1
- IDE - Pycharm
- License - Apache License 2.0 (See LICENSE.md)
