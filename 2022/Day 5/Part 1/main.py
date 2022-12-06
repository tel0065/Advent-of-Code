import re
from typing import List, Any

def main():
    '''
        This opens the file to find the row that contains the column labels
        We take the length of that row and set it equal to n which we will use
        to build our stacks list later.
    '''
    find_range = open('input.txt').read()
    for line in find_range.split('\n'):
        line = "".join(line.split())                               # removes all the whitespaces
        if line and line.isdigit():                                # if there is a line and it's all digits
            n = len(line)                                          # setup our variable
            break                                                  # We found our line, so stop looking further
    del find_range                                                 # We won't be using this again, so del it

    '''
        Parser
    '''
    stacks: List[List[Any]] = [[] for _ in range(n)]
    instructions = []
    with open('input.txt') as file:
        for lines in file:
            temp = "".join(lines.split())                          # removes all the whitespaces
            if lines and not lines.isspace():                      # if there is a line and it's not a blank line
                if temp.isalnum() and re.findall('move', temp):    # if the line contains letters/numbers and the word 'move'
                    tmp = re.findall(r'\d+', lines)                # find all the digits using regex, ignore the rest
                    instructions.append(list(map(int, tmp)))       # append it to our instructions list
                elif temp.isdigit():                               # if the line is all numbers
                    continue                                       # just move on, we don't care about it anymore
                else:                                            
                    for i in range(0, len(lines), 4):              # go through the lines in chunks of 4 starting at 0
                        crate = lines[i:i + 4]                     # add the line to a var
                        if '[' in crate:                           # if a bracket is found position [0], we know a letter proceeds [1]
                            stacks[i//4].append(crate[1])          # append to our 2D list by dividing the index by 4 to find the position

    '''
        The list is in the wrong order and needs to be reversed
    '''
    for i in range(len(stacks)):                                   # go through the stack
        stacks[i] = stacks[i][::-1]                                # this is what reverses to the order

    '''
        Parse the instruction set
    '''
    for i in range(len(instructions)):
        num_elements = int(instructions[i][0])                     # position [i][0] will always be the number of crates to move
        source = int(instructions[i][1])                           # position [i][1] will always be the source
        destination = int(instructions[i][2])                      # position [i][2] will always be the destination

    '''
        This just loops through the number of elements we need to move
        Then appends the crates to the new location by popping them off the old location
    '''
    for _ in range(num_elements):
        stacks[destination - 1].append(stacks[source - 1].pop())  

    '''
        Output - Prints the top crates to get our answer
    '''
    top_crate = ""
    for crates in range(len(stacks)):
        top_crate += stacks[crates][-1]
    print(top_crate)

if __name__ == "__main__":
    main()