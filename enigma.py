#coding=utf-8
#Author: sangwf@qq.com
#Usage:
#$python enigma.py x y z hello
#rjzus
#$ python enigma.py x y z rjzus
#hello
import sys

rotor1 = {'a':'b', 'b':'a', 'c':'d', 'd':'c', 'e':'f', 'f':'e', 'g':'h', 'h':'g',
    'i':'j', 'j':'i', 'k':'l', 'l':'k', 'm':'n', 'n':'m', 'o':'p', 'p':'o', 'q':'r',
    'r':'q', 's':'t', 't':'s', 'u':'v', 'v':'u', 'w':'x', 'x':'w', 'y':'z', 'z':'y'}
    
rotor2 = {'a':'c', 'b':'b', 'c':'a', 'd':'f', 'e':'e', 'f':'d', 'g':'i', 'h':'h',
    'i':'g', 'j':'l', 'k':'k', 'l':'j', 'm':'o', 'n':'n', 'o':'m', 'p':'r', 'q':'q',
    'r':'p', 's':'u', 't':'t', 'u':'s', 'v':'x', 'w':'w', 'x':'v', 'y':'z', 'z':'y'}
    
rotor3 = {'a':'d', 'b':'c', 'c':'b', 'd':'a', 'e':'h', 'f':'g', 'g':'f', 'h':'e',
    'i':'l', 'j':'k', 'k':'j', 'l':'i', 'm':'p', 'n':'o', 'o':'n', 'p':'m', 'q':'t',
    'r':'s', 's':'r', 't':'q', 'u':'x', 'v':'w', 'w':'v', 'x':'u', 'y':'y', 'z':'z'}

plugboard = {'a':'b', 'k':'l', 'c':'d', 'm':'n', 'e':'f', 'o':'p', 'g':'h', 'q':'r',
    'i':'j', 'y':'z'}

reflector = {'a':'s', 'b':'t', 'c':'u', 'd':'v', 'e':'w', 'f':'x', 'g':'y', 'h':'z',
    'i':'r', 'j':'q', 'k':'p', 'l':'o', 'm':'n'}

def invert_dict(d):  
    return dict((v,k) for k,v in d.iteritems()) 

def rotate(rotor):
    new_rotor = dict()
    for k,v in rotor.items():
        new_v = chr(ord(v) + 1)
        if (ord(v) + 1) > ord('z'):
            new_v = 'a'
        new_rotor[k] = new_v
    return new_rotor

if len(sys.argv) != 5:
    print "argc=", len(sys.argv)
    print "python enigma.py [Rotor1] [Rotor2] [Rotor3] [INPUT CODE]"
    sys.exit()

#for i in range(0, len(sys.argv)):
#    print "Parameter", i, sys.argv[i]

R1 = sys.argv[1].lower()
R2 = sys.argv[2].lower()
R3 = sys.argv[3].lower()
input_code = sys.argv[4].lower()

for i in range(ord(R1) - ord('a')):
    rotor1 = rotate(rotor1)
for i in range(ord(R2) - ord('a')):
    rotor2 = rotate(rotor2)
for i in range(ord(R1) - ord('a')):
    rotor3 = rotate(rotor3)



invert_plugboard = invert_dict(plugboard)
invert_rotor1 = invert_dict(rotor1)
invert_rotor2 = invert_dict(rotor2)
invert_rotor3 = invert_dict(rotor3)
invert_reflector = invert_dict(reflector)
reflector = dict(invert_reflector.items() + reflector.items())

output_code = ""

for i in range(len(input_code)):
    c = input_code[i] #当前字符
    encode_c = c
    if c in plugboard:
        encode_c = plugboard[c]
    elif c in invert_plugboard:
        encode_c = invert_plugboard[c]
    encode_c = rotor1[encode_c]
    encode_c = rotor2[encode_c]
    encode_c = rotor3[encode_c]
    encode_c = reflector[encode_c]
    encode_c = invert_rotor3[encode_c]
    encode_c = invert_rotor2[encode_c]
    encode_c = invert_rotor1[encode_c]
    if encode_c == c: #出来的又回到了按下的按键，肯定是有插线的
        if encode_c in plugboard:
            encode_c = plugboard[encode_c]
        else:
            encode_c = invert_plugboard[encode_c]
    else:
        if encode_c in plugboard and plugboard[encode_c] != c:
            encode_c = plugboard[encode_c]
        elif encode_c in invert_plugboard and invert_plugboard[encode_c] != c:
            encode_c = invert_plugboard[encode_c]
    output_code += encode_c
    #转动一次轮子
    rotor1 = rotate(rotor1)
    invert_rotor1 = invert_dict(rotor1)
    if i > 0 and i % 26 == 0:
        rotor2 = rotate(rotor2)
        invert_rotor2 = invert_dict(rotor2)
    if i > 0 and i % (26 * 26) == 0:
        rotor3 = rotate(rotor3)
        invert_rotor3 = invert_dict(rotor3)        
    
print output_code
