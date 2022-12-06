from typing import List, Any

def main(): 
    elvesList: List[Any] = []
    with open("elves_food_list.txt", "r") as list:
        tempList: List[Any] = []
        lines: List[str] = list.readlines()
        
        for line in lines:
            if line.strip():
                calories: List[int] = [int(line)]
                tempList.append(calories)
            else:
                elvesList.append(sum(tempList, []))
                tempList.clear()
        
    maxcalories: int = 0
    totalcalories: int = 0
    for row in range(len(elvesList)):
        if totalcalories > maxcalories:
            maxcalories = totalcalories
        totalcalories = 0
        for col in range(len(elvesList[row])):
            totalcalories += elvesList[row][col]

    print("Largest Amount of Calories Is ->", maxcalories)
    

if __name__ == "__main__":
    main()