#!/usr/bin/env python

# 문자열 변수 선언
str_var = "This is my python code."

# 인덱싱
print(str_var[11])
print(str_var[-1])
print(str_var[-5])

# 슬라이싱
print(str_var[11:17])
print(str_var[11:-6])

# 대문자
print(str_var.upper())

# swap
print(str_var.swapcase())

# Format String
weather = "흐림"
temp = 15.8

# % code (%s, %d, %f)
res = "오늘 날씨는 %s 입니다. 기온은 %f도 입니다." % (weather, temp)
print(res)

# .format()
res1 = "오늘 날씨는 {} 입니다. 기온은 {}도 입니다.".format(weather, temp)
print(res1)

# f""
res2 = f"오늘 날씨는 {weather} 입니다. 기온은 {temp}도 입니다."
print(res2)


# 사용자로부터 문자열 입력받기
inp = input("값을 입력해주세요.")

# 이 값을 1 더해서 출력하기
num = int(inp) + 1
print(f"입력받은 값에 1을 더하면, {num} 입니다.")