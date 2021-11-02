import os                                             
from pathlib import Path                                

S = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO":['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}
def pickDirectory(value):
    for category, suffixes in S.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'                                       # If filetype doesn't exist in our dictionary

for item in os.scandir():
    if item.is_dir():
        continue
    filePath = Path(item)
    filetype = filePath.suffix.lower()
    directory = pickDirectory(filetype)
    directoryPath = Path(directory)
    if directoryPath.is_dir() != True:
        directoryPath.mkdir()
    filePath.rename(directoryPath.joinpath(filePath))