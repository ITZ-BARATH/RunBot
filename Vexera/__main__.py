from Vexera import BOT, UBOT, TBOT, BOT_TOKEN

from telethon import __version__ as otazu

from pyrogram import __version__ as uuu

PHOTO = "https://graph.org//file/44772fd4c942df289fb05.jpg"

START = f"""
────「 Vexera 」────
Hᴇʏ Usᴇʀs
Vᴇxᴇʀᴀ Տᴛᴀʀᴛᴇᴅ Տᴜᴄᴄᴇssғᴜʟʟʏ 
➖➖➖➖➖➖➖➖➖➖➖➖➖
❍ 𝗣ʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ : {uuu}
❍ 𝗧ᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : {otazu}
➖➖➖➖➖➖➖➖➖➖➖➖➖
➛ Try Me I Have Cool Features 💖 ××
"""


@Bot.on_message(filters.command("pyro start"))
async def pyro_start(_, message):
   await message.reply_text("Pyro has been Started Already.")


if __name__ == "__main__":
    BOT.run()
    with BOT:
        BOT.send_message("-1001768984791", "....")
        
 #start message 
    #UBOT is Userbot client 
#TBOT is Telethon client
#BOT is pyrogram client 
