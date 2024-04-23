

from string import ascii_lowercase as l

def make_the_code(code):
    if len(code) > 26:
        return code[:26]
    return code * (26//len(code)) + code[:26 % len(code)]


def shift(code_letter, letter, anti_shift=False):
    if anti_shift:
        shift_factor = (-l.index(code_letter))%26
    else:
        shift_factor = (l.index(code_letter))%26
    return l[(l.index(letter)+shift_factor)%26]


def encode(text, code, encrypt=True):
    text = text.lower()
    output = ""
    code = make_the_code(code)
    for i in range(len(text)):
        print("string", i, text[i])
        if text[i] not in l:
            output += text[i]
            continue
        output += shift(code[i % 26], text[i], encrypt)
    return output


def friendly_version():
    """gets the input from users and encrypt, decrypts/decrypts it"""
    c = input("Would you like to encrypt something in the cli?(y/n)\n--> ")
    if c != "y":
        return "Okay, Bye"
    code_word = input("What's your code word?\n--> ")
    text = input("Type Secret Message Below: (Enter to Submit)\n")
    encrypt = False if input("Encrypt or Decrypt (t/f):") != "t" else True
    return encode(text, code_word, encrypt)


if __name__ == "__main__":
    print(friendly_version())
    # print(encode("Okay, the invaders will enter the city from the north at 4am in the morning", "ishan"))
    #
    # print(encode("gsty, bae avoaqwzl jate rflmk gzm cvlg fegu tuw goelz tt 4if vf mhr uhraavz", "ishan", False))

