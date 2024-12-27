input_list = list(map(int, input("Enter the list elements separated by spaces: ").split()))
unique_list = sorted(set(input_list))
number_of_sublist = int(input("Enter the number of sublists: "))

cnt = int(0)

ans_list = []
temp = []

for i in unique_list:
    if cnt == 2:
        temp.append(i)
        ans_list.append(temp)
        cnt = 0
        temp = []
    else:
        cnt+=1
        temp.append(i)

print("Sublists are: ",ans_list)

