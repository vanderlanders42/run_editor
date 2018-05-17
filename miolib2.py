# coding: utf8
#miolib2 (Momioka's Idiot sOrting LIBrary 2) Version 1.02
#Copyright 2017,2018 Red Ponies A.F.

import random

"""
 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A  PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
"""

voyelle=["a", "e", "y", "u", "i", "o"]
consonne=["z", "r", "t" ,"m" ,"w" ,"x" ,"c" ,"v" ,"b" , "n"]
consoos=["p" ,"q" ,"s" ,"d" ,"f" ,"g" ,"h" ,"j" ,"k" , "l"]
kana=["あ", "う", "い", "れ", "允", "臼", "乙", "し", "く", "か", "丨", "一", "ア"]

def lettre(nombre):
    txt=""
    voyel=int(nombre[0])
    conso=int(nombre[1])
    conos=int(nombre[2])
    kanac=int(nombre[3])
    i=0
    while i < voyel:
        i+=1
        num=random.randrange(0,5)
        txt+=voyelle[num]
    i=0
    while i < conso:
        i+=1
        num=random.randrange(0,9)
        txt+=consonne[num]
    i=0
    while i < conos:
        i+=1
        num=random.randrange(0,9)
        txt+=consoos[num]
    i=0
    while i < kanac:
        i+=1
        num=random.randrange(0,12)
        txt+=kana[num]

	#Separation de caractères
    txt+="¥"
    return(txt)

