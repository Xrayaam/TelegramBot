import os
import telegram
import logging
from telegram.ext import Updater, MessageHandler, Filters
import openai

# دریافت توکن ربات تلگرام از متغیرهای محیطی
telegram_token = os.environ.get("TELEGRAM_TOKEN")
if not telegram_token:
    # اگر توکن ربات تلگرام وجود نداشت، خطای مناسب را نشان دهید
    print("Please set the TELEGRAM_TOKEN environment variable.")
    exit()
    
# دریافت توکن OpenAI از متغیرهای محیطی
openai_token = os.environ.get("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")
if not openai_token:
    # اگر توکن OpenAI وجود نداشت، خطای مناسب را نشان دهید
    print("Please set the OPENAI_TOKEN environment variable.")
    exit()

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
updater = Updater(token=telegram_token, use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_to_message))

# شروع ربات
updater.start_polling()

# نمایش لاگ ها
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Bot started')
updater.idle()