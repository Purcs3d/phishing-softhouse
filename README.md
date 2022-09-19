# Welcome gamers to phishing-softhouse #

**DO NOT EVER COMMIT DIRECTLY TO MAIN!!!**  
If you commit to main I will commit arson on your house and sleep with your mother!!

This will act as a short intro to how we function, rather than what the program *is* and *will* do.

## Docstrings and Code Hints ##

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

## Functions ##

- CamelCase will be used in functions and classes (e.g. `ThisIsAFunction`)
