import hashlib
from PIL import Image

hash_table = {"25d77f471f7d9d1ceb46c8db7058d0c9": "Y",
        "667007e63266e61075a1e31200abf59a": "R",
        "d1a7eea623e7a62a69de9b1258c3f63d": "L",
        "c57f9e58f0fb3cd8a40dbde6ed12ecfd": "N",
        "e4f6ffcb62e81218423c7b24f1e8c096": "C",
        "fc6118adec896979e199901bd6c69479": "U",
        "98a2dbaa8e30aa7cae39dd55353c5772": "O", 
        "e8d51edb87921e53b3c2c0379e530b87": "D",
        "27c16da73bd6462e561dc53d4dc890dc": "S",
        "30074c8483b1ee1721e4fdf93d61edad": "W", 
        "57096cd533ee29aa9a62c76cc45520ac": "M",
        "3ee3b541e5a6d0cd0c2eab2ca2f91457": "Q",
        "73d5ce1c983fcc59e743890caa28fddb": "B",
        "252ec364a3bdf36c69fd5ce5d1e08bc4": "P",
        "875bcdaf63b78f25f10d52aa0abf063e": "H",
        "819bc8439a7b7e0885dad67ebb619c7f": "A",
        "9674c43fe326b9667ca89766c338030c": "I", 
        "eab667b48725a4d2decd4a39bf1c488b": "F",
        "a98566c4c54aa9913da8a3b748221efb": "K",
        "dc685fa704c3cb6c90bbf97cf77db946": "X",
        "1f494601582bf3629f5ae9df28a1d393": "Z",
        "05507b921e00535e3e28880e7a6c925c": "T",
        "3a40c02276198a3d39b5ed081363cd81": "E",
        "6f54413417aceac08fe1b5e353539b2e": "J",
        "84a6f7abdc885f308894fb6b99348329": "V",
        "1d7c0903c8a902fdfa3e6143b283724a": "G"}

total_str = ""
for i in range(11264):
    tmp = hashlib.md5(open(f'./img/{i}.png', 'rb').read()).hexdigest()
    try:
        total_str += hash_table[tmp]
    except:
        print(f"Error: {i}.png")
        total_str += "_"

print(total_str)

