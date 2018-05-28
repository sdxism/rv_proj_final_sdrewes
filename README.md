# Red Ventures Rest API Project

## Requirements
* Python 3.6 or above
* Sqlite3
* Flask
* Pandas (optional)

## Folder Structure
```
rv_proj_final_sdrewes
  /app
    /data_provider
    /routes
  /data
  /db
```
**app** - this contains the application code

**data** - this contains the raw .csv files 

**db** - this contains the database file and database initialiation script

## To Run
1. Fork the repository
2. Clone the forked repository
3. Setup a virtual python environment

    3a. ```python3 -m venv ./venv```

4. Start the virtual environment

    4a. ```./venv/bin/activate```
    
5. Install the *sqlite3* package
    
    5a. ```pip3 install sqlite3```
    
6. Install *flask* package

    6a. ```pip3 install flask```
    
7. Run the application

    7a. ```python3 run.py```
    
8. Exit virtual environment

    8a. ```deactivate()```

## API Endpoints

### Base URL
```http://127.0.0.1:5000```

### State Endpoints
**State names** must have the first letter capitalized

**State abbreviations** must be capitialized

| URI      | Request | Example           | Response | Result  |
| :-------------: |:-------------: | :-------------: | :-----: | :-----:|
| ```/state/<state>/cities```     | GET | /state/Alabama/cities      | 200 |   List of city json objects |
| ```/state/<state>/cities```      | GET |/state/AL/cities      | 200  |List of city json objects |
| ```/state/<state>/cities```      | GET | /state/feafe14/cities      | 400 |   Error message |
| ```/state/<state>/cities```      | GET | /state/alabama/cities      | 400 |   Error message |
| ```/state/<state>/cities```      | GET | /state/al/cities      | 400 |   Error message |

### User Endpoints
| URI      | Request | Example           | Response | Result  |
| :-------------: |:-------------: | :-------------: | :-----: | :-----:|
| ```/user/<user>/visits```     | GET | /user/1/visits      | 200 |   List of city json objects |
| ```/user/<user>/visits```      | POST | /user/1/visits      | 200  | List of city json objects |
| ```/user/<user>/visits/states```     | GET | /user/1/visits/states      | 200 |   List of state json objects |
| ```/user/<user>/visit/<visit>```     | GET | /user/1/visit/1      | 200 |   None |
