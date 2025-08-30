Lab2=r"C:\Users\HP\STT\Lab2\bugs_diffs_mine.csv"

import pandas as pd
import os

df=pd.read_csv(Lab2)

print("Total number of commits: ", df["Hash"].nunique())
print("Total number of files: ", df["Filename"].nunique())

fpc=df.groupby("Hash")["Filename"].nunique()
mean=fpc.mean()
print("Average modified files per commit: ", mean)

print("Distribution of fix types: ", df["LLM Inference (fix type)"].value_counts())
print()

print("most frequently modified files: ")
print(df["Filename"].value_counts().head(1))
print()


df["Extention"]=df["Filename"].apply(lambda x: os.path.splitext(x)[1])
print("Most frequently modified extension: ")
print(df["Extention"].value_counts().head(1))