# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
dict_numbers = {'One': "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("text4.txt", 'r', encoding="utf-8") as f:
    with open("text4_1.txt", 'w', encoding="utf-8") as f2:
        for line in f:
            list_number_eng = line.split()
            for item in dict_numbers.items():
                if item[0] == list_number_eng[0]:
                    list_number_eng[0] = item[1]
                    str_number_ru = " ".join(list_number_eng)
                    f2.writelines(str_number_ru + "\n")
print("Файл записан")
