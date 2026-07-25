import mod1
import mod2
import facade
import mod9
from manage_error import KeyNotFoundError
import subprocess

def main_function():
    print("lettre apparue")
    loop=True
    while loop== True:
        _,root,guid=mod1.make_root()
        try:
            mod9.hide_volume(root)
            print("lettre disparue")
            result,_=mod1.reconnaissance_cle(guid)
            fichiers_de_la_cle= facade.forwardfile_toanalyze(guid)
            print(result)
            if result== "FALSE":
                id_used=mod2.create_id(guid)
                dico=mod2.create_memory(fichiers_de_la_cle, id_used, guid)
                mod2.save_memory(dico)
            if result== "TRUE":
                sous_dict, identifiant=mod2.load_memory(guid)
                if sous_dict is None:
                    mod2.save_memory(identifiant, fichiers_de_la_cle, guid)
                else:
                    mod2.diff_save_memory(identifiant,guid, fichiers_de_la_cle)
            
        except KeyNotFoundError:
            print("Cle retiree. scan interrompu, nous enclenchons\n veuillez s'il vous plait rebrancher la cle.\n le scan reprendra du debut ")
            continue
        finally:
            try:
                mod9.appear_volume(root, guid)
            except:
              subprocess.run(["mountvol", "/r"])

truc= main_function()
