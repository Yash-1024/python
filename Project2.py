list_size = int(input("Enter how many numbers u wish to have: "))
print("Enter positive/negative Numbers")
list1 = []

for i in range(list_size):
    item = int(input())
    list1.append(item)
i = 0
try:
    for i in range(list_size):
        if list1[i] < 0:
            list1.pop(i)
except Exception as e:
    pass
finally:
    print(list1)