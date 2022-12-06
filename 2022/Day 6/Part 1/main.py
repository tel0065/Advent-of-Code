def main():
    with open('input.txt') as file:
        lines = file.readlines()
    
    for line in lines:
        print(f'The first start-of-packet marker is complete after {findMarker(line, 4)} characters')
    
    for line in lines:
        print(f'The first start-of-packet marker is complete after {findMarker(line, 14)} characters')
        
        
def findMarker(line, block_size): 
    for c in range(len(line) - block_size + 1):
        block = set(line[c:c + block_size])
        if len(block) == block_size:
            return block_size + c
    return None      

if __name__ == "__main__":
    main()