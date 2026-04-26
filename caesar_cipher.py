print("Caesar cipher tool")

choice = input("Enter E for Encryption or D for Decryption: ")
text = input("Enter a message: ")
key = int(input("Enter a shift key: "))

def caesar(text,key):
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                start = ord("A")
            else:
                start = ord("a")

            if choice.upper() == "E":
                result += chr((ord(ch)-start+key)%26+start)
            else:
                result += chr((ord(ch)-start-key)%26+start)
        else:
            result = result + ch
    return result

result = caesar(text,key)

print("Result: ",result)