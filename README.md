# Discord Bot

This is a Discord bot made with [discord.py](https://github.com/Rapptz/discord.py).  
The bot is used to manage **forum tickets (threads)** and help moderators close them.

## Features
- `/resolve_name` → set your custom resolve name (the name shown when you close a ticket).
- `/resolve` → close and lock a forum ticket. The ticket will be renamed like:  
  `[DONE YourName] Ticket Name`.

## Permissions
The bot needs these permissions to work:
- Manage Threads
- Manage Messages
- Send Messages
- Send Messages In Threads 
- View Channels
- Manage Channels
- Manage Roles
- Read Message History  

Also, the bot role should be **higher than the roles of users** in the server.

## How to use
1. Clone this repo.
2. Install dependencies:
   `pip install discord.py`
3. Put your bot token in the script:
   `bot.run("BotToken")`
4. Run the bot:
   `python DiscordBot.py`
