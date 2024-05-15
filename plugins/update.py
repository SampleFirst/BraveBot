from pyrogram import Client, filters
from info import ADMINS 
from utils import temp, get_verify_status, update_verify_status

@Client.on_message(filters.command("update"))
async def update_user(client, message):
    name = temp.U_NAME
    text = message.text.split("_")
    if len(text) == 2:
        user_id = text[0]
        short_var = text[1]
        if await db.is_user_exist(user_id):
            status = await get_verify_status(user_id)
            date_var = status["date"]
            time_var = status["time"]
            
            await update_verify_status(client, user_id, short_var, date_var, time_var)
            
            # Reply to the message
            await client.send_message(
                chat_id=message.chat.id,
                text=f"#UpdateForUser\n"
                     f"User id: {user_id}\n"
                     f"short number: {short_var}\n"
                     f"Me: {name}."
            )
        else:
            await client.send_message(
                chat_id=message.chat.id,
                text=f"#UserNotFound\n"
                     f"user id: {user_id}\n"
                     f"Me: {name}"
            )
          
