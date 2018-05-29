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

## Database Schema
![alt text](https://github.com/sdxism/rv_proj_final_sdrewes/blob/master/schema1.png)


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
**For users that do not exist:**
* An empty list of cities or states will be returned on get request
* A 200 response will be returned on post request
* A 200 response will be returned on delete request


**For adding visits:**
* The object being sent must be Json
* The city and state must exist in the database
* The city name just be as it appears in the datbase
* State name must be as it appears in the database
    ``` 
    {
      "city":"Detroit",
      "state":"Michigan"
    }
    ```
* Stave abbreviations must be capitalized
    ```
    {
      "city":"Detroit",
      "state":"MI"
    }
    ```

| URI      | Request | Example           | Response | Result  |
| :-------------: |:-------------: | :-------------: | :-----: | :-----:|
| ```/user/<user>/visits```     | GET | /user/1/visits      | 200 |   List of city json objects |
| ```/user/<user>/visits```      | POST | /user/1/visits      | 200  | None |
| ```/user/<user>/visits/states```     | GET | /user/1/visits/states      | 200 |   List of state json objects |
| ```/user/<user>/visit/<visit>```     | DELETE | /user/1/visit/1      | 200 |   None |


### All Other Endpoints
Anything not listed above will 404
