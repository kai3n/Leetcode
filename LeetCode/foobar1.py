# Foobar solution 1
def build_dict():
    d = {}
    examples = ["code", "Braille", "The quick brown fox jumps over the lazy dog"]
    binary_examples = ["100100101010100110100010", "000001110000111010100000010100111000111000100010", "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"]

    for i in range(len(examples)):
        j = 0
        for c in examples[i]:
            if c.isupper():
                d[c.lower()] = binary_examples[i][j+6:j+12]
                j += 12
            else:
                d[c] = binary_examples[i][j:j+6]
                j += 6
    return d

d = build_dict()

def translate_word(d, word):
    binary_res = ""
    for w in word:
        if w.isupper():
            binary_res += "000001"
        binary_res += d[w.lower()]
    return binary_res

assert translate_word(d, "Braille") == "000001110000111010100000010100111000111000100010"