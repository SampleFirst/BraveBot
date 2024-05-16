import datetime
import time
import asyncio
from pyrogram import Client, filters
from database.users_chats_db import db
from info import ADMINS
from utils import save_group_settings

@Client.on_message(filters.command("updatesettings") & filters.user(ADMINS))
async def update_chats_settings(client, message):
    sts = await message.reply_text('Updating chats settings for default...')
    total_chats = await db.total_chat_count()
    start_time = time.time()
    count = 0
    complete = 0
    
    chats = await db.get_all_chats()
    
    for chat in chats:
        chat_id = chat.get("id")
        await save_group_settings(chat_id, 'button', True)
        await save_group_settings(chat_id, 'botpm', False)
        await save_group_settings(chat_id, 'file_secure', True)
        await save_group_settings(chat_id, 'imdb', False)
        await save_group_settings(chat_id, 'spell_check', True)
        await save_group_settings(chat_id, 'welcome', True)
        await save_group_settings(chat_id, 'auto_delete', True)
        await save_group_settings(chat_id, 'auto_ffilter', True)
        await save_group_settings(chat_id, 'max_btn', True)
        await save_group_settings(chat_id, 'is_shortlink', False)
        
        count += 1
        complete += 1
        
        if not complete % 20:
            await sts.edit(f"Total Chats: {total_chats}\nTotal Complete: {complete}\nTotal Complete Percentage: {complete/total_chats*100:.2f}%")
    
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"All users updated with default verification status.\nTime taken: {time_taken}")
    
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
        short_temp = "4"
        date_temp = "1999-12-31"
        time_temp = "23:59:59"
        await db.update_verification(user_id, short_temp, date_temp, time_temp)
        
        count += 1
        complete += 1
        
        if not complete % 20:
            await sts.edit(f"Total Users: {total_users}\nTotal Complete: {complete}\nTotal Complete Percentage: {complete/total_users*100:.2f}%")
    
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"All users updated with default verification status.\nTime taken: {time_taken}")


@Client.on_message(filters.command("update_user"))
async def update_user(client, message):
    start_time = time.time()
    sts = await message.reply_text('Updating user...')
    userid = message.from_user.id
    try:
        short_temp = "4"
        date_temp = "1999-12-31"
        time_temp = "23:59:59"
        await db.update_verification(userid, short_temp, date_temp, time_temp)
        
        time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
        await sts.edit(f"All users updated with default verification status.\nTime taken: {time_taken}")
    
    except Exception as e:
        await sts.edit(f"An error occurred: {str(e)}")
