import asyncio


async def stopServer(message, client, arguments, bot):
    await message.channel.send('Stopping the Minecraft server in 5 minutes...')
    try:
        container = client.containers.get('server_minecraft-mc-1')
        container.exec_run('rcon-cli "/say The server will reset in 5 min"')
        await asyncio.sleep(240)  # Attendre 4 minutes
        container.exec_run('rcon-cli "/say The server will reset in 1 min"')
        await asyncio.sleep(60)  # Attendre 1 minute
        container.stop()
        await message.channel.send('Minecraft server stopped.')
    except Exception as e:
        await message.channel.send(f'Error: {e}')