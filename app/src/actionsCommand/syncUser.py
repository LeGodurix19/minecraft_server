from models.permissionUsers import PermissionUser
from db_init import SessionLocal, init_db
from models.syncUsers import SyncUser

async def syncUser(message, client, arguments, bot):
    try:
        if len(arguments) == 0:
            await message.channel.send(f'Error: ```!sync <tagname>```')
            return
        elif len(arguments) != 1:
            await message.channel.send(f'Error: Invalid number of arguments.')
            return
        tagname = arguments[0]
        db = SessionLocal()
        sync_user = SyncUser(minecraft_username=tagname, user_id=message.author.id, username=message.author.name)
        permission_user = PermissionUser(user_id=message.author.id, permission=0)
        db.add(sync_user)
        db.add(permission_user)
        db.commit()
        db.refresh(sync_user)
        db.refresh(permission_user)
        db.close()
        await message.channel.send(f'User {tagname} synced. You can now execute commands. Use !help to see the list of commands.')
    except Exception as e:
        await message.channel.send(f'Error: {e}')