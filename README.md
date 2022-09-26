# Welcome gamers to phishing-softhouse #

**DO NOT EVER COMMIT DIRECTLY TO MAIN!!!**

***
***

## Our Git Conventions ##

### Add and Commit ###

In your terminal, while standing inside the repo on your local computer, perform:
1. `git add <file/dir>` - Adds the files and directory you want to add to a commit (use `.` as file to add all files in your current standing directory)
2. `git commit -m <commit message>` - Commits (does *not* push) and adds a message that will describe this commit in the git-tree
3. `git push` - Pushes your local files to the Github cloud repository. Now anyone within the team can see your files and commits

### Pull form Cloud ###

In your terminal, while standing inside the repo on your local computer, perform:
1. `git pull` - This will pull newer files from the Github cloud onto your local computer (including new branches)

If and error message of `HEAD is behind`, the files on Github is newer than your local files.
In case of this perform a "rebase" or "hard reset" (will try and keep your code, but updating unmodified code with the new code on the cloud). If you are unsure which one to use, ask a project teammate.

Or you can perform a force fetch, **overwriting local code** (*this will remove any changes you have not yet pushed*) with the one on the Github. To perform such, use:
1. git fetch --all
2. git reset --hard
3. git pull

### Merges ###

Due to `main` being default and locking it demands monitary contribution, we have decided to use a branch as a "main".
This means all "pull requests" will have to be done towards the branch **`real-main`**.

Pull requests are therefore done (using UI) by:  
1. Press ``New pull request``-button on branch  
2. In "base"-banner (top left), change from "main" to "real-main"
3. Commit pull request
4. Press ``Pull request`` in side repo navigationbar
5. Press the pull request you want to merge
6. Press ``Merge pull request``-button if you are satisfied with your branch and want to add your code to "real-main"

***


## Code Standards ##
### Docstrings and Code Hints ###

Following is a code example of so called "python code hints" and docstring formatting

```py
def func(param1: type, param2: (int)) -> str:
"""
Description: [followed by two spaces]  
  [Indentation] This should be a short summary of what the function does and how to use it. 
  Do **NOT** describe how it works. 
  Lines should generally not go above 79 chars in length. If a description is long, kindly 
  split it to new rows and match the 
  indentation of the previous line
  
[One blank row is important between sections. It improves readability and allows interpreters 
to format docstrings (e.g. pylance)]
Intput: (followed by two spaces)  
  - param1 (type): description
  - param2 (int): used to do stuff
  - [inputs are written in list format, using "*", "+", or "-". followed by the type (e.g.
    "int", "string", etc) within paranthesis]
  
  
 Return: (Same line without indentation). This will be a short description of what is being 
         returned. Do not specify type unless it is neccessary.
         If a line gets too long (generally ~85 chars) use the next line and indent it to 
         match the start of the previous paragraph.
         In this example the function will already has a "hint" ("-> str") in the function 
         call (standardized in Python3), and therefore is not needed in the "return" docstring
"""

  [Code goes here and stuff]
  print("docstring example")
```

### Misc ###

- CamelCase will be used in functions and classes (e.g. `ThisIsAFunction`)
- Try to adhere to [PEP8](https://peps.python.org/pep-0008/) standards
