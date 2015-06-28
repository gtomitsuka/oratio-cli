clihelp = {
    "init": """Takes the ID of a module, downloads the data from the Oratio
server and puts it in the working directory as module.json.

oratio-cli init [module_id]

In case module_id is not provided as an argument, it has to be inputted through
STDIN.""",
    "auth": """Requests the OAuth token for access to the Oratio servers.
First, open your browser and log in, then paste the token on the CLI.

oratio-cli auth""",
    "rmsession": """Deletes the file that holds your Oratio OAuth Token.

oratio-cli rmsession""",
    "status": """Shows a list of files that would be included in the module.
Takes .oratio-ignore in account.

oratio-cli status""",
    "ignored": """Shows a list of files that have been ignored by
.oratio-ignore.

oratio-cli ignored""",
    "compress": """Compresses all files in the working directory (that are not
ignored by .oratio-ignore) into an oratiomodule.tar.gz file.

oratio-cli compress""",
    "publish": """Uploads the oratiomodule.tar.gz file in the working directory
to the Oratio Marketplace.

oratio-cli publish""",
    "quit": "Can only be used interactively. Quits the interactive console",
    "help": """Shows help for a specific command.

oratio-cli help <command>"""
}
