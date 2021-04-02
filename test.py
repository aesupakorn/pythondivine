# Prog-10: Steganography
# 6?3?????21 Name ?

import math
import copy
import numpy
from PIL import Image

# -----------------------------------------
def load_image(filename):     
    im = Image.open(filename).convert('RGB')  
    return numpy.asarray(im).tolist()      
  
def save_image(img, filename):    
    im = Image.fromarray(numpy.uint8(img))   
    im.save(filename)
    
def show_image(filename):   
    im = Image.open(filename)  
    im.show()         

def clone_image(img):
    return copy.deepcopy(img)

def char_to_bits(ch):
    return ('0000000' + bin(ord(ch))[2:])[-8:]

def bits_to_char( bits ):
    return chr( bits_to_int(bits) )

def int_to_bits(n):
    return ('0'*16 + bin(n)[2:])[-16:]

def bits_to_int( bits ):
    return int(bits,2)

def main():
    op = input('E(mbed text) or G(et text): ')
    if op == 'E' or op == 'G':
        file_in = input('Input image file (.png): ')
        if file_in[-4:] != '.png':
            file_in = file_in + '.png'
        if op == 'E':
            text = input('Text to be embedded: ')
            file_out = file_in[:-4] + '_x' + '.png'
            success = embed_text_to_image(text, file_in, file_out)
            if success:
                print('The output image file is', file_out)
            else:
                print('Need a bigger image.')
        else:
            txt = get_embedded_text_from_image(file_in)
            if txt == '':
                print('No hidden text.')
            else:
                print('The hidden text is', txt)
    else:
        print('Try again, re-enter E or G')
# --------------------------------------------------
def hidden(characters):
    resultstr = '' 
    for i in range (16,len(characters),8):
        resultstr += bits_to_char(characters[i:i+8])
    return resultstr

# --------------------------------------------------
def embed_text_to_image(text, file_in, file_out):
    pass 


# --------------------------------------------------
def get_embedded_text_from_image(file_in):
    resultbit = ''
    characters = ''
    answer = ''
    image = load_image(file_in)
    for i in image:
        for j in i:
            for k in j:
                if (k%2 == 0):
                    resultbit += '0'
                else:
                    resultbit += '1'
    
    resultbit=resultbit.split('0100111101001011') 
    characters = resultbit[1]
    
    
    answer = '0100111101001011' + resultbit[1] + '0100111101001011'
    return answer


# --------------------------------------------------
SPECIAL_BITS = '0100111101001011'
main()
