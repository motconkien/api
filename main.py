from flask import Flask, jsonify, request
import logging
from database import db,TradingData
import os

#set up file log to debug
logging.basicConfig(level=logging.INFO, filename='api.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

#connect database
#__file__: current path
# join means concate the current path with file name is test.sqlite3
db_path = os.path.join(os.path.dirname(__file__),'test.sqlite3')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

# mt4,mt5 sends data in json format-> flask api will handle by request.json
@app.route('/api/post_data', methods = ['POST'])
def add_data():
    data = request.json
    
    #add to database and save to log to debug
    trading_data = TradingData(
        symbol = data['symbol'],
        open_price = data['open_price'],
        volume = data['volume'],
        market_price = data['market_price'],
        swap = data['swap'],
        floating_pl = data['floating_pl'],
    )
    logging.info(f'Recieved data from symbol: {trading_data.symbol}')
    logging.info(f'Recieved data from symbol: {trading_data.open_price}')
    logging.info(f'Recieved data from symbol: {trading_data.volume}')
    logging.info(f'Recieved data from symbol: {trading_data.market_price}')
    logging.info(f'Recieved data from symbol: {trading_data.swap}')
    logging.info(f'Recieved data from symbol: {trading_data.floating_pl}')

    db.session.add(trading_data)
    db.session.commit()

    logging.info(f'Add data to database')

    #return data for client;'
    return jsonify({'Status': 'Recieved successfully'}),200 

if __name__ == '__main__':
    app.run(debug=False)