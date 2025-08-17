import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai

# --- Replace with your tokens ---
BOT_TOKEN = "8178470012:AAEfXIJynD0LglxHx0e7XPjOttf9eJ-zvZw" # Your Telegram Bot Token
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY" # Paste your Gemini API Key here

# --- Configure Gemini ---
genai.configure(api_key=AIzaSyCc-mBqA5qmI3zgSYccZCf1ap4MkbpX-OY)
model = genai.GenerativeModel('gemini-1.5-flash') # Using the fast and capable Flash model

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! 👋 I am a bot powered by Gemini. Ask me anything!")

# Function to handle messages and get a response from Gemini
async def reply_to_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    
    # Let the user know the bot is "thinking"
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')

    try:
        # Send the user's message to Gemini and get the response
        gemini_response = model.generate_content(user_message)
        response = gemini_response.text
    
    except Exception as e:
        print(f"An error occurred: {e}")
        response = "Sorry, I'm having trouble thinking right now. 🧠⚡️ Please try again later."

    # Send Gemini's response back to the user
    await update.message.reply_text(response)

# Main function
def main():
    print("Starting bot...")
    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_to_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
