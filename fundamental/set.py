#!/usr/bin/env python

# fruits = {"apple", "banana", "blueberry"}
# print(fruits)

# fruits.add("orange")
# print(fruits)

# fruits.remove("banana")
# print(fruits)

fruits1 ={"apple", "strawberry", "peach"}
fruits2 ={"banana", "strawberry", "orange"}

# 합집합
union = fruits1.union(fruits2)
print("합집합:", union)
# print(fruits1 | fruits2)

# 교집합
intersection = fruits1.intersection(fruits2)
print("교집합:", intersection)

# 차집합
diff1 = fruits1.difference(fruits2)
diff2 = fruits2.difference(fruits1)

print("차집합 (f1 - f2):", diff1)
print("차집합 (f2 - f1):", diff2)