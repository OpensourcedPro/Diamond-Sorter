import logging
import asyncio
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types
from sqlighter import SQLighter

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6868892310:AAG4btGMOOIFvjjj-7MV7L7E4SMkHa2i9ro")
dp = Dispatcher(bot)

db = SQLighter


@dp.message_handler(commands=['start'])
async def subscribe(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        db.add_subscriber(message.from_user.id)
    else:
        db.update_subscription(message.from_user.id, True)

    await message.answer(
        "You have successfully subscribed to the newsletter!\nWait, new reviews will be released soon and you will be the first to know about them =)")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
