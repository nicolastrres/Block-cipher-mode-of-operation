from helper import string_to_bits

def non_encoder(block, key):
   """A basic encoder that doesn't actually do anything"""
   return pad_bits_append(block, len(key))

def pad_bits_append(small, size):
    diff = max(0, size - len(small))
    return small + [0] * diff

def electronic_codebook(plain_text, key, block_size, encoder):
    cipher = []
    binary_plain_text = string_to_bits(plain_text)
    binary_key = string_to_bits(key)
    plain_text_blocks = [binary_plain_text[i:i+block_size] for i in range(0, len(binary_plain_text), block_size)]
    for block in plain_text_blocks:
        cipher.extend(encoder(block, binary_key))
    return cipher
