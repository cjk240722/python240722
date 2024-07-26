#Chap11_데이터프레임_위아래_좌우연결.py
from pandas import Series, DataFrame
import pandas as pd 

#DataFrame은 딕셔너리로도 만들 수 있다. 
data = {'첫번째' : [1,2], '두번째': [3,4]}
df = pd.DataFrame(data=data)


print(df)