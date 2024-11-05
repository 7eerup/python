#!/usr/bin/env python

# 파일 내용 출력
with open("python.txt", "r") as file:
    # 파일 데이터 쓰기
    data = file.readlines()
    print(data)