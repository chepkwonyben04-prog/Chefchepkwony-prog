from telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ==========================
# BOT SETTINGS
# ==========================

TOKEN = "8246218784:AAGNYCOvxTwgDEEYG5CU-n7JhId-R3Fin3Y"

EMAIL = "chepkwonyben04@gmail.com"
EMAIL_PASSWORD = "umxb oiqi mvys mane"

# ==========================
# START COMMAND
# ==========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        ["📚 My Books", "🍲 Cookbooks"],
        ["🆕 New Releases", "👨‍🍳 About the Author"],
        ["🌍 Follow Me", "📞 Contact Me"],
    ]

    await update.message.reply_text(
        "👋 Welcome to Chef Chepkwony Author!\n\nChoose an option below:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
    )


# ==========================
# BUTTONS
# ==========================

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    # BOOKS

    if text == "📚 My Books":

        keyboard = [
            [InlineKeyboardButton(
                "📖 The Unseen Never Gets Justice",
                url="https://www.amazon.com/dp/B0H6V7MDV7"
            )],
            [InlineKeyboardButton(
                "🔥 The Gavel and the Fire (Book 1)",
                url="https://www.amazon.com/dp/B0H6J6DQN8"
            )],
        ]

        await update.message.reply_text(
            "📚 MY BOOKS",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # COOKBOOKS

    elif text == "🍲 Cookbooks":

        keyboard = [
            [InlineKeyboardButton("🥤 Smoothies 101", url="https://amazon.com")],
            [InlineKeyboardButton("💪 High Protein 101", url="https://amazon.com")],
            [InlineKeyboardButton("🍛 Swahili Food 101", url="https://amazon.com")],
            [InlineKeyboardButton("🌮 Kenyan Street Food 101", url="https://amazon.com")],
            [InlineKeyboardButton("🍗 Air Fryer Kenyan Style 101", url="https://amazon.com")],
            [InlineKeyboardButton("🥘 African Food Prep 101", url="https://amazon.com")],
        ]

        await update.message.reply_text(
            "🍲 AVAILABLE COOKBOOKS",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # NEW RELEASES

    elif text == "🆕 New Releases":

        await update.message.reply_text(
            "📢 New books are coming soon.\nStay tuned!"
        )

    # ABOUT

    elif text == "👨‍🍳 About the Author":

        await update.message.reply_text(
            "Chef Chepkwony is an author, chef and storyteller dedicated to creating inspiring novels and practical cookbooks that impact lives."
        )

    # FOLLOW

    elif text == "🌍 Follow Me":

        keyboard = [
            [InlineKeyboardButton("📘 Facebook", url="https://www.facebook.com/profile.php?id=61591381624618")],
            [InlineKeyboardButton("📸 Instagram", url="https://www.instagram.com/chefchepkwony4?igsh=MTQwYnF1NGQ3ZGZ4bQ==")],
            [InlineKeyboardButton("🐦 X", url="https://x.com/Chefchepkwon")],
            [InlineKeyboardButton("🧵 Threads", url="https://www.threads.com/@chefchepkwony4")],
            [InlineKeyboardButton("🎵 TikTok", url="https://tiktok.com/@chefkip_254")],
            [InlineKeyboardButton("▶️ YouTube", url="https://youtube.com/@chefchepkwony?si=7pXRTwIQnaISMVxc")],
            [InlineKeyboardButton("📌 Pinterest", url="https://pinterest.com/chepkwonyben/")],
            [InlineKeyboardButton("💬 WhatsApp", url="https://wa.me/message/XEALBDXUXVHQA1")],
            [InlineKeyboardButton("🎮 Discord", url="https://discord.com/users/chefchepkwonyke")],
        ]

        await update.message.reply_text(
            "🌍 Follow Chef Chepkwony everywhere!",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # CONTACT

    elif text == "📞 Contact Me":

        await update.message.reply_text(
            "📧 Email: chepkwonyben04@gmail.com"
        )

    else:

        await update.message.reply_text(
            "Please choose an option from the menu."
        )


# ==========================
# MAIN
# ==========================

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, buttons)
)

print("🤖 Bot is running...")

app.run_polling()