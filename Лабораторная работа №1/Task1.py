numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

value1 = sum(numbers[0:4])
value2 = sum(numbers[5:20])
main_value = value1+value2

middle_arifm = main_value/len(numbers)
new_object = middle_arifm
numbers[4] = new_object







print("Измененный список:", numbers)
