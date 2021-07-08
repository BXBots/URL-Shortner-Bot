# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from pyrogram import Client as FayasNoushad
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = """
Hai {}, 

`I am a link shortner telegram bot`.

👲 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : [ʙx ʙᴏᴛᴢ](https://telegram.me/BX_Botz)


"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔰Join Updates Channel🔰', url='https://telegram.me/Bx_Botz')
        ]]
    )

@FayasNoushad.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTONS,
        disable_web_page_preview=True
    )
