"""
> Xythrion
> Copyright (c) 2020 Xithrius
> MIT license, Refer to LICENSE for more info
"""


from collections import OrderedDict, defaultdict
from random import choice, randint

import discord
from discord.ext import commands as comms

from xythrion.utils import codeblock


class Randoms(comms.Cog):
    """Picking a bunch of different things at random (games based on random chance).

    Attributes:
        bot (:obj:`comms.Bot`): Represents a Discord bot.
        card_values (list): All possible values for a card
        card_suites (list): All possible suites for a card

    """

    def __init__(self, bot):
        """Creating important attributes for this class.

        Args:
            bot (:obj:`comms.Bot`): Represents a Discord bot.

        """
        self.bot = bot
        self.card_values = [*range(2, 11), 'Jack', 'Queen', 'King', 'Ace']
        self.card_suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        self.rps_options = {
            'rock': ['fire', 'scissors', 'snake', 'human', 'wolf', 'sponge', 'tree'],
            'paper': ['air', 'rock', 'water', 'devil', 'dragon', 'lightning'],
            'fire': ['scissors', 'paper', 'snake', 'human', 'tree', 'wolf', 'sponge'],
            'scissors': ['air', 'tree', 'paper', 'snake', 'human', 'wolf', 'sponge'],
            'gun': ['rock', 'tree', 'fire', 'scissors', 'snake', 'human', 'wolf'],
            'water': ['devil', 'dragon', 'rock', 'fire', 'scissors', 'gun', 'lightning'],
            'air': ['fire', 'rock', 'water', 'devil', 'gun', 'dragon', 'lightning'],
            'sponge': ['paper', 'air', 'water', 'devil', 'dragon', 'gun', 'lightning'],
            'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
            'devil': ['rock', 'fire', 'scissors', 'gun', 'lightning', 'snake', 'human'],
            'dragon': ['devil', 'lightning', 'fire', 'rock', 'scissors', 'gun', 'snake'],
            'lightning': ['gun', 'scissors', 'rock', 'tree', 'fire', 'snake', 'human'],
            'snake': ['human', 'wolf', 'sponge', 'tree', 'paper', 'air', 'water'],
            'wolf': ['sponge', 'paper', 'air', 'water', 'lightning', 'dragon', 'devil'],
            'tree': ['wolf', 'dragon', 'sponge', 'paper', 'air', 'water', 'devil']
        }

    """ Commands """

    @comms.command()
    async def dice(self, ctx: comms.Context, rolls: int = 1) -> None:
        """Rolls a die as many times as you want.

        Args:
            ctx (:obj:`comms.Context`): Represents the context in which a command is being invoked under.
            rolls (int, optional): The amount of times the die will be rolled.

        Returns:
            bool: Always None.

        Command examples:
            >>> [prefix]dice
            >>> [prefix]dice 100

        """
        if rolls > 10 or rolls < 0:
            return await ctx.send('`Rolls must be between 1 and 10.`')

        elif rolls > 1:
            s = sum([randint(1, 6) for x in range(rolls)]) / rolls
            avg = f'`Die was rolled {rolls} times. Average output: {round(s, 2)}`'

        else:
            avg = f'`Die was rolled once. Output: {randint(1, 6)}`'

        embed = discord.Embed(description=avg)

        await ctx.send(embed=embed)

    @comms.command()
    async def card(self, ctx: comms.Context, amount: int = 1) -> None:
        """Picks cards from a deck.

        Args:
            ctx (:obj:`comms.Context`): Represents the context in which a command is being invoked under.
            amount (int, optional): The amount of cards that will be picked.

        Returns:
            bool: Always None.

        Command examples:
            >>> [prefix]card
            >>> [prefix]card 10

        """
        if amount > 5 or amount < 0:
            return await ctx.send('`Rolls must be between 1 and 10.`')

        d = defaultdict(int)
        for _ in range(amount):
            d[f'{choice(self.card_values)} of {choice(self.card_suites)}'] += 1

        lst = OrderedDict(sorted(d.items()))
        lst = [f'({v}) {k}' for k, v in d.items()]

        embed = discord.Embed(description=codeblock(lst))

        await ctx.send(embed=embed)

    @comms.command(aliases=['rockpaperscissors'])
    async def RPS(self, ctx: comms.Context, option: str) -> None:
        """Plays a game of rock paper sissors against the bot.

        Args:
            ctx (:obj:`comms.Context`): Represents the context in which a command is being invoked under.
            option (str): The option that the user chooses.

        Returns:
            bool: Always None.

        Command examples:
            >>> [prefix]RPS
            >>> [prefix]rps wolf

        """
        option = option.lower()

        if option not in self.options.keys():
            url = 'https://umop.com/rps15.htm'
            block = f'`Unknown option "{option}". Please pick from the possible options:` ' + url

            await ctx.send(block)

        else:
            lst = list(self.options.keys())
            lst.remove(option)
            computer_choice = choice(lst)

            embed = discord.Embed(
                title=f'`Computer {"lost" if computer_choice in self.options[option] else "won"}`',
                description=f'`Computer picked {computer_choice}, and you picked {option}.`'
            )

            await ctx.send(embed=embed)


def setup(bot: comms.Bot) -> None:
    """The necessary function for loading in cogs within this file.

    Args:
        bot (:obj:`comms.Bot`): Represents a Discord bot.

    Returns:
        type(None): Always None.

    """
    bot.add_cog(Randoms(bot))
