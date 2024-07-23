#DemoStrRE.py


# 문자열 변수
data = '<<< spam and ham >>>'
result = data.strip("<> ")
print(data)
print(result)
result = result.replace("spam", "spam egg")
print(result)
lst = result.split()
print(lst)
print(":)".join(lst))


strA = "python is very powerful"
print(len(strA))
print(strA.capitalize())
print(strA.upper())
print(strA.lower())


#정규 표현식
import re

result = re.search("[0-9]*th", "35th")
print(result)
print(result.group()) # 찾은 단어만 보여주는 group()함수

result = re.search("apple", "this is apple")
print(result)
print(result.group())

result = re.search("\d{4}", "올해는 2024년입니다.") #4자리 숫자를 보여줘
print(result)
print(result.group())
