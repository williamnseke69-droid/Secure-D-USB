import hashlib
import facade
import uuid
import json
import os 
import mod1

fichiers_de_la_cle= facade.forwardfile_toanalyze()
fichiers_modifies=[]
nouveaux_fichiers=[]
fichiers_modifies=[]
fichiers_non_ouvert=[]
fichiers_cibles=[]
chemin_disparu=[]
chemins_modifies=[]

"""ici, les fonctions apelees par main.py lorsque la cle n'est pas connue:
- create_id(): cree un fichier dans la racine de la cle, puis ecris un id genere au hasard a l'interieur
- create_memory(): hash tous les fichiers de la liste brute transferee par mod1, et les enregistrent dans un dico imbrique
- json_exist:s'assure que le pc contient un fichier memoire. Si oui, convertit son contenu en dictionnaire qui sera modifie tout au de l'algo
- save_mamory: enregistre le dictionnaire obtenu apres create_memory dans un fichier json acrasant son ancien contenu
"""

def json_exist():
    if os.path.exists("memoire.json")== True:
        fichier_memoire= open("memoire.json", "r", encoding="utf-8")
        memoire=json.load(fichier_memoire)
    else: 
        memoire={}
    return memoire  

def create_id():
    identifiant= f"id_cle{uuid.uuid4().hex[:4]}"
    marqueur= open("C:/Users/EVERMATE/ma_cle/secure_d_usb.txt", "w")
    marqueur.write(identifiant)
    return identifiant
    
def create_memory(liste_fichiers):  
    memoire=json_exist()
    id_cle= create_id()
    memoire[id_cle]={}
    for element in liste_fichiers:   
        hasheur= hashlib.sha256()
        try:
            fic= open(element, "rb")
        except:
            continue
        content= fic.read()
        hasheur.update(content)
        code= hasheur.hexdigest()
        memoire[id_cle][element]=code
    return memoire

def save_memory():
    dico=create_memory(fichiers_de_la_cle)
    with open("memoire.json", "w", encoding="utf-8") as fichier_memoire:
        json.dump(dico, fichier_memoire, indent=4, ensure_ascii=False)
        
"""ici, les fonctions appelees par main.py lorsque la cle est connu:

"""


def load_memory():
    _,id_cle=mod1.reconnaissance_cle()
    with open("memoire.json", "r", encoding="utf-8") as fichier_memoire:
        memoire=json.load(fichier_memoire)
        if id_cle in memoire:
            memoire=memoire[id_cle]
            return memoire
        
memoire=load_memory()
init_state=memoire.copy()

def generate_hash(element):
    hasheur= hashlib.sha256()
    try:
        fic= open(element, "rb")
    except:
        fichiers_non_ouvert.append(element)
    content= fic.read()
    hasheur.update(content)
    code= hasheur.hexdigest()
        
    return code
        
def classify_file():
    for file in fichiers_de_la_cle:
        hash=generate_hash(file)
        if file in memoire and hash== memoire[file]:
            continue
        if file not in memoire:
            nouveaux_fichiers.append(file)
            for element in nouveaux_fichiers :
                memoire[element]=hash
        if file in memoire and hash!= memoire[file]:
            fichiers_modifies.append(file)
            for element in fichiers_modifies:
                memoire[element]=hash
    fichiers_cibles= fichiers_modifies + nouveaux_fichiers
    return fichiers_cibles

def clean_memory(): 
    for key in init_state:
        if key not in fichiers_de_la_cle:
            chemin_disparu.append(key)
        for chemin in chemin_disparu:
           hash_path=init_state[chemin] 
           for element in nouveaux_fichiers:
               code=generate_hash(element)
               if hash_path==code:
                   chemins_modifies.append(key)
    for path in chemins_modifies:
        del memoire[path]
        
        
        

      
            
            
            
        
        
        
        
            
        
