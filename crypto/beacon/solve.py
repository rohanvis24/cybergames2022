from math import gcd
from Crypto.Util.number import long_to_bytes

with open("./messages.txt", "r") as f:
    all_n = []
    all_m = []
    for i in f.readlines():
        i = i.strip()
        n = i.split(":")[1].split(",")[0].strip()
        m = i.split(":")[3][:-1].strip()
        all_n.append(int(n))
        all_m.append(int(m))
    
    factored = {}
    for i in all_n:
        for j in all_n:
            output = gcd(i, j)
            if output != 1 and i != j:
                if i not in factored.keys():
                    factored[str(i)] = (output, i // output)
                    assert i == factored[str(i)][0] * factored[str(i)][1]
                if j not in factored.keys():
                    factored[str(j)] = (output, j // output)
                    assert j == factored[str(j)][0] * factored[str(j)][1]


    for k in factored.keys():
        v = factored[k]

        print(f"n: {k}")
        print(f"p: {v[0]}")
        print(f"q: {v[1]}")
        print(f"m: {all_m[all_n.index(int(k))]}")

        totient = (v[0]-1) * (v[1]-1)
        d = pow(65537, -1, totient)

        plaintext = pow(all_m[all_n.index(int(k))], d, int(k))
        print(long_to_bytes(plaintext).decode())
