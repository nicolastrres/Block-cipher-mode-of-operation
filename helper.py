def pad_bits(bits, pad):
    bits_length = len(bits)
    assert bits_length <= pad
    return [0] * (pad-bits_length) + bits

ASCII_BITS = 8

def ascii_char_to_bits(ascii_letter):
    bits = []
    if ascii_letter == 0:
        return [0]
    while ascii_letter > 0:
        bits = [ascii_letter % 2] + bits
        ascii_letter = ascii_letter // 2
    return pad_bits(bits, ASCII_BITS)


def string_to_bits(string_to_convert):
    binary_string = []
    for letter in string_to_convert:
        ascii_char = ord(letter)
        bits_letter = ascii_char_to_bits(ascii_char)
        binary_string = binary_string + bits_letter
    return binary_string

