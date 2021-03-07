def caesarCipherEncryptor(string, key):
    # Write your code here.
    a_code = ord('a')
    z_code = ord('z')
    result = ''
    for s in string:
        s_code = ord(s)
        shifted = s_code + key
        if shifted > z_code:
            new_code = (shifted - z_code) % 26 + a_code - 1
        else:
            new_code = shifted
        new_s = chr(new_code)
        result += new_s
    return result
