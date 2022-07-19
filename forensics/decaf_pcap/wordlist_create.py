lmao_1 = ["Karma", "karma"]
lmao_2 = ["Coffee", "coffee"]

for a in lmao_1:
    for b in lmao_2:
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    for l in range(10):
                        next_pass = f"{a}{b}{i}{j}{k}{l}"
                        print(next_pass)
                    next_pass = f"{a}{b}{i}{j}{k}"
                    print(next_pass)
                next_pass = f"{a}{b}{i}{j}"
                print(next_pass)

