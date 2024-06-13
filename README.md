Country Configuration Manager
=============================

This is a FastAPI application for managing country configurations.

Project Structure
-----------------

* `__pycache__/`: Python cache directory
* `.env`: Environment file for storing database URL
* `.gitignore`: Git ignore file
* `app/`: Application directory
	+ `__pycache__/`: Python cache directory
	+ `database.py`: Database configuration file
	+ `main.py`: Main application file
	+ `models.py`: Database models file
	+ `schemas.py`: API schema file
	+ `test.py`: Test file
* `requirements.txt`: List of dependencies required by the application

Setup
-----

## Setup


#### Clone the repository

git clone https://github.com/your-username/country-configuration-manager.git


#### Install dependencies

pip install -r requirements.txt


#### Set up your database


Update the `SQLALCHEMY_DATABASE_URL` in the `.env` file with your database connection string.


### Running the Application


To run the application, use the following command:

uvicorn app.main:app --reload


### API Endpoints


#### Create a new country configuration


**POST /create_configuration**


* Description: Create a new country configuration.

* Example Usage:

curl -X POST "http://localhost:8000/create_configuration" -H "Content-Type: application/json" -d ' { "country_code": "IND", "business_name": "Example Company", "registration_number": "12345" }'


#### Retrieve country configuration by country code


**GET /get_configuration/{country_code}**


* Description: Retrieve country configuration by country code.

* Example Usage:

curl -X GET "http://localhost:8000/get_configuration/IND"


#### Update country configuration


**POST /update_configuration**


* Description: Update country configuration.

* Example Usage:

curl -X POST "http://localhost:8000/update_configuration" -H "Content-Type: application/json" -d ' { "country_code": "IND", "business_name": "Updated Company", "registration_number": "54321" }'


#### Delete country configuration by country code


**DELETE /delete_configuration**


* Description: Delete country configuration by country code.

* Query Parameter:

	+ `country_code`: Code of the country configuration to delete.

* Example Usage:

curl -X DELETE "http://localhost:8000/delete_configuration?country_code=IND"


Note: Replace `http://localhost:8000` with your actual API endpoint URL.
