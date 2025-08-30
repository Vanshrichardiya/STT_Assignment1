import pandas as pd
import torch 
from transformers import RobertaTokenizer, RobertaModel
import sacrebleu

df=pd.read_csv(r"C:\Users\HP\STT\Lab3\bugs_diffs_mine.csv", encoding='utf-8')



tokenizer=RobertaTokenizer.from_pretrained("microsoft/codebert-base")
model=RobertaModel.from_pretrained("microsoft/codebert-base")

semantic=[]
token=[]

for i in range(len(df)):
    print(i)
    before=str(df.loc[i, "Source Code (before)"])
    after=str(df.loc[i, "Source Code (current)"])

    try:
        i1=tokenizer(before, return_tensors="pt",truncation=True,max_length=512)
        i2=tokenizer(after, return_tensors="pt",truncation=True,max_length=512)
        with torch.no_grad():
            out1=model(**i1)
            out2=model(**i2)
        emb1=out1.last_hidden_state[0,0,:]
        emb2=out2.last_hidden_state[0,0,:]
        cos_sim=torch.nn.functional.cosine_similarity(emb1, emb2, dim=0).item()
        semantic.append(cos_sim)
    except:
        semantic.append(None)

    try:
        bleu=sacrebleu.sentence_bleu(after, [before])
        token.append(bleu.score/100)
    except:
        token.append(None)

df["Semantic_Similarity"]=semantic
df["Token_Similarity"]=token

df.to_csv(r"C:\Users\HP\STT\Lab3\bugs_diffs_mine_with_similarity.csv", index=False)
