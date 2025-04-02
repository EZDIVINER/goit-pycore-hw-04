import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def vizual_direct(way_path, space = ""):

    path = Path(way_path)

    if  not path.exists() or not path.is_dir():
        print(Fore.RED + "Помилка: Вказаний шлях не є директорією" )
        return
    
    for item in path.iterdir():
        if item.is_dir():
            print(Fore.BLUE + space + item.name +"/")
            vizual_direct(item, space + "  ")
        elif item.is_file():
            print(Fore.GREEN + space + item.name)
            


if __name__ == "__main__":

    if len(sys.argv)<2:
        print(Fore.RED + "Не вказано шлях до диреторії")
        sys.exit(1)

    way_path = sys.argv[1]

    vizual_direct(way_path)


    