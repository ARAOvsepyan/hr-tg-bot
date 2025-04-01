import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.types import BotCommand

from config import Config
from handlers import router


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Начать работу с ботом"),
        BotCommand(command="/quiz", description="Пройти тест на профориентацию")
    ]
    await bot.set_my_commands(commands)


async def on_startup(bot: Bot):
    try:
        await set_bot_commands(bot)
        await bot.send_message(Config.ADMIN_ID, "🟢 Бот успешно запущен!")
    except Exception as e:
        logging.error(f"Не удалось отправить сообщение админу: {e}")


async def main():
    # Настройка логгирования
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    logger = logging.getLogger(__name__)

    try:
        # Инициализация бота
        bot = Bot(
            token=Config.BOT_TOKEN,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )

        # Проверка токена
        try:
            bot_info = await bot.get_me()
            logger.info(f"Бот @{bot_info.username} успешно инициализирован")
        except Exception as e:
            logger.error(f"Ошибка инициализации бота: {e}")
            return

        # Настройка хранилища
        storage = MemoryStorage()
        dp = Dispatcher(storage=storage)

        # Регистрация роутеров
        dp.include_router(router)
        dp.startup.register(on_startup)

        # Запуск бота
        logger.info("Запуск бота...")
        await dp.start_polling(bot)

    except Exception as e:
        logger.error(f"Фатальная ошибка: {e}")
    finally:
        if 'bot' in locals():
            await bot.session.close()
        logger.info("Бот остановлен")


if __name__ == "__main__":
    asyncio.run(main())
