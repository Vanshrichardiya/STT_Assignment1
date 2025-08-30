from pydriller import Repository
import csv

Path=r"C:\Users\HP\STT\Lab2\jinja"

with open("bugs_commits.csv", "w", newline="", encoding="utf-8") as f:
    file=csv.writer(f)
    file.writerow(["Hash", "Message", "Hashes of parents", "Is a merge commit?", "List of modified files"])

    commits=Repository(Path).traverse_commits()
    for i in commits:
        commit=i.msg.lower()

        for j in commit.split():
            found=False;
            if j in ["fix", "bug", "error"]:
                file.writerow([i.hash,i.msg,[k for k in i.parents],i.merge,[new_file.new_path for new_file in i.modified_files]])
                found=True
                break
            if found:
                break

