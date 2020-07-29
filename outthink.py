n = 100
p = 4
q = 5


for outthink in range(n):
    if outthink % p == 0:
        print("OUT")
        continue
    elif outthink % q == 0:
        print("THINK")
        continue
    elif outthink % p and outthink % q == 0:
        print("OUTTHINK")
        continue
    else:
        print(p)
        print(q)
