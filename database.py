from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

# Database model
class TradingData(db.Model):
    #syntax: colname = db.Column(db.datatype), nullable means not null
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False)
    open_price = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Float, nullable=False)
    market_price = db.Column(db.Float, nullable=False)
    swap = db.Column(db.Float, nullable=False)
    floating_pl = db.Column(db.Float, nullable=False)


