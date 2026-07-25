import hashlib
import uuid
import json
import os 
import mod1
from manage_error import KeyNotFoundError

"""ici, les fonctions apelees par main.py lorsque la cle n'est pas connue:
- create_id(): cree un fichier dans la racine de la cle, puis ecris un id genere au hasard a l'interieur
- create_memory(): hash tous les fichiers de la liste brute transferee par mod1, et les enregistrent dans un dico imbrique
- json_exist:s'assure que le pc contient un fichier memoire. Si oui, convertit son contenu en dictionnaire qui sera modifie tout au de l'algo
- save_mamory: enregistre le dictionnaire obtenu apres create_memory dans un fichier json acrasant son ancien contenu
"""

def json_exist():
    if os.path.exists("memoire.json")== True:
        with open("memoire.json", "r", encoding="utf-8") as fichier_memoire:
            memoire=json.load(fichier_memoire)
    else: 
        memoire={}
    return memoire  

def create_id(racine):
    identifiant= f"id_cle{uuid.uuid4().hex[:4]}"
    path= os.path.join(racine,"secure_d_usb.txt")
    try:
        with open(path, "w") as  marqueur:
            marqueur.write(identifiant)
            return identifiant
    except OSError:
        raise KeyNotFoundError

def create_memory(liste_fichiers, id_cle, racine):
  
    memoire= json_exist() 
    memoire[id_cle]={}
    for element in liste_fichiers:   
        hasheur= hashlib.sha256()
        try:
           with open(element, "rb") as fic:
                content= fic.read()
                hasheur.update(content)
                code= hasheur.hexdigest()
                element=os.path.relpath(element, racine)
                memoire[id_cle][element]=code
        except:
            continue
    return memoire

def save_memory(dicto):
    
    atomic_writting(dicto)

"""ici, les fonctions appelees par main.py lorsque la cle est connu:

"""

def load_memory(racine):
    try:
        _,id_cle=mod1.reconnaissance_cle(racine)
    except:
        raise KeyNotFoundError
    memoire=json_exist()
    if id_cle in memoire:
        memoire= memoire[id_cle]
        inter_dict={}
        for path, hash in memoire.items():
            path= os.path.join(racine, path )
            inter_dict[path]=hash
        memoire=inter_dict
        return memoire, id_cle
    else:
        return None, id_cle

def copy_memory(racine):   
    memoire,_=load_memory(racine)
    init_state=memoire.copy()
    return init_state

def generate_hash(element):
    hasheur= hashlib.sha256()
    with open(element, "rb") as fic :
        content= fic.read()
        hasheur.update(content)
        code= hasheur.hexdigest()
    return code

def classify_file(racine, liste_fichiers):
    fichiers_non_ouvert=[]
    nouveaux_fichiers=[]
    fichiers_modifies=[]
    memoire,_=load_memory(racine)
    for file in liste_fichiers: 

        try: 
            hash=generate_hash(file)
        except :
            print("le fichier n'a pas pu etre ouvert")
            fichiers_non_ouvert.append(file)
            if os.path.exists(racine)== False:
                raise KeyNotFoundError
            else:
                continue
        
        if file in memoire and hash== memoire[file]:
            continue
        if file not in memoire:
            nouveaux_fichiers.append(file)
            memoire[file]=hash
        if file in memoire and hash!= memoire[file]:
            fichiers_modifies.append(file)
            memoire[file]=hash
    fichiers_cibles= fichiers_modifies + nouveaux_fichiers
    return fichiers_cibles, memoire

def clean_memory(racine, liste_fichiers):
    nouveaux_fichiers=[]
    chemin_disparu=[]
    chemins_modifies=[]
    init_state= copy_memory(racine)
    _,memoire=classify_file(racine,liste_fichiers)
    for path in init_state:
        if path not in liste_fichiers:
            chemin_disparu.append(path)
    for chemin in chemin_disparu:
        hash_path=init_state[chemin] 
        for element in nouveaux_fichiers:
               
            try: 
                code=generate_hash(element)
            except:
                print("le fichier n'a pas pu etre ouvert")
                continue
                
            if hash_path==code:
                chemins_modifies.append(chemin)
    suppresions=set(chemin_disparu)- set(chemins_modifies)
   
    for element in suppresions :
        del memoire[element]
    for element in chemins_modifies:
        del memoire[element]
    inter_dict={}
    for path, hash in memoire.items():
        path= os.path.relpath(path, racine)
        inter_dict[path]=hash
        memoire=inter_dict
    return memoire

def diff_save_memory(id_used, racine, liste_fichiers):
    active_memory= json_exist()
    dico=clean_memory(racine, liste_fichiers)
    active_memory[id_used]= dico
    atomic_writting(active_memory)

def atomic_writting(dictionnaire):
    with open("memoire_temp.json", "w", encoding="utf-8") as fichier_memoire:
        json.dump(dictionnaire, fichier_memoire, indent=4, ensure_ascii=False)
    os.replace("memoire_temp.json", "memoire.json")
