'''
可以複製todolist的架構, 但請記得更改class & function的名稱
這個檔案的名字也可以改
'''

import discord
from discord.ext import commands
from core import Cog_Extension

class Custom2(Cog_Extension):
    def __init__(self, bot):
        self.todo = []
        super().__init__(bot)
    pass

async def setup(bot):
    await bot.add_cog(Custom2(bot))