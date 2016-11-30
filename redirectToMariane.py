import socket
import os
import os.path
import shutil


def AM_I_HOME():
    print('checking home')
    Home = '192.168.43.211'
    MyIP = socket.gethostbyname(socket.gethostname())

    if MyIP == Home:
        place = 'Home'
        
    else:
        place = 'Not Home'
    return place


def IS_DISK_THERE(vol_Path):
    print('checkingdisk')
    
    if os.path.exists(vol_Path):
        answer = "yes"
    else:
        answer = "no"

    return answer

        

def LET_S_CLEAN_THIS_SHIT(targets, download_Path, pathOUT):
    print('lets')
    downloads = os.listdir(download_Path)
    FilesToMove = set()
    for files in downloads:
        FileToList = files.split(".")
        if len(FileToList) == 2:
            
            if FileToList[1] in targets:
                pathIN = download_Path+"/{}".format(files)
                print(pathIN)
                
                #getatime donne durée depuis dernière accession en milliseconde
                #on prend 3 semaines
                if os.path.getatime(pathIN) >181400:
                    print(old)
                    print (os.path.getatime(pathIN))
                    shutil.copy(pathIN,pathOUT)
#                    os.remove(pathIN)
                else:
                    continue               
        else:
            pass
        
        return 




targets = {"pdf","jpeg","png","pkg","dmg","docx","pptx","xclx"}
download_Path = "/Users/williamdedecker/Downloads"
pathOUT = "/Volumes/ELIXIR/AUTODATA"
vol_Path ="/Volumes/BOOT"

if AM_I_HOME() != 'home':
    if IS_DISK_THERE(vol_Path) == 'yes':
        LET_S_CLEAN_THIS_SHIT(targets, download_Path, pathOUT)
        print("done")
    else:
        pass
else:
    pass


    
    
    





    #find pdf jpeg png pkg dmg docx pptx xclx (principal polution dans downloads)
#os.remove(path) 
    #shutil.copy(dossier_source+fichier,dossier_cible)
