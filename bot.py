import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Get your bot token from environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")  # ✅ Do not hardcode in production

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! 👋 I am your bot. Ask me anything simple!")

# Handle plain text messages
async def reply_to_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()

    # Simple keyword-based responses
    if "hi" in user_message or "hello" in user_message:
        response = "Hello there! 😊"
    elif "how are you" in user_message:
        response = "I’m good, thanks for asking! How are you?"
    elif "your name" in user_message:
        response = "I’m AHC Results Bot 🤖"
    elif "bye" in user_message:
        response = "Goodbye! 👋 Have a great day!"
    else:
        response = "Sorry, I don’t understand that yet. 🙈"

    await update.message.reply_text(response)

# Main bot function
def main():
    if not BOT_TOKEN:
        raise ValueError("❌ BOT_TOKEN environment variable not set!")

    app = Application.builder().token(BOT_TOKEN).build()

    # Command handler
    app.add_handler(CommandHandler("start", start))

    # Message handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_to_message))

    print("✅ Bot is running 24/7...")
    app.run_polling()

if __name__ == "__main__":
    main()
