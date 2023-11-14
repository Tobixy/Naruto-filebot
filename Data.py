# Credits: @tobiix
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Commands for BOT Users
 ├ /start - Start the Bot
 ├ /about - About this Bot
 ├ /help - Help Commands for this Bot
 ├ /ping - Check if the bot is alive
 └ /uptime - Check the bot's status
 
 ❏ Commands for BOT Admins
 ├ /logs - View bot logs
 ├ /setvar - Set variable using a bot command
 ├ /delvar - Delete variable using a bot command
 ├ /getvar - View a specific variable using a bot command
 ├ /users - View bot user statistics
 ├ /batch - Create links for more than one file
 ├ /speedtest - Test the bot server's speed
 └ /broadcast - Broadcast a message to bot users

👨‍💻 Developed by </b><a href='https://t.me/team_devsX'>@team_devsx</a>
"""

    close = [
        [InlineKeyboardButton("Close", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("Help & Commands", callback_data="help"),
            InlineKeyboardButton("Close", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("About Me", callback_data="about"),
            InlineKeyboardButton("Close", callback_data="close")
        ],
    ]

    ABOUT = """
<b>About this Bot:

@{} is a Telegram Bot for storing posts or files that can be accessed through a special link.

 • Creator: @{}
 • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
 • Source Code: <a href='https://github.com/mrismanaziz/File-Sharing-Man'>File-Sharing-Man v4</a>

👨‍💻 Developed by </b><a href='https://t.me/team_devsX'>@team_devsx</a>
