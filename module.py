import os 
import subprocess

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

for path_explored,_,_ in os.walk(chemin):
    
    resultat=subprocess.run(f'dir /ah /b "{path_explored}"', shell=True, capture_output=True, encoding="utf-8") 
    resultat= resultat.stdout
    resultat= resultat.splitlines()
    for element in resultat:
        
      fichiers_caches.append(os.path.join(path_explored, element))
      
print(fichiers_caches)
print(len(fichiers_caches))
    
for element in fichiers_caches:
    for path,_,files in os.walk(chemin):
        if element in files:
            index= fichiers_caches.index(element)
            fichiers_caches[index]=os.path.join(path,element)
            

            
print(fichiers_caches)
print(len(fichiers_caches))
   
    

    
    

    

 
