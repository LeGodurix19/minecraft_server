import os
from db_init import SessionLocal
from actionsCommand import rebootServer, startServer, statusServer, stopServer, whitelistPlayer, modifDifficulty, helpCommand, syncUser, inGame

from models.commandLogs import CommandLog
from models.syncUsers import SyncUser
from models.permissionUsers import PermissionUser

from externalFunctions.log_command import log_command

from functions_list import functions

async def executeCommand(message, client, bot):
    content = message.content.split()
    if len(content) == 0:
        return
    command = content[0]
    arguments = content[1:]
    
    if command[0] != '!':
        return

    if str(message.channel.id) != os.getenv('ID_CHANNEL'):
        return
    
    command = command[1:]
    
    if command == "sync":
        await syncUser.syncUser(message, client, arguments, bot)
        return
    db = SessionLocal()
    command_logs = db.query(SyncUser).where(SyncUser.user_id == message.author.id).all()
    if len(command_logs) == 0:
        db.close()
        await message.channel.send(f'You are not in sync with the bot. Please exec !sync <mincraft_tag>.')
        return
    db.close()
    
    db = SessionLocal()
    permission = db.query(PermissionUser).where(PermissionUser.user_id == message.author.id).all()
    if len(permission) == 0:
        db.close()
        await message.channel.send(f'You are not in sync with the bot. Please exec !sync <mincraft_tag>.')
        return
    permission = permission[0].permission
    db.close()
    
    log_command(command, ' '.join(arguments), message.author.id)
    
    for function in functions:
        if command == function['command']:
            if function['permission'] > permission:
                await message.channel.send(f'You don\'t have the permission to exec this command.')
                return
            if function['command'] == "help":
                await message.channel.send(embed=await function['function'](functions))
            elif isinstance(function['function'], str):
                await message.channel.send(function['function'])
            else:
                await function['function'](message, client, arguments, bot)
            return
    return

