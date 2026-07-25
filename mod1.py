import os
import win32com.client
import win32file
from manage_error import KeyNotFoundError

def wait_for_volume():
    loop=True
    while loop== True:
        event= win32com.client.GetObject(r"winmgmts:\\.\root\cimv2")
        guetteur= event.ExecNotificationQuery("SELECT * FROM Win32_VolumeChangeEvent")
        controleur=guetteur.NextEvent()
        type_event= controleur.Properties_("EventType")
        type_event= type_event.Value
        if type_event== 3:
            continue
        else:
            nom_volume=controleur.Properties_("DriveName")
            nom_volume=nom_volume.Value
            nom_volume=nom_volume+ "\\"
            guid=nom_volume+ "\\"
            guid= win32file.GetVolumeNameForVolumeMountPoint(guid)
            return type_event, nom_volume, guid

def make_root():
    type_event, root, guid=wait_for_volume()
    return type_event, root, guid
    
def reconnaissance_cle(key_path):
    try:
        for element in os.listdir(key_path):  
            element= os.path.join(key_path, element)
            if os.path.isfile(element)== True:  
                element_copy= os.path.basename(element)
                nom, ext= os.path.splitext(element_copy)
                if nom== "secure_d_usb" and ext==".txt":
                    try: 
                        marqueur= open(element, "r")
                    except:
                        print("procedure d'arret")
                    identifiant= marqueur.read()
                    return "TRUE", identifiant
    except:
       raise KeyNotFoundError       
    return "FALSE", "None"

def fill_fichiers_de_la_cle(key_path):
    fichiers_de_la_cle= []   
    for path, _, fichiers in os.walk(key_path):
        if os.path.exists(key_path)== False:
            raise KeyNotFoundError
        for element in fichiers:
            fichiers_de_la_cle.append(os.path.join(path,element))
    return fichiers_de_la_cle

