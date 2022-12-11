# Welcome to phishing-softhouse #

## Requirements ##

- Python3.10+
- PIP 22.3.1
- Flask 2.2.2
- Pytest 7.2.0
- URL-parser 3.0.3
- validators 0.20.0
- python-whois 0.9.18
- psycopg2 2.9.5
- beautifulsoup4 4.11.1

***

## Our Git Conventions ##

### Issues ###

- Avoid having the *first character* in an issue be a number (0-9). This interferes with issue-ID fast tabbing when checking out a branch connected to the issue

### Import and export requirements.txt

```shell
pip install pipreqs                       # install pipreqs
python -m  pipreqs.pipreqs . --force      # export requirements.txt
pip install -r requirements.txt           # import requirements.txt
```

***

## Code Standards ##

### Docstrings and Code Hints ###

Following is a code example of so called "python code hints" and docstring formatting

```py
def func(param1: type, param2: (int)) -> str: # author name goes here
"""
Description: [followed by two spaces]  
  [Indentation] This should be a short summary of what the function does and how to use it.
  Do **NOT** describe how it works.
  Lines should generally not go above 79 chars in length. If a description is too long, 
  split it to new rows and match the indentation of the previous line

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

  [...]
  print("docstring example")
```

### Misc ###

- CamelCase will be used in functions and classes (e.g. `ThisIsAFunction`)
