from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://images.app.goo.gl/MTLXTSDCA4MLHScP7",
                caption=(f"""● **ᴍᴇʀʜᴀʙᴀ** {message.from_user.mention} \n\n● **𝖡𝖾𝗇** {bot} !\n\n● **sᴇsʟɪ sᴏʜʙᴇᴛʟᴇʀᴅᴇ ᴍᴜ̈ᴢɪᴋ ᴄ̧ᴀʟᴀʙɪʟᴇɴ sᴇssɪᴢ sɪɴᴇᴍᴀ ᴏʏᴜɴᴜ ᴠᴇ ʏᴀş ᴛᴀʜᴍɪɴ ᴏʏɴᴀʏᴀʙɪʟᴇᴄᴇɢ̆ɪɴɪᴢ ʙᴏᴛᴜᴍ . . !** \n\n● **ʙᴀɴ ʏᴇᴛᴋɪsɪᴢ, sᴇs ʏᴏ̈ɴᴇᴛɪᴍ ʏᴇᴛᴋɪsɪ ᴠᴇʀɪᴘ ᴀsɪsᴛᴀɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇʏɪɴ . . !**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👨‍💻 Developer", url="https://t.me/qocayeffdi"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❤️‍🔥 Söhbət Dəsdək", url="https://t.me/creativtemaa"
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
                        "Qrupa Əlavə et", url=f"https://t.me/creativmusicbot?startgroup=true"
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
                         "🖤 Söhbət qrupum", url="https://t.me/creativtemaa")
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
    await query.edit_message_text(f"""<b>\nsᴇsʟɪ sᴏʜʙᴇᴛ ᴋᴏᴍᴜᴛʟᴀʀɪ » /vbul => ᴠɪᴅᴇᴏ ɪɴᴅɪʀ . \n» /bul => ᴍᴜᴢɪᴋ ɪɴᴅɪʀ . \n» /oynat => ᴍᴜᴢɪᴋ ᴏʏɴᴀᴛ . \n» /durdur => ᴍᴜᴢɪɢɪ ᴅᴜʀᴅᴜʀ . \n» /devam => ᴍᴜᴢɪɢɪ sᴜʀᴅᴜʀ . \n» /atla =>  ᴍᴜᴢɪɢɪ ᴀᴛʟᴀ . \n» /son => ᴍᴜᴢɪɢɪ sᴏɴʟᴀɴᴅɪʀ . \n» /katil => ᴀsɪsᴛᴀɴɪ ɢʀᴜʙᴀ ᴅᴀᴠᴇᴛ ᴇᴅᴇʀ . \n» /reload => ᴀᴅᴍɪɴ ʟɪsᴛᴇsɪɴɪ ɢᴜɴᴄᴇʟʟᴇʀ .</b>\n\n\n sᴇssɪᴢ sɪɴᴇᴍᴀ ᴏʏᴜɴ ᴋᴏᴍᴜᴛʟᴀʀɪ: \n» /oyun => ʏᴇɴɪ ᴏʏᴜɴ ʙᴀşʟᴀᴛɪʀ . \n» /ogretmen => ᴏ̈ɢ̆ʀᴇᴛᴍᴇɴ ᴏʟᴍᴀᴋ \n» /puan => ɢʀᴜᴘ ᴜ̈ᴢᴇʀᴇ ᴘᴜᴀɴʟᴀʀ </b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "📩 Sahibim", url="https://t.me/qocayeffdi")
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
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBu botun adminler için komut menüsü 🤩\n\n ▶️ /devam - şarkı çalmaya devam et\n ⏸️ /durdur - çalan parçayı duraklatmak için\n 🔄 /atla- Sıraya alınmış müzik parçasını atlatır.\n ⏹ /son - müzik çalmayı durdurma\n 🔼 /ver botun sadece yönetici için kullanılabilir olan komutlarını kullanabilmesi için kullanıcıya yetki ver\n 🔽 /al botun yönetici komutlarını kullanabilen kullanıcının yetkisini al\n\n ⚪ /asistan - Müzik asistanı grubunuza katılır.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Admin", url="https://t.me/bashirliabinjz")
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
    await query.edit_message_text(f"""● **𝖬𝖾𝗋𝗁𝖺𝖻𝖺** {query.from_user.mention} \n\n● **𝖡𝖾𝗇** {bot} !\n\n● **𝖲𝖾𝗌𝗅𝗂 𝖲𝗈𝗁𝖻𝖾𝗍𝗅𝖾𝗋𝖽𝖾 müzik 𝖢𝖺𝗅𝖺𝖻𝗂𝗅𝖾𝗇 𝖡𝗈𝗍𝗎𝗆 . . !** \n\n● **𝖡𝖺𝗇 𝖸𝖾𝗍𝗄𝗂𝗌𝗂𝗓, 𝖲𝖾𝗌 𝖸𝗈𝗇𝖾𝗍𝗂𝗆 𝖸𝖾𝗍𝗄𝗂𝗌𝗂 𝗏𝖾𝗋𝗂𝗉 𝖠𝗌𝗂𝗌𝗍𝖺𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾𝗒𝗂𝗇 . . !**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎉 Məni grupuna əlavə et 🎉", url=f"https://t.me/creativmusicbot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🇦🇿 𝐀𝐬𝐢𝐬𝐭𝐚𝐧", url="https://t.me/CinomMusicAsissantX"
                    ),
                    InlineKeyboardButton(
                        "✨️ Sahib", url="https://t.me/qocayeffdi"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 komandalar" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "❤️‍🔥 Grupum", url=f"https://t.me/creativtemaa"
                    )
                ]
                
           ]
        ),
    )
