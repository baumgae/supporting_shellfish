# -*- coding: utf-8 -*-
import os
import shutil

sourcePath = "C:\\Users\Helga\CloudComputing\Database\Bilder\entpackt"
destinationPath = "C:\\Users\Helga\CloudComputing\Database\Bilder\destination"

personList = os.listdir(sourcePath)
# Get List of emotions from the 1st person without the "mixed"
emotionList = os.listdir(sourcePath + "\\" + personList[0])	
# Check if element "mixed" exists in List, before removing
if "mixed" in emotionList:
    emotionList.remove("mixed")

for person in personList:
        for emotion in emotionList:
                for path, takes, files in os.walk(sourcePath + "\\" + person + "\\" + emotion):
                        # For each take
                        for take in takes:      
                                sourceTakePath = os.path.join(sourcePath + "\\" + person + "\\" + emotion, take)
                                                
                                # For each picture
                                for path, dirs, files in os.walk(sourceTakePath):
                                        file_count = len(files)
                                        getMiddle = int(file_count / 2)
                                        selectedIndex = getMiddle +1 
                                        fileToCopy = files[selectedIndex]          
                                        print("-- Person " + person + "-- File to copy: " + fileToCopy)

                                        # Duplicate picture and rename it
                                        base, extension = os.path.splitext(fileToCopy)
                                        newFileToCopyPath = os.path.join(sourceTakePath, person + "_" + emotion + "_" + take + "_" + base + extension)
                                        shutil.copy(os.path.join(sourceTakePath, fileToCopy), newFileToCopyPath)

                                        # Move duplicate into destination
                                        destination = os.path.join(destinationPath, emotion)
                                        shutil.move(newFileToCopyPath, destination)
                                        print("Picture moved into:" + emotion)

