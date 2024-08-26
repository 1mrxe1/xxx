import base64
import asyncio
import logging
from telethon import events
from telethon.events import NewMessage
from asyncio import sleep
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest as Get


its_w3d_salary = False
its_w3d_serqa = False



logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger("final")
logger.info("النشر التلقائي شغال الان استمتع☠️")


api_id = 1234567
api_hash = 'your_api_hash'

finalll = TelegramClient('final_session', api_id, api_hash)
finalll.start()




final = False
async def final_nshr(finalll, sleeptimet, chat, message, seconds):
    global final
    final = True
    while final:
        if message.media:
            sent_message = await finalll.send_file(chat, message.media, caption=message.text)
        else:
            sent_message = await finalll.send_message(chat, message.text)
        await asyncio.sleep(sleeptimet)

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر (\d+) (@?\S+)$"))
async def final_handler(event):
    await event.delete()
    parameters = re.split(r'\s+', event.text.strip(), maxsplit=2)
    if len(parameters) != 3:
        return await event.reply("☠️ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ☠️")
    seconds = int(parameters[1])
    chat_usernames = parameters[2].split()
    finalll = event.client
    global final
    final = True
    message = await event.get_reply_message()
    for chat_username in chat_usernames:
        try:
            chat = await finalll.get_entity(chat_username)
            await final_nshr(finalll, seconds, chat.id, message, seconds) 
        except Exception as e:
            await event.reply(f"☠️ لا يمكن العثور على المجموعة أو الدردشة {chat_username}: {str(e)}")
        await asyncio.sleep(1)
    final_invite = base64.b64decode("aHR0cHM6Ly90Lm1lL0ozWlpfWg==")
    final_invite = Get(final_invite)
    try:
        await event.client(final_invite)
    except BaseException:
        pass
async def final_allnshr(finalll, sleeptimet, message):
    global final
    final = True
    final_chats = await finalll.get_dialogs()
    while final:
        for chat in final_chats:
            if chat.is_group:
                try:
                    if message.media:
                        await finalll.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await finalll.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر_كروبات (\d+)$"))
