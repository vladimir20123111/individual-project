from db_logic import *
from config import *
from telebot import TeleBot

bot = TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, """Привет! Я бот-менеджер проектов
Помогу тебе сохранить твои проекты и информацию о них!) 
""")

@bot.message_handler(commands=['create'])
def start_command(message, self):
    id = message.chat.id
    name = bot.send_message(message.chat.id, """напишыте названия проекта""")
    info = bot.send_message(message.chat.id, """напишыте описание проекта""")
    conn = sqlite3.connect(self.DATABASE)
    with conn:
        conn.execute('INSERT INTO projects VALUES (?, ?, ?)', (id, name, info))
    conn.commit()

    
if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    bot.infinity_polling()