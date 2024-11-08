#!/usr/bin/env python

my_list = [10, 20, 30]
print(my_list)

# append()
ex_list = []
ex_list.append(10)
ex_list.append(15)
ex_list.append(20)
print(ex_list)

# append()
ex_list1 = [40, 50, 60]
ex_list1.append(10)
ex_list1.append(15)
ex_list1.append(20)
print(ex_list1)

# len()
ex_list2 = [40, 50, 60]
ex_list2.append(10)
ex_list2.append(15)
ex_list2.append(20)
print(len(ex_list2))

# slice()
ex_list3 = [70, 80, 90]
ex_list3.append(10)
ex_list3.append(15)
ex_list3.append(20)

sliced = ex_list3[2:]
print("sliced: ", sliced)


fruits = ["apple", "banana", "blueberry", "cherry"]

# 바나나 포함?
is_banana_included = "banana" in fruits
print("Is banana included?", is_banana_included)

# 체리 순서를 찾아라
index_cherry = fruits.index("cherry")
print("Cherry is ", index_cherry)

# 리스트 정렬
numbers = [4, 2, 1, 3, 7, 8, 5]
print("Unsorted ", numbers)

# sort()
numbers.sort()
print("Sorted ", numbers)

# sort()reverse
numbers.sort(reverse=True)
print("Sorted (Reverse) ", numbers)

# 리스트 요소 추가 및 제거
ex_list4 = []
ex_list4.append(1)
ex_list4.append(2)
ex_list4.append(3)
print(ex_list4)

# extend()
ex_list4.extend([4, 5, 6])
print(ex_list4)

# append()
ex_list4.append([7, 8])
print(ex_list4)

print(ex_list4[-1])

# max() min()
max_value = max(my_list)
min_value = min(my_list)
print(f"최대 값은 {max_value}, 최소 값은 {min_value} 입니다.")