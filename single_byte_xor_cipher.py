# Single-byte XOR cipher
# The hex encoded string:
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# has been XOR'd against a single character. Find the key, decrypt the message.
# You can do this by hand. But don't: write code to do it for you.
# How? Devise some method for "scoring" a piece of English plaintext. 
# Character frequency is a good metric. Evaluate each output and choose the one with the best score.

code = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
#===========ROUGH=================================
import codecs
codecs.decode(code,'hex')

x=codecs.decode(hex(int(code,16)^222)[2:],'hex')

hex_string = "0x616263"[2:] 
bytes_object = bytes. fromhex(code) 
ascii_string = bytes_object.decode("ASCII") 
print(ascii_string)


#=====================found this online=======================================

# Ref: https://github.com/Shubhankar-Nath/Cryptopals/blob/master/Set1/breakXor.py

# import binascii
from Crypto.Util.strxor import strxor_c

#decrementing whendiagraphs are found
def has_forbidden_digraphs( text ):
    local_score=0
    forbidden_digraphs = ['cj','fq','gx','hx','jf','jq','jx','jz','qb','qc','qj','qk','qx','qz','sx','vf','vj','vq','vx','wx','xj','zx']
    for digraph in forbidden_digraphs:
        if digraph in text:
            local_score-=1
    return local_score

#adding when common words are found
def has_english_words( text ):
    local_score=0;
    most_frequent_words = ['a','of','\'s','the', 'and', 'have', 'that', 'for',
    'you', 'with', 'say', 'this', 'they', 'but', 'his', 'from',
    'that', 'not', "n't", 'she', 'what', 'their', 'can', 'who',
    'get', 'would', 'her', 'make', 'about', 'know', 'will',
    'one', 'time', 'there', 'year', 'think', 'when', 'which',
    'them', 'some', 'people', 'take', 'out', 'into','just', 'see',
    'him', 'your', 'come', 'could', 'now', 'than', 'like', 'other',
    'how', 'then', 'its', 'out', 'two', 'more ,these', 'want',
    'way', 'look', 'first', 'also', 'new', 'because', 'day',
    'more', 'use', 'man', 'find', 'here', 'thing', 'give', 'many']
    for word in most_frequent_words:
        if word in text:  # some issue here
            local_score+=1
    return local_score

def brute(cipher):
    score=[]
    for i in range(32, 128):
        #taking only printable characters
        text = strxor_c(bytes(cipher,'utf-8'),i )
        score.append(has_english_words(text)+has_forbidden_digraphs(text))
    temp=score.index(max(score))
    return temp+32


# def conv(value):
#     return binascii.unhexlify(value)

cipher = input("Enter cipher:  ")
key_ascii=brute(cipher)
key=chr(key_ascii)
print ("The key is: "+key)
text = strxor_c(cipher,key_ascii)
print ("The plaintext is: "+text)