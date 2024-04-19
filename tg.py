import telegram
import os
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv(".env")
    token=os.environ['TOKEN']
    bot = telegram.Bot(token="7023144175:AAFNrL2XdYfO1olmN8gDxc7py26eInzOw6g")
    bot.send_message(chat_id="@testingmain", text="I'm sorry Dave I'm afraid I can't do that.")
    print(bot.get_me())