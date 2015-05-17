rij1 = input()
rij2 = input()
rij3 = input()

spel = rij1 + rij2 + rij3

if spel[0]==spel[3]==spel[6]=='1' or spel[1]==spel[4]==spel[7]=='1' or spel[2]==spel[5]==spel[8]=='1':
    print('Player 1 wins')
elif spel[0]==spel[1]==spel[2]=='1' or spel[3]==spel[4]==spel[5]=='1' or spel[6]==spel[7]==spel[8]=='1':
    print('Player 1 wins')
elif spel[0]==spel[4]==spel[8]=='1' or spel[2]==spel[4]==spel[6]=='1':
    print('Player 1 wins')
elif spel[0]==spel[3]==spel[6]=='2' or spel[1]==spel[4]==spel[7]=='2' or spel[2]==spel[5]==spel[8]=='2':
    print('Player 2 wins')
elif spel[0]==spel[1]==spel[2]=='2' or spel[3]==spel[4]==spel[5]=='2' or spel[6]==spel[7]==spel[8]=='2':
    print('Player 2 wins')
elif spel[0]==spel[4]==spel[8]=='2' or spel[2]==spel[4]==spel[6]=='2':
    print('Player 2 wins')
else:
    print('No winner')