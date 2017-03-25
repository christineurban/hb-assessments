"""Models and database functions for cars db."""

from flask_sqlalchemy import SQLAlchemy

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Brand(db.Model):
    """Car brand."""

    __tablename__ = "brands" 

    brand_id = db.Column(db.String(3),
                         primary_key=True)
    name = db.Column(db.String(20),
                     nullable=False,
                     unique=True)
    founded = db.Column(db.Integer,
                        nullable=False)
    headquarters = db.Column(db.String(50),
                             nullable=False)
    discontinued = db.Column(db.Integer,
                             nullable=True)

    model = db.relationship("Model", backref="brand")

    def __repr__(self):
        """Show info about brand."""

        return "<Brand id={} name={} founded={} hq={} dc={}>".format(
               self.brand_id, self.name, self.founded, self.headquarters, self.discontinued)

class Model(db.Model):
    """Car model."""

    __tablename__ = "models"

    model_id = db.Column(db.Integer,
                         primary_key=True,
                         autoincrement=True)
    year = db.Column(db.Integer,
                        nullable=False)
    brand_id = db.Column(db.String(3),
                         db.ForeignKey("brands.brand_id"))
    name = db.Column(db.String(20),
                     nullable=False)

    def __repr__(self):
        """Show info about model."""

        return "<Model id={} year={} brand_id={} name={}>".format(
               self.model_id, self.year, self.brand_id, self.name)

# End Part 1


##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///cars'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
