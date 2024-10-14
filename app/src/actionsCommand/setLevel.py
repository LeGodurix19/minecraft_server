
from requests import Session
from models.syncUsers import SyncUser
from models.permissionUsers import PermissionUser
from db_init import SessionLocal


async def setLevel(message, client, arguments, bot):
    # checkExec('difficulty', message.author.id)
    
    try:
        if len(arguments) != 2:
            await message.channel.send(f'Error: ```!setLevel <minecraft_tagname> <0|1|2|3>```')
            return
        user_tag = arguments[0]
        permissionLevel = arguments[1]
        db = SessionLocal()
        user_id = db.query(SyncUser).where(SyncUser.minecraft_username == user_tag).all()
        user_id = user_id[0].user_id
        set_permission_level(db, user_id, permissionLevel)
        await message.channel.send(f'User {user_tag} permission level set to {permissionLevel}.')
        db.close()
        
    except Exception as e:
        await message.channel.send(f'Error: {e}')
        
def set_permission_level(db: Session, user_id: int, permission_level: str):
    # Vérifiez si l'utilisateur existe déjà dans la base de données
    existing_user = db.query(PermissionUser).filter(PermissionUser.user_id == user_id).first()
    
    if existing_user:
        # Mettre à jour le niveau de permission de l'utilisateur existant
        existing_user.permission = permission_level
    else:
        # Créer une nouvelle entrée pour l'utilisateur
        new_user = PermissionUser(user_id=user_id, permission=permission_level)
        db.add(new_user)
    
    # Commit les changements à la base de données
    db.commit()