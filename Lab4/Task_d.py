import pandas as pd
df=pd.read_csv(r"C:\Users\HP\STT\Lab4\repo_diffs.csv")

def clean_dff(s):
    lines=[]
    for l in str(s).splitlines():
        l=l.strip()
        if l.startswith("@@") or l.startswith("---") or l.startswith("+++") or l.isdigit():
            continue
        lines.append(l.lstrip("+-0123456789. "))
    return set(lines)

def compare(s,t):
    if(clean_dff(s)==clean_dff(t)):
        return "Yes"
    else:
        return "No"
    
df["Discrepancy"]=df.apply(lambda row: compare(row["diff_myers"], row["diff_hist"]), axis=1)
df.to_csv(r"C:\Users\HP\STT\Lab4\repo_diffs_discrepency.csv", index=False)