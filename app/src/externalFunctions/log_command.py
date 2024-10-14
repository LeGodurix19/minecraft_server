from db_init import SessionLocal, init_db
from models.commandLogs import CommandLog

def log_command(command, arguments, user_id):
    print(f'Logging command: {command} {arguments} {user_id}')
    db = SessionLocal()
    command_log = CommandLog(command=command, arguments=arguments, user_id=user_id)
    db.add(command_log)
    db.commit()
    db.refresh(command_log)
    db.close()