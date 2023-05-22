# Elevation-Based Navigation (ELeNA) using MVC architecture
## by DJNA
What is ELeNA ? 

Elevation-based Navigation (EleNa) is a software application which computes an optimal route between a source and a destination with either maximum or minimum elevation gain with an additional constraint of the total distance upto x% of the shortest path.

# Steps to execute the software:

## Setup up the Virtual environment (optional but preferred)

ELeNA software has a dependencies of certain packages and their specific versions of the sme to run properly. Hence, it is advisable to create a new virtual environment. Steps to create virtual environment on different os types are mentioned below :


### Os type :  Windows

python3 -m venv venv

.\venv\scripts\activate


### Os type : macOS

python3 -m venv .venv

source .venv/bin/activate


### Os type : Linux

python3 -m venv .venv

source .venv/bin/activate

## Setup up Flask environment

By defining and exporting flask environment as well as the path to the app.py would be benificial as well as easier to run the software with the command 'flask run' instead of executing the python file again and again.

### Os type : macOS

export FLASK_ENV=development

export FLASK_APP=src/App.py

### Os type :  Windows

set FLASK_APP=src/App.py

set FLASK_ENV=development

## Install the depenedencies mentioned in requirements.txt

* pip3 install -r requirements.txt

## Execute the software application
* flask run 

## Test the application with unit test cases mentioned in test.py
* python3 test/test.py

## User Manual : How to use the application
* To access the web interface, please visit http://127.0.0.1:5000/
* On the web interface, users can input the start location, end location, maximum percentage deviation from the shortest path, and their preference for elevation.
* After entering the necessary information, users can click the "Calculate" button.
* Upon clicking the "Calculate" button, the web interface will display the total distance, elevation gain, elevation path, and step-by-step directions.
* To reset the input parameters, users can simply click the "Reset" button.


## Documentation

Please consult the provided URL for a concise documentation : 
*Insert report.pdf url link*

## Demo 

Please navigate to the mentioned url to witness a bried demo of our project : 
*Insert url link*

