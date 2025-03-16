import os

now_path = os.getcwd()
print(f"Working Folder : {now_path}")
os.chdir("C:\\")
now_path = os.getcwd()
print(f"Working Folder : {now_path}")
folders = os.listdir()
print(f"Folders : {folders}")
print(folders[-1])
if folders[-1] == "new_folder":
    os.rmdir(folders[-1])

print(f"Folders : {folders}")
print(folders[-1])
if folders[-1] == "new_folder":
    os.rmdir(folders[-1])

pwd = "C:\\Users\\muhasebe\\Desktop\\berk\\Python1"
os.chdir(pwd)

if not os.path.exists("new_folder"):
    os.mkdir("new_folder")
    print("new folder has been created.")
else:
    os.rmdir("new_folder")
    print("Folder has been deleted.")

print(f"Public folder location : {os.getenv ("PUBLIC")}")