def encrypt(txtc):
    txt=""
    for i in txtc:
        if i=="U":
            txt+=lettre("1542")
        elif i=="L":
            txt+=lettre("1234")
        elif i=="a":
            txt+=lettre("1324")
        elif i=="M":
            txt+=lettre("4231")
        elif i=="g":
            txt+=lettre("4213")
        elif i=="d":
            txt+=lettre("3214")
        elif i=="e":
            txt+=lettre("3124")
        elif i=="n":
            txt+=lettre("3098")
        elif i=="v":
            txt+=lettre("2442")
        elif i=="c":
            txt+=lettre("1227")
        elif i=="p":
            txt+=lettre("7829")
        elif i=="q":
            txt+=lettre("1458")
        elif i=="i":
            txt+=lettre("9852")
        elif i=="t":
            txt+=lettre("1481")
        elif i=="l":
            txt+=lettre("9888")
        elif i=="u":
            txt+=lettre("7272")
        elif i=="s":
            txt+=lettre("2727")
        elif i=="r":
            txt+=lettre("1221")
        elif i=="b":
            txt+=lettre("8801")
        elif i=="%":
            txt+=lettre("8081")
        elif i=="|":
            txt+=lettre("8080")
        elif i=="à":
            txt+=lettre("7787")
        elif i=="^":
            txt+=lettre("7877")
        elif i=="²":
            txt+=lettre("9181")
        elif i=="E":
            txt+=lettre("9801")
        elif i=="}":
            txt+=lettre("7212")
        elif i=="D":
            txt+=lettre("7122")
        elif i=="°":
            txt+=lettre("4296")
        elif i==";":
            txt+=lettre("6386")
        elif i=="=":
            txt+=lettre("1010")
        elif i=="&":
            txt+=lettre("9152")
        elif i=="J":
            txt+=lettre("4200")
        elif i=="<":
            txt+=lettre("4279")
        elif i=="G":
            txt+=lettre("9724")
        elif i=="C":
            txt+=lettre("4444")
        elif i=="!":
            txt+=lettre("6666")
        elif i=="+":
            txt+=lettre("6576")
        elif i=="x":
            txt+=lettre("6756")
        elif i=="Z":
            txt+=lettre("9879")
        elif i=="Q":
            txt+=lettre("1186")
        elif i=="o":
            txt+=lettre("1286")
        elif i=="m":
            txt+=lettre("1386")
        elif i=="ê":
            txt+=lettre("1486")
        elif i=="f":
            txt+=lettre("1586")
        elif i=="é":
            txt+=lettre("1686")
        elif i=="V":
            txt+=lettre("1786")
        elif i=="'":
            txt+=lettre("1886")
        elif i==",":
            txt+=lettre("6526")
        elif i=="h":
            txt+=lettre("6312")
        elif i=="w":
            txt+=lettre("6121")
        elif i==">":
            txt+=lettre("6989")
        elif i=='"':
            txt+=lettre("1418")
        elif i=="{":
            txt+=lettre("3945")
        elif i=="µ":
            txt+=lettre("2508")
        elif i=="/":
            txt+=lettre("2058")
        elif i=="?":
            txt+=lettre("2048")
        elif i=="\\":
            txt+=lettre("1242")
        elif i==":":
            txt+=lettre("2020")
        elif i=="-":
            txt+=lettre("4848")
        elif i=="I":
            txt+=lettre("9081")
        elif i=="]":
            txt+=lettre("8484")
        elif i=="(":
            txt+=lettre("1826")
        elif i==".":
            txt+=lettre("1792")
        elif i=="X":
            txt+=lettre("2826")
        elif i=="P":
            txt+=lettre("3182")
        elif i=="F":
            txt+=lettre("3386")
        elif i=="ç":
            txt+=lettre("3486")
        elif i=="K":
            txt+=lettre("3487")
        elif i=="W":
            txt+=lettre("3586")
        elif i=="H":
            txt+=lettre("3334")
        elif i=="B":
            txt+=lettre("4343")
        elif i=="~":
            txt+=lettre("1313")
        elif i=="@":
            txt+=lettre("4136")
        elif i=="O":
            txt+=lettre("8611")
        elif i=="R":
            txt+=lettre("8622")
        elif i=="T":
            txt+=lettre("6521")
        elif i=="S":
            txt+=lettre("9170")
        elif i=="A":
            txt+=lettre("9710")
        elif i=="j":
            txt+=lettre("6512")
        elif i=="z":
            txt+=lettre("6152")
        elif i=="#":
            txt+=lettre("7648")
        elif i==")":
            txt+=lettre("7468")
        elif i=="[":
            txt+=lettre("6369")
        elif i=="N":
            txt+=lettre("1639")
        elif i=="Y":
            txt+=lettre("9316")
        elif i=="è":
            txt+=lettre("9631")
        elif i=="y":
            txt+=lettre("3113")
        elif i=="k":
            txt+=lettre("7742")
        elif i=="0":
            txt+=lettre("5959")
        elif i=="1":
            txt+=lettre("5599")
        elif i=="2":
            txt+=lettre("5536")
        elif i=="3":
            txt+=lettre("6561")
        elif i=="4":
            txt+=lettre("9496")
        elif i=="5":
            txt+=lettre("9062")
        elif i=="6":
            txt+=lettre("1296")
        elif i=="7":
            txt+=lettre("2431")
        elif i=="8":
            txt+=lettre("7216")
        elif i=="9":
            txt+=lettre("6721")
        elif i=="ß":
            txt+=lettre("9901")
        elif i=="_":
            txt+=lettre("7195")
        elif i=="	":
            txt+=lettre("7915")
        elif i=="*":
            txt+=lettre("7815")
        elif i=="$":
            txt+=lettre("7185")
        elif i=="§":
            txt+=lettre("7825")
        elif i=="ù":
            txt+=lettre("7285")
        elif i=="ü":
            txt+=lettre("6258")
		#Espace
        elif i==" ":
            txt+="¤"
    return(txt)

