import math
import matplotlib.pyplot as plt
#-------------------------------------------------
def show_barcode(digits, ean13_code):
    x = [[int(e) for e in ean13_code]]
    plt.axis('off')
    plt.imshow(x, aspect='auto', cmap='binary')
    plt.title(digits)
    plt.show()
#-------------------------------------------------
def test1():
    digits = input('Enter a 13-digit number: ')
    codes = encode_EAN13(digits)
    if codes == '':
        print(digits, 'is not an EAN-13 number.')
    else:
        decoded_digits = decode_EAN13(codes)
        if decoded_digits == digits:
            show_barcode(digits, codes)
        else:
            print('Error in decoding.')
#-------------------------------------------------
L_codes = ['0001101', '0011001', '0010011', '0111101', '0100011', \
 '0110001', '0101111', '0111011', '0110111', '0001011']
G_codes = ['0100111', '0110011', '0011011', '0100001', '0011101', \
 '0111001', '0000101', '0010001', '0001001', '0010111']
R_codes = ['1110010', '1100110', '1101100', '1000010', '1011100', \
 '1001110', '1010000', '1000100', '1001000', '1110100']
#=================================================
LG_pattern= ['LLLLLL','LLGLGG','LLGGLG','LLGGGL','LGLLGG','LGGLLG',\
    'LGGGLL','LGLGLG','LGLGGL','LGGLGL']
result2=''
count=0


def codes_of( digits, patterns ):
    result = ''
    for i in range(0,len(digits)):
        if patterns[i] == 'L':
            result+=L_codes[int(digits[i])]
        elif patterns[i] == 'G':
            result+=G_codes[int(digits[i])]
        elif patterns[i] == 'R':
            result+=R_codes[int(digits[i])]
    return result 


def digits_of(codes):
    count = 0
    result2=''
    while count != len(codes):
        count1=0

        if codes[count] == '0':
        
            lstcode=''
            for i in range(count,count+7):
                lstcode+=codes[i]
                if(codes[i]=='1'):
                    count1+=1
            
            if(count1 % 2 == 0):
               
                for j2 in range(0,len(G_codes)):
                    if lstcode == G_codes[j2]:
                        result2+=str(j2)
                        
                        break 
            else :
                for j2 in range(0,len(L_codes)):
                    if lstcode == L_codes[j2]:
                        result2+=str(j2)
                        break          
        else:
            lstcode2=''
            for i in range(count,count+7):
                lstcode2+=codes[i]
            for j2 in range(0,len(R_codes)):
                if lstcode2 == R_codes[j2]:
                    result2+=str(j2)
                    break
        count+=7   
    return result2


def patterns_of( codes ):
    count = 0
    result2=''
    while count != len(codes):
        count1=0

        if codes[count] == '0':
        
            lstcode=''
            for i in range(count,count+7):
                lstcode+=codes[i]
                if(codes[i]=='1'):
                    count1+=1
            
            if(count1 % 2 == 0):
               
                for j2 in range(0,len(G_codes)):
                    if lstcode == G_codes[j2]:
                        result2+='G'
                        break
                    else:
                        result2+=''
            else :
                for j2 in range(0,len(L_codes)):
                    if lstcode == L_codes[j2]:
                        result2+='L'
                        break 
                    else:
                        result2+=''         
        else:
            lstcode2=''
            for i in range(count,count+7):
                lstcode2+=codes[i]
            for j2 in range(0,len(R_codes)):
                if lstcode2 == R_codes[j2]:
                    result2+='R'
                    break
                else:
                        result2+='' 
        count+=7   
    if(len(result2) != count/7): 
        return ''
    else:
        return result2
        

def check_digit( digits ):
    total=0
    for i in range(0,len(digits)):
        if i%2==0:
            total+=(int(digits[i])*1)
        else:
            total+=(int(digits[i])*3)
    return str(((int(total/10)+1)*10-total)%10)


def firstnum_pattern(digits):
    i = int(digits[0])
    return LG_pattern[i]


def reverse_firstnum(patterns):
    for i in range(0,len(LG_pattern)):
        if patterns == LG_pattern[i]:
            break
    return  str(i)


def encode_EAN13( digits ):
    head_tail='101'
    middle = '01010'
    checkpart = check_digit(str(digits[0:12]))
    if checkpart == digits[12]:
        fpart = str(digits[1:7])
        spart = str(digits[7:13])
        firtpart =codes_of(fpart,firstnum_pattern(digits))
        secondpart = codes_of(spart,'RRRRRR')
        last = head_tail + firtpart + middle + secondpart + head_tail
        return str(last)
    else:
        return ''


def decode_EAN13( codes ):  
    usecode1 = str(codes[3:45])
    usecode2 = str(codes[50:92])
    firstnum=reverse_firstnum(patterns_of(usecode1))
    mergecode= firstnum+digits_of(usecode1)+digits_of(usecode2)
    return mergecode

test1()