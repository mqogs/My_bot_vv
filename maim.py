
import telebot
import os

# بياناتك الخاصة
TOKEN = '8378581003:AAFDK1-vxH8I-o1LdNdVwY4nid7N4me-ZLM'
ADMIN_ID = 1899767509

# تهيئة البوت
bot = telebot.TeleBot(TOKEN)

# ملف لتخزين اليوزرات (بما أن القائمة طويلة)
USER_LIST_FILE = "users.txt"

def load_users():
    if os.path.exists(USER_LIST_FILE):
        with open(USER_LIST_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    return []

# أمر البداية للتحكم في الأداة
@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id == ADMIN_ID:
        bot.reply_to(message, "أهلاً يا مصطفى، الأداة مربوطة وجاهزة للعمل على الموقع.")
    else:
        bot.reply_to(message, "هذا البوت مخصص للمطور فقط.")

# مثال: أمر لجلب اليوزرات من القائمة اللي عطيتني إياها
@bot.message_handler(commands=['show_users'])
def show_users(message):
    users = load_users()
    if users:
        bot.reply_to(message, f"عدد اليوزرات الموجودة في الأداة: {len(users)}")
    else:
        bot.reply_to(message, "القائمة فارغة، تحتاج لإضافة اليوزرات.")

# تشغيل البوت
if name == "main":
    print("البوت متصل ويعمل الآن...")
    bot.polling(none_stop=True)
