# this is a Tic Tac Toe game

def display_board(list1):
    print(list1[1],'|',list1[2],'|',list1[3])
    print('---------')
    print(list1[4],'|',list1[5],'|',list1[6])
    print('---------')
    print(list1[7],'|',list1[8],'|',list1[9])
# display_board(list1)

def player1():
    i='ip'
    while i not in {'X','O'}:
        ip=input('Player1 select the option X or O\n')
        if ip.upper() in {'X','O'}:
            i=ip.upper()
            i2={'X','O'}-{i}
            i2=list(i2)
            i2=i2[0]
            print(f'Player 1 selected {i}\nPlayer 2 is {i2}')
            return i,i2
        else:
            print('Invalid input (X,O)')
# player1()
def dumb_board():
    print('\n\n')
    print('1','|','2','|','3')
    print('---------')
    print('4','|','5','|','6')
    print('---------')
    print('7','|','8','|','9')

def board(i,i2,list1):    
    while True:
        dumb_board()
        if ' ' not in list1:
            return 'Draw'
        pos1=int(input('Player1 enter position : '))
        
        if pos1 in range(1,10) and list1[pos1] not in ['X','O']:
            print(list1[pos1])
            list1[pos1]=i
            display_board(list1)
        else:
            print('Enter valid position') 
        if list1[1]==list1[2]==list1[3]==i or list1[4]==list1[5]==list1[6]==i or list1[7]==list1[8]==list1[9]==i or list1[1]==list1[4]==list1[7]==i or list1[2]==list1[5]==list1[8]==i or list1[3]==list1[6]==list1[9]==i or list1[1]==list1[5]==list1[9]==i or list1[3]==list1[5]==list1[7]==i :
            
            return 'Player 1 is Winner'     
        dumb_board()
        if ' ' not in list1:
            return 'Draw'      
        pos2=int(input('Player2 enter position : '))
        if pos2 in range(1,10) and list1[pos2] not in ['X','O']:
            list1[pos2]=i2
            display_board(list1)
        else:
            list1[pos1]=' '
            print('Enter valid position')         
        if list1[1]==list1[2]==list1[3]==i2 or list1[4]==list1[5]==list1[6]==i2 or list1[7]==list1[8]==list1[9]==i2 or list1[1]==list1[4]==list1[7]==i2 or list1[2]==list1[5]==list1[8]==i2 or list1[3]==list1[6]==list1[9]==i2 or list1[1]==list1[5]==list1[9]==i2 or list1[3]==list1[5]==list1[7]==i2 :            
            return 'Player 2 is Winner'
        if ' ' not in list1:
            return 'Draw'
    
def replay():
    status='no'
    while status not in ['Y','N']:
        stat=input('Do you want to play again (Y,N):')
        if stat.upper() not in ['Y','N']:
            print('Enter valid input')
        else:
            status=stat
            if stat.upper()=='Y':
                return True 
            else:
                return False     



def game():
    
    list1=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    print('Welcome to Tic Tac Toe game')
    i,i2=player1()    
    result=board(i,i2,list1)
    print(result) 
    if replay()== True:
        game()
    else:
        return 'Thanks for playing'    
    
    
print(game())   