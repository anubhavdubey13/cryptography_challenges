# Fixed XOR
# Write a function that takes two equal-length buffers and produces their XOR combination.
# feed the string:
# 1c0111001f010100061a024b53535009181c
# after hex decoding, and when XOR'd against:
# 686974207468652062756c6c277320657965
# should produce:
# 746865206b696420646f6e277420706c6179

# What is XOR?: 0^0, 1^1 = 0, else 0^1 = 1

# this isnt working yet. I dont wanna copy the code. Lemme have a better understanding na
# I kinda get it
# I convert hex to int and apply xor on int then convert back to hex
# under the hood, xor is applied to the binary format and then the output is returned as int
# I have tested this in console so I get it now

hex_1 = "1c0111001f010100061a024b53535009181c"
hex_2 = "686974207468652062756c6c277320657965"

# import codecs
# decode_hex = codecs.decode(hex_1, 'hex')
# print(decode_hex)

# Ref: https://stackoverflow.com/questions/36242887/how-to-xor-two-strings-in-python
def xor_two_str(str1, str2):
    return hex(int(str1,16) ^ int(str2,16))[2:]

xor_two_str(hex_1, hex_2)

#======================= Testing =================================
# picking 17 and 38 randomly

'{0:b}'.format(17)   # binary representation of 17 
# output: 10001

'{0:b}'.format(38)  
# output: 100110

# 100110 xor 010001 = 110111 
int('110111',2) # = 55 # also 2 denotes base it is being converted from

17^38 # = 55
