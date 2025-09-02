import os
from discord import Intents, Client, Message
from dotenv import load_dotenv
from typing import Final
import responses  

# Cargar variables de entorno
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")


intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# ID PANDA
USUARIO_OBJETIVO_ID = 320190829564002306  

# Funcionalidad de mensajes
async def send_message(message: Message, user_message: str, usar_contradiccion=False) -> None:
    if not user_message:
        print(f"El usuario {message.author} no ha enviado un mensaje")
        return
    
    print(f"Mensaje recibido: {user_message}")

    if usar_contradiccion:
        message_to_send: str = responses.contradecir_mensaje(user_message)
    else:
        message_to_send: str = await responses.manejar_mensaje(user_message)

    await message.channel.send(message_to_send)

# Inicio de la ejecución del bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} está en línea!')

# Manejo de mensajes
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    # Si es el usuario objetivo → contradecir SIEMPRE
    if message.author.id == USUARIO_OBJETIVO_ID:
        await send_message(message, message.content, usar_contradiccion=True)

    # Si mencionan al bot → IA decide qué hacer
    elif client.user.mentioned_in(message) and message.author.id != USUARIO_OBJETIVO_ID:
        await send_message(message, message.content)

client.run(TOKEN)
