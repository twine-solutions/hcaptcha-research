def big_int_to_bytes(big_int): 
    byte_array = big_int.to_bytes((big_int.bit_length() + 7) // 8, byteorder='big', signed=True) 

    if len(byte_array) < 8: 
        byte_array = byte_array.rjust(8, b'\x00') 
     
    return byte_array 
 
big_int = 6258495943336606
byte_array = big_int_to_bytes(big_int) 
 
char_codes = list(byte_array) 
char_codes.reverse() 

print(char_codes)
