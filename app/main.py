from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random
import secret_token

bot = Bot(secret_token.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Welcome!\nPlease, enter /help command to get the list of available commands")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(
        "The list of available commands: \n/help: see the options \n/print text: print the given text \n/roll: roll a dice \n/flip: flip a coin \n/rand: get a random number (1-100) \n/whoami: user info")


@dp.message_handler(commands=['print'])
async def process_print_command(message: types.Message):
    text = message.get_args()
    if not text:
        return await message.reply("Here could've been your ad")
    await message.reply(str(text), reply=False)


@dp.message_handler(commands=['roll'])
async def process_roll_command(message: types.Message):
    await bot.send_dice(message.chat.id)


@dp.message_handler(commands=['flip'])
async def process_flip_command(message: types.Message):
    if random.randint(0, 1):
        await message.reply("HEADS")
    else:
        await message.reply("TAILS")


@dp.message_handler(commands=['rand'])
async def process_rand_command(message: types.Message):
    num = random.randint(1, 100)
    if (num == 100):
        await message.reply("Congrats! You got 100 out of 100!")
    else:
        await message.reply("Try again! You got only " + str(num) + " out of 100")


@dp.message_handler(commands=['whoami'])
async def process_whoami_command(message: types.Message):
    await message.reply(
        "id: " + str(message.chat.id) + "\nusername: " + str(message.chat.username) + "\nfirst name: " + str(
            message.chat.first_name) + "\nlast name: " + str(message.chat.last_name))


@dp.message_handler()
async def process_message(message: types.Message):
    await message.reply("Please, enter /help command to see the options")


if __name__ == '__main__':
    executor.start_polling(dp)
