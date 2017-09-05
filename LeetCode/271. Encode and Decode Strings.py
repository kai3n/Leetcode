def encode(strs):
    return ''.join(s.replace('|', '||') + ' | ' for s in strs)

def decode(s):
    return [t.replace('||', '|') for t in s.split(' | ')[:-1]]

print(encode('apple'))
print(decode(encode('apple')))