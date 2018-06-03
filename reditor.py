# coding: utf8
#REditor (Run Editor) Version 1.50
#Copyright 2017,2018 Vladimir Vanderlanders, REDPONIES A.F.

from sys import argv
from sys import exit
from colorama import Fore, Back, Style, init

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
init()
#Definition internes

def txtopen(file):
    #Variable globale pour le nom du fichier.
    global fileref
    fileref = file
    
    print (Fore.BLACK + Back.WHITE + "         Run Editor - Version 1.50         " + Style.RESET_ALL)
    print("File : " + file)
    
    text = open(file, 'r', encoding="utf-8")
    #Variable globale contenant via une liste le texte.
    global content
    content = text.readlines()
    global ref_content
    ref_content = content
    text.close()
    numl = lines()
    
    print ("Lines : " + str(numl) + "\nUse 'help' for a list of all commands.")
    print (Fore.BLACK + Back.WHITE + "                                           " + Style.RESET_ALL + "\n")
    
    listing()
    prompt()

def prompt():
    #Boucle pour recevoir les commandes.
    term = input("Ready\n")
    command = term.split(' ', 1)[0]
    args = term.partition(' ')[-1]
    if command in dico:
        #print (command + "/" + args)
        if args != '':
            dico[command](args)
        else:
            dico[command]()
        prompt()
    else:
        print(Fore.RED + "Syntax error\n" + Style.RESET_ALL)
        prompt()

def lines():
    #Calcule le nombre de lignes (Pour le compte au début du programme).
    with open(fileref, encoding="utf-8") as f:
        num_lines = sum(1 for _ in f)
    return num_lines


#Definitions externes

def listing():
    #Affiche chaque ligne du fichier, avec son numéro.
    nbrl = 1
    for line in content:
        line = line.split('\n')[0]
        print (Fore.BLACK + Back.CYAN + str(nbrl) + Style.RESET_ALL + line)
        nbrl = nbrl + 1
    print ('\n')

def add(txt):
    #Lineused doit préalablement être défini par gotoline().
    global lineused
    linemod = ""
    linemod = lineused.replace("\n", "")
    linemod = linemod + txt + "\n"
    #print(nlineused)
    content[nlineused] = linemod
    lineused = linemod

def delete(n):
    n = int(n)
    n -= 1
    del content[n]

def insert(txt):
    linemod = txt + "\n"
    #print(nlineused)
    content.insert(nlineused, linemod)
    lineused = linemod

def edit(n):
    gotoline(n)
    delete(n)
    print(Fore.BLACK + Back.GREEN + "EDIT " + n + " :" + Style.RESET_ALL)
    txt = input()
    insert(txt)
	
def lol(n):
    #Truc TOTALEMENT inutile, mais à fort potentiel de conneries.
    if int(n) != 0:
        gotoline(11)
        delete(11)
        txt = "<betadata>"
        insert(txt)

    else:
        gotoline(11)
        delete(11)
        txt = "<metadata>"
        insert(txt)

def cassohtoa():
    #Sortie unique du programme, avec confirmation.
    #TODO: Prise en compte de l'édition du fichier ou non.
    confirm = input("Save file ? (Y/n)")
    if confirm != 'n':
        savefile()
        exit()
    else :
        exit()

def gotoline(n,p=0):
    #La variable p permet de zapper ou non le print, utile pour les definitions de cryptage.
    n = int(n)
    n -= 1
    while len(content) <= n:
        content.append("")
    global lineused
    lineused = content[n]
    if p==0:
        print ("Line selected : " + lineused)
        pass
    else:
        pass
    global nlineused
    nlineused = n

def savefile():
    if fichier_choisi == True :
        sv = open(fileref, "r+", encoding="utf-8")
        sv.seek(0)
        sv.truncate()
        for line in content:
            sv.write("%s" % line)
        sv.close
    else :
        nom_save = input("Name of the file ?")

def savecopy(sfile):
    #Crée le fichier
    cr = open(sfile, "a")
    cr.close()
    #Ecrit le fichier
    sv = open(sfile, "r+", encoding="utf-8")
    sv.seek(0)
    sv.truncate()
    for line in content:
        sv.write("%s" % line)
    sv.close

def jeanne():
    print("-----Help-----\n")
    print("-Basics:\n")
    print("list: Show text file, and line number")
    print("save: Save text file")
    print("saveas [directory/name] Save a copy of the file with that name")
    print("edit [line number]: Edit line")
    print("exit: Quit the Run Editor")
    print("\n-Advanced:\n")
    print("line [line number]: Select a line")
    print("add [text]: Add text to this line")
    print("ins [text]: Insert text to this line")
    print("del [line number]: Delete line")
    print("\n-Misc.:\n")
    print("lol [0/1]: For AbiWord files ONLY, do mess with them if lol 1 used, restore with lol 0")

dico = {'list':listing, 'add':add, 'lol':lol, 'exit':cassohtoa, 'line':gotoline, 'save':savefile, 'del':delete, 'ins':insert, 'edit':edit, 'help':jeanne, 'saveas':savecopy}

#Execution
if len(argv) == 1:
    print(Fore.YELLOW + "WARNING: No file selected ! Starting with none." + Style.RESET_ALL)
    fichier_choisi = False
    filetoopen = "dummy"
    cr = open("dummy", "a")
    cr.close()
    txtopen(filetoopen)
elif len(argv) == 2:
    fichier_choisi = True
    filetoopen = argv[1]
    txtopen(filetoopen)
else:
    print("Too many arguments !")
    print("Syntax: reditor or reditor file")
