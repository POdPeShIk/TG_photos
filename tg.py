import telegram
import os
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv(".env")
    token=os.environ['TOKEN']
    chat_id= "@testingmain"
    file_id='images/APOD/image_apod_1.jpg'
    bot = telegram.Bot(token="7023144175:AAFNrL2XdYfO1olmN8gDxc7py26eInzOw6g")
    bot.send_message(chat_id="@testingmain", text="I'm sorry Dave I'm afraid I can't do that.")
    message = bot.send_document(chat_id="@testingmain", document=open('images/APOD/image_apod_1.jpg', 'rb'))
    message.document.file_id
    print(bot.get_me())