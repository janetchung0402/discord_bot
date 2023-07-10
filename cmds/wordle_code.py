from urllib.request import urlopen
import random
# myURL = urlopen("https://gist.githubusercontent.com/cfreshman/d97dbe7004522f7bc52ed2a6e22e2c04/raw/633058e11743065ad2822e1d2e6505682a01a9e6/wordle-nyt-words-14855.txt")
# lines = myURL.readlines()
# print(len(lines))
# for i in lines[10]:
#     print(chr(i),i)
# print(lines[10])
#  
#https://gist.githubusercontent.com/cfreshman/d97dbe7004522f7bc52ed2a6e22e2c04/raw/633058e11743065ad2822e1d2e6505682a01a9e6/wordle-nyt-words-14855.txt

# myURL = urlopen("https://gist.githubusercontent.com/cfreshman/d97dbe7004522f7bc52ed2a6e22e2c04/raw/633058e11743065ad2822e1d2e6505682a01a9e6/wordle-nyt-words-14855.txt")
#         lines = myURL.readlines()
#         ret = random.randint(0,len(lines))
#         save=[]
#         test_ans=[]
#         a=False
#         for i in lines[ret]:
#             save.append(chr(i))
#         save.pop()
#         for i in ans:
#             test_ans.append(i)
#         for line in lines:
#             for i in line:
#                 save.append(chr(line))
#                 save.pop()
#             if test_ans==save:
#                 a=True
#                 break
#             else:
#                 continue
#         if a==False:
#             await ctx.send("這好像不是個單字")

# myURL = urlopen("https://gist.githubusercontent.com/cfreshman/d97dbe7004522f7bc52ed2a6e22e2c04/raw/633058e11743065ad2822e1d2e6505682a01a9e6/wordle-nyt-words-14855.txt")
# lines = myURL.readlines()
# ret = random.randint(0,len(lines))
# correct=[]
# for i in lines[ret]:
#     correct.append(chr(i))
# correct.pop()
# print(correct)
'''
ans=input()
test_ans=[]
for i in ans:
        test_ans.append(i)
for line in lines:
    for i in line:
        save.append(chr(line))
        save.pop()
    if test_ans==save:
        a=True
        break
    else:
        continue
if a==False:
    print("這好像不是個單字")
'''

'''
list1=[]
ans=["a","b","c","d","e"]
word=input()
for i in word:
    list1.append(i)
for i in range(len(list1)):
    if list1[i]==ans[i]:
        key=ans[i]
        print(chr(ord(key)-ord("a")+ord("A")),end="")
    elif list1[i] in ans:
        print(list1[i],end="")
    else:
        print("#",end="")
'''

