import os
from flask import Flask
import threading
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("8610026193:AAE-Wk_Kio9t_SEWSNOcTe7V7jY7msUsZoQ")
EXNESS_LINK = "https://one.exness-track.com/a/https://one.exnessonelink.com/a/u99i5kr9of" # REPLACE THIS
FREE_CHANNEL_ID = -1004387682136 # REPLACE WITH YOUR CHANNEL ID
ADMIN_ID = 6463942425 # REPLACE WITH YOUR TELEGRAM ID

app_flask = Flask('')

@app_flask.route('/')
def home():
    return "Bot is alive"

def run():
    app_flask.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = f"""
Hey {user.first_name}! 👋

Welcome to Forex Signals Nigeria Free 🔥

Commands:
1.  /broker - Get my Exness link 
2.  /signals - See today's signals

I dey drop 2-3 signals daily here 👇
"""
    await update.message.reply_text(welcome_text)

async def broker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Open Exness Account", url=EXNESS_LINK)]]
    text = """
This is the broker I use 👇

**Why Exness:**
✅ $10 minimum deposit
✅ Instant withdrawal to Nigerian bank  
✅ MT4/MT5 platform

After signup + deposit, send me screenshot.
I go add you to VIP.
"""
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

async def signals(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Check the channel for today's signals 👇\nhttps://t.me/yourfreechannel")

async def addsignal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    
    signal_text = ' '.join(context.args)
    if not signal_text:
        await update.message.reply_text("Usage: /addsignal Pair: EURUSD | BUY | Entry: 1.0850")
        return
    
    full_msg = f"""
🔥 **NEW SIGNAL** 🔥

{signal_text}

SL: Manage risk
TP: Take profit at 1:2

Not financial advice. Trade at your own risk.
Join VIP for early signals: /broker
"""
    await context.bot.send_message(chat_id=FREE_CHANNEL_ID, text=full_msg, parse_mode='Markdown')
    await update.message.reply_text("✅ Signal posted to channel!")

def main():
    keep_alive()
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("broker", broker))
    app.add_handler(CommandHandler("signals", signals))
    app.add_handler(CommandHandler("addsignal", addsignal))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
