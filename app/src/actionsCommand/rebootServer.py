import asyncio
from externalFunctions.checkExec import checkExec


async def rebootServer(message, client, arguments, bot):
    # checkExec('reboot', message.author.id)
    
    await message.channel.send('Rebooting the Minecraft server in 5 minutes...')
    if arguments:
        new_level = arguments[0]
        success = await modify_env_file(new_level)
        if success:
            await message.channel.send(f'Environment file updated with LEVEL={new_level}.')
        else:
            await message.channel.send('Failed to update the environment file.')
            return
    
    try:
        container = client.containers.get('server_minecraft-mc-1')
        container.exec_run('rcon-cli "/say The server will reset in 5 min"')
        await asyncio.sleep(240)  # Attendre 4 minutes
        container.exec_run('rcon-cli "/say The server will reset in 1 min"')
        await asyncio.sleep(60)  # Attendre 1 minute
        container.restart()
        await message.channel.send('Minecraft server rebooted.')
    except Exception as e:
        await message.channel.send(f'Error: {e}')   
        
        
# async def modify_env_file(level_name):
#     env_file_path = '/data/server.properties'
#     new_content = []

#     # Read the existing file and modify the relevant line
#     try:
#         with open(env_file_path, 'r') as file:
#             lines = file.readlines()
#             for line in lines:
#                 if line.startswith('level-name='):
#                     new_content.append(f'level-name={level_name}\n')
#                 else:
#                     new_content.append(line)
        
#         # Write the modified content back to the file
#         with open(env_file_path, 'w') as file:
#             file.writelines(new_content)

#         return True

#     except Exception as e:
#         print(f"An error occurred while modifying the .env_minecraft file: {e}")
#         return False
    
    
async def modify_env_file(level_name):
    env_file_path = '/data/server.properties'
    try:
        # Open the file and read all lines
        with open(env_file_path, 'r') as file:
            lines = file.readlines()
        # Write the updated content back to the file
        with open(env_file_path, 'w') as file:
            for line in lines:
                if line.startswith('level-name='):
                    file.write(f'level-name={level_name}\n')
                else:
                    file.write(line)
        return True
    except Exception as e:
        print(f"An error occurred while modifying the server.properties file: {e}")
        return False