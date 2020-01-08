import random
import time
words=[]
print('what is your name')
#輸入玩家姓名#
name=input()
#歡迎玩家#
print('Hello '+ name +'. Time to play hangman!')
print(' ')
#等一秒#
time.sleep(1)
print('Start guessing...')
time.sleep(0.5)
#秘密字元設定#
import csv
#讀入題目
with open('wordbankj.csv', newline='') as csvfile:
    Question = list(csv.reader(csvfile))
    for row in Question:
        words.append(row[0])
word=random.choice(words)       
#創造一個變量#
guesses=''
#可猜的次數#
turns=10
#while loop#
while turns>0:
    #以0開頭的計數器#
    unfinished=0
    #每個在秘密字元中的字#
    for letter in word:
        #看玩家是否有猜到#
        if letter in guesses:
            #有的話，印出來#
            print(letter)
        else:
            #如果沒有，印空格#
            print('_')
            #未完成的空格
            unfinished=unfinished + 1
    #當空格等於0時
    if unfinished==0:
        print('you win!!!')
        break
    print('guess a letter!')
    #請玩家猜#
    guess=input()
    #不能猜超過一個字母
    while len(guess)>1:
        print('you could only guess one letter')
        guess=input()
    guesses+=guess
    #如果玩家的字不在秘密字元中#
    if guess not in word:
        #猜的次數減一#
        turns=turns-1
        #印錯誤#
        print('Wrong!')
        #印你還有幾次機會#
        print('You have', + turns, 'more guesses')
        #如果沒機會了#
        if turns==0:
        #印你輸了#
              print('You Lose!')
              print('the word is', word)
        


