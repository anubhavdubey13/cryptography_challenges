# Hex to base64

# The string:
# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# convert to:
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

# Rules:
# Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
# (I still don't understand it after going through several websites)

# Since I don't know most of the terms here, time to Google.

# Hex: https://www.youtube.com/watch?v=4EJay-6Bioo
# base64: https://www.youtube.com/watch?v=aUdKd0IFl34

# Ref: https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
# import codecs
# hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
# b64 = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()
# print(b64)

def hex_to_base64(hex_code):
    import codecs
    decode_hex = codecs.decode(hex, 'hex')
    # print(decode_hex) # The folks who wrote this challenge are funny
    encode_base64 = codecs.encode(decode_hex, 'base64')
    # print(encode_base64)
    final = encode_base64.decode()
    print(final)
    
hex_to_base64(hex)
    