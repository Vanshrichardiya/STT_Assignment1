import pandas as pd

File=r"C:\Users\HP\STT\Lab2\bugs_diffs_mine.csv"
df=pd.read_csv(File)

sample_msgs={"fix bug", "fixed bugs", "bug fix", "minor fix", "fix errors"}
sample_keywords={"fix", "bug", "error"}
def precise(message):
    if not isinstance(message, str):
        return False
    list=message.strip().lower()
    if(len(list)<3):
        return False
    if list in sample_msgs:
        return False
    if not any(k in list for k in sample_keywords):
        return False
    return True

Developer=df["Message"].dropna().apply(precise)
Dev_true=Developer.sum()
print("Precision of Developer: ", Dev_true/len(Developer))

LLM=df["LLM Inference (fix type)"].dropna().apply(precise)
LLM_true=LLM.sum()
print("Precision of LLM: ", LLM_true/len(LLM))

Rectifier=df["Rectified Message"].dropna().apply(precise)
Rect_true=Rectifier.sum()
print("Precision of Rectifier: ", Rect_true/len(Rectifier))