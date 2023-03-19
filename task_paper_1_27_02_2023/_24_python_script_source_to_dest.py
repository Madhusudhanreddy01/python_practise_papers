'''24. Write a python script to copy files from a directory D1 based on timestamp(current_date) 
to another directory D2 and delete the source directory D1. 
Whenever the script is called this program must run.'''


import os

def move_onedir_to_another(source,destination):
    files = os.listdir(source)
    #print(files)


    for i in files:
        source_path = os.path.join(source,i)
        destination_path=os.path.join(destination,i)
        os.rename(source_path, destination_path)

    return destination_path

if __name__ == '__main__':
    source="D:\Python\os_path\old"
    destination="D:\Python\os_path\demo"
    print(move_onedir_to_another(source,destination))

# -----------------------------------------------------------------

# import os
# import shutil

# def move_onedir_to_another(source,destination):
#     files = os.listdir(source)
#     #print(files)


#     for i in files:
#         source_path = os.path.join(source,i)
#         destination_path=os.path.join(destination,i)
#         shutil.move(source_path, destination_path)

#     return destination_path

# if __name__ == '__main__':
#     source="D:\Python\os_path\demo"
#     destination="D:\Python\os_path\old"
#     print(move_onedir_to_another(source,destination))