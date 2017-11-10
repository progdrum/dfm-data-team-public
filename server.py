from flask import Flask, render_template
from shared import db
from data_processing import read_and_clean_data, insert_into_db, query_data


app = Flask(__name__)

# Configure the Flask app to connect to this database
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgres://sean:testdb@localhost:5432/testdb'

# Initialize the app with the SQLAlchemy object from the model file
db.init_app(app)

# Create the database
db.create_all()


@app.route("/")
def output():
    """
    Brings up page to parse the data, insert into the database 
    and redirect to the next page, displaying the result.
    
    :return: 
    """
    processed_data = read_and_clean_data('example_report.csv')
    insert_into_db('used_car_campaign', processed_data)

    return render_template('home')


@app.route("/results")
def show_results():
    return query_data()


if __name__ == "__main__":
    app.run(debug=True)
