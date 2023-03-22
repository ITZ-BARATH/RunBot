from pyrogram import filters
from Vexera import BOT as Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

punda = [
    [
InlineKeyboardButton("Go Main Page", 
callback_data="start"),
    ],
    [
        
InlineKeyboardButton("DEV COMMANDS", 
callback_data="dhelp"),
    ],
]

@Client.on_callback_query(filters.regex("dhelp"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**
♡︎𝗗𝗲𝘃 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀♡︎

/eval - To run A Code
/logs - Get A Bot Logs
/sh - To Install packages
**
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="help")]]
        ),
    )


@Client.on_callback_query(filters.regex("help"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**
♡︎𝗛𝗲𝗹𝗽 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀♡︎

/id - Get a User Id/Chat ID💖
/tm - Reply a media To Get telegra.ph link
**
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="start")]]
        ),
    )


START = f"""
────「 [Vexera](https://graph.org//file/3650014818cd34600f408.jpg) 」────
Hᴇʏ, User!!
I ᴀᴍ Vᴇxᴇʀᴀ I Hᴀᴠᴇ Cᴏᴏʟ Fᴇᴡᴛᴜʀᴇs
➖➖➖➖➖➖➖➖➖➖➖➖➖
[Pᴀᴛᴄʜ Uᴘᴅᴀᴛᴇ Dᴇᴛᴀɪʟs]
➖➖➖➖➖➖➖➖➖➖
Lᴀsᴛ Uᴘᴅᴀᴛᴇ : 18:3:23
Pᴀᴛᴄʜ Nᴀᴍᴇ : Bᴇᴛᴀ
➖➖➖➖➖➖➖➖➖➖➖➖➖
Nᴇxᴛ Pᴀᴛᴄʜ Dᴀᴛᴇ : 30:4:23
Nᴇxᴛ Pᴀᴛᴄʜ Nᴀᴍᴇ : Ultra

Send Help To know My Ultra Powers⚡
"""
buttons = [
    [
        InlineKeyboardButton(
            text=f"[► Add Vexera To Your Group ◄]",
            url=f"https://telegram.dog/Vexera_50_bot?startgroup=true",
        )
    ],
    [
        
        InlineKeyboardButton(
            text="𓆩𝗧ᴏᴏɴ 𝗟ɪɴᴋᴢ𓆪", url="https://telegram.dog/Toon_LinkZ"
        ),

InlineKeyboardButton("Help", 
callback_data="help"),
    ],
    [
        InlineKeyboardButton(
            text="[► Support ◄]", url=f"https://telegram.dog/FutureCity005"
        ),
        InlineKeyboardButton(text="📢 Updates", url="https://telegram.dog/Updates004"),
    ],
]


@Client.on_message(filters.command("start") & filters.private)
def start(bot, message):
    text = START
    reply_markup = InlineKeyboardMarkup (buttons)
    message.reply(
    text=text,
    reply_markup=reply_markup,
    disable_web_page_preview=False
)

@Client.on_callback_query(filters.regex("start"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
    text = START,
    reply_markup = InlineKeyboardMarkup (buttons)
        )
        
