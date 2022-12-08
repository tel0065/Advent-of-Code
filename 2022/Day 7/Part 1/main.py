from typing import Dict, Any

def main():
    folders: Dict[Any, Any] = {}
    breadcrumbs = []
    current_path = ''
  
    with open('input.txt') as file:
        for lines in file:
            lines = lines.split()
            if lines[0] == '$':
                if lines[1] == 'cd':
                    if lines[2] == '/':
                        current_path = '/'
                        breadcrumbs = ['/']
                        if current_path not in folders.keys():
                            folders[current_path] = 0
                    elif lines[2] == '..':
                        current_path = '/'.join(current_path.split('/')[:-1])
                        breadcrumbs.pop()
                    else:
                        if current_path == '/':
                            current_path += lines[-1]
                        else:
                            current_path += '/'+"".join(lines[-1])
                        breadcrumbs.append(current_path)
                        if current_path not in folders.keys():
                            folders[current_path] = 0
                elif lines[1] == 'ls':
                    continue
                elif lines[1] == 'dir':
                    continue
            elif lines[0].isdigit():
                file_size = int(lines[0])
                for directory in breadcrumbs:
                    folders[directory] += file_size
                    
    calculate_size_of_folders = [d for d in folders.values() if d <= 100000]
    print(f'The Sum of All of the Directories With a Total Size of at Most 100,000 is [{sum(calculate_size_of_folders)}]')

if __name__ == "__main__":
    main()