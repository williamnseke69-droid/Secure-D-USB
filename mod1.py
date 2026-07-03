import os
import stat
import hashlib

chemin= "C:\\Users\\EVERMATE\\ma_cle" 

def reconnaissance_cle():
    for element in os.listdir(chemin):
        element= os.path.join(chemin, element)
        if os.path.isfile(element)== True:  
            element_copy= os.path.basename(element)
            nom, ext= os.path.splitext(element_copy)
            if nom== "secure_d_usb" and ext==".txt": 
                marqueur= open(element, "r")
                identifiant= marqueur.read()
                return "TRUE", identifiant
            
    return "FALSE", "None"


def fill_fichiers_de_la_cle(key_path):
    fichiers_de_la_cle= []   
    for path, _, fichiers in os.walk(key_path):
        for element in fichiers:
            fichiers_de_la_cle.append(os.path.join(path,element))
    return fichiers_de_la_cle
