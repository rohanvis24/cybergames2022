counter = 0
with open("./n2t-rom.bin", "rb") as f:
    while True: 
        # Convert hex to binary
        next_inst_1 = f.read(1)
        next_inst_2 = f.read(1)
        first_half = format(int.from_bytes(next_inst_1, 'little'), '08b')
        second_half = format(int.from_bytes(next_inst_2, 'little'), '08b')
        full_inst = first_half + second_half

        if full_inst == "0000000000000000":
            counter += 1
        else:
            counter = 0

        if counter == 3:
            break

        # A instruction
        if full_inst[0] == "0":
            # Check for writing to the screen
            print(f"@{int(full_inst[1:], 2)}")
            
        # C instruction
        else:
            a = full_inst[3]
            c = full_inst[4:10]
            d = full_inst[10:13]
            j = full_inst[13:]
            dest = "0"
            comp = "null"
            jump = "null"
            
            # Deal with comp
            if c == "101010":
                comp = "0"
            elif c == "111111":
                comp = "1"
            elif c == "111010":
                comp = "-1"
            elif c == "001100":
                comp = "D"
            elif c == "110000":
                if a == "0":
                    comp = "A"
                else:
                    comp = "M"
            elif c == "001101":
                comp = "!D"
            elif c == "110001":
                if a == "0":
                    comp = "!A"
                else:
                    comp = "!M"
            elif c == "001111":
                comp = "-D"
            elif c == "110011":
                if a == "0":
                    comp = "-A"
                else:
                    comp = "-M"
            elif c == "011111":
                comp = "D+1"
            elif c == "110111":
                if a == "0":
                    comp = "A+1"
                else:
                    comp = "M+1"
            elif c == "001110":
                comp = "D-1"
            elif c == "110010":
                if a == "0":
                    comp = "A-1"
                else:
                    comp = "M-1"
            elif c == "000010":
                if a == "0":
                    comp = "D+A"
                else:
                    comp = "D+M"
            elif c == "010011":
                if a == "0":
                    comp = "D-A"
                else:
                    comp = "D-M"
            elif c == "000111":
                if a == "0":
                    comp = "A-D"
                else:
                    comp = "M-D"
            elif c == "000000":
                if a == "0":
                    comp = "D&A"
                else:
                    comp = "D&M"
            else:
                if a == "0":
                    comp = "D|A"
                else:
                    comp = "D|M"
            
            # Deal with dest
            if d == "000":
                dest = "null"
            elif d == "001":
                dest = "M"
            elif d == "010":
                dest = "D"
            elif d == "011":
                dest = "MD"
            elif d == "100":
                dest = "A"
            elif d == "101":
                dest = "AM"
            elif d == "110":
                dest = "AD"
            else:
                dest = "AMD"

            # Deal with jump
            if j == "000":
                jump = "null"
            elif j == "001":
                jump = "JGT"
            elif j == "010":
                jump = "JEQ"
            elif j == "011":
                jump = "JGE"
            elif j == "100":
                jump = "JLT"
            elif j == "101":
                jump = "JNE"
            elif j == "110":
                jump = "JLE"
            else:
                jump = "JMP"
            
            if comp == "null":
                print(f"{dest};{jump}\r")
            elif jump == "null":
                print(f"{dest}={comp}\r")
            else:
                print(f"{comp};{jump}\r")
