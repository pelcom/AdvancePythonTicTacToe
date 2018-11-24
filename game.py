from __future__ import print_function 
challengeDictionary = ['rock', 'scissors', 'paper', 'lizard', 'spock']
challengeSolutionDictionary = [[1,3], [2,3], [0,4], [2,4], [0,1]]
def wins(first,second):
    try:
        return (challengeDictionary.index(second) in challengeSolutionDictionary[challengeDictionary.index(first)])
    except Exception as e:
        return False

def spaceIsEmpty(board, position):
    
    return board[position] == ' '

def boardIsFull(board):
    for i in range(0,9):
        if spaceIsEmpty(board, i):
            return False
    return True


def getIndexOfCoordinate(row,column):
    return (3*(row-1)+column)-1

def isWinning(board,myMark):
    
    return ((board[6] == myMark and board[7] == myMark and board[8] == myMark) or # across the top
    (board[3] == myMark and board[4] == myMark and board[5] == myMark) or # across the middle
    (board[0] == myMark and board[1] == myMark and board[2] == myMark) or # across the bottom
    (board[6] == myMark and board[3] == myMark and board[0] == myMark) or # down the middle
    (board[7] == myMark and board[4] == myMark and board[1] == myMark) or # down the middle
    (board[8] == myMark and board[5] == myMark and board[2] == myMark) or # down the right side
    (board[6] == myMark and board[4] == myMark and board[2] == myMark) or # diagonal
    (board[8] == myMark and board[4] == myMark and board[0] == myMark)) # diagonal

def wouldLoseIfOpponentIsAdded(formerBoard,myMark,opponentMark,position):
    board = formerBoard.copy()
    board[position] = opponentMark
    return ((board[6] == myMark and board[7] == myMark and board[8] == myMark) or # across the top
    (board[3] == myMark and board[4] == myMark and board[5] == myMark) or # across the middle
    (board[0] == myMark and board[1] == myMark and board[2] == myMark) or # across the bottom
    (board[6] == myMark and board[3] == myMark and board[0] == myMark) or # down the middle
    (board[7] == myMark and board[4] == myMark and board[1] == myMark) or # down the middle
    (board[8] == myMark and board[5] == myMark and board[2] == myMark) or # down the right side
    (board[6] == myMark and board[4] == myMark and board[2] == myMark) or # diagonal
    (board[8] == myMark and board[4] == myMark and board[0] == myMark)) # diagonal

def tryChallenge(firstPlayer):
    userChallengeInput = input(firstPlayer+' pick one of rock, scissors, paper, lizard, spock: ').lower()
    computerRandom = random.randint(0, 4)
    computerChoosen = challengeDictionary[computerRandom]
    return (userChallengeInput, computerChoosen)

def getRowAndColumn(playerName,ownSymbol):
    print(playerName+', where would you like to place your '+ownSymbol)
    currentRow = input('Row: ').lower()
    while not(isinstance(int(currentRow), numbers.Number)):
        currentRow = input('Row: ').lower()
    currentColumn = input('Column: ').lower()
    while not(isinstance(int(currentRow), numbers.Number)):
        currentColumn = input('Column: ').lower()
    return (int(currentRow),int(currentColumn))

def placeSomething(board,row,column,value):
    board[getIndexOfCoordinate(row,column)] = value

def attemptGame(board,currentPlayer,ownSymbol,opponentSymbol,currentRow,currentColumn):
    print('In order to win your square you must win a game of Rock, Scissors,Paper, Lizard, Spock')
    userChallengeInput = ""
    computerChoosen = ""
    while (userChallengeInput==computerChoosen):
        userChallengeInput, computerChoosen = tryChallenge(currentPlayer)
        print(currentPlayer+', computer mentioned '+computerChoosen)
        print(currentPlayer+', you mentioned '+userChallengeInput)
        if(userChallengeInput==computerChoosen):
            print(currentPlayer+', it is a draw so you are to try again')
        

    if wins(userChallengeInput,computerChoosen):
        print(currentPlayer+',you won so your marker will be placed at row: '+str(currentRow)+' column: '+str(currentColumn))
        placeSomething(board,int(currentRow),int(currentColumn),ownSymbol)
    elif wouldLoseIfOpponentIsAdded(gameBoard,ownSymbol,opponentSymbol,getIndexOfCoordinate(currentRow,currentColumn)):
        print(currentPlayer+', you lost but putting your opponent marker would make your opponent win so we will leave the space empty')
    else:
        print(currentPlayer+',you lost so your opponent marker will be placed at row: '+str(currentRow)+' column: '+str(currentColumn))
        placeSomething(board,int(currentRow),int(currentColumn),opponentSymbol)

def drawBoard(board):
    
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')
    
 
def replay():
    
    return input('Player 1 enter your name: ').lower()



print("Hi I'm Proggie McFundy and welcome to the CompSci Squares!")

import random
import numbers
import decimal
while True:
    # Reset` the board
    gameBoard = [' '] * 9
    position = ' '
    firstPlayerMarker = 'X'
    secondPlayerMaker = 'O'
    firstUser = input('Player 1 enter your name: ').lower()
    secondUser = input('Player 2 enter your name: ').lower()
    randomFirst = random.randint(0, 1)
    turn = 0;
    firstPlayer = ''
    secondPlayer = ''
    if randomFirst == 0:
        firstPlayer = firstUser
        secondPlayer = secondUser
    else:
        firstPlayer = secondUser
        secondPlayer = firstUser
    nextMessage = firstPlayer+ ' will be playing with symbol X, and gets to pick the first spot on the board'
    print(nextMessage)
    gameStarted = True
    while gameStarted:
        drawBoard(gameBoard)
        if ((turn%2) == 0):
            currentRow,currentColumn = getRowAndColumn(firstPlayer,firstPlayerMarker)
            attemptGame(gameBoard,firstPlayer,firstPlayerMarker,secondPlayerMaker,currentRow,currentColumn)
			
            if isWinning(gameBoard, firstPlayerMarker):
                print('Congratulations! You have won the game!')
                gameStarted = False
            else:
                if boardIsFull(gameBoard):
                    print('The game is a draw!')
                    gameStarted = False
                    break
                else:
                    turn = turn+1

        else:
            currentRow,currentColumn = getRowAndColumn(secondPlayer,secondPlayerMaker)
            attemptGame(gameBoard,secondPlayer,secondPlayerMaker,firstPlayerMarker,currentRow,currentColumn)
			
            if isWinning(gameBoard, secondPlayerMaker):
                print('Congratulations! You have won the game!')
                gameStarted = False
            else:
                if boardIsFull(gameBoard):
                    print('The game is a draw!')
                    gameStarted = False
                    break
                else:
                    turn = turn+1
