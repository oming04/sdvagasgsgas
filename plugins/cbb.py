# (©)Codexbotz
# Recode by @mrismanaziz
# Modified by @SilenceSpe4ks
# t.me/SharingUserbot X t.me/infobotmusik

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import CHANNEL, GROUP, OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>📚 ᴛᴇɴᴛᴀɴɢ ʙᴏᴛ ɪɴɪ 📚\n\n☕ OWNER : <a href='tg://settings'>KEPO YA?</a>\n☕ MAU BOT KAYA GINI : <a href='https://t.me/kntl99999'>PC AJA</a></b>\n",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🔒 𝗧𝘂𝘁𝘂𝗽 🔒", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
