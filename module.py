import os 
import stat

executables= [".exe",".dll",".bat",".cmd",".ps1", ".vbs", ".msi",".scr",".com",
              ".lnk", ".jar", ".reg", ".ade", ".adp", ".apk", ".app", ".appx", ".appcontent-ms", ".application", ".appref-ms", ".asp", ".aspx", ".asx", ".bas", ".bat", ".bgi", ".cab", ".cdxml", ".cer", ".chm", ".cmd", ".cnt", ".com", ".cpl", ".crt", ".csh", ".der", ".diagcab", ".exe", ".fxp", ".gadget", ".grp", ".hlp", ".hpj", ".hta", ".htc", ".img", ".inf", ".ins", ".iso", ".isp", ".its", ".jar", ".jnlp", ".js", ".jse", ".ksh", ".library-ms", ".lnk", ".mad", ".maf", ".mag", ".mam", ".maq", ".mar", ".mas", ".mat", ".mau", ".mav", ".maw", ".mcf", ".mda", ".mdb", ".mde", ".mdt", ".mdw", ".mdz", ".mht", ".mhtml", ".msc", ".msh", ".msh1", ".msh1xml", ".msh2", ".msh2xml", ".mshxml", ".msi", ".msp", ".mst", ".msu", ".ops", ".osd", ".pcd", ".pif", ".pl", ".plg", ".prf", ".prg", ".printerexport", ".ps1", ".ps1xml", ".ps2", ".ps2xml", ".psc1", ".psc2", ".psd1", ".psdm1", ".pssc", ".pst", ".py", ".pyc", ".pyo", ".pyw", ".pyz", ".pyzw", ".reg", ".scf", ".scr", ".search-ms", ".sct", ".settingcontent-ms", ".shb", ".shs", ".theme", ".tmp", ".udl", ".url", ".vb", ".vbe", ".vbp", ".vbs", ".vhd", ".vhdx", ".vsmacros", ".vsw", ".webpnp", ".website", ".ws", ".wsb", ".wsc", ".wsf", ".wsh", ".xbap", ".xll", ".xnk"]

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
            


 
