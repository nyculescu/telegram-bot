import telegram
# Updater lib is used to listen to new messages being sent to our bot and
# then a message handler with the dispatcher class
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
# from tracker import get_prices
# import cryptocompare
import coinmarketcapapi
from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError

telegram_bot_token = "1736568748:AAFybS5euK76Ec2JNueYSN8jy8439MGhZDw"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

# def crypto_get_prices():
#     crypto_data = get_prices()
#     for i in crypto_data:
#         coin = crypto_data[i]["coin"]
#         price = crypto_data[i]["price"]
#         change_day = crypto_data[i]["change_day"]
#         change_hour = crypto_data[i]["change_hour"]
#         message += f"Coin: {coin}\nPrice: ${price:,.2f}\nHour Change: {change_hour:.3f}%\nDay Change: {change_day:.3f}%\n\n"
#         return message

command_list = "/start\n/stop-bot\n/eth-price\n" #TODO: make it tuple of callbaks and text

def help_list(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=command_list)

# def start(update, context):
#     chat_id = update.effective_chat.id
#     message = "Hai sa traiesti! Aici botu' tau personal ;)"
#     # used the send_message method provided by the Telegram library to send messages to our users 
#     # when they expect a response. The method takes in a parameter called chat_id that is uniquely assigned to every Telegram user along with the message we want to send.
#     context.bot.send_message(chat_id=chat_id, text=message)

def stop_bot(update, context):
    updater.stop()
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bot stopped")

# def eth_price(update, context):
#     # exchange = 'binancedex'
#     # eth_usdt = cryptocompare.get_avg('ETH', currency='USD', exchange=exchange)
#     eth_usd = cryptocompare.get_price('ETH', currency='USD', full=False)
#     # eth_usd = "1 Eth = %d USD\nMarket: %d\n", eth_usd, "Binance"
#     context.bot.send_message(chat_id=update.effective_chat.id, text=eth_usd)

def eth_price(update, context):
    r = CoinMarketCapAPI('{a3301629-efa1-417b-88e5-59bcef11d14b}').cryptocurrency_info(symbol='BTC')
    print('Ethereum price: ', r.data)

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    # print(update.message.text)

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

# A command handler is a block of code called when a bot user triggers a certain command
# dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("stop_bot", stop_bot))
dispatcher.add_handler(CommandHandler("help", help_list))
dispatcher.add_handler(CommandHandler("eth", eth_price))

dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))

print("bot started")

updater.start_polling()
