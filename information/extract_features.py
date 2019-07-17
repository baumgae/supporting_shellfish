import os
import shutil


sourcePath = "helgaspPfad/Source_Images"
destinationPath = "helgasPfad/Destination_Images"

for person in sourcePath:
    path, dirs, files = next(os.walk(sourcePath + "/" + person))

    for emotion in dirs:
        path, dirs, files = next(os.walk(sourcePath + "/" + person + "/" + emotion))
        emotion_folder = os.path.dirname(emotion)

        for take in dirs:
            path, dirs, files = next(os.walk(sourcePath + "/" + person + "/" + emotion + "/" + take))
            file_count = len(files)
            getMiddle = file_count / 2

            fileToCopy = files.index(getMiddle + 1)

            path2, dirs2, files2 = next(os.walk(destinationPath))

            for em in dirs2:
                if emotion_folder == em:
                    copy = shutil.copy(fileToCopy, destinationPath + "/" + emotion_folder)








