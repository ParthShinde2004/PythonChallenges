"""This is a SUPER-SECRET language. Rövarspråket is not very complicated: 
you take an ordinary word and replace the consonants with the consonant 
doubled and with an "o" in between. So the consonant "b" is replaced by "bob"
, "r" is replaced with "ror", "s" is replaced with "sos", and so on. Vowels are 
left intact. It's made for Swedish, but it works just as well in English."""

import re
import string

swedish_consonants = ''.join(set(string.lowercasr) - set('aeiouy'))


def encode_rovarspraket(msg):
    encode_consonant = lambda c: c.group(0) + 'o' + c.group(0).lower()
    return re.sub(r'(?i)[' + swedish_consonants + r']', encode_consonant, msg)


def decode_rovarspraket(msg):
    decode_consonant = lambda c: c.group(1)
    return re.sub(r'(?i)([' + swedish_consonants + r'])o\1', decode_consonant, msg)
