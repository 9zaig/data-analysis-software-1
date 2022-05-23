# data-analysis-software

## 1 - What is the data analysis software ?

the data analysis software is a python based program that take xml files from wafer and automaticly extract the data and save a data analysis graph for each file with differents curve :

- the raw spectrum curve
- the transmission spectrum reference with the fitted ref
- The flatten transmission spectrum
- The raw data IV analysis
- The fitted IV analysis

it also create a dataFrame with data from all the files that we can use to analyse our data.

## 2 - How to install the required library ?

you can install the required the required library by typing in the console the following command 
```bash

python3 setup.py
```

## How to use it ?

the user can directly change the parameters in the run.py file to acces more efficiently what he want. He can change the following parameters : 

- the lot_id
- the wafer_id
- the xy_ coord
- device_name
- the option for saving the figures
- the option for showing the figures when running the program

 ## Author

 김태인 , 최수빈 , 신용진 , Maël Jaouen