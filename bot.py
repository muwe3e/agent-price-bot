import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN is not configured")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привет! Я бот для обновления прайсов.\n\n"
        "Пока я умею принимать текст. "
        "Следующий этап — разбор цен и наценки."
    )


@dp.message(F.text)
async def receive_text(message: Message):
    if message.text.startswith("/"):
        return

    await message.answer(
        f"Принял текст ({len(message.text)} символов).\n"
        "Обработку прайса подключим следующим этапом."
    )


async def main():
    async with bot:
        await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
