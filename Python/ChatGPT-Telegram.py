import os
import telegram
import logging
from telegram.ext import Updater, MessageHandler, Filters
import openai
import sys
from dotenv import load_dotenv , find_dotenv
from subprocess import call
load_dotenv(find_dotenv())

# دریافت توکن ربات تلگرام از متغیرهای محیطی
telegram_token = os.getenv('TELEGRAM_TOKEN')
if telegram_token is None:
    logging.error("Please set the TELEGRAM_TOKEN environment variable.")
    exit(1)
updater = Updater(token=telegram_token, use_context=True)
    
# دریافت توکن OpenAI از متغیرهای محیطی
openai_token = os.environ.get("OPENAI_TOKEN")
if not openai_token:
    # اگر توکن OpenAI وجود نداشت، خطای مناسب را نشان دهید
    print("Please set the OPENAI_TOKEN environment variable.")
    
# تعیین مدل GPT-3
model_engine = "davinci"

def reply_to_message(update, context):
    # استخراج متن پیام ارسال شده توسط کاربر
    user_input = update.message.text.strip()
    if not user_input:
        # اگر متن پیام خالی بود، پاسخی ندهید
        return
    # استفاده از مدل GPT-3 برای پاسخ به پیام
    response = openai.Completion.create(
        engine=model_engine,
        prompt=user_input + "\n\n", # استفاده از یک خط خالی به عنوان جداکننده بین ورودی و خروجی
        max_tokens=100,
        n=1,
        stop="\n\n", # استفاده از یک خط خالی به عنوان نشانه‌ای برای پایان خروجی
        temperature=0.5,
    )
    # استخراج متن پاسخ
    bot_response = response.choices[0].text.strip()
    # ارسال پاسخ به کاربر
    if bot_response:
        update.message.reply_text(bot_response)




# تعیین MessageHandler برای پاسخ به پیام ها
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_to_message))

# شروع ربات
updater.start_polling()

# نمایش لاگ ها
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Bot started')
updater.idle()