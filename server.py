from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgres://sean:weakpassword@localhost:5432/testdb'


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
