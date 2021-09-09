encodeinp = input()
decodeinp = input()

def encode(str):
    out = ""

    for i in str:
        ch = ord(i)
        if 65<=ch<=90 or 97<=ch<=122:
            out += chr(ch+5)
        elif i == " " or i == "." or i == ",":
            out += i
        else:
            return "INVALID INPUT"
    return out

def decode(str):
    out = ""

    for i in str:
        ch = ord(i)
        if 65<=ch<=90 or 97<=ch<=122:
            out += chr(ch-5)
        elif i == " " or i == "." or i == ",":
            out += i
        else:
            return "INVALID INPUT"

    return out

encodeout = encode(encodeinp)
decodeout = decode(decodeinp)

if encodeout == "INVALID INPUT" or  decodeout == "INVALID INPUT":
    print("INVALID INPUT")
else:
    print(encodeout)
    print(decodeout)


