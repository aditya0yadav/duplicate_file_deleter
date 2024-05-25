import os 
import filecmp

file_dir = input("Enter teh path here :")
directory = os.listdir(file_dir)


deletion_needed = []
consideration = []
for i in directory:
    
    basename1, extension1 = os.path.splitext(i)
    
    for j in directory :
        if  os.path.getsize(i) != 0:
            basename, extension = os.path.splitext(j)
            if filecmp.cmp(i,j) == True and i != j and j not in deletion_needed and extension1 == extension:
                deletion_needed.append(j)
        else :
            consideration.append(j)

deletion_needed = list(set(deletion_needed))
consideration = list(set(consideration))
print(deletion_needed)
print("*" * 30)
print("Do you wnat to these empty files ?")
print(consideration)

if len(deletion_needed) == 0:
    print("No duplicate files found")

else :
    print("do yo wnat to delete the file")
    take = input("Enter y for yes and n for no :")

    if take == 'y':
        for i in deletion_needed:
            file_path = os.path.join(file_dir, i)
            if os.path.exists(file_path):
                os.remove(file_path)
            print("Files deleted successfully")
    else :
        print("Files not deleted")

if len(consideration) == 0:
    print("No empty files found")
else :
    print("do yo wnat to delete the file ofconsideration")
    print("All consideration files are empty files")
    take = input("Enter y for yes and n for no :")

    if take == 'y':
        for i in consideration:
            file_path = os.path.join(file_dir, i)
            if os.path.exists(file_path):
                os.remove(file_path)
            print("Files deleted successfully")
    else :
        print("Files not deleted")


