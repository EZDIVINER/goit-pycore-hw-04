from pathlib import Path 



def get_cats_info(path):
    try:

        cats_info = []

        file_path = Path(path)
        if not file_path.is_file():
            print("Файл не знайдено")

        with file_path.open(encoding= 'utf-8') as file:
            for l in file:
                id, name, age = l.strip().split(',')
                cats_info.append({"id" : id, "name" : name, "age" : age})

        return cats_info
    
    except Exception as e:
        print("Помилка")
        return []

cats_info = get_cats_info("Task2\Task2.txt")
for cat in cats_info:
    print(cat)
