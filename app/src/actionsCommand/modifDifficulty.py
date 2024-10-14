from externalFunctions.checkExec import checkExec


async def modifDifficulty(message, client, arguments, bot):
    # checkExec('difficulty', message.author.id)
    
    try:
        if len(arguments) == 0:
            await message.channel.send(f'Error: ```!difficulty <easy|normal|hard>```')
            return
        elif len(arguments) != 1:
            await message.channel.send(f'Error: Invalid number of arguments.')
            return
        tagname = arguments[0]
        container = client.containers.get('server_minecraft-mc-1')
        if tagname == "easy":
            container.exec_run(f'rcon-cli "/difficulty easy"')
        elif tagname == "normal":
            container.exec_run(f'rcon-cli "/difficulty normal"')
        elif tagname == "hard":
            container.exec_run(f'rcon-cli "/difficulty hard"')
        else:
            await message.channel.send(f'Error: Difficulty not found.')
            return
        await message.channel.send(f'Difficulty changed to {tagname}.')
    except Exception as e:
        await message.channel.send(f'Error: {e}')