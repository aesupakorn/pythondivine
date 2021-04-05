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
    

# --------------------------------------------------
def embed_text_to_image(text, file_in, file_out):
    if len(load_image(file_in))*len(load_image(file_in)[0]) < math.ceil(16+8/3):
        return False 
    else:
        clone = clone_image(load_image(file_in))
        text_in_bi = ''
        track = 0 
        len_text_in_bi = int_to_bits(len(text))

        for t in text:
            text_in_bi += char_to_bits(t)

        text_in_bi = '0100111101001011'+ len_text_in_bi + text_in_bi + '0100111101001011'
        if (math.ceil(len(text_in_bi)/3) > len(clone)*len(clone[0]) or len(text)>65535):
            return False
        else:
            for i in range(len(clone)):
                for j in range(len(clone[i])):
                    for k in range(len(clone[i][j])):
                        if int(clone[i][j][k])%2 == 0:
                            if text_in_bi[track] == '1' :
                                clone[i][j][k]+=1 
                    
                        else:
                            if text_in_bi[track] == '0' :
                                clone[i][j][k]-=1
                        track+=1
                        if(track == len(text_in_bi)):
                            save_image(clone,file_out)
                            return True
    
# --------------------------------------------------
def get_embedded_text_from_image(file_in):
    resultbit = ''
    characters = ''
    resultstr = '' 
    image = load_image(file_in)
    for i in image:
        for j in i:
            for k in j:
                if (k%2 == 0):
                    resultbit += '0'
                else:
                    resultbit += '1'
    resultbit=resultbit.split('0100111101001011') 
    if(len(image[0])*len(image) < math.ceil(16+8/3) or (resultbit[0]!='' and len(resultbit)< 3) or (bits_to_int((resultbit[1][0:16])) != len(resultbit[1][16:])/8)):
        return "" 
    else:
        characters = resultbit[1]
    
        for i in range (16,len(characters),8):
            resultstr += bits_to_char(characters[i:i+8])
    
        return resultstr
     
# --------------------------------------------------
SPECIAL_BITS = '0100111101001011'
main()
