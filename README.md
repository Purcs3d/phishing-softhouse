# Welcome to phishing-softhouse #

This program was developed in the course DV1512

The program analyzes URL:s to classify them as phishy/not phishy

## Setup ##
* Download the program by cloning the repository into your chosen directory of your local device
```shell
git clone https://github.com/Purcs3d/phishing-softhouse.git 
```
* Or download the zip file and extract into your chosen directory
* Then navigate to the directory where the program is located and the map "URL-analyzer" and then 
* To setup or reset database:
  * Go to the directory "URL-analyzer/tests" and then run:
  *  On Windows:
  ```shell
  python -m pytest test_database.py
  ```
  * On Linux:
  ```shell
  python3 -m pytest test_database.py
  ```
* Run the program:
  * On Windows:
  ```shell
  python main.py server       # to run it on a web browser
  #or
  python main.py terminal     # to run the program in your terminal
  ```
  * On Linux:
  ```shell
  python3 main.py server       # to run it on a web browser
  #or
  python3 main.py terminal     # to run the program in your terminal
  ```
* If you have any problem with running the program or setting up the database you might want to:
  * Update the settings in the config.py file located in the map "URL-analyzer/src". 
  * Update your python version
  * Update or install all modules in the "URL-analyzer/requirements.txt" file

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

### Import and export requirements.txt

```shell
pip install pipreqs                       # install pipreqs
python -m  pipreqs.pipreqs . --force      # export requirements.txt
pip install -r requirements.txt           # import requirements.txt
```

***

## Software bill of materials
* All libraries are found in the "URL-analyzer/requirements.txt" file
* The whitelist in the database are from here: https://github.com/mitchellkrogza/Phishing.Database (accessed 2022-11)
* The active phising links we used for testing was also found here: https://github.com/mitchellkrogza/Phishing.Database (accessed 2022-12)

