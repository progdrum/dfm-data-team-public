from flask_sqlalchemy import SQLAlchemy


# The SQLAlchemy object is being created here, so that it can be shared
# across files without creating any circular dependencies.

# Create the SQLAlchemy object so that we can use it in the application
db = SQLAlchemy()