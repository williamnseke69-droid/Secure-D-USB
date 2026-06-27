import facade
import os
import stat
 
executables= [".exe",".dll",".bat",".cmd",".ps1", ".vbs", ".msi",".scr",".com",
              ".lnk", ".jar", ".reg",".js", ".ade", ".adp", ".apk", ".app", ".appx", 
              ".appcontent-ms", ".application", ".appref-ms", ".asp", ".aspx",
              ".asx", ".bas", ".bgi", ".cab", ".cdxml", ".cer", ".chm", ".cnt",
              ".cpl", ".crt", ".csh", ".der", ".diagcab", ".fxp", ".gadget", ".grp", ".hlp", ".hpj"
              , ".hta", ".htc", ".img", ".ins", ".iso", ".isp", ".its", ".jnlp", ".jse",
              ".ksh", ".library-ms", ".mad", ".maf", ".mag", ".mam", ".maq", ".mar", ".mas", ".mat", ".mau",
              ".mav", ".maw", ".mcf", ".mda", ".mdb", ".mde", ".mdt", ".mdw", ".mdz", ".mht", ".mhtml", ".msc", ".msh", 
              ".msh1", ".msh1xml", ".msh2", ".msh2xml", ".mshxml", ".msp", ".mst", ".msu", ".ops", ".osd", ".pcd"
              , ".pif", ".pl", ".plg", ".prf", ".prg", ".printerexport",".ps1xml", ".ps2", ".ps2xml", ".psc1", ".psc2",
              ".psd1", ".psdm1", ".pssc", ".pst", ".py", ".pyc", ".pyo", ".pyw", ".pyz", ".pyzw", ".scf", ".search-ms",
              ".sct", ".settingcontent-ms", ".shb", ".shs", ".theme", ".tmp", ".udl", ".url", ".vb", ".vbe", ".vbp", ".vhd", ".vhdx",
              ".vsmacros", ".vsw", ".webpnp", ".website", ".ws", ".wsb", ".wsc", ".wsf", ".wsh", ".xbap", ".xll", ".xnk"]

fichiers_systeme= ["svchost", "ntoskrnl", "explorer","svchosts",
    "lsass", "lsasses", "crss","winlogon", "wininit", "services",
        "smss","taskhost", "taskhostw","dwn","spoolsv","cmd",
            "powershell","regedit","taskmgr","msiexec","rundll32",
                "regsvr32","wsript","cscript","mshta","svchost32",
                    "svhost","system32","windows","win32"]

extensions_trompeuses=[".pdf", ".doc", ".docx", ".xls", "xlsx", ".ppt", ".pptx",
                       ".txt", ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".heic",
                       ".mp3", ".mp4", ".mov", "avi", ".wav", ".zip", ".rar"]

chemin= "C:\\Users\\EVERMATE\\ma_cle" 

fichiers_prioritaires=[]                                              
without_extensions=[]
filesys_prioritaires=[] 
fichiers_caches=[]
double_extensions=[]
fichiers_normaux=[]

categorie= {"prioritaire":fichiers_prioritaires, "systeme_prioritaire":filesys_prioritaires, 
            "cache":fichiers_caches, "sans_extension":without_extensions, "extension_double":double_extensions, "normal":fichiers_normaux}

fichiers_de_la_cle= facade.forwardfile_toanalyze()

def categoriser_fichiers(chemin_fichier):
    
    name_fichier= os.path.basename(chemin_fichier)
    nom,extensions= os.path.splitext(name_fichier.lower())
    
    if "." in nom:
        _,ext=  os.path.splitext(nom)
        if ext in extensions_trompeuses:
          return "extension_double"   
    if extensions in executables and nom not in fichiers_systeme:        
        return "prioritaire"
    if nom=="autorun" and extensions== ".inf":
        return "prioritaire"
    if nom in fichiers_systeme and extensions in executables:
        return "systeme_prioritaire"
    if extensions =="" :
        return "sans_extension"
    metadonnees=os.stat(chemin_fichier)
    if metadonnees.st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN == 2: 
                return "cache"
    return "normal" 

def fill_type_fichier():
    for element in fichiers_de_la_cle:
       categorie_fichier= categoriser_fichiers(element)              
       categorie[categorie_fichier].append(element)
       
type_fichier= fill_type_fichier()
 

       
         
    



    


        
               




