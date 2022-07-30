from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://telegra.ph/file/754c4457767c0ef064ea7.jpg",
                caption=(f"""● **ᴍᴇʀʜᴀʙᴀ** {message.from_user.mention} \n\n● **𝖡𝖾𝗇** {bot} !\n\n● **sᴇsʟɪ sᴏʜʙᴇᴛʟᴇʀᴅᴇ ᴍᴜ̈ᴢɪᴋ ᴄ̧ᴀʟᴀʙɪʟᴇɴ sᴇssɪᴢ sɪɴᴇᴍᴀ ᴏʏᴜɴᴜ ᴠᴇ ʏᴀş ᴛᴀʜᴍɪɴ ᴏʏɴᴀʏᴀʙɪʟᴇᴄᴇɢ̆ɪɴɪᴢ ʙᴏᴛᴜᴍ . . !** \n\n● **ʙᴀɴ ʏᴇᴛᴋɪsɪᴢ, sᴇs ʏᴏ̈ɴᴇᴛɪᴍ ʏᴇᴛᴋɪsɪ ᴠᴇʀɪᴘ ᴀsɪsᴛᴀɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇʏɪɴ . . !**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👨‍💻 Developer", url="https://t.me/Rexxuxxxnx"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❤️‍🔥 Söhbət Dəsdək", url="https://t.me/GOLD_FED_TEAM"
                    ),
                    InlineKeyboardButton(
                        "⚡️ Kanalım", url="https://t.me/QocayefBlog"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🐊 Komandalar" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Qrupa Əlavə et", url=f"https://t.me/GOLDMusccbot?startgroup=true"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["bilgi", f"bilgi@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text("● **önəmli :\n\n botun aktiғ işləməsi üçün bu üç ʏᴇᴛᴋɪʏᴇ ehtiyacı var :\n\n> mesajları silmə ,\n> bağlantı ilə dəvət ,\n> və səsli söhbətləri yönəltmə  ,**", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "✨️ Bütün Komandalar", callback_data="herkes")
                 ],[
                     InlineKeyboardButton(
                         "🗯️ 𝖠𝗇𝖺 menyu ", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "🖤 Söhbət qrupum", url="https://t.me/TinyCactusGroup")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text("● **𝖭𝗈𝗍 :\n\n 𝖡𝗈𝗍𝗎𝗇 𝖠𝗄𝗍𝗂𝖿 işlemesi üçün bu 𝖴𝖼 𝗒𝖾𝗍𝗄𝗂𝗒𝖾 ehtiyacı 𝖵𝖺𝗋 :\n\n> 𝖬𝖾𝗌𝖺𝗃𝗅𝖺𝗋𝗂 𝖲𝗂𝗅𝗆𝖾 ,\n> 𝖡𝖺𝗀𝗅𝖺𝗇𝗍𝗂 𝖣𝖺𝗏𝖾𝗍 𝖤𝗍𝗆𝖾 ,\n> 𝖲𝖾𝗌𝗅𝗂 𝖲𝗈𝗁𝖻e𝗍 𝖸𝗈𝗇𝖾𝗍𝗆𝖾 ,**", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "🐊 Bütün komandalar", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "🗯️ 𝖠𝗇𝖺 𝖬𝖾𝗇𝗎", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "🇦🇿 Kanalım", url="https://t.me/QocayefBlog")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>\nsᴇsʟɪ sᴏʜʙᴇᴛ ᴋᴏᴍᴜᴛʟᴀʀɪ » /vbul => video tapar . \n» /tap => mahnı tapar . \n» /play => mahnını başladar . \n» /durdur => mahnını dayandırar . \n» /devam => dayanan mahnını basladar . \n» /atla =>  sıradaki mahnıya keçər . \n» /son => mahnını sonladırar . \n» /katil => asistan qrupa qatılar  . \n» /reload => botu yenidən başladar .</b>\n\n\n sᴇssɪᴢ sɪɴᴇᴍᴀ ᴏʏᴜɴ ᴋᴏᴍᴜᴛʟᴀʀɪ: \n» /oyun => ʏᴇɴɪ ᴏʏᴜɴ ʙᴀşʟᴀᴛɪʀ . \n» /ogretmen => ᴏ̈ɢ̆ʀᴇᴛᴍᴇɴ ᴏʟᴍᴀᴋ \n» /puan => ɢʀᴜᴘ ᴜ̈ᴢᴇʀᴇ ᴘᴜᴀɴʟᴀʀ </b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "📩 Sahibim", url="https://t.me/Rexxuxxxnx")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Arxaya ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun adminlər üçün komanda menyusu 💣\n\n ▶️ /devam - mahnı oxumaqa dəvam et\n ⏸️ /durdur - oxuyan mahnını dayandırmaq üçün\n 🔄 /atla- Sıraya alınmış mahnını  keçmsk.\n ⏹ /son - mahnı oxumaqı dayandırma\n 🔼 /ver botun sadece yönetici için kullanılabilir olan komutlarını kullanabilmesi için kullanıcıya yetki ver\n 🔽 /al botun yönetici komutlarını kullanabilen kullanıcının yetkisini al\n\n ⚪ /asistan - Müzik asistanı grubunuza katılır.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Admin", url="https://t.me/tupurceyaktif")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Arxaya ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""● **Salam** {query.from_user.mention} \n\n● **Mən** {bot} !\n\n● **𝖲ə𝗌𝗅𝗂 𝖲𝗈𝗁𝖻ə𝗍𝗅ə𝗋𝖽ə mahnı oxuya bilən 𝖡𝗈𝗍a𝗆 . . !** \n\n● **𝖡𝖺𝗇 𝖸𝖾𝗍𝗄𝗂𝗌𝗂𝗓, 𝖲s𝗌 İdarə 𝖸𝖾𝗍𝗄𝗂𝗌𝗂 𝗏𝖾𝗋𝗂b 𝖠𝗌𝗂𝗌𝗍𝖺𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 Əlavə edin . . !**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎉 Məni grupuna əlavə et ⚡️", url=f"https://t.me/GOLDMusccbot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🇦🇿 𝐀𝐬𝐢𝐬𝐭𝐚𝐧", url="https://t.me/GOLDAsisstan"
                    ),
                    InlineKeyboardButton(
                        "✨️ Sahib", url="https://t.me/Rexxuxxxnx"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 komandalar" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "❤️‍🔥 Grupum", url=f"https://t.me/TinyCactusGroup"
                    )
                ]
                
           ]
        ),
    )
