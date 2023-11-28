# nums = [5, 6, 12.2, True, '4', 'Hello']
nums = [5, 6, 10, 7, -4, 5, 16]
nums[0] = 34.4
#print(nums[3])

nums2 = [2, 5.9, 5.6, 'Keyboard', [5, 2, 'Home work', True]]#мінусові індекси будуть брати індекси з кінця масиву [-1], останній елемент масиву, [-2] передостанній елемент масиву
print(nums2[-1][2])

nums.append(45)
nums.append(6)
nums.append(5)
nums.insert(1, False)
#nums.extend(nums2)
""" nums.sort() """
nums.reverse()
#nums.pop()
nums.remove(34.4)
""" nums.clear() """
nums.count(5)
print(nums)
print(nums.count(5))
print(nums.count(6))
print(len(nums))