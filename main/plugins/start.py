#Github.com/Vasusen-code

import os
from .. import bot as Drone
from telethon import events, Button

from ethon.mystarts import start_srb
    
S = '/' + 's' + 't' + 'a' + 'r' + 't'

@Drone.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):    
    Drone = event.client                    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("أرسل لي أي صورة مصغرة كرد على هذه الرسالة.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("ماكو صورة مصغرة.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("لا يوجد صورة مصغرة.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("تم حفظ الصورة الرمزية بنجاح ✅🔥!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):  
    Drone = event.client            
    await event.edit('مـحـاولـة 🔁.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('إزالة ❌!')
    except Exception:
        await event.edit("لم يتم حفظ الصورة الرمزية❌.")                        
  
@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    text = "اهلا بك عزيزي ارسل رابط وان كان خاصة ارسل رابط الدعوة 🔥🤭"
    await start_srb(event, text)
    
