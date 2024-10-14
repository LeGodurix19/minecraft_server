import logging
import docker
import discord

async def inGame(message, client, arguments, bot):
    try:
        docker_client = docker.from_env()
        container = docker_client.containers.get('server_minecraft-mc-1')

        # Obtenir les informations des joueurs connectés via la commande 'list' de Minecraft
        exec_command = container.exec_run('rcon-cli list')
        player_info = exec_command.output.decode('utf-8').strip()
        
        # Extraire le nombre de joueurs et leurs identifiants
        player_lines = player_info.split(': ')
        if len(player_lines) > 1:
            players_inGame = player_lines[1].split(', ')
        else:
            players_inGame = ["none"]
        
        # Construire l'embed de réponse
        embed = discord.Embed(
            title="Players in Game",
            color=discord.Color.blue()
        )
        for player in players_inGame:
            embed.add_field(
                name=player,
                value="",
                inline=False
            )
        
        await message.channel.send(embed=embed)
    except docker.errors.APIError as e:
        await message.channel.send(f'Error executing Docker command: {e}')
    except Exception as e:
        await message.channel.send(f'Error: {e}')