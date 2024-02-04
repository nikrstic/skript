import random
with open("strukture/smsSpam.txt", "r") as f:
    lines=f.readlines()
random.shuffle(lines)
string=''.join(lines)
with open("strukture/shuffle.txt","w") as f1:
    f1.write(string)
