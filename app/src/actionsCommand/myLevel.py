from models.permissionUsers import PermissionUser
from db_init import SessionLocal


async def myLevel(message, client, arguments, bot):
    # checkExec('difficulty', message.author.id)
    
    try:
        db = SessionLocal()
        permissionsUser = db.query(PermissionUser).where(PermissionUser.user_id == message.author.id).all()
        if len(permissionsUser) == 0:
            db.close()
            await message.channel.send(f'You are not in sync with the bot. Please exec !sync <mincraft_tag>.')
            return
        await message.channel.send(f'Your permission level is {permissionsUser[0].permission}.')
        db.close()
        
    except Exception as e:
        await message.channel.send(f'Error: {e}')