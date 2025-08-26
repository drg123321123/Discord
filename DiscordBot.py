# Close and lock tickets in a forum. Commands: /resolve - closes and locks the ticket ; /resolve_name "YourName" - when using /resolve, it changes the tickets name to "[DONE "The name you choose when using /resolve_name"] + tickets original name

import discord
from discord.ext import commands
intents=discord.Intents.default()
intents.guilds=True
intents.members=True
bot=commands.Bot(command_prefix="!",intents=intents)
resolve_names={}
REQUIRED_ROLE="Mod On PM"
def has_mod_role(interaction:discord.Interaction):
    return any(role.name==REQUIRED_ROLE for role in interaction.user.roles)
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot is online as {bot.user}")
@bot.tree.command(name="resolve_name",description="Set your resolve name")
async def resolve_name(interaction:discord.Interaction,name:str):
    if not has_mod_role(interaction):
        await interaction.response.send_message("You don't have permission.",ephemeral=True)
        return
    resolve_names[interaction.user.id]=name
    await interaction.response.send_message(f"Your resolve name has been set to **{name}**",ephemeral=True)
@bot.tree.command(name="resolve",description="Close and lock a forum ticket")
async def resolve(interaction:discord.Interaction):
    if not has_mod_role(interaction):
        await interaction.response.send_message("You don't have permission.",ephemeral=True)
        return
    if not isinstance(interaction.channel,discord.Thread):
        await interaction.response.send_message("This command only works inside forum tickets.",ephemeral=True)
        return
    name=resolve_names.get(interaction.user.id,interaction.user.name)
    thread=interaction.channel
    new_name=f"[DONE {name}] {thread.name}"
    try:
        await thread.edit(name=new_name,locked=True,archived=True)
    except Exception as e:
        await interaction.response.send_message(f"Couldn't close the ticket: {e}",ephemeral=True)
        return
    await interaction.response.send_message(f"Ticket closed and renamed to **{new_name}**")
bot.run("BotToken")
