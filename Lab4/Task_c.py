import pandas as pd
from pydriller import Repository

list=[ "https://github.com/bumptech/glide", "https://github.com/nostra13/Android-Universal-Image-Loader","https://github.com/square/picasso"]

all_data=[]

def flatten_diff(diff_parsed):
    if not diff_parsed:
        return ""
    result = []
    for change_type, changes in diff_parsed.items():
        for change in changes:
            result.append(" ".join(map(str, change)))
    return "\n".join(result)

for i in list:
    print("Mining repository: ", i)
    myers_data={}
    for j in Repository(i, skip_whitespaces=True, histogram_diff=False).traverse_commits():
        for k in j.modified_files:
            key=(j.hash, k.new_path, k.old_path)
            myers_data[key]={"old_file path":k.old_path, "new_file path":k.new_path, "commit SHA":j.hash, "parent commit SHA":j.parents[0] if j.parents else None, "commit message":j.msg, "diff_myers":k.diff}
    
    for j in Repository(i, skip_whitespaces=True, histogram_diff=True).traverse_commits():
        for k in j.modified_files:
            key=(j.hash, k.new_path, k.old_path)
            hist = flatten_diff(k.diff_parsed)
            if key in myers_data:
                myers_data[key]["diff_hist"]=hist
    all_data.extend(myers_data.values())
df=pd.DataFrame(all_data)
df.to_csv(r"C:\Users\HP\STT\Lab4\repo_diffs.csv", index=False)
