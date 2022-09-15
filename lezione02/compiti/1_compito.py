list_len = 5
first_list = []
second_list = []

print("Insert 5 numbers for the first list: ")

while len(first_list) < list_len:
    first_list.append(int(input("Insert number: ")))

print("Insert 5 numbers for the second list: ")

while len(second_list) < list_len:
    second_list.append(int(input("Insert number: ")))   

third_list = []

for number in first_list:
    third_list.append(number)

for number in second_list:
    third_list.append(number)

print(f"This is your list: {third_list}")