from typing import List


def main():
    with open('input.txt') as big_list:
        assignments: List[List[str]] = [
            sections.strip().replace(',', '-').split('-') for sections in big_list
        ]
        
    overlap_found: int = 0
    for pairs in assignments:
        e1s, e1e, e2s, e2e = map(int, pairs)
        
        elf2_overlap = (e1s <= e2s <= e1e) and (e1s <= e2e <= e1e)
        elf1_overlap = (e2s <= e1s <= e2e) and (e2s <= e1e <= e2e)

        if elf2_overlap or elf1_overlap:
            overlap_found += 1    
        
    print(overlap_found)


if __name__ == "__main__":
    main()