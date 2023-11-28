tuples = (1, 2, 3, 4, 5, 6, [7, 8], 9, "ten")
print(tuples[1:10:3])
print(tuples.count(3))

for i in tuples:
    print(i)

nums = [7, 6]
tupleNums = tuple(nums)
print(tupleNums)