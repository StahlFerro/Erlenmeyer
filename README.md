# IMVR (International Marine Vessel Registry)

This is a simple web API made with [Flask](http://flask.pocoo.org/) for our university project

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

These are the following requirements to run IMVR
- Python 3.7
- PostgreSQL 10.0 or above

### Installing

Create a virtual environment for the project, and then activate it
```
cd /path/to/IMVR
python3.7 -m venv venv
(Linux bash) source venv/bin/activate
(Windows powershell) venv\bin\Activate.ps1
(Windows cmd.exe) venv\bin\activate.bat
```
Install the requirements from the `requirements.txt` file included in the project
```
pip install -r requirements.txt
```
Create a postgres database named `IMVR_DATA`, either from the command line, or from a GUI like pgAdmin
```
psql -U postgres
CREATE DATABASE IMVR_DATA
```
Apply all the migrations to generate the database's tables
```
flask db upgrade
```
Insert all the data from `data.sql`
```
psql IMVR_DATA postgres
\i data.sql
```
Run the app
```
flask run
```
Try from the browser (localhost:5000), or test the API using `curl` below
```
curl -i http://localhost:5000/api/ships -X GET
```

## Built With

* [Python](https://www.python.org/) - Language
* [Flask](http://flask.pocoo.org/) - Web framework
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - Object-Relational Mapper (ORM)
* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) - REST API library
* [PostgreSQL](https://www.postgresql.org/) - Database
* [Jinja2](http://jinja.pocoo.org/docs/2.10/) - Web templating engine (packaged together with Flask)
* [Cerberus](http://docs.python-cerberus.org/en/stable/index.html) - Request validation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments
