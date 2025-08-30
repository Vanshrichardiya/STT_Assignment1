import pandas as pd
from radon.metrics import mi_visit
from radon.complexity import cc_visit
from radon.raw import analyze

df=pd.read_csv(r"C:\Users\HP\STT\Lab3\bugs_diffs_mine.csv")

def metrics(code):
    code=str(code)

    try:
        mi=mi_visit(code, True)
    except:
        mi=None

    
    try:
        list=cc_visit(code)
        cc=0
        if(list):
            total=0
            for i in list:
                total+=i.complexity
            cc=total/len(list)
    except:
        cc=None
    
    try:
        loc=analyze(code).loc
    except:
        loc=None
    
    return mi, cc, loc

list=["MI_Before", "CC_Before", "LOC_Before"]
df[list]=pd.DataFrame(df["Source Code (before)"].apply(metrics).tolist(), index=df.index)

list=["MI_After", "CC_After", "LOC_After"]
df[list]=pd.DataFrame(df["Source Code (current)"].apply(metrics).tolist(), index=df.index)

df["MI_Change"]=df["MI_After"]-df["MI_Before"]
df["CC_Change"]=df["CC_After"]-df["CC_Before"]
df["LOC_Change"]=df["LOC_After"]-df["LOC_Before"]


df=df.drop(columns=["MI_Before", "CC_Before", "LOC_Before","MI_After", "CC_After", "LOC_After"])

df.to_csv(r"C:\Users\HP\STT\Lab3\bugs_diffs_mine.csv", index=False)
