import discord
from discord.ext import commands
import json 
from core import Cog_Extension
# git 
class TodoList(Cog_Extension):
    # Initialization 
    def __init__(self, bot):
        self.todo = []
        super().__init__(bot)
        
        '''
        todo 是一個 list 變數
        你可以在各個function中對self.todo做操作
        來當作模擬todolist

        你可能需要用到的function 
        list : append, remove, sort
        ctx.send(str)

        '''
        
    # Add todolist 
    # item 是要增加的待辨事項
    @commands.command()
    async def AddTodoList(self, ctx,item):
        self.item=item
        self.todo.append(item)
        await ctx.send(self.todo)
        pass 

    # Remove todolist
    # item 是要移除的待辨事項
    @commands.command()
    async def RemoveTodoList(self, ctx, item):
        self.item=item
        try :
            self.todo.remove(item)
            await ctx.send(self.todo)
        except:
            await ctx.send("此代辦事項不存在")
        pass 

    # Sort todolist
    @commands.command()
    async def SortTodoList(self, ctx):
        self.todo.sort()
        for item in self.todo:
            await ctx.send(item)
        if self.todo==[]:
            await ctx.send("沒有任何代辦事項")
        pass 


    # Clear todolist
    @commands.command()
    async def ClearTodoList(self, ctx):
       self.todo.clear()
       
       pass 

async def setup(bot):
    await bot.add_cog(TodoList(bot))

