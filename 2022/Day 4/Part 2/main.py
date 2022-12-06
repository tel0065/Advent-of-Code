from typing import List


def main():
    '''
        Opens input.txt to read
        strips out the new line characters
        replaces ',' with '-'
        splits using '-' as the delimiter
        
        end result: [['2', '4', '6', '8'], ['2', '3', '4', '5'], ['5', '7', '7', '9'], ['2', '8', '3', '7'], ['6', '6', '4', '6'], ['2', '6', '4', '8']]
    '''
    with open('input.txt') as big_list:
        assignments: List[List[str]] = [
            sections.strip().replace(',', '-').split('-') for sections in big_list
        ]
    
    # iterable counter
    overlap_found: int = 0
    for pairs in assignments:
        '''
            e1s -> elf1 start
            e1e -> elf1 end
            e2s -> elf2 start
            e2e -> elf2 end
            
            We set each of these variables to the corresponding int in the list using the map function
        '''
        e1s, e1e, e2s, e2e = map(int, pairs)
        
        elf2_overlap = (e1s <= e2e) and (e1e >= e2s)
        elf1_overlap = (e2s <= e1e) and (e2e >= e1s)

        if elf2_overlap or elf1_overlap:
            overlap_found += 1    
        
    print(overlap_found)


if __name__ == "__main__":
    main()