def info(word):
    print(word, end="")
    print("!")
    
# test_func("World")
# word = 'Space'
# test_func(word)
# test_func("Ukraine")

""" def summa(a, b):
    res = a + b
    info(res)
    return res
    
res1 = summa(7, 5)
res2 = summa(8.3, 7.7)
res3 = summa("Hi ", "World")
print(res1)
print(res2)
print(res3) """

def minimal(list):
    min_num = list[0]
    for i in list:
        if min_num > i:
            min_num = i
    return min_num
    
nums = [2.6, 3.4, 8.1, 1.9, -10, 4.3, 5.7]
res1 = minimal(nums)

nums2 = [3, 2, 5, 8, 4]
res2 = minimal(nums2)

if res1 < res2:
    print(res1)
else:
    print(res2)
    
func = lambda x, y: x * y
print(func(11, 2))