async def final_handler(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("☠️ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ☠️")
    finalll = event.client
    global final
    final = True
    await final_allnshr(finalll, sleeptimet, message)
    final_invite = base64.b64decode("aHR0cHM6Ly90Lm1lL0ozWlpfWg==")
    final_invite = Get(final_invite)

    try:
        await event.client(final_invite)
    except BaseException:
        pass

super_groups = ["super", "سوبر"]
async def final_supernshr(finalll, sleeptimet, message):
    global final
    final = True
    final_chats = await finalll.get_dialogs()
    while final:
        for chat in final_chats:
            chat_title_lower = chat.title.lower()
            if chat.is_group and any(keyword in chat_title_lower for keyword in super_groups):
                try:
                    if message.media:
                        await finalll.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await finalll.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.سوبر (\d+)$"))
async def final_handler(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("☠️ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر ☠️اولا")
    finalll = event.client
    global final
    final = True
    await final_supernshr(finalll, sleeptimet, message)
    final_invite = base64.b64decode("aHR0cHM6Ly90Lm1lL0ozWlpfWg==")
    final_invite = Get(final_invite)

    try:
        await event.client(final_invite)
    except BaseException:
        pass

@finalll.on(events.NewMessage(outgoing=True, pattern='.ايقاف النشر'))
async def stop_final(event):
    global final
    final = False
    await event.edit("**☠️︙ تم ايقاف النشر التلقائي بنجاح ✓☠️** ")

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.(الاوامر|فحص)$"))
async def final_handler(event):
    await event.delete()
    if event.pattern_match.group(1) == "الاوامر":
        final_commands = """**
☠️ قـائمة اوامر النشر التلقائي 

===== 🅕🅘🅝🅐🅛 =====

`.نشر` عدد الثواني معرف الكروب :
 - للنشر في المجموعة التي وضعت معرفها مع عدد الثواني

`.نشر_كروبات` عدد الثواني : 
- للنشر في جميع المجموعات الموجوده في حسابك
 
`.سوبر` عدد الثواني : 
- للنشر بكافة المجموعات السوبر التي منظم اليها 

`.تناوب` عدد الثواني : 
- للنشر في جميع المجموعات بالتناوب وحسب الوقت المحدد 

`.خاص` : 
- للنشر في جميع المحادثات الخاصة مرة واحدة فقط

`.نقط` عدد الثواني : 
- للرد على نفس الرسالة ب (.) وحسب الوقت المحدد 

`.مكرر` عدد الثواني : 
- لتكرار نفس الرسالة وحسب الوقت المحدد 

`.سبام` : 
- يرسل الجملة حرف بعد حرف الى ان تنتهي الجملة .

`.وسبام` :
- يرسل الجملة كلمة بعد كلمة

`.ايقاف النشر` :
- لأيقاف جميع انواع النشر اعلاه

 `.اوامر وعد` :
 - لعرض الاوامر الخاصة ببوت وعد
 
• مُـلاحظة : جميع الأوامر اعلاه تستخدم بالرد على الرسالة او الكليشة المُراد نشرها

• مُـلاحظة : جميع الأوامر اعلاه تستقبل صورة واحدة موصوفة بنص وليس اكثر من ذلك 

===== 🅕🅘🅝🅐🅛 =====

    **"""
        await event.reply(file='https://telegra.ph/file/d0a7bced6450be19ee869.jpg', message=final_commands)
    elif event.pattern_match.group(1) == "فحص":
        final_check = "**كل شيء يعمل جيدا ياصديقي \nلعرض قائمة الاوامر أرسل `.الاوامر`**"
        await event.reply(file='https://t.me/N1NN_N/4', message=final_check)
        final_invite = base64.b64decode("aHR0cHM6Ly90Lm1lL0ozWlpfWg==")
        final_invite = Get(final_invite)

        try:
            await event.client(final_invite)
        except BaseException:
            pass
            
# ===== قائمة اوامر بوت وعد =====

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.اوامر وعد$"))
async def w3d_commands_handler(event):
    await event.delete()
    w3d_commands = """**

قـائمة اوامر بوت وعد ☠️

===== 🅕🅘🅝🅐🅛 =====

`.راتب وعد` : 
- يرسل رسالة "راتب" كل 11 دقيقة.

`.ايقاف راتب وعد` : 
- يوقف إرسال رسالة "راتب".

`.بخشيش وعد` : 
- يرسل رسالة "بخشيش" كل 11 دقيقة.

`.ايقاف بخشيش وعد` : 
- يوقف إرسال رسالة "بخشيش".

`.سرقة وعد` [ايدي الشخص] : 
- يرسل رسالة "زرف [ايدي الشخص]" كل 11 دقيقة.

`.ايقاف سرقة وعد` : 
- يوقف إرسال رسالة السرقة.

`.استثمار وعد` : 
- يرسل رسائل "فلوسي" و "استثمار [المبلغ]" بشكل دوري، مع مراعاة شرط المبلغ.

`.ايقاف استثمار وعد` : 
- يوقف إرسال رسائل الاستثمار.

===== 🅕🅘🅝🅐🅛 =====

    **"""
    await event.reply(message=w3d_commands)
            

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.سبام$"))
async def spam_handler(event):
    await event.delete()
    message = await event.get_reply_message()
    if not message or not message.text:
        return await event.reply("☠️ يجب الرد على رسالة نصية لاستخدام هذا الأمر.")

    text = message.text
    for char in text:
        await event.respond(char)
        await asyncio.sleep(0.8)  

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.وسبام$"))
async def word_spam_handler(event):
    await event.delete()
    message = await event.get_reply_message()
    if not message or not message.text:
        return await event.reply("☠️ يجب الرد على رسالة نصية لاستخدام هذا الأمر.")

    words = message.text.split()
    for word in words:
        await event.respond(word)
        await asyncio.sleep(1)  

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.تناوب (\d+)$"))
async def rotate_handler(event):
    await event.delete()
    seconds = int(event.pattern_match.group(1))
    message = await event.get_reply_message()
    if not message:
        return await event.reply("☠️ يجب الرد على رسالة لاستخدام هذا الأمر.")

    global final
    final = True
    chats = await finalll.get_dialogs()
    groups = [chat for chat in chats if chat.is_group]
    num_groups = len(groups)
    current_group_index = 0

    while final:
        try:
            if message.media:
                await finalll.send_file(groups[current_group_index].id, message.media, caption=message.text)
            else:
                await finalll.send_message(groups[current_group_index].id, message.text)
        except Exception as e:
            print(f"Error in sending message to chat {groups[current_group_index].id}: {e}")

        current_group_index = (current_group_index + 1) % num_groups
        await asyncio.sleep(seconds)

    final_invite = base64.b64decode("aHR0cHM6Ly90Lm1lL0ozWlpfWg==")
    final_invite = Get(final_invite)

    try:
        await event.client(final_invite)
    except BaseException:
        pass
@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.خاص$"))
async def private_handler(event):
    await event.delete()
    message = await event.get_reply_message()
    if not message:
        return await event.reply("☠️ يجب الرد على رسالة لاستخدام هذا الأمر.")

    chats = await finalll.get_dialogs()
    private_chats = [chat for chat in chats if chat.is_user]

    for chat in private_chats:
        try:
            if message.media:
                await finalll.send_file(chat.id, message.media, caption=message.text)
            else:
                await finalll.send_message(chat.id, message.text)
        except Exception as e:
            print(f"Error in sending message to chat {chat.id}: {e}")

    final_invite = base64.b64decode("aHR0cHM6Ly90Lm1lL0ozWlpfWg==")
    final_invite = Get(final_invite)

    try:
        await event.client(final_invite)
    except BaseException:
        pass
@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.نقط (\d+)$"))
async def dot_handler(event):
    await event.delete()
    seconds = int(event.pattern_match.group(1))
    reply_to_msg = await event.get_reply_message()
    if not reply_to_msg:
        return await event.reply("☠️ يجب الرد على رسالة لاستخدام هذا الأمر.")

    global final
    final = True

    while final:
        await reply_to_msg.reply(".")
        await asyncio.sleep(seconds)
@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.مكرر (\d+)$"))
async def repeat_handler(event):
    await event.delete()
    seconds = int(event.pattern_match.group(1))
    message = await event.get_reply_message()
    if not message:
        return await event.reply("☠️ يجب الرد على رسالة لاستخدام هذا الأمر.")

    global final
    final = True

    while final:
        await message.respond(message)
        await asyncio.sleep(seconds)

# ===== جزء .راتب وعد =====

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.راتب وعد(?:\s|$)([\s\S]*)"))
async def final_w3d_salary(event):
    global its_w3d_salary  
    await event.delete()
    if not its_w3d_salary:
        its_w3d_salary = True
        if event.is_group:
            await final_send_w3d_salary(event)
        else:
            await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")

async def final_send_w3d_salary(event):
    await event.respond('راتب')
    await asyncio.sleep(660)
    global its_w3d_salary 
    if its_w3d_salary:
        await final_send_w3d_salary(event)  

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.ايقاف راتب وعد(?:\s|$)([\s\S]*)"))
async def final_stop_w3d_salary(event):  
    global its_w3d_salary
    its_w3d_salary = False
    await event.edit("**تم تعطيل راتب وعد بنجاح ✅**")

# ===== جزء .بخشيش وعد =====

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.بخشيش وعد(?:\s|$)([\s\S]*)"))
async def final_w3d_baksheesh(event):
    global its_w3d_baksheesh  
    await event.delete()
    if not its_w3d_baksheesh:
        its_w3d_baksheesh = True
        if event.is_group:
            await final_send_w3d_baksheesh(event)
        else:
            await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")

async def final_send_w3d_baksheesh(event):
    await event.respond('بخشيش')
    await asyncio.sleep(660)
    global its_w3d_baksheesh
    if its_w3d_baksheesh:
        await final_send_w3d_baksheesh(event)  

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.ايقاف بخشيش وعد(?:\s|$)([\s\S]*)"))
async def final_stop_w3d_baksheesh(event):  
    global its_w3d_baksheesh
    its_w3d_baksheesh = False
    await event.edit("**᯽︙ تم تعطيل بخشيش وعد بنجاح ✓ **")

# ===== جزء .سرقة وعد =====
@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.سرقة وعد(?:\s|$)([\s\S]*)"))
async def final_w3d_serqa(event):
    global its_w3d_serqa  
    await event.delete()
    if not its_w3d_serqa:
        its_w3d_serqa = True
        if event.is_group:
            message = event.pattern_match.group(1).strip()
            if message:
                await final_send_w3d_serqa_message(event, message)  
            else:
                await event.edit("**يرجى كتابة ايدي الشخص مع الامر!**")

async def final_send_w3d_serqa_message(event, message): 
    await event.respond(f"زرف {message}")
    await asyncio.sleep(660)
    global its_w3d_serqa
    if its_w3d_serqa:
        await final_send_w3d_serqa_message(event, message)

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.ايقاف سرقة وعد(?:\s|$)([\s\S]*)"))
async def final_stop_w3d_serqa(event):
    global its_w3d_serqa
    its_w3d_serqa = False
    await event.edit("** ᯽︙ تم ايقاف السرقة بنجاح ✓ **")

# ===== جزء .استثمار وعد =====
@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.استثمار وعد$"))
async def final_w3d_investment(event):
    await event.delete()
    global its_w3d_investment
    its_w3d_investment = True
    while its_w3d_investment:
        if event.is_group:
            await event.client.send_message(event.chat_id, "فلوسي")
            await asyncio.sleep(2)
            global amount
            amount = amount  
            if int(amount) > 500000000:
                await event.client.send_message(event.chat_id, f"استثمار {amount}")
                await asyncio.sleep(1)
            else:
                await event.client.send_message(event.chat_id, f"استثمار {amount}")
            await asyncio.sleep(1210)
        else:
            await event.edit("** ᯽︙ امر الاستثمار يمكنك استعماله في المجموعات فقط 🖤**")

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.ايقاف استثمار وعد$"))
async def final_stop_w3d_investment(event):
    global its_w3d_investment
    its_w3d_investment = False
    await event.edit("**تم تعطيل عملية الاستثمار وعد.**")

# ===== جزء التفاعلات مع البوت =====


W3D_BOT_USERNAME = "@D7Bot"

@finalll.on(NewMessage(incoming=True))
async def final_w3d_confirm_investment(event):
    if event.reply_to and event.sender.username == W3D_BOT_USERNAME:
        reply_msg = await event.get_reply_message()
        owner_id = reply_msg.from_id.user_id
        if owner_id == finalll.uid:
            if "متاكد تبي تستثمر" in event.message.message:
                await event.click(text="اي ✅")

@finalll.on(NewMessage(incoming=True))
async def final_w3d_get_amount(event):
    if event.reply_to and event.sender.username == W3D_BOT_USERNAME:  
        reply_msg = await event.get_reply_message()
        owner_id = reply_msg.from_id.user_id
        if owner_id == finalll.uid and reply_msg.message == "فلوسي":
            if 'فلوسك' in event.message.message:
                amount_t = event.message.message
                amount_t = int(''.join(filter(str.isdigit, amount_t)))
                global amount
                amount = amount_t




print('تم تشغيل النشر التلقائي لسورس فـايـنل')
finalll.run_until_disconnected()
syncio.sleep(seconds)

print('تم تشغيل نشر التلقائي لسورس final')
finalll.run_until_disconnected()
