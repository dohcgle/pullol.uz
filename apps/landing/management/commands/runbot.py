import asyncio
import logging
from django.core.management.base import BaseCommand
from django.conf import settings
from aiogram import Bot, Dispatcher
from apps.bot.handlers import router

# Configure logging
logging.basicConfig(level=logging.INFO)

class Command(BaseCommand):
    help = 'Runs the Telegram bot'

    def handle(self, *args, **options):
        # Get token from settings
        token = settings.BOT_TOKEN
        
        if not token:
            self.stdout.write(self.style.ERROR("BOT_TOKEN environment variable is not set."))
            return

        async def main():
            bot = Bot(token=token)
            dp = Dispatcher()
            dp.include_router(router)
            
            # Start polling
            self.stdout.write(self.style.SUCCESS("Bot started polling..."))
            await dp.start_polling(bot)

        from aiogram.utils.token import TokenValidationError
        
        try:
            asyncio.run(main())
        except TokenValidationError:
             self.stdout.write(self.style.ERROR("Bot tokeni noto'g'ri! Iltimos .env faylida to'g'ri BOT_TOKEN kiritilganligini tekshiring."))

        except KeyboardInterrupt:
            self.stdout.write(self.style.SUCCESS("Bot stopped."))
