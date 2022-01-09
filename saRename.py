import os
base = "accounts"
count = 1
for file in os.listdir(base):
    abspath = os.path.join(base,file)
    destpath = os.path.join(base,f"{count}.json")
    os.rename(abspath,destpath)
    count += 1