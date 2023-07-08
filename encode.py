import list_to_string

def encode(s):
    n=int(input("Shift by how many numbers? "))
    s=list(s)
    for i in range(len(s)):
        s[i]=list_to_string.li[(list_to_string.li.index(s[i])+n)%26]
    print(f'Here\'s the encoded message: {list_to_string.listtostring(s)}')