import list_to_string

def decode(s):
    n=int(input("Shift by how many numbers? "))
    s=list(s)
    for i in range(len(s)):
        s[i]=list_to_string.li[(list_to_string.li.index(s[i])-n+26)%26]
    print(f'Here\'s the decoded message: {list_to_string.listtostring(s)}')