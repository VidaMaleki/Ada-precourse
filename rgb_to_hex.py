def color_converter(red, green, blue):
    result = "#" + f'{number_to_hex_string(red)}{number_to_hex_string(green)}{number_to_hex_string(blue)}'
    return result
    

def number_to_hex_string(num):
    prefix = '0x'
    hex_string = hex(num)
    if hex_string.startswith(prefix):
        hex_string = hex_string[len(prefix):]
    if len(hex_string) < 2:
        hex_string = '0' + hex_string
    return hex_string.upper()

print(color_converter(100, 50, 5))