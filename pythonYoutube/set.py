""" #Множина
data = {'hello', 5, 5, True}
data.pop
data.add(6)
data.add(7)
data.update([7 , '24.5', 22])
data.remove(6)
print(data)

nums = [1, 2, 3, -1, 4, 7.3, 7.7]
res = set(nums)
word = 'Hello'
print(set(word)) """

string = input("Enter word: ")
split_string = string.split()
sort_string = [word for word in split_string if len(word) >= 3]
set_string = set(sort_string)
my_list = list(set_string)
my_list.sort()
lenght = int(len(my_list))
#dict_string = {'set': my_list}
#print(dict_string)
for i in range(lenght):
    print(i + 1,": ", my_list[i], sep="")

#frozenset
""" datas = frozenset([2, 5, 10, 7])#не можна вносити зміни """