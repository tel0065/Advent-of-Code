def main():
    with open('input.txt') as file:
        lines = file.readlines()

    length = 14
    line = lines[0]
    for i in range(len(line) - length + 1):
        marker = set(line[i:i + length])
        if len(marker) == length:
            print(f'The first start-of-packet marker is complete after {i + length} characters')
            break
        else:
            pass

if __name__ == "__main__":
    main()
