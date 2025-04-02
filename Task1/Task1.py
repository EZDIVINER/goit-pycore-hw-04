from pathlib import Path 

with open('Task1\Task1.txt', 'w') as file:
    content = file.write('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000')





def total_salary(path):
    try:
        total = 0 
        count = 0

        #Перевірка на існування файлу 
        file_path = Path(path)
        if not file_path.is_file():
            print("Файл не знайдено")

        with file_path.open(encoding = 'utf-8') as file:
            for l in file:
                name, salary = l.strip().split(',')
                total += int(salary)
                count +=1

        average = total/count
        return total, average
        
    except Exception as e:
        print("Помилка")
        return 0, 0
            
path = 'Task1.txt'        
total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")