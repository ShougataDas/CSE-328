dic = {
    'a' : 10,
    'b': 16,
    'c': 32,
    'd': 4,
    'e': 8
}

for key,value in dic.items():
    if value % 16 == 0:
        print(f"{key}: valid")
    else:
        print(f"{key}: not valid")

