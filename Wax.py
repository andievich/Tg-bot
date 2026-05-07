import re
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

phones = set()

def normalize_phone(text):
    digits = re.sub(r'\D', '', text)

    if len(digits) == 11 and digits.startswith('8'):
        digits = '7' + digits[1:]

    elif len(digits) == 10:
        digits = '7' + digits

    if len(digits) == 11 and digits.startswith('7'):
        return digits

    return None


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    found = re.findall(r'[\d\+\-\(\)\s]{10,20}', text)

    for item in found:
        phone = normalize_phone(item)

        if phone:
            phones.add(phone)
            print(phone)

    with open("phones.txt", "w") as f:
        for p in sorted(phones):
            f.write(p + "\n")


app = 8434229506:AAExBKba1dUhfpmfQbPSzlpgkVDw03ZDjuU

app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()
