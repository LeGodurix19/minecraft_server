from actionsCommand import rebootServer, startServer, statusServer, stopServer, whitelistPlayer, modifDifficulty, helpCommand, syncUser, inGame, myLevel, setLevel

functions = [
        {
            "command": "hello",
            "arguments": None,
            "function": "Hello!",
            "help": "Print Hello!",
            "permission": 0
        }, {
            "command": "up",
            "arguments": None,
            "function": startServer.startServer,
            "help": "Start the server",
            "permission": 2
        }, {
            "command": "down",
            "arguments": None,
            "function": stopServer.stopServer,
            "help": "Stop the server",
            "permission": 2
        }, {
            "command": "reboot",
            "arguments": ["!world_name"],
            "function": rebootServer.rebootServer,
            "help": "Reboot the server",
            "permission": 3
        }, {
            "command": "status",
            "arguments": None,
            "function": statusServer.statusServer,
            "help": "Get the status of the server (up or down, the memory usage, the number of players and the list of players)",
            "permission": 1
        }, {
            "command": "whitelist",
            "arguments": ["usertag_minecraft"],
            "function": whitelistPlayer.whitelistPlayer,
            "help": "Add a player to the whitelist",
            "permission": 1
        }, {
            "command": "help",
            "arguments": None,
            "function": helpCommand.helpCommand,
            "help": "Get the list of commands",
            "permission": 0
        }, {
            "command": "difficulty",
            "arguments": ["easy|normal|hard"],
            "function": modifDifficulty.modifDifficulty,
            "help": "Change the difficulty of the server",
            "permission": 2
        }, {
            "command": "inGame",
            "arguments": None,
            "function": inGame.inGame,
            "help": "Return the list of players in game",
            "permission": 0
        }, {
            "command": "myLevel",
            "arguments": None,
            "function": myLevel.myLevel,
            "help": "Return your level",
            "permission": 0
        }, {
            "command": "setLevel",
            "arguments": ["usertag_minecraft", "level"],
            "function": setLevel.setLevel,
            "help": "Set the level of a player",
            "permission": 3
        }
    ]