import datetime
import time
import asyncio
from pyrogram import Client, filters
from database.users_chats_db import db
from info import ADMINS

@Client.on_message(filters.command("update_users"))
async def update_users(client, message):
    start_time = time.time()
    sts = await message.reply_text('Updating users...')
    userid = message.from_user.id
    try:
        short_temp = "5"
        timer_temp = "00:00:30"
        today_temp = "1"
        date_temp = "1998-12-31"
        time_temp = "23:59:59"
        await db.update_verification(userid, short_temp, timer_temp, today_temp, date_temp, time_temp)
        
        time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
        await sts.edit(f"All users updated with default verification status.\nTime taken: {time_taken}")
    
    except Exception as e:
        await sts.edit(f"An error occurred: {str(e)}")

@Client.on_message(filters.command("verifyy"))
async def verification_dataz(client, message):
    # Get user ID
    user_id = message.from_user.id
    # Get verification data
    verification_data = await db.get_verified(user_id)
    # Format the verification data
    short = verification_data['short']
    timer = verification_data['timer']
    today = verification_data['today']
    date = verification_data['date']
    time_ = verification_data['time']
    
    formatted_data = f"""
    Short link: {short}
    Timer: {timer}
    Today: {today}
    Date: {date}
    Time: {time_}
    """
    # Send the formatted data as a message
    await message.reply_text(formatted_data)
