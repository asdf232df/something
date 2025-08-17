from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- Replace with your Bot Token ---
BOT_TOKEN = "8178470012:AAEfXIJynD0LglxHx0e7XPjOttf9eJ-zvZw"

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! 👋 I am your bot. Ask me anything simple!")

# Function to handle messages
async def reply_to_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()

    # Simple responses
    if "hi" in user_message or "hello" in user_message:
        response = "Hello there! 😊"
    elif "how are you" in user_message:
        response = "I’m good, thanks for asking! How are you?"
    elif "your name" in user_message:
        response = "I’m AHC Results Bot 🤖"
    elif "bye" in user_message:
        response = "Goodbye! 👋 Have a great day!"
    elif "what can you do" in user_message:
        response = "I can chat with you, answer simple questions, and help you with basic tasks!"
    elif "who made you" in user_message:
        response = "I was created by a developer using Python and the Telegram Bot API! 🧑‍💻"
    elif "tell me a joke" in user_message:
        response = "Why don’t scientists trust atoms? Because they make up everything! 😄"
    elif "what is your purpose" in user_message:
        response = "I'm here to assist, inform, and chat with you in a friendly way! 🤗"
    elif "how old are you" in user_message:
        response = "I'm just a few lines of code, so technically ageless! ⏳"
    elif "thank you" in user_message or "thanks" in user_message:
        response = "You're welcome! 😊"
    else:
        response = "Sorry, I don’t understand that yet. 🙈"

    await update.message.reply_text(response)


# Main function
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_to_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
