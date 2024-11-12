#!/usr/bin/env python

# 튜플 생성
startcraft = ("Terran", "Protoss", "Zerg")

race = (startcraft[0])

print("race: ",race)    # Terran


# 빈 튜플 생성
my_tupe = (1, )

fruits =("apple", "banana", "blueberry")
first = fruits[0]
print("first :", first)

# 패킹과 언패킹
pkg = 1,2,3
print(pkg)

v1, v2, v3 = pkg
print(f"{v1}, {v2}, {v3}")


tuple = (1,2,3,4,5,6,7,8)
val1, val2, val3, *vals, _ = tuple

vals.append(10)
print(vals)