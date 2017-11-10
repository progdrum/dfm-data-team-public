from flask import Flask
from ucc_model import db


app = Flask(__name__)

# Configure the Flask app to connect to this database
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgres://sean:testdb@localhost:5432/testdb'

# Initialize the app with the SQLAlchemy object from the model file
db.init_app(app)


@app.route("/")
def output():
    """
    Brings up page to parse the data, insert into the database 
    and redirect to the next page, displaying the result.
    
    :return: 
    """
    return "Output results here."


if __name__ == "__main__":
    app.run(debug=True)
