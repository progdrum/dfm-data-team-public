from json2html import json2html
from flask import Flask, render_template
from shared import db
from data_processing import read_and_clean_data, insert_into_db, query_data


app = Flask(__name__)

# Configure the Flask app to connect to this database
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgres://thatguy:thatguy@localhost/exercise'

# Initialize the app with the SQLAlchemy object from the model file
db.init_app(app)

# Create the database
db.create_all(app=app)


@app.route("/")
def output():
    """
    Brings up page to parse the data, insert into the database 
    and redirect to the next page, displaying the result.
    
    :return: 
    """
    return render_template('home.html')


@app.route("/results/")
def show_results():
    processed_data = read_and_clean_data('example_report.csv')
    insert_into_db('used_car_campaign', processed_data)

    return json2html.convert(query_data())


if __name__ == "__main__":
    app.run(debug=True)