def decrypt(txtc):
    voyel=0
    conso=0
    conos=0
    kanac=0
    txt=""
    for i in txtc:
        if i == "¥":
            voyel=str(voyel)
            conso=str(conso)
            conos=str(conos)
            kanac=str(kanac)
            nb=""
            nb=voyel+conso+conos+kanac
            nb=int(nb)
            if nb==1542:
                txt+="U"
            elif nb==1234:
                txt+="L"
            elif nb==1324:
                txt+="a"
            elif nb==4231:
                txt+="M"
            elif nb==4213:
                txt+="g"
            elif nb==3214:
                txt+="d"
            elif nb==3124:
                txt+="e"
            elif nb==3098:
                txt+="n"
            elif nb==2442:
                txt+="v"
            elif nb==1227:
                txt+="c"
            elif nb==7829:
                txt+="p"
            elif nb==1458:
                txt+="q"
            elif nb==9852:
                txt+="i"
            elif nb==1481:
                txt+="t"
            elif nb==9888:
                txt+="l"
            elif nb==7272:
                txt+="u"
            elif nb==2727:
                txt+="s"
            elif nb==1221:
                txt+="r"
            elif nb==8801:
                txt+="b"
            elif nb==8081:
                txt+="%"
            elif nb==8080:
                txt+="|"
            elif nb==7787:
                txt+="à"
            elif nb==7877:
                txt+="^"
            elif nb==9181:
                txt+="²"
            elif nb==9801:
                txt+="E"
            elif nb==7212:
                txt+="}"
            elif nb==7122:
                txt+="D"
            elif nb==4296:
                txt+="°"
            elif nb==6386:
                txt+=";"
            elif nb==1010:
                txt+="="
            elif nb==9152:
                txt+="&"
            elif nb==4200:
                txt+="J"
            elif nb==4279:
                txt+="<"
            elif nb==9724:
                txt+="G"
            elif nb==4444:
                txt+="C"
            elif nb==6666:
                txt+="!"
            elif nb==6576:
                txt+="+"
            elif nb==6756:
                txt+="x"
            elif nb==9879:
                txt+="Z"
            elif nb==1186:
                txt+="Q"
            elif nb==1286:
                txt+="o"
            elif nb==1386:
                txt+="m"
            elif nb==1486:
                txt+="ê"
            elif nb==1586:
                txt+="f"
            elif nb==1686:
                txt+="é"
            elif nb==1786:
                txt+="V"
            elif nb==1886:
                txt+="'"
            elif nb==6526:
                txt+=","
            elif nb==6312:
                txt+="h"
            elif nb==6121:
                txt+="w"
            elif nb==6989:
                txt+=">"
            elif nb==1418:
                txt+='"'
            elif nb==3945:
                txt+="{"
            elif nb==2508:
                txt+="µ"
            elif nb==2058:
                txt+="/"
            elif nb==2048:
                txt+="?"
            elif nb==1242:
                txt+="\\"
            elif nb==2020:
                txt+=":"
            elif nb==4848:
                txt+="-"
            elif nb==9081:
                txt+="I"
            elif nb==8484:
                txt+="]"
            elif nb==1826:
                txt+="("
            elif nb==1792:
                txt+="."
            elif nb==2826:
                txt+="X"
            elif nb==3182:
                txt+="P"
            elif nb==3386:
                txt+="F"
            elif nb==3486:
                txt+="ç"
            elif nb==3487:
                txt+="K"
            elif nb==3586:
                txt+="W"
            elif nb==3334:
                txt+="H"
            elif nb==4343:
                txt+="B"
            elif nb==1313:
                txt+="~"
            elif nb==4136:
                txt+="@"
            elif nb==8611:
                txt+="O"
            elif nb==8622:
                txt+="R"
            elif nb==6521:
                txt+="T"
            elif nb==9170:
                txt+="S"
            elif nb==9710:
                txt+="A"
            elif nb==6512:
                txt+="j"
            elif nb==6152:
                txt+="z"
            elif nb==7648:
                txt+="#"
            elif nb==7468:
                txt+=")"
            elif nb==6369:
                txt+="["
            elif nb==1639:
                txt+="N"
            elif nb==9316:
                txt+="Y"
            elif nb==9631:
                txt+="è"
            elif nb==3113:
                txt+="y"
            elif nb==7742:
                txt+="k"
            elif nb==5959:
                txt+="0"
            elif nb==5599:
                txt+="1"
            elif nb==5536:
                txt+="2"
            elif nb==6561:
                txt+="3"
            elif nb==9496:
                txt+="4"
            elif nb==9062:
                txt+="5"
            elif nb==1296:
                txt+="6"
            elif nb==2431:
                txt+="7"
            elif nb==7216:
                txt+="8"
            elif nb==6721:
                txt+="9"
            elif nb==9901:
                txt+="ß"
            elif nb==7195:
                txt+="_"
            elif nb==7915:
                txt+="	"
            elif nb==7815:
                txt+="*"
            elif nb==7185:
                txt+="$"
            elif nb==7825:
                txt+="§"
            elif nb==7285:
                txt+="ù"
            elif nb==6258:
                txt+="ü"
            voyel=0
            conso=0
            conos=0
            kanac=0
        elif i == "¤":
            txt+=" "
        else:
            for elt in voyelle:
                if i == elt:
                    voyel+=1
            for elt in consonne:
                if i == elt:
                    conso+=1
            for elt in consoos:
                if i == elt:
                    conos+=1
            for elt in kana:
                if i == elt:
                    kanac+=1
    return txt
