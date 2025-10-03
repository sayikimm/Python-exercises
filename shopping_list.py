my_list = []

a = input("Add list: ").split(",")
b = input("Delete list: ").split(",")

def funct(i, j):
    for item in i:
        my_list.append(item)
    for item in j:
        if item in my_list:
            my_list.remove(item)

    return my_list

my_list = []
print(funct(a, b))