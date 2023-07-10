import discord
from discord.ext import commands
import json 
from core import Cog_Extension
import urllib
import random
from urllib.request import urlopen


confirm=False
count=0
class Wordle(Cog_Extension):
    # Initialization 
    def __init__(self, bot):
        super().__init__(bot)

    @commands.command()
    async def Play(self, ctx):
        global confirm
        global correct
        global count
        await ctx.send("#####")
        pass

        '''
        TODO 
        要在爬好的單字庫中, 隨機挑選一個單字做為預設的答案
        '''
        if confirm==False: # 選一個答案 放到correct(list)裡 用confirm判斷有沒有寫過
            myURL = urlopen("https://gist.githubusercontent.com/cfreshman/d97dbe7004522f7bc52ed2a6e22e2c04/raw/633058e11743065ad2822e1d2e6505682a01a9e6/wordle-nyt-words-14855.txt")
            lines = myURL.readlines()
            ret = random.randint(0,len(lines))
            correct=[]
            for i in lines[ret]:
                correct.append(chr(i))
            correct.pop()
            confirm=True
            #print(correct)
        print(correct)
    

    
    @commands.command()
    async def Ask(self, ctx, ans):
        global confirm
    
        global correct
        global count
        count+=1
        time=0
        '''
        ans 是使用者傳入的猜測答案

        TODO
        1. 沒有play直接ask : 請先輸入 Play 指令 V
        2. 不是5個字的單字 : 請輸入5個字母的單字 V
        3. 不是單字的英文組合(不在單字庫中) : 這好像不是個單字
        4. 答對 : 恭喜答對!!! V
        5. 猜太多次了 : 真可惜, 答案是{answer} V
        '''
        list1=[]  #把輸入的東西放到list1裡
        for i in ans:
            list1.append(i)

        if confirm==False: # 請先輸入 Play 指令
            await ctx.send("請先輸入 Play 指令")

        if len(list1)!=5: #不是5個字的單字
            await ctx.send("請輸入5個字母的單字")


        output=[]
        for i in range(len(list1)):  #開始對比
            # 大寫 = 位置對字母也對
            # 小寫 = 字母對但位置不對
            # = 都不對
            if list1[i]==correct[i]:
                key=list1[i]
                output.append(chr(ord(key)-ord("a")+ord("A")))
                time+=1
            elif list1[i] in correct:
                output.append(list1[i])
            else:
                output.append("#")
        if confirm==True:
            if time==5: #全對
                confirm=False
                count=0
                await ctx.send("恭喜答對!!")

            elif count==6: #猜太多次
                await ctx.send("真可惜, 答案是"+correct[0]+correct[1]+correct[2]+correct[3]+correct[4])
                confirm=False
                count=0
            else: #正常狀況
                await ctx.send(output[0]+output[1]+output[2]+output[3]+output[4])

async def setup(bot):
    await bot.add_cog(Wordle(bot))