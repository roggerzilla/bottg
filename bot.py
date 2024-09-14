import asyncio
import sys
from telegram import Update
from telegram.ext import Application, CommandHandler
import random

# Token del bot (el que obtuviste de BotFather)
TOKEN = '7273590738:AAHA3F05cvkKJodzPYAVGvNGMuRfRDtHncc'

# Lista de participantes
participantes = []

# Comando para que los usuarios se unan
async def start(update: Update, context):
    user = update.message.from_user
    if user.username not in participantes:
        participantes.append(user.username)
        await update.message.reply_text(f'{user.username} ha sido añadido a la lista de jugadores.')
    else:
        await update.message.reply_text(f'{user.username} ya está en la lista.')

# Comando para elegir quién pregunta y quién responde
async def spin_bottle(update: Update, context):
    if len(participantes) < 2:
        await update.message.reply_text("Necesitas al menos 2 participantes para jugar.")
        return

    preguntador = random.choice(participantes)
    respondedor = random.choice(participantes)

    while preguntador == respondedor:
        respondedor = random.choice(participantes)

    await update.message.reply_text(f'{preguntador} hará la pregunta a {respondedor}!')

# Configuración del bot
def main():
    # Crea la aplicación del bot
    application = Application.builder().token(TOKEN).build()

    # Añadir manejadores de comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("spin", spin_bottle))

    # Iniciar el bot con polling
    application.run_polling()

if __name__ == '__main__':
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

    main()
