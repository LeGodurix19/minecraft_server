import logging
import docker
import discord

async def statusServer(message, client, arguments, bot):
    try:
        docker_client = docker.from_env()
        container = docker_client.containers.get('server_minecraft-mc-1')
        status = container.status
        
        # Obtenir les statistiques du conteneur Docker
        stats = container.stats(stream=False)
        mem_usage = stats['memory_stats']['usage']
        mem_limit = stats['memory_stats']['limit']
        mem_usage_mb = mem_usage / (1024 * 1024)
        mem_limit_mb = mem_limit / (1024 * 1024)
        
        # Obtenir les informations des joueurs connectés via la commande 'list' de Minecraft
        exec_command = container.exec_run('rcon-cli list')
        player_info = exec_command.output.decode('utf-8').strip()
        
        # Extraire le nombre de joueurs et leurs identifiants
        player_lines = player_info.split(': ')
        if len(player_lines) > 1:
            players_inGame = player_lines[1].split(', ')
        else:
            players_inGame = []
        
        num_players = len(players_inGame)
        
        # Construire l'embed de réponse
        embed = discord.Embed(
            title="Server Status",
            description="Current status of the Minecraft server",
            color=discord.Color.blue()
        )
        embed.add_field(name="Status", value=status, inline=False)
        embed.add_field(
            name="Docker RAM Usage",
            value=f"{mem_usage_mb:.2f} MB / {mem_limit_mb:.2f} MB ({(mem_usage_mb/mem_limit_mb) * 100:.2f}%)",
            inline=False
        )
        embed.add_field(name="Number of Players Connected", value=str(num_players), inline=False)
        embed.add_field(
            name="Player Logins",
            value=", ".join(players_inGame) if len(players_inGame) != 0 else "None",
            inline=False
        )
        
        await message.channel.send(embed=embed)
    except docker.errors.APIError as e:
        embed = discord.Embed(
            title="Error",
            description=f"Error executing Docker command: {e}",
            color=discord.Color.red()
        )
        await message.channel.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="Error",
            description=f"An error occurred: {e}",
            color=discord.Color.red()
        )
        await message.channel.send(embed=embed)