s=0
cont=0
for c in range(1,501):
    if c%2!=0:
        if c%3==0:
            s += c
            cont += 1
print(s)
print(cont)