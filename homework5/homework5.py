# File: homework5.py

# --- Vocabulary Review ---

# 1. Git is the local version control software system while GitHub is a websit that hosts Git repositories remotely
# 2. The Terminal is the interface window while the command line is the input window
# 3. The local repository is on your computer while the remote repository is online
# 4. Version control is the system to track and manage changes to files
# 5. The staging area is where changes are prepared before they are committed
# 6. git add adds files to the staging area
# 7. git commit saves staged changes with a message
# 8. git push uploads the local commits to the remote repository
# 9. git status shows the current status of the files in the repository
# 10. git pull fetches and merges updates from the remote repository
# 11. pwd prints the current working directory
# 12. ls lists the files and folders in the directory
# 13. cd changes directories
# 14. nano opens a text editor in the terminal
# 15. touch creates a new empty file in the directory
# 16. mv moves or renames files
# 17. rm removes files
# 18. cat displays the contents of the file

# --- A Directory Tree ---
# Questions:

# 1. pwd
# 2. ls
# 3. cd ~/python_decal/brianna_repo
#    git pull
# 4. cd ~/python_decal/judy_decal/homework
# 5. cat homework.py
# 6. git add .
#    git commit -m "saving hw"
#    git push
# 7. git push origin main 
#   It means that the remote branch has updates that aren't in the the local copy
# 8. ~/Recent/

# --- Homework 3 Review ---
def checkDataType(x):
    return type(x).__name__

def evenOrOdd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def duplicateList(lst):
    new_list = []
    for item in lst:
        new_list.append(item)
        new_list.append(item)
    return new_list


def square(num):
    return num * num


print("Duplicate",duplicateList(['1','2','3']))