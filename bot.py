import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('EternityXBot')

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up bot with command prefix and intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Required for role checks
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)  # Disable default help command

# Add role checks
def is_admin():
    async def predicate(ctx):
        return ctx.author.guild_permissions.administrator
    return commands.check(predicate)

def is_moderator():
    async def predicate(ctx):
        return any(role.name.lower() in ['moderator', 'admin'] for role in ctx.author.roles)
    return commands.check(predicate)

# Event: Bot is ready and connected
@bot.event
async def on_ready():
    logger.info(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name="!help for commands"))

# Basic commands that don't require Web3
@bot.command(name='festival', help='Details about the Visual World Music Festival')
async def festival(ctx):
    embed = discord.Embed(
        title="Visual World Music Festival 2026",
        description="The world's first blockchain-powered music experience!",
        color=0x00ff00
    )
    embed.add_field(
        name="📅 Date & Time",
        value="January 15-17, 2026\n2:00 PM - 12:00 AM Daily",
        inline=False
    )
    embed.add_field(
        name="📍 Location",
        value="MMRDA Grounds, Bandra Kurla Complex\nMumbai, Maharashtra 400051",
        inline=False
    )
    embed.add_field(
        name="Features",
        value="• Holographic Performances\n• Interactive AR Zones\n• ETX-Powered Transactions\n• Exclusive NFT Collectibles",
        inline=False
    )
    await ctx.send(embed=embed)

@bot.command(name='help', help='List all commands')
async def help_command(ctx):
    embed = discord.Embed(
        title="EternityXBot Commands",
        description="Use `!command` to interact with the bot.",
        color=0x0000FF
    )
    embed.add_field(name="Festival Commands", value="""
        `!festival` - Festival information
        `!help` - Show this help message
    """, inline=False)
    embed.set_footer(text="Follow @EternityX on X for updates!")
    await ctx.send(embed=embed)

if __name__ == "__main__":
    try:
        bot.run(TOKEN)
    except Exception as e:
        logger.error(f"Bot stopped due to error: {str(e)}")