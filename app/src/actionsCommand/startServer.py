async def startServer(message, client, arguments, bot):
    await message.channel.send('Starting the Minecraft server...')
    try:
        container = client.containers.get('server_minecraft-mc-1')
        container.start()
        await message.channel.send('Minecraft server started.')
    except Exception as e:
        await message.channel.send(f'Error: {e}')