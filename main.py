#!/usr/bin/python3

import os
import csv
import time
import subprocess



# get folder location
def main():
    dir_path = os.getcwd()

    newDataArray = []

    # print("   The current path is: \n" + dir_path + "\n   Please make sure your file named:\n")
    # print(" packagelist.txt \n")
    # print("   is in this directory\n")
    # print("\n\n")
    answer = input("Ready to Run? [Y/n]: ")
    if answer == "Y":




        # run code here to list row
        # create the packagelist file using pacman -Q > packagelist.txt

        subprocess.call("pacman -Q > packagelist.txt", shell=True)
        print("packagelist.txt created in directory: " + dir_path + "\n")

        #need separate by space then print first row to new text file
        with open('packagelist.txt', newline='') as f:
            reader = csv.reader(f,  delimiter=' ')
            for row in reader:
               # print was just for test
               # print(row[0])
                newDataArray.append(row[0])
        # test array
        # print (newDataArray)
        # write array to csv
        output = csv.writer(open('packageList.csv', 'w'), delimiter=',', lineterminator='\n')
        for x in newDataArray: output.writerow([x])

    else:
        print("You have chosen to exit by not saying Y\n")
        print("Exiting in 5 seconds . . .\n")
        time.sleep(5)
        exit()

if __name__ == "__main__":
    
    main()
