# Stone,Paper,Scissor
import random,sys
print('stone,paper,scissor')
win=0
loss=0
tie=0
while True:
    print('%s win,%s loss,%s tie'%(win,loss,tie))
    while True:
        print('enter your option :(s)stone (p)paper (sc)scissors or (q)quit')
        playerchoice=input()
        if playerchoice=='q':
           sys.exit()
        if playerchoice == 's' or playerchoice == 'p' or playerchoice =='sc':
           break
        #print('type one of s,p,sc,q')
    if playerchoice == 's':
        print('stone versus   ')
    elif playerchoice == 'p':
        print('paper versus   ')
    elif playerchoice == 'sc':
        print('scissor versus   ')

    randomNumber=random.randint(1,3)
    if randomNumber==1:
        computerchoice='s'
        print('stone')
    elif randomNumber==2:
        computerchoice='p'
        print('paper')
    elif randomNumber==3:
        computerchoice='sc'
        print('scissor')
    if playerchoice==computerchoice:
        print('tie')
        tie=tie + 1
    elif playerchoice== 's' and computerchoice=='sc':
        print('player win')
        win = win + 1
    elif playerchoice== 'p' and computerchoice=='s':
        print('player win')
        win = win + 1
    elif playerchoice== 'sc' and computerchoice=='p':
        print('player win')
        win = win + 1
    elif playerchoice== 's' and computerchoice=='p':
        print('player losses')
        loss = loss + 1
    elif playerchoice== 'p' and computerchoice=='sc':
        print('player losses')
        loss = loss + 1
    elif playerchoice== 'sc' and computerchoice=='s':
        print('player losses')
        loss = loss + 1
