import list_to_string
import art
import encode
import decode

print(art.logo)

cont=""
while 1:
    if cont=="no":
        break
    op=input("Do you want to encode or decode the string: ").lower()
    input_string=input("Enter your string: ").lower()
    s=input_string
    cont="a"
    
    if op=="encode":
        encode.encode(s)
    elif op=="decode":
        decode.decode(s)
    else:
        print("incorrect input")
        break
    while 1:
        if cont=="yes" or cont=="no":
            break
        cont=input("type yes to perform again or no to stop:").lower()
    