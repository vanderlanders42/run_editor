# coding: utf8
#miolib (Momioka's Idiot sOrting LIBrary) Version 1.01
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
consonne=["z", "r", "t", "p" ,"q" ,"s" ,"d" ,"f" ,"g" ,"h" ,"j" ,"k" ,"l" ,"m" ,"w" ,"x" ,"c" ,"v" ,"b" , "n"]

def lettre(nombre):
    txt=""
    voyel=int(nombre[0])
    conso=int(nombre[1])
    i=0
    while i < voyel:
        i+=1
        num=random.randrange(0,5)
        txt+=voyelle[num]
    i=0
    while i < conso:
        i+=1
        num=random.randrange(0,20)
        txt+=consonne[num]
	#Separation de caractères
    txt+="¥"
    return(txt)

def encrypt(txtc):
    txt=""
    for i in txtc:
        if i=="U":
            txt+=lettre("01")
        elif i=="L":
            txt+=lettre("02")
        elif i=="a":
            txt+=lettre("03")
        elif i=="M":
            txt+=lettre("04")
        elif i=="g":
            txt+=lettre("05")
        elif i=="d":
            txt+=lettre("06")
        elif i=="e":
            txt+=lettre("07")
        elif i=="n":
            txt+=lettre("08")
        elif i=="v":
            txt+=lettre("09")
        elif i=="c":
            txt+=lettre("10")
        elif i=="p":
            txt+=lettre("11")
        elif i=="q":
            txt+=lettre("12")
        elif i=="i":
            txt+=lettre("13")
        elif i=="t":
            txt+=lettre("14")
        elif i=="l":
            txt+=lettre("15")
        elif i=="u":
            txt+=lettre("16")
        elif i=="s":
            txt+=lettre("17")
        elif i=="r":
            txt+=lettre("18")
        elif i=="b":
            txt+=lettre("19")
        elif i=="%":
            txt+=lettre("20")
        elif i=="|":
            txt+=lettre("21")
        elif i=="à":
            txt+=lettre("22")
        elif i=="^":
            txt+=lettre("23")
        elif i=="²":
            txt+=lettre("24")
        elif i=="E":
            txt+=lettre("25")
        elif i=="}":
            txt+=lettre("27")
        elif i=="D":
            txt+=lettre("29")
        elif i=="°":
            txt+=lettre("31")
        elif i==";":
            txt+=lettre("32")
        elif i=="=":
            txt+=lettre("33")
        elif i=="&":
            txt+=lettre("34")
        elif i=="J":
            txt+=lettre("35")
        elif i=="<":
            txt+=lettre("36")
        elif i=="G":
            txt+=lettre("37")
        elif i=="C":
            txt+=lettre("38")
        elif i=="!":
            txt+=lettre("39")
        elif i=="+":
            txt+=lettre("40")
        elif i=="x":
            txt+=lettre("41")
        elif i=="Z":
            txt+=lettre("42")
        elif i=="Q":
            txt+=lettre("43")
        elif i=="o":
            txt+=lettre("44")
        elif i=="m":
            txt+=lettre("45")
        elif i=="ê":
            txt+=lettre("46")
        elif i=="f":
            txt+=lettre("47")
        elif i=="é":
            txt+=lettre("48")
        elif i=="V":
            txt+=lettre("49")
        elif i=="'":
            txt+=lettre("50")
        elif i==",":
            txt+=lettre("51")
        elif i=="h":
            txt+=lettre("52")
        elif i=="w":
            txt+=lettre("53")
        elif i==">":
            txt+=lettre("54")
        elif i=='"':
            txt+=lettre("55")
        elif i=="{":
            txt+=lettre("56")
        elif i=="µ":
            txt+=lettre("57")
        elif i=="/":
            txt+=lettre("58")
        elif i=="?":
            txt+=lettre("59")
        elif i=="\\":
            txt+=lettre("63")
        elif i==":":
            txt+=lettre("64")
        elif i=="-":
            txt+=lettre("65")
        elif i=="I":
            txt+=lettre("66")
        elif i=="]":
            txt+=lettre("67")
        elif i=="(":
            txt+=lettre("68")
        elif i==".":
            txt+=lettre("69")
        elif i=="X":
            txt+=lettre("72")
        elif i=="P":
            txt+=lettre("73")
        elif i=="F":
            txt+=lettre("74")
        elif i=="ç":
            txt+=lettre("75")
        elif i=="K":
            txt+=lettre("76")
        elif i=="W":
            txt+=lettre("77")
        elif i=="H":
            txt+=lettre("78")
        elif i=="B":
            txt+=lettre("79")
        elif i=="~":
            txt+=lettre("82")
        elif i=="@":
            txt+=lettre("83")
        elif i=="O":
            txt+=lettre("84")
        elif i=="R":
            txt+=lettre("85")
        elif i=="T":
            txt+=lettre("86")
        elif i=="S":
            txt+=lettre("87")
        elif i=="A":
            txt+=lettre("88")
        elif i=="j":
            txt+=lettre("90")
        elif i=="z":
            txt+=lettre("91")
        elif i=="#":
            txt+=lettre("92")
        elif i==")":
            txt+=lettre("93")
        elif i=="[":
            txt+=lettre("94")
        elif i=="N":
            txt+=lettre("95")
        elif i=="Y":
            txt+=lettre("96")
        elif i=="è":
            txt+=lettre("97")
        elif i=="y":
            txt+=lettre("98")
        elif i=="k":
            txt+=lettre("99")
		#Espace
        elif i==" ":
            txt+="¤"
    return(txt)

