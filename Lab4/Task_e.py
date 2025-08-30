import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\HP\STT\Lab4\repo_diffs_discrepency.csv")
mismatch=df[df["Discrepancy"]=="No"].copy()

mismatch.reset_index(drop=True, inplace=True)
mismatch["File_Type"] = "Other"

for i in range(len(mismatch)):
    path=mismatch.at[i, "new_file path"]
    if path is None or str(path)=="nan":
        mismatch.at[i, "File_Type"]="Other"
        continue
    path=str(path).lower()
    if "test" in path:
        mismatch.at[i, "File_Type"]="Test Code"
    elif "readme" in path:
        mismatch.at[i, "File_Type"]="README"
    elif "license" in path:
        mismatch.at[i, "File_Type"]="LICENSE"
    else:
        mismatch.at[i, "File_Type"]="Source Code"

counts=mismatch["File_Type"].value_counts()

print("Mitsmatch Statisticks:")
print(counts)

plt.figure(figsize=(8,6))
counts.plot(kind="bar", color="lavender", edgecolor="black")
plt.ylabel("Number of mismatches")
plt.xlabel("File Type")
plt.show()