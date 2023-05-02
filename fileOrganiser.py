import os
import shutil

path=os.getcwd()
path = os.path.realpath(path) 
extensions={
    'pdf': 'Documents',
    'txt': 'Documents',
    'doc':'Documents',
    'docx':'Documents',
    'dotx':'Documents',
    'odt':'Documents',
    'jpg':'Images',
    'jpeg':'Images',
    'gif':'Images',
    'png':'Images',
    'svg':'Images',
    'mp3':'Musics',
    'wav':'Musics',
    'flv':'Musics',
    'mp4':'Videos',
    'avi':'Videos',
    'mov': 'Videos',
    'wmv': 'Videos',
    'zip':'Compressed',
    'rar':'Compressed',
    'gz':'Compressed',
    '7z':'Compressed',
    'iso':'Compressed',
    'psd':'Photoshop',
    'ai':'Illustrator',
    'eps':'Illustrator',
    'ps':'Illustrator',
    'xls':'Spreadsheets',
    'xlt':'Spreadsheets',
    'xlsx':'Spreadsheets',
    'xltx':'Spreadsheets',
    'ppt':'Presentation',
    'pptx':'Presentation',
    'exe':'Executables',
    'py':'Python',
    'pyc':'Python',
    'c':'C',
    'tmp':'Temporary',
    'js':'Java Script'
}

for entry in os.listdir(path):
    if os.path.isfile(os.path.join(path, entry)):
        try:
            file_name, file_extension = os.path.splitext(entry)  
            dir_name= extensions[file_extension[1:]]
            try:
                os.mkdir(f"{dir_name}")
            except FileExistsError:
                pass
            
        except:
            try:
                dir_name="Miscellaneous"
                os.mkdir(f"{dir_name}")
            except FileExistsError:
                pass
        destination=os.path.join(path,dir_name)
        dest=shutil.move(entry,destination)