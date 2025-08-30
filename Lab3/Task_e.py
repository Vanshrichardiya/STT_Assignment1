import pandas as pd

df=pd.read_csv(r"C:\Users\HP\STT\Lab3\bugs_diffs_mine_with_similarity.csv", encoding='utf-8')

sem=[]
tok=[]
agree=[]

for i in range(len(df)):
    print(i)
    s=df.loc[i, "Semantic_Similarity"]
    t=df.loc[i, "Token_Similarity"]

    if pd.notna(s):
        if s>0.995:
            sem.append("Minor")
        else:
            sem.append("Major")
    else:
        sem.append(None)
        
    if pd.notna(t):
        if t>0.9:
            tok.append("Minor")
        else:
            tok.append("Major")
    else:
        tok.append(None)

    if sem[-1] is not None and tok[-1] is not None:
        if(sem[-1]==tok[-1]):
            agree.append("YES")
        else:
            agree.append("NO")
    else:
        agree.append(None)

df["Semantic_Class"]=sem
df["Token_Class"]=tok
df["Classes_Agree"]=agree

df.to_csv(r"C:\Users\HP\STT\Lab3\bugs_diffs_with_classes.csv", index=False)