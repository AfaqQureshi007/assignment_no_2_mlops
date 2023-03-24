from flask import Flask, jsonify, render_template, request
from ai_model import live_predict
from threading import Timer

a1=live_predict()
a1.make_data_and_train()
app = Flask(__name__)

def train_model():
    a1.make_data_and_train()
    print('\n\n\n\n\n\n\n\n\n it works fine \n\n\n\n\n\n\n\n\n')
    Timer(61.0,train_model).start()


train_model()

@app.route('/price')
def get_price():
    # Create a CCXT exchange instance
    #exchange = ccxt.binance()
    # Get the ticker for Bitcoin/USDT
    #symbol = 'BTC/USDT'
    # ticker = exchange.fetch_ticker(symbol)
    # # Get the datetime and price from the ticker
    # datetime1 = ticker['timestamp']
    # datetime_obj = datetime.datetime.fromtimestamp(datetime1 / 1000)
    # datetime_str = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
    # price = ticker['last']
    # high_price=ticker['high']
    # low_price=ticker['low']
    # bid=ticker['bid']
    # bidVolume=ticker['bidVolume']
    # ask=ticker['ask']
    # askVolume=ticker['askVolume']
    # vwap=ticker['vwap']
    # open1=ticker['open']
    # close1=ticker['close']
    # previousClose=ticker['previousClose']
    # change=ticker['change']
    # percentage=ticker['percentage']
    # average=ticker['average']
    # baseVolume=ticker['baseVolume']
    # quoteVolume=ticker['quoteVolume']
    datetime_str,price,high_price,low_price,bid,bidVolume,ask,askVolume,vwap,open1,close1,previousClose,change,percentage,average,baseVolume,quoteVolume,invalue,datetime_str1=a1.live_Price_Display()    
    # Return a JSON  response with the datetime and price
    
    response = {'datetime': datetime_str, 'price': price,'high_price' : high_price ,
                'Open1':open1,'bidVolume':bidVolume  ,'bid':bid ,'low_price':low_price ,
                'ask':ask,'askVolume':askVolume ,'vwap':vwap,'close1':close1,
                'previousClose':previousClose,'change':change,'percentage':percentage,
                'average':average,'baseVolume':baseVolume,'quoteVolume':quoteVolume, 'future_date': datetime_str1, 
                'future_price': invalue}
    return jsonify(response)

@app.route('/predict_it',methods=['POST'])
def get_prediction():
    date_ = request.form['predictor']
    ret = a1.get_user_predict(date_)
    ret = round(ret,2)
    return jsonify({'response':ret}) 

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)