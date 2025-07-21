
import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN", "TON_TOKEN_ICI")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [["📞 Appelle-moi", "📋 Voir mes prestations"], ["🧾 Demande de devis"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Bienvenue chez MécaChoc34 👨‍🔧", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    if text == "📞 Appelle-moi":
        await update.message.reply_text("Appelez-moi au 07 71 77 96 04 📞")
    elif text == "📋 Voir mes prestations":
        await update.message.reply_text("🚗 Prestations :
- Entretien
- Réparations
- Turbo
- Et plus encore sur Montpellier/Sète.")
    elif text == "🧾 Demande de devis":
        await update.message.reply_text("Envoyez-moi la marque, le modèle et les réparations souhaitées 📸")
    else:
        await update.message.reply_text("Merci pour votre message ! Nous vous répondrons rapidement.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

if __name__ == "__main__":
    print("Bot MécaChoc34 lancé...")
    app.run_polling()
