import datetime
import time
import asyncio
from pyrogram import Client, filters
from database.users_chats_db import db
from info import ADMINS

@Client.on_message(filters.command("updateusers") & filters.user(ADMINS))
async def update_users_verifications(client, message):
    sts = await message.reply_text('Updating users...')
    total_users = await db.total_users_count()
    start_time = time.time()
    count = 0
    complete = 0
    
    users = await db.get_all_users()
    
    for user in users:
        user_id = user.get("id")
        short_temp = "5"
        timer_temp = "00:00:30"
        today_temp = "1"
        date_temp = "1999-12-31"
        time_temp = "23:59:59"
        await db.update_verification(user_id, short_temp, timer_temp, today_temp, date_temp, time_temp)
        
        count += 1
        complete += 1
        
        if not complete % 20:
            await sts.edit(f"Total Users: {total_users}\nTotal Complete: {complete}\nTotal Complete Percentage: {complete/total_users*100:.2f}%")
    
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"All users updated with default verification status.\nTime taken: {time_taken}")
    
@Client.on_message(filters.command("update_users"))
async def update_users(client, message):
    start_time = time.time()
    sts = await message.reply_text('Updating users...')
    userid = message.from_user.id
    try:
        short_temp = "5"
        timer_temp = "00:00:30"
        today_temp = "1"
        date_temp = "1999-12-31"
        time_temp = "23:59:59"
        await db.update_verification(userid, short_temp, timer_temp, today_temp, date_temp, time_temp)
        
        time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
        await sts.edit(f"All users updated with default verification status.\nTime taken: {time_taken}")
    
    except Exception as e:
        await sts.edit(f"An error occurred: {str(e)}")
