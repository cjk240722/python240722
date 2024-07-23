#DemoFile.py

#파일쓰기(유니코드)
f = open("demo.txt", "wt", encoding="utf-8")
f.write("첫번째라인\n두번째라인\n세번쨰라인\n")
f.close()

#파일읽기
f = open("demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)

f.close()
