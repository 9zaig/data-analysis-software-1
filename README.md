
![header](https://capsule-render.vercel.app/api?type=rounded&color=gradient&height=150&section=header&text=Data%20analysis%20software&fontSize=75&fontAlignY=55)

<img alt="Python" src ="https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white"/>




## Contents

1. [What is the data analysis software?](#1-what-is-the-data-analysis-software-)
2. [How to install the required library?](#2-how-to-install-the-required-library-)
3. [How to use it?](#3-how-to-use-it-)
4. [How does it work?](#4-how-does-it-work-)


## 1. What is the data analysis software ?
The data analysis software is a python based program that take xml files from wafer and automaticly extract the data and save a data analysis graph for each file with differents curve :

- Raw spectrum curve
- Transmission spectrum reference with the fitted ref
- Flatten transmission spectrum
- Raw data IV analysis
- Fitted IV analysis

It also create a dataFrame with data from all the files that we can use to analyse our data.

## 2. How to install the required library ?

You can install the required the required library by typing in the console the following command 
```bash
python3 setup.py
```

## 3. How to use it ?

User can directly change the parameters in the run.py file to acces more efficiently what he want. He can change the following parameters : 

- Lot_id
- Wafer_id
- xy_ coord
- Device_name
- Option for saving the figures
- Option for showing the figures when running the program

## 4. How does it work ? 
### core.py

### extracting.py

-Getting data for graph from xml file 

-Use xml.etree.ElementTree 

### filter.py

- 

### fitting.py

- Fitting data

### graphplot.py

- Drawing Graph

### handler.py

### tocsv.py

- Convert data in matrix form to csv 
 
 ## Author

 김태인 , 최수빈 , 신용진 , Maël Jaouen
