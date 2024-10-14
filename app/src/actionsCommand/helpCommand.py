import discord

async def helpCommand(listCommand):
    embed = discord.Embed(
        title="Liste des commandes",
        description="Les commandes disponibles sont ( ! signifie argument(s) non nécessaire(s) ) :",
        color=discord.Color.blue()
    )
    embed.add_field(
            name=f"Permissions:",
            value=f"0: Utilisateur\n1: Modérateur\n2: Administrateur\n3: Propriétaire",
            inline=False
        )
    listCommand = sorted(listCommand, key=lambda x: x['permission'])
    for struct in listCommand:
        arguments = ""
        if struct['arguments'] is not None:
            for elem in struct['arguments']:
                arguments += f"<{elem}> " if elem is not None else ""
        level = struct['permission']
        title = struct['command'][0].upper() + struct['command'][1:]
        command = struct['command']
        details = struct['help']
        embed.add_field(
            name=f"__**{title}:**__",
            value=f"*Niveau de permission*: {level}\n{details}\n```!{command} {arguments}```",
            inline=False
        )
    return embed