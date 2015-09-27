# TC-Telegram-Bot
This is a Telegram bot that execute commands in TrinityCore console via telnet.

## Installing

To run this bot you need the python-telegram-bot library, you can install it by

`pip install python-telegram-bot`

To install it from source you can download it from [https://github.com/leandrotoledo/python-telegram-bot](https://github.com/leandrotoledo/python-telegram-bot)




## Configuration

After installing the client you must configure it settings the following parameters:

`
HOST = "127.0.0.1"	#IP of the server
port = 3443		#Port of the server
username = ""		#Username telnet access 
password = ""		#Password telnet access
logs = 1		#Enable/Disable logs (1/0)

TOKEN = ""		#Token of your telegram bot that you created from @BotFather
`

The last parameter it's the Token of your bot that you receive while creating it with @BotFather (ask this bot on telegram).

After configuration you can run your bot, remind to enable telnet in etc/worldserver.conf (RA.* settings) and open your worldserver.


## FAQ

My bot **doesn't run** and **return the follow error**:

`
    LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
IndexError: list index out of range
`

Send a message to your Bot and (re)run the file main.py.


