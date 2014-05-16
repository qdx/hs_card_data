# Hearth Stone unreliable card data api
## Introduction
This project attempt to keep an card data db and api for further use.

## Prerequisites and installation
* requests: pip install requests
* beautifulsoup4: pip install beautifulsoup4  
* peewee: pip isntall peewee
If you are using pip as the package manager just like me

## How to use
#### Fetch data from online
Run ``` python crawler.py ``` and you will find a ```./data/``` directory that stores all the card data. 

#### Import into MySQL

 1. Create a file named ```local.cfg``` in root of this repo
 2. Write you MySQL config to the cfg file, here is an example 

     ```
        [mysql]
        hs_db   = hearth_stone
        host    = localhost
        port    = 3306
        user    = root
        passwd  = root
    ```

 3. Run ```python ImportDB.py``` then you should have your data in a table named ```card```.

## Data Source
Currently, the data source is from:  
http://hearthstone.gamepedia.com/  

Specifically from:  
http://hearthstone.gamepedia.com/Spell_cards  
http://hearthstone.gamepedia.com/Equipment_cards  
http://hearthstone.gamepedia.com/Minion  

# Disclaimer
This is just a web crawler that crawls publicly available data from 
the web, if you think any of this is violating your copy right or any
rights, please let me know. Otherwise, I won't take any responsibility
for the consequences caused by this project.  
The reliability of the data solely relies on hearthstone.gamepedia.com.
