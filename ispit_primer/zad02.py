recnik = {}
with open("input.txt", "r") as f:
    lines = f.readlines()
for line in lines:
    if line != '\n':
        a = line.split()
        for i in range(0, len(a)):
            for j in range(i+1, len(a)):
                par = (a[i], a[j])
                if par not in recnik:
                    recnik[par] = 1
                else:
                    recnik[par] += 1
sortirani = dict(sorted(recnik.items(), key=lambda x: (-x[1], x[0])))
#print(sortirani)
a=next(iter(sortirani))
print(f"{next(iter(sortirani))[0]} {next(iter(sortirani))[1]}")
print(f"{sortirani[a]}")