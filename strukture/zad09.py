cnt=0
sam=0
spam=0
with open('strukture/smsSpam.txt','r') as f:
    while True:
        line=f.readline()
        if not line:
            break
        if (line.split()[0] == "ham"):
            spam+=1
        if (line.split()[0] == "spam"):
            sam+=1
        
        cnt+=1

print(cnt)
print(sam)
print(spam)
print(spam+sam)