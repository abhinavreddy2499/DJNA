# Elevation-Based Navigation (ELeNA) using MVC architecture
## by DJNA
What is ELeNA ? 

Elevation-based Navigation (EleNa) is a software application which computes an optimal route between a source and a destination with either maximum or minimum elevation gain with an additional constraint of the total distance upto x% of the shortest path.


# Steps to run:

## Setting up the Virtual environment

### Linux
sudo apt-get install python3-venv    # If needed

python3 -m venv .venv

source .venv/bin/activate

### macOS
python3 -m venv .venv

source .venv/bin/activate

export FLASK_ENV=development

export FLASK_APP=src/App.py

### Windows
python3 -m venv .venv

.venv\scripts\activate

set FLASK_ENV=development

set FLASK_APP=src/App.py


## Install dependencies / requirements using the command
* pip3 install -r requirements.txt

## Running the application
* flask run

## Testing the application (unit test cases)
* python3 test/test.py

## Using the application
* Open your web browser and go to http://127.0.0.1:5000/ to access the web interface.
*  Enter the start location, end location, maximum percentage deviation from the shortest path, and elevation preference.
*   Click on the "Calculate" button to view the total distance, elevation gain, elevation path, and directions.
*  To reset the input parameters, click the "Reset" button.
