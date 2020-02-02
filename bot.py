import yaml
from pathlib import Path

from discord import __version__ as discver, Activity, ActivityType
from discord.ext.commands import Bot

# using path to assign config.yaml to CONFIG_FILE
CONFIG_FILE = Path('config.yaml')

# opening our config file
with open(CONFIG_FILE, 'r') as yaml_file:
    config = yaml.safe_load(yaml_file)

# creating our bot object
bot = Bot(
    activity=Activity(
        name=f'{config["prefix"]}help | D&D 5e',
        type=ActivityType.watching
    ),
    command_prefix=config["prefix"],
    pm_help=True
)

# assign config file to bot
bot.config = config


def main():
    """Tries to load every cog and start up the bot"""
    for extension in bot.config['load_extensions']:
        try:
            bot.load_extension(extension)
        except:
            print(f'failed to load extension: {extension}')

    print("bot is up and running")
    bot.run(config['token'])


if __name__ == '__main__':
    main()
