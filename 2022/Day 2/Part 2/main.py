# funtion to convert character to int based on points awarded for each symbol
# 1 for Rock, 2 for Paper, and 3 for Scissors
def getsymbolpoints ( symbol ):
    if symbol.upper() == 'A' or symbol.upper() == 'X': # ROCK
        return 1 # 1 Point for Rock
    elif symbol.upper() == 'B' or symbol.upper() == 'Y': # PAPER
        return 2 # 2 Points for Paper
    elif symbol.upper() == 'C' or symbol.upper() == 'Z': # SCISSORS
        return 3 # 3 Points for Scissors
    else:
        return 0 # Error, 0 points

# funtion to convert character to the move you need to play for the intended outcome from the guide
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
def getsymbol ( p1move, p2move ):
    if p2move.upper() == 'X': # X means we need to LOSE
        if p1move == 1: # if p1 throws rock
            return 3 # we throw scissors to lose
        elif p1move == 2: # if p1 throws paper
            return 1 # we throw rock to lose
        else:
            return 2 # otherwise p1 threw scissors so we throw paper to lose
    elif p2move.upper() == 'Y': # Y means we need to DRAW
        return p1move # we simply throw the same symbol as p1
    elif p2move.upper() == 'Z': # Z means we need to WIN
        if p1move == 1: # if p1 throws rock
            return 2 # we throw paper to win
        elif p1move == 2: # if p1 throws paper
            return 3 # we throw scissors to win
        else:
            return 1 # otherwise p1 threw scissors so we throw rock to win
    else:
        return 0 # Error, 0 points
    

# funtion to convert character to int based on p2 (you) winning/losing/drawing the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won)
def getwinner ( p1move, p2move ):
    # P2 (you) wins
        # (p1 == 1 and p2 == 2) -> p1 = rock, p2 = paper -> paper beats rock -> p2 wins
        # (p1 == 2 and p2 == 3) -> p1 = paper, p2 = scissors -> scissors beats paper -> p2 wins
        # (p1 == 3 and p2 == 1) -> p1 = scissors, p2 = rock -> rock beats scissors -> p2 wins
    if (p1move == 1 and p2move == 2) or (p1move == 2 and p2move == 3) or (p1move == 3 and p2move == 1):
        return 6 # 6 points for winning
    # Players Draw
        # (p1 == 1 and p2 == 1) -> p1 = rock, p2 = rock -> draw
        # (p1 == 2 and p2 == 2) -> p1 = paper, p2 = paper -> draw
        # (p1 == 3 and p2 == 3) -> p1 = scissors, p2 = scissors -> draw
    elif (p1move == 1 and p2move == 1) or (p1move == 2 and p2move == 2) or (p1move == 3 and p2move == 3):
        return 3 # 3 points for a draw
    # P1 (opponent) wins
        # (p1 == 1 and p2 == 3) -> p1 = rock, p2 = scissors -> rock beats scissors -> p1 wins
        # (p1 == 2 and p2 == 1) -> p1 = paper, p2 = rock -> paper beats rock -> p1 wins
        # (p1 == 3 and p2 == 2) -> p1 = scissors, p2 = paper -> scissors beats paper -> p1 wins  
    elif (p1move == 1 and p2move == 3) or (p1move == 2 and p2move == 1) or (p1move == 3 and p2move == 2):
        return 0 # 0 points for losing
    else:
        return 0 # error, return 0

    
def main():   
    game = [] # setup our list
    with open('moves.txt') as rounds: # open the text file
        for symbols in rounds: # move through it line by line
            game.append(symbols.split()) # add the lines to our list making a 2D list

    score = 0 # set our score to 0
    for i in range(len(game)): # Go through each round
        p1 = int(getsymbolpoints(game[i][0])) # get the points for each p1 symbol 
        p2 = int(getsymbol(p1, game[i][1])) # get the move we need to throw per the guide
        round = int(getwinner(p1, p2)) # get the points corresponding to which player won the round
        if round == 6: # if 6 is returned, we won! YAY! 
            print(' Won! :)')
            score += p2 + round # add together the symbol points + victory points
        elif round == 0: # if 0 is returned, we lost! SAD!
            print('Lost! :(')
            score += p2 + round # add together the symbol points + victory points
        else:
            print('Draw! :P') # otherwise it's a draw
            score += p2 + round # add together the symbol points + victory points

    print('\nYour Score:', score) # display our final score
    
    
if __name__ == "__main__":
    main()
