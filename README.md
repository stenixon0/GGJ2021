# GGJ2021

This Discord bot was made for the 2021 Global Game Jam!

Many thanks to my group members Arianna Eiler, Nicholas Jager, Nicholas Jurkiewicz, and Ray Lu

Instructions can be found at https://globalgamejam.org/2021/games/soulmates-6

An even number of players is required (4 is the minimum but more than 6 is recommended)


# Installation
Download main.py, gamestate.py, and text.py into the same folder

Create a new discord bot and invite to the desired server
For more detailed instructions on how to do this: https://realpython.com/how-to-make-a-discord-bot-python/

Open up notepad and type the following (without asterix):

DISCORD_TOKEN=*Your_Token*
DISCORD_GUILD=*Your_Server*

save the file as .env

# Running the Program

In a command terminal of your choice, run main.py

If set-up correctly, a message of "*Your Bot* has connected to Discord!" will print to the terminal

Then, have at least four participants type !join in the server. 

You can check how many players are registered with !players

Once all 4 participants have entered, anyone can type !begin to assign the roles
Each participant will receive a DM with instructions about their roles

!begin will reassign roles each time it's called