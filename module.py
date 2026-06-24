import os 
import stat

executables= [".exe",".dll",".bat",".cmd",".ps1", ".vbs", ".msi",".scr",".com",
              ".lnk", ".jar", ".reg"]

fichiers_systeme= ["svchost", "ntoskrnl", "explorer","svchosts",
    "lsass", "lsasses", "crss","winlogon", "wininit", "services",
        "smss","taskhost", "taskhostw","dwn","spoolsv","cmd",
            "powershell","regedit","taskmgr","msiexec","rundll32",
                "regsvr32","wsript","cscript","mshta","svchost32",
                    "svhost","system32","windows","win32"]

chemin= "C:\\Users\\EVERMATE\\ma_cle" 

fichiers_prioritaires=[]                                              
without_extensions=[]
filesys_prioritaires=[] 
fichiers_caches=[]

for path, _, fichiers in os.walk(chemin):
    for element in fichiers:
       element=element.lower()
       nom,extensions= os.path.splitext(element)
       
       if extensions in executables and nom not in fichiers_systeme:        
           fichiers_prioritaires.append(os.path.join(path,element))
       if nom=="autorun" and extensions== ".inf":
           fichiers_prioritaires.append(os.path.join(path,element))
       if nom in fichiers_systeme and extensions in executables:
           filesys_prioritaires.append(os.path.join(path,element))
       if extensions =="" :
           without_extensions.append(os.path.join(path,element))          
       if "." in nom:
           _,ext=os.path.splitext(nom)
           if ext in extensions_trompeuses:
               double_extension.append(element)
               

for path,_,fichiers in os.walk(chemin):
    for element in fichiers:
        element= os.path.join(path, element)
        metadonnees=os.stat(element)
        if metadonnees.st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN == 2:
            fichiers_caches.append(element)
            


 
