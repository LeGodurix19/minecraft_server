import datetime
from db_init import SessionLocal, init_db
from models.commandLogs import CommandLog

async def checkExec(command, user_id):
    try:
        db = SessionLocal()
        command_logs = db.query(CommandLog)\
                        .where(CommandLog.user_id == user_id)\
                        .where(CommandLog.command == command)\
                        .where(CommandLog.timestamp >= datetime.datetime.now() - datetime.timedelta(days=1))\
                        .all()
        db.close()
        if len(command_logs) >= 5:
            return f'Error: You have executed {command} 5 times in the last 24 hours. Please wait.'

    except Exception as e:
        return f'Error: {e}'