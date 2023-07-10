# Sprout2023py---

[Spec 簡報](https://hackmd.io/@Fireball0424/HkED_0UXn)


#To-do list
    使用一般對list的操作:
    append,remove,sort...

#Wordle
    confirm=False    #判斷有沒有傳過play
    count=0   #傳過幾次Ask，超過六次就挑戰失敗

    $Play :
    若confirm==False，
    用readlines()把所有單字存到list中，用randint選出一個數字(答案的索引值)
    將答案存到correct(list)中
    confirm=True

    $ask xxxxx:
    若輸入!=5:("請輸入5個字母的單字")
    若confirm==False，("請先輸入 Play 指令")

    開始比對，將輸入存到一個list1(list)中，並與correct比對
    每比對一次，count+=1，並將結果存到output(list)

    若count==6:
    宣布失敗並重新開始

    正常狀況:
    輸出output