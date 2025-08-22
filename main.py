import os
import time
import logging
from dotenv import load_dotenv
import telebot
from telebot import types
import google.generativeai as genai
from flask import Flask, request


load_dotenv("env")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GOOGLE_API_KEY     = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL       = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

if not TELEGRAM_BOT_TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN در .env تنظیم نشده.")
if not GOOGLE_API_KEY:
    raise RuntimeError("GOOGLE_API_KEY در .env تنظیم نشده.")


logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")


genai.configure(api_key=GOOGLE_API_KEY)
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN, parse_mode="Markdown")
model = genai.GenerativeModel(GEMINI_MODEL)


def send_typing(chat_id, seconds=0.6):
    bot.send_chat_action(chat_id, "typing")
    time.sleep(seconds)

def gemini_reply(user_text: str) -> str:
    try:
        response = model.generate_content(user_text)
        return response.text.strip() or "نتونستم پاسخی تولید کنم."
    except Exception as e:
        logging.exception("خطا در تماس Gemini:")
        return "اوه! اتصال به سرویس هوش مصنوعی با مشکل مواجه شد."

def safe_reply(chat_id, text, reply_to_message_id=None):
    MAX_LEN = 4000
    if not text:
        text = "پاسخی دریافت نشد."
    chunks = [text[i:i+MAX_LEN] for i in range(0, len(text), MAX_LEN)]
    for idx, chunk in enumerate(chunks):
        bot.send_message(chat_id, chunk, reply_to_message_id=reply_to_message_id if idx == 0 else None)


@bot.message_handler(commands=['start', 'help'])
def handle_start(message: types.Message):
    name = message.from_user.first_name or "دوست عزیز"
    text = (
        f"سلام {name}! \n"
        "من با **Google Gemini** کار می‌کنم و به سؤالاتت جواب می‌دم.\n\n"
        "دستورها:\n"
        "/model — نمایش/تغییر مدل فعلی\n"
        "/about — اطلاعات"
    )
    bot.reply_to(message, text)

@bot.message_handler(commands=['about'])
def handle_about(message: types.Message):
    bot.reply_to(message, "پشتیبانی‌شده توسط Google AI Studio (Gemini). لطفاً اطلاعات حساس ارسال نکنید.")

@bot.message_handler(commands=['model'])
def handle_model(message: types.Message):
    global GEMINI_MODEL, model
    parts = message.text.strip().split(maxsplit=1)
    if len(parts) == 1:
        bot.reply_to(message, f"مدل فعلی: `{GEMINI_MODEL}`\nمثال برای تغییر: `/model gemini-1.5-flash`")
    else:
        GEMINI_MODEL = parts[1]
        model = genai.GenerativeModel(GEMINI_MODEL)
        bot.reply_to(message, f"مدل به `{GEMINI_MODEL}` تغییر کرد.")

@bot.message_handler(content_types=['text'])
def handle_text(message: types.Message):
    chat_id = message.chat.id
    user_text = (message.text or "").strip()
    if not user_text:
        bot.reply_to(chat_id, "یه متن بفرست ")
        return

    send_typing(chat_id)
    answer = gemini_reply(user_text)
    safe_reply(chat_id, answer, reply_to_message_id=message.message_id)


app = Flask(__name__)

@app.route(f"/{TELEGRAM_BOT_TOKEN}", methods=["POST"])
def webhook():
    update = telebot.types.Update.de_json(request.get_json(force=True))
    bot.process_new_updates([update])
    return "ok", 200
