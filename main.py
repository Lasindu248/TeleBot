import os
from os import error
import logging
import pyrogram
import time
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

KINGAMDA = Client(
    "king-amda",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_IMG = "https://telegra.ph/file/6a277e0bb77d5c5e87666.jpg"

START_TEXT = """
හේ හේ හිච්චි පුතේ 😇
දන්නවනේ ඉතින්. මම තමයි අපේ නිපුන් කොලුවගෙ ඇසිස්ටන්ට්.. ඌ දැන් පට්ට බිසී 😅 
ඉස්සර වගේ නෙවේනෙ පුතේ දැන් වගකීම් එහෙමත් වැඩිනෙ ඒකාට 😅 
ඉතින් පුතේ ඔය හෙල්ප් බටන් එක එබුවම විස්තරේ එයි 😇 ගහලම බලපම්කෝ.. 
එහෙනම් හිච්චි පුතේ අපි කැපුනා 🥸
"""

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('𝑹𝒆𝒑𝒐', url='https://github.com/Lasindu248/Assistant-Bot'),
        InlineKeyboardButton('𝑰𝒏𝒃𝒐𝒙',url='https://t.me/NiupunDinujaya')
        ]]
)


HELP_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('𝑰𝒏𝒃𝒐𝒙', url='https://t.me/NiupunDinujaya'),
        InlineKeyboardButton('𝑹𝒆𝒑𝒐',url='https://github.com/Lasindu248/Assistant-Bot')
        ]]
)

CONTACT_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('𝑰𝒏𝒃𝒐𝒙', url='https://t.me/NiupunDinujaya')
        ]]
)

HELP_TEXT = """
පුතේ මේ තීන්නෙ කමාන්ඩ්ස් ටික 👇

/help
/about
/contact
/website
/social
/github

හේ හේ මරු හැබැයි 😎
"""

ABOUT_TEXT = """
ස්ටාර්ට් ටෙක්ස්ට් එකේ තිබ්බ වගේ මේක තමයි පුතෙ නිපුන් කොලුවගෙ ඇසිස්ටන්ට් 😇 \n\n නිපුන්ව කන්ටැක්ට් කරගන්න හැටි , සෝසල් මීඩියා , ගිට්හබ් ප්‍රොෆයිල් එක වගේ ඔක්කොම මේ බොටාගෙ තීනව 🤓 \n\n පහළ තීන බටන් ටික ඔබලා බලාම් 😎 \n\n\n බලපම් ඉතිම් පුතේ 🥸
"""

CONTACT_TEXT = """
හිච්චි පුතේ නිපුන් කොලුව පොඩ්ඩක් බිසී මේ දවස් වල 🥲 \n\n ඉතින් @NiupunDinujaya ඉන්බොක්ස් ගිහිල්ල කන්ටැක්ට් කරගනිම් 🙂 \n\n රිප්ලයි කරන්න පරක්කු උනා කියල උගෙ ලොකුකම දැන් කියල හිතන්න එපා හිච්චි පුතේ 🥰 \n\n එහෙනම් කොල්ලො මැසේජ් එකක් දාලා වරෙම් 🥸
"""

WEBSITE_TEXT = """
හේ හේ හිච්චි පුතේ නිපුන් කොලුව වෙබ්සිටෙ එක හැදුවෙ PHP වලින් 😎 \n\n එකෙ උගෙ එක එක ප්‍රොජෙක්ට් තීනව බර්ත්ඩේ ගිෆ්ට් , ප්‍රශ්නවට වගේ .. යට තීන බටන් වලින් ගිහිල්ලම බලාම්කො
"""

HELP_IMG = "https://telegra.ph/file/50d549faaddb997964d38.jpg"

ABOUT_IMG = "https://telegra.ph/file/d0fc910ccee655abf8083.jpg"

CONTACT_IMG = "https://telegra.ph/file/03759e625dd1af8c55923.jpg"

WEBSITE_IMG = "https://telegra.ph/file/1bd95dd19b2e858a90cb0.jpg"

ABOUT_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('𝑯𝒆𝒍𝒑', url='http://t.me/NipunPrivateAssistantBot?help'),
        InlineKeyboardButton('𝑨𝒃𝒐𝒖𝒕',url='http://t.me/NipunPrivateAssistantBot?about')
        ],
        [
        InlineKeyboardButton('𝑪𝒐𝒏𝒕𝒂𝒄𝒕', url='http://t.me/NipunPrivateAssistantBot?contact'),
        InlineKeyboardButton('𝑾𝒆𝒃𝒔𝒊𝒕𝒆',url='http://t.me/NipunPrivateAssistantBot?website')
        ],
        [
        InlineKeyboardButton('𝑺𝒐𝒄𝒊𝒂𝒍 𝑴𝒆𝒅𝒊𝒂', url='http://t.me/NipunPrivateAssistantBot?social'),
        InlineKeyboardButton('𝑮𝒊𝒕𝒉𝒖𝒃',url='http://t.me/NipunPrivateAssistantBot?github')
        ]]
)

@KINGAMDA.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_photo(START_IMG)
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTON,
        disable_web_page_preview=True,
        quote=True
        
)
        
@KINGAMDA.on_message(filters.private & filters.command(["help"]))
async def start(bot, update):
    await update.reply_photo(HELP_IMG)
    await update.reply_text(
        text=HELP_TEXT.format(update.from_user.mention),
        reply_markup=HELP_BUTTON,
        disable_web_page_preview=True,
        quote=True
        
)    
    
@KINGAMDA.on_message(filters.private & filters.command(["about"]))
async def start(bot, update):
    await update.reply_photo(ABOUT_IMG)
    await update.reply_text(
        text=ABOUT_TEXT.format(update.from_user.mention),
        reply_markup=ABOUT_BUTTON,
        disable_web_page_preview=True,
        quote=True
        
) 
    
@KINGAMDA.on_message(filters.private & filters.command(["contact"]))
async def start(bot, update):
    await update.reply_photo(CONTACT_IMG)
    await update.reply_text(
        text=CONTACT_TEXT.format(update.from_user.mention),
        reply_markup=CONTACT_BUTTON,
        disable_web_page_preview=True,
        quote=True
        
) 


KINGAMDA.run()  
