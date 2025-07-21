from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📞 Appelle-moi", url="tel:+33771779604")],
        [InlineKeyboardButton("🛠 Voir mes prestations", callback_data='prestations')],
        [InlineKeyboardButton("📝 Demander un devis", callback_data='devis')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🚗 Bienvenue chez MecaChoc34 !\nChoisis une option ci-dessous 👇",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "prestations":
        await query.edit_message_text(text=""" 
🛠 *Prestations disponibles Meca'Choc34* :
- Diagnostic panne
- Remplacement turbo, vanne EGR, embrayage
- Freinage, amortisseurs, distribution
- Dépannage à domicile ou sur site
        """, parse_mode='Markdown')
    elif query.data == "devis":
        await query.edit_message_text(text="📝 Envoie-moi la marque, le modèle, l’année et les symptômes de ton véhicule pour recevoir un devis rapide.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()
