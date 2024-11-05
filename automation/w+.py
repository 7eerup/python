#!/usr/bin/env python

# 파일 열기 및 출력
with open("python.txt", "w+") as file:
    data = "python coding"
    file.write(data)

    file.seek(0)    # 커서 맨 앞 이동
    line = file.readlines()
    print(line)