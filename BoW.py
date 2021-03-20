def read_txt():
    f = open(input("File name = "))
    text = f.read()
    f.close()
    return text
def read_stop():
    s=open("stopwords.txt")
    stp=s.read().split()
    s.close()
    return stp
txt = read_txt()
stop = read_stop()
def fhash(txt,M):
    value=0
    for j in range(len(txt)):
        value += (ord(txt[j])*(37**j))
        
    return value%M

def line_count(txt):
    line = (txt.count("\n"))+1
    return line 


def char_count(txt):
    char = (len(txt)-txt.count("\n"))
    return char 
    

def alphanumeric_count(txt):
    count = 0 
    for i in txt:
        if((ord(i)>=65 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57) ):
            count+=1
        else:
            pass
    return count


def word_count(txt):
    for i in txt:
        if((ord(i)>=65 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57) or ord(i)==32 ):
            txt = txt.replace(i,i.lower())
    
        elif(i=="\n"):
            txt = txt.replace(i," ")  

        else:
            txt = txt.replace(i,"")

        newtxt = txt.split(" ")
    return len(newtxt)


def Bow(txt):
    realtxt=[]
    for i in txt:
        if((ord(i)>=65 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57) or ord(i)==32 ):
            txt = txt.replace(i,i.lower())  

        else:
            txt = txt.replace(i," ")

    newtxt = txt.split()

    for i in newtxt:
        if i not in stop:
            realtxt.append(i)

    end=[]

    for i in realtxt:
        if [i, realtxt.count(i)] not in end:
            end.append([i, realtxt.count(i)])
    return end


def Bow2(txt,M):
    realtxt=[]
    for i in txt:
        if((ord(i)>=65 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57) or ord(i)==32 ):
            txt = txt.replace(i,i.lower())
    
        else:
            txt = txt.replace(i," ")

    newtxt = txt.split()

    for i in newtxt:
        if i not in stop:
            realtxt.append(i)


    end=[]
    vbow=[]


    for i in realtxt:
        vbow.append(fhash(i,M))
        

    for i in vbow:
        if [i, vbow.count(i)] not in end:
            end.append([i, vbow.count(i)])
    return end

while(True):
    feature = str(input("Use feature hashing ? (y,Y,n,N) "))
    if feature.lower() == 'y' :
        M=int(input("M = "))
        print(f'''-------------------
char count = {char_count(txt)}
alphanumeric count = {alphanumeric_count(txt)}
line count = {line_count(txt)}
word count = {word_count(txt)}
Bow = {Bow2(txt,M)}''')
        break
    elif feature.lower()== 'n':
        print(f'''-------------------
char count = {char_count(txt)}
alphanumeric count = {alphanumeric_count(txt)}
line count = {line_count(txt)}
word count = {word_count(txt)}
Bow = {Bow(txt)}''')
        break
    else :
        print("Try again.")