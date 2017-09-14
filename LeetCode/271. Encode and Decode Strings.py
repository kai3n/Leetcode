def encode(strs):
    return ''.join(s.replace('|', '||') + ' | ' for s in strs)

def decode(s):
    return [t.replace('||', '|') for t in s.split(' | ')[:-1]]

class Codec:

    def encode(self, strs):
        return ''.join('%d:' % len(s) + s for s in strs)

    def decode(self, s):
        strs = []
        i = 0
        while i < len(s):
            j = s.find(':', i)
            i = j + 1 + int(s[i:j])
            strs.append(s[j+1:i])
        return strs

test= Codec()
print(test.encode('apple32rnlkwef'))
