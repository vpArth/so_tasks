# https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e/solutions

hamm = {'000': '0','001': '0','010': '0','011': '1','100': '0','101': '1','110': '1','111': '1'}

def chunked_str(s, sz):
    return (s[i:i+sz] for i in range(0, len(s), sz))

def encode(string):
    return ''.join(3*bit for char in string for bit in format(ord(char), '08b'))

def decode(bits):
    repaired = ''.join(hamm[triplet] for triplet in chunked_str(bits, 3))
    return ''.join(chr(int(byte, 2)) for byte in chunked_str(repaired, 8))

print(decode("100111111000111001000010000111111000000111001111000111110110111000010111"), "hey")
