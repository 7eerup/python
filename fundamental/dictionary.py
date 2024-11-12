#!/usr/bin/env python

person = {"name": "kcb", "age": "30", "city": "Seoul"}
person_detail = {"country": "대한민국", "marriage": True}

person.update(person_detail)

print(f"이름은{person['name']}, 나이는{person['age']}, 고향은{person['city']}입니다.")

country = person.get("country", "알 수 없음")
print(f"국적은 {country} 입니다.")

print("Before", person.keys())

del person['marriage']

print("After", person.keys())