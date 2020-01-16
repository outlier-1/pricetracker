import codecs


def char_to_hex(char, prefix='', postfix=''):
    hex_val = codecs.encode(char.encode(), "hex")
    return "{pre}{hex}{post}".format(pre=prefix,hex=hex_val.decode().upper(),
                                     post=postfix)