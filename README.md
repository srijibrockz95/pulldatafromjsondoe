Pre-requisite:
1. Goto repo directory and open bash and type the following (provided python3 and pip module is installed):

     pip install -r requirement.txt

2. Check settings.ini for connection string as per requirement (provided PostgresSQL server is installed)
3. Open python terminal inside the repo directory and run the following code snippet to create the schema (one-time)

     from Pullout import db
     db.create_all()

To execute the flask app locally, goto repo directory and open bash and type the following:
     export FLASK_APP=runserver.py
     flask run --port=5000

now to browse the application open browser and hit the below endpoints in chronological order:

1. http://localhost:5000/showdataintable (or simply in bash run, curl -X GET http://localhost:5000/showdataintable)
2. http://localhost:5000/showdataingraph (or simply in bash run, curl -X GET http://localhost:5000/showdataingraph)
