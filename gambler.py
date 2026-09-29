from time import sleep;import discord;import datetime;import random;import asyncio;
from discord import Option;from datetime import timedelta;
from discord.ext import commands;from discord.ext.commands import MissingPermissions, MissingRequiredArgument;
intents = discord.Intents.default();intents.message_content = True;bot = discord.Bot(command_prefix="!", intents=intents);server = [1548684304819691743];
class test_button_view(discord.ui.View):
    def __init__(self, author_id: int, Bet_id: int, Member: discord.Member, Author: discord.Member):
        super().__init__();self.author_id = author_id;self.Bet_id = Bet_id;self.Member = Member;self.Author = Author;
    @discord.ui.button(label="Yes", style=discord.ButtonStyle.green)
    async def ybutton(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user.id != self.Bet_id:await interaction.respond(f'Not you! <@{interaction.user.id}>', ephemeral=True);return;
        await interaction.respond(f'<@{interaction.user.id}> accept has the bet');
        await interaction.message.edit(content="processing...", embed=None, view=None);
        await interaction.channel.send('uhhh');await asyncio.sleep(5);result = random.randint(1, 2);
        if result == 1:
            await interaction.channel.send(f'<@{self.author_id}> WIN');await interaction.channel.send(f'```ansi\n\u001b[2;33m[SERVER] <@{self.Bet_id}> get \u001b[2;31mtimeout\u001b[0m\u001b[2;33m by [SERVER] for <"Lost to timeout bet"> duration <1 minute>\u001b[0m```' );
            timeout_until = discord.utils.utcnow() + timedelta(minutes=1);
            await self.Author.timeout(until=timeout_until, reason='bet yourself for some reason');
        elif result == 2:
            await interaction.channel.send(f'<@{self.Bet_id}> WIN');await interaction.channel.send(f'```ansi\n\u001b[2;33m[SERVER] <@{self.Author.id}> get \u001b[2;31mtimeout\u001b[0m\u001b[2;33m by [SERVER] for <"Lost to timeout bet"> duration <1 minute>\u001b[0m```');
            timeout_until = discord.utils.utcnow() + timedelta(minutes=1);
            await self.Member.timeout(until=timeout_until, reason='bet yourself for some reason');self.stop();
    @discord.ui.button(label="No", style=discord.ButtonStyle.red)
    async def nbutton(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user.id != self.Bet_id:await interaction.respond(f'Not you! <@{interaction.user.id}>', ephemeral=True); return;
        await interaction.respond(f'<@{interaction.user.id}> not accept the bet');
        await interaction.message.edit(content="removing...", embed=None, view=None);self.stop();
@bot.slash_command(guild_ids = server, name='bet-timeout',description='idk')
async def timeout(ctx,member:Option(discord.Member,required=True)):
    view = test_button_view(author_id=member.id,Bet_id=ctx.author.id,Member = member,Author = ctx.author);
    if member.id == ctx.author.id:timeout_until = discord.utils.utcnow() + timedelta(minutes=5);await ctx.author.timeout(until=timeout_until,reason='bet yourself for some reason');await ctx.respond(
        f'<@{member.id}> bet yourself and got timeout for 5 minute for some reason');
    else:
        await ctx.send(f'<@{member.id}>');
        declared_bet = discord.Embed(title=f"{ctx.author} has declared a bet to you", color=discord.Color.red());
        declared_bet.add_field(name='Are you want to bet to him too', value=f'{ctx.author}?');
        declared_bet.add_field(name="loser get timeout for 1 minute", value='');
        declared_bet.set_thumbnail(url=ctx.author.avatar.url);await ctx.respond(embed=declared_bet, view=view);
@bot.slash_command(guild_ids = server, name='un-timeout',description='lazy to un-timeout')
async def un_timeout(ctx,member:Option(discord.Member,required=True)):await member.remove_timeout();await ctx.respond(f'<@{member.id}> has been untimed out.');
@bot.slash_command(guild_ids = server, name='un-timeout-all',description='lazy to un-timeout')
async def un_timeout_all(ctx,member:Option(discord.Member,required=False)):await member.remove_all_timeout();await ctx.respond(f'every people has been untimed out.');
@bot.slash_command(guild_ids=server, name='random-timeout', description='lazy to un-timeout')
async def random_timeout(ctx):
    user_ids = [PUT-USER-ON-HERE];
  target_id = random.choice(user_ids);
    try:
        member = await ctx.guild.fetch_member(target_id);
        timeout_until = discord.utils.utcnow() + timedelta(minutes=1);
        await member.timeout(until=timeout_until, reason='random timeout');
        await ctx.respond(f'<@{member.id}> has been randomly timed out for 1 minute.');
    except discord.NotFound:await ctx.respond(f"Tried to timeout <@{target_id}>, but they aren't in this server!");
    except discord.Forbidden:await ctx.respond(f"don't have enough permission to timeout <@{target_id}>");
@timeout.error
async def timeout_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.respond("can't timeout");
    else:
        raise error;
@un_timeout.error
async def remove_timeout_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.respond("can't remove time out");
    else:
        raise error;
bot.run('PUT-TOKEN-ON-HERE');
