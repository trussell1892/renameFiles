import os
import shutil
from os import path

def renameFiles():

        rootdir = os.path.dirname(os.path.realpath(__file__))
        rootdir = input("Please enter a path to your files: ")

        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                filepath = subdir + os.sep + file

                src = filepath

                
                videoExt = ['.mp4', '.avi', '.mkv']   #clean these files     
                extToDelete = ['.jpg', '.txt']        #delete these files
                ext = src[-4:]                        #grab extention

                if ext in extToDelete:                 #deleting files
                    os.remove(filepath)

                if ext in videoExt and os.path.isfile(src):     #checking if they are video files
                                
                    dst = src.replace("BluRay", "")
                    dst = dst.replace("[YTSAM]", "")
                    dst = dst.replace("1080", "")
                    dst = dst.replace("YIFY", "")
                    dst = dst.replace("720p", "")
                    dst = dst.replace("X264", "")
                    dst = dst.replace("x264", "")
                    dst = dst.replace(".", " ")
                    dst = dst.replace("-", "")
                    dst = dst.replace("HDRip", "")
                    dst = dst.replace("XviD", "")
                    dst = dst.replace("AC3", "")
                    dst = dst.replace("EVO", "")
                    dst = dst.replace("WEB", "")
                    dst = dst.replace("DVDRip", "")
                    dst = dst.replace("GHOULS", "")
                    dst = dst.replace("ENG", "")
                    dst = dst.replace("DVDR", "")
                    dst = dst.replace("[YTSAG]", "")
                    dst = dst.replace("HSTS", "")
                    dst = dst.replace("GAZ", "")
                    dst = dst.replace("S01", "SeasonOne")
                    dst = dst.replace("S02", "Two")
                    dst = dst.replace("S03", "Three")
                    dst = dst.replace("S04", "Four")
                    dst = dst.replace("S05", "Five")
                    dst = dst.replace("S06", "Six")
                    dst = dst.replace("S06", "YIFY")
                    dst = dst.replace("S07", "Seven")
                    dst = dst.replace("S08", "Eight")
                    dst = dst.replace("S09", "Nine")
                    dst = dst.replace("S10", "Ten")
                    dst = dst.replace("S11", "Eleven")
                    dst = dst.replace("S12", "Tweleve")
                    dst = dst.replace("S13", "Thirteen")
                    dst = dst.replace("S14", "Fourteen")
                    dst = dst.replace("S15", "Fifteen")
                    dst = dst.replace("S16", "Sixteen")
                    dst = dst.replace("S17", "Seventeen")
                    dst = dst.replace("S18", "Eighteen")
                    dst = dst.replace("S19", "Nineteen")
                    dst = dst.replace("S20", "Twenty")
                    dst = dst.replace("S22", "TwentyTwo")
                    dst = dst.replace("S23", "TwentyThree")
                    dst = dst.replace("S25", "TwentyFour")
                    dst = dst.replace("E01", "One")
                    dst = dst.replace("E02", "Two")
                    dst = dst.replace("E03", "Three")
                    dst = dst.replace("E04", "Four")
                    dst = dst.replace("E05", "Five")
                    dst = dst.replace("E06", "Six")
                    dst = dst.replace("E07", "Seven")
                    dst = dst.replace("E08", "Eight")
                    dst = dst.replace("E09", "Nine")
                    dst = dst.replace("E10", "Ten")
                    dst = dst.replace("E11", "Eleven")
                    dst = dst.replace("E12", "Tweleve")
                    dst = dst.replace("E13", "Thirteen")
                    dst = dst.replace("E14", "Fourteen")
                    dst = dst.replace("E15", "Fifteen")
                    dst = dst.replace("E16", "Sixteen")
                    dst = dst.replace("E17", "Seventeen")
                    dst = dst.replace("E18", "Eighteen")
                    dst = dst.replace("E19", "Nineteen")
                    dst = dst.replace("E20", "Twenty")
                    dst = dst.replace("E21", "TwentyOne")
                    dst = dst.replace("E22", "TwentyTwo")
                    dst = dst.replace("E23", "TwentyThree")
                    dst = dst.replace("E25", "TwentyFour")

                            
                    dst = dst[:-3]                      #chop extention as it has no period
                    dst = dst + ext                     # join filename with extention
                    
                
                    os.rename(src, dst)                  #rename the files
                    
                    print(dst + "****file cleaned up.*****")
                    

renameFiles()