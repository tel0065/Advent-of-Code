from typing import List, Any

def main():
    elvesList: List[Any] = []
    with open("elves_food_list.txt", "r") as list:
        tempList = []
        lines = list.readlines()
        
        for line in lines:
            if line.strip():
                calories: List[int] = [int(line)]
                tempList.append(calories)
            else:
                elvesList.append(sum(tempList, []))
                tempList.clear()

    maxcalories: List[int] = []
    totalcalories: int = 0
    for row in range(len(elvesList)):
        maxcalories.append(totalcalories)
        totalcalories = 0
        for col in range(len(elvesList[row])):
            totalcalories += elvesList[row][col]

    maxcalories.sort(reverse=True)
    topthree: int = 0
    for i in range(3):
        topthree += maxcalories[i]
    print("The number of calories carried by the top three Elves is ->", topthree)

if __name__ == "__main__":
    main()