def decrypt(txtc):
    voyel=0
    conso=0
    txt=""
    for i in txtc:
        if i == "¥":
            voyel=str(voyel)
            conso=str(conso)
            nb=""
            nb=voyel+conso
            nb=int(nb)
            if nb==1:
                txt+="U"
            elif nb==2:
                txt+="L"
            elif nb==3:
                txt+="a"
            elif nb==4:
                txt+="M"
            elif nb==5:
                txt+="g"
            elif nb==6:
                txt+="d"
            elif nb==7:
                txt+="e"
            elif nb==8:
                txt+="n"
            elif nb==9:
                txt+="v"
            elif nb==10:
                txt+="c"
            elif nb==11:
                txt+="p"
            elif nb==12:
                txt+="q"
            elif nb==13:
                txt+="i"
            elif nb==14:
                txt+="t"
            elif nb==15:
                txt+="l"
            elif nb==16:
                txt+="u"
            elif nb==17:
                txt+="s"
            elif nb==18:
                txt+="r"
            elif nb==19:
                txt+="b"
            elif nb==20:
                txt+="%"
            elif nb==21:
                txt+="|"
            elif nb==22:
                txt+="à"
            elif nb==23:
                txt+="^"
            elif nb==24:
                txt+="²"
            elif nb==25:
                txt+="E"
            elif nb==26:
                txt+="ばか！"
            elif nb==27:
                txt+="}"
            elif nb==28:
                txt+="ばか！"
            elif nb==29:
                txt+="D"
            elif nb==30:
                txt+="ばか！"
            elif nb==31:
                txt+="°"
            elif nb==32:
                txt+=";"
            elif nb==33:
                txt+="="
            elif nb==34:
                txt+="&"
            elif nb==35:
                txt+="J"
            elif nb==36:
                txt+="<"
            elif nb==37:
                txt+="G"
            elif nb==38:
                txt+="C"
            elif nb==39:
                txt+="!"
            elif nb==40:
                txt+="+"
            elif nb==41:
                txt+="x"
            elif nb==42:
                txt+="Z"
            elif nb==43:
                txt+="Q"
            elif nb==44:
                txt+="o"
            elif nb==45:
                txt+="m"
            elif nb==46:
                txt+="ê"
            elif nb==47:
                txt+="f"
            elif nb==48:
                txt+="é"
            elif nb==49:
                txt+="V"
            elif nb==50:
                txt+="'"
            elif nb==51:
                txt+=","
            elif nb==52:
                txt+="h"
            elif nb==53:
                txt+="w"
            elif nb==54:
                txt+=">"
            elif nb==55:
                txt+='"'
            elif nb==56:
                txt+="{"
            elif nb==57:
                txt+="µ"
            elif nb==58:
                txt+="/"
            elif nb==59:
                txt+="?"
            elif nb==60:
                txt+="ばか！"
            elif nb==61:
                txt+="ばか！"
            elif nb==62:
                txt+="ばか！"
            elif nb==63:
                txt+="\\"
            elif nb==64:
                txt+=":"
            elif nb==65:
                txt+="-"
            elif nb==66:
                txt+="I"
            elif nb==67:
                txt+="]"
            elif nb==68:
                txt+="("
            elif nb==69:
                txt+="."
            elif nb==70:
                txt+="ばか！"
            elif nb==72:
                txt+="X"
            elif nb==73:
                txt+="P"
            elif nb==74:
                txt+="F"
            elif nb==75:
                txt+="ç"
            elif nb==76:
                txt+="K"
            elif nb==77:
                txt+="W"
            elif nb==78:
                txt+="H"
            elif nb==79:
                txt+="B"
            elif nb==80:
                txt+="ばか！"
            elif nb==81:
                txt+="ばか！"
            elif nb==82:
                txt+="~"
            elif nb==83:
                txt+="@"
            elif nb==84:
                txt+="O"
            elif nb==85:
                txt+="R"
            elif nb==86:
                txt+="T"
            elif nb==87:
                txt+="S"
            elif nb==88:
                txt+="A"
            elif nb==89:
                txt+="ばか！"
            elif nb==90:
                txt+="j"
            elif nb==91:
                txt+="z"
            elif nb==92:
                txt+="#"
            elif nb==93:
                txt+=")"
            elif nb==94:
                txt+="["
            elif nb==95:
                txt+="N"
            elif nb==96:
                txt+="Y"
            elif nb==97:
                txt+="è"
            elif nb==98:
                txt+="y"
            elif nb==99:
                txt+="k"
            voyel=0
            conso=0
        elif i == "¤":
            txt+=" "
        else:
            for elt in voyelle:
                if i == elt:
                    voyel+=1
            for elt in consonne:
                if i == elt:
                    conso+=1
    return txt
