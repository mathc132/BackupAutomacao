import pandas as pd
from sqlalchemy import create_engine 
import pymysql
import random



db_coon = create_engine('mysql+pymysql://root:@localhost/treino')
df = pd.DataFrame(pd.read_sql("SELECT * from alunos", con=db_coon))


print(df)
#print(df + a)

df.to_excel("output.xlsx",sheet_name = "PlanilhaPandas")
#df.to_excel('output1.xlsx'),shee
