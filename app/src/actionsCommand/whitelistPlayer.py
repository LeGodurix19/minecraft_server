async def whitelistPlayer(message, client, arguments, bot):
    try:
        if len(arguments) == 0:
            await message.channel.send(f'Error: ```!whitelist <minecraft_tagname>```')
            return
        elif len(arguments) != 1:
            await message.channel.send(f'Error: Invalid number of arguments.')
            return
        tagname = arguments[0]
        container = client.containers.get('server_minecraft-mc-1')
        container.exec_run(f'rcon-cli "/whitelist add {tagname}"')
        await message.channel.send(f'Player {tagname} added to the whitelist.')
    except Exception as e:
        await message.channel.send(f'Error: {e}')