import datetime
import time
from pyrogram import Client, filters
from database.users_chats_db import db
from info import ADMINS

@Client.on_message(filters.command("update_users") & filters.user(ADMINS))
async def update_users(client, message):
    total_users = await db.total_users_count()
    sts = await message.reply_text('Updating your messages...')
    start_time = time.time()
    count = 0
    complete = 0
    
    async for user in await db.get_all_users():
        user_id = user.get("id")
        short_temp = "1"
        date_temp = "1999-12-31"
        time_temp = "23:59:59"
        await db.update_verification(user_id, short_temp, date_temp, time_temp)
        
        count += 1
        complete += 1
        
        if not complete % 20:
            await sts.edit(f"Total Users: {total_users}\nTotal Complete: {complete}\nTotal Complete Percentage: {complete/total_users*100:.2f}%")
    
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"All users updated with default verification status.\nTime taken: {time_taken}")
