# -*- coding: utf-8 -*-
import os
import re
import shutil
from sklearn.model_selection import train_test_split

personPath = "C:\\Users\Helga\CloudComputing\Database\Bilder\entpackt"
originPath = "C:\\Users\Helga\CloudComputing\Database\Bilder\destination"
destinationPath = "C:\\Users\Helga\CloudComputing\Database\Bilder"

allPersons = os.listdir(personPath)

person_train, person_test, = train_test_split(allPersons, test_size=0.25)

print(*person_train, sep = ", ")
print(*person_test, sep = ", ")

emotionList = os.listdir(originPath)

def filter_and_copy_pictures(filterData, destinationPath):
    for emotion in emotionList:
        selectedPictures = []
        # Filter pictures
        for path, dirs, files in os.walk(originPath + "\\" + emotion):
            for fd in filterData:
                regex = re.compile(r'^'+ re.escape(fd))
                filtered = []
                filtered = filter(regex.search, files)
                for pic in filtered:
                    selectedPictures.append(pic)

        fullDestinationPath = os.path.join(destinationPath, emotion)
        # Delete all files that might be there from a previous run
        for file in os.scandir(fullDestinationPath):
            os.unlink(file.path)
        # Copy the pictures
        for picture in selectedPictures:
            fileToCopyPath = os.path.join(originPath + "\\" + emotion, picture)
            shutil.copy(fileToCopyPath, fullDestinationPath)

filter_and_copy_pictures(person_test, os.path.join(destinationPath, "testdata"))
filter_and_copy_pictures(person_train, os.path.join(destinationPath, "trainingsdata"))
    

        


