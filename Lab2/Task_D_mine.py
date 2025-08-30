from pydriller import Repository
import csv
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

Path=r"C:\Users\HP\STT\Lab2\jinja"
Task_c=r"C:\Users\HP\STT\Lab2\bugs_commits.csv"


# Loading bug fixing commit hashes from Task(c) file
print("Step 1")
hashes={i["Hash"] for i in csv.DictReader(open(Task_c, encoding="utf-8"))}


print("Step 2")
print()

tokenizer=AutoTokenizer.from_pretrained("mamiksik/CommitPredictorT5")
model=AutoModelForSeq2SeqLM.from_pretrained("mamiksik/CommitPredictorT5")

print("Step 3")
print()

def llm_commit(i: str)->str:
    if(i.strip()):
        input=tokenizer(i,return_tensors="pt", truncation=True, max_length=500)
        output=model.generate(**input, max_length=70)

        return tokenizer.decode(output[0], skip_special_tokens=True)
    else:
        return ""


print("Step 4")
print()

def rectifier(message: str, filename: str, i: str, llm: str)->str:
    msg=message.strip()
    sample_msgs=["fix bug", "fixed bugs", "bug fix", "minor fix", "fix errors"]
    if(len(msg.split())<3 or msg.lower() in sample_msgs) and llm:
        return llm
    
    if filename and "test" in filename.lower():
        return f"{llm} (test-related)" if llm else f"{msg} (test-related)"
    if filename and "parser" in filename.lower():
        return f"{llm} (parser-related)" if llm else f"{msg} (parser-related)"
    
    return msg

print("Final Step 5")
print()

with open("bugs_diffs_mine.csv", "w", newline="", encoding="utf-8") as f:
    file=csv.writer(f)
    file.writerow(["Hash", "Message", "Filename", "Source Code (before)", "Source Code (current)", "Diff", "LLM Inference (fix type)", "Rectified Message"])

    for i in Repository(Path).traverse_commits():
        if i.hash not in hashes:
            continue

        for j in i.modified_files:
            File=j.new_path if j.new_path else ""
            difference=j.diff if j.diff else ""

            if not File.endswith(".py"):
                continue
            if not j.source_code_before or not j.source_code:
                continue
            if not difference.strip():
                continue

            llm=llm_commit(difference)
            rectified=rectifier(i.msg, File, difference, llm)

            file.writerow([i.hash, i.msg.strip(), File, j.source_code_before if j.source_code_before else "", j.source_code if j.source_code else "", difference, llm, rectified])

print("Executed")
