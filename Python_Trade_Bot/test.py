import alpaca_trade_api as trade_api
from alpaca_trade_api.entity import Clock

class pythonBuyBot:
 msg = "Hello world"
 print(msg)
 alpaca_endpoint = 'https://paper-api.alpaca.markets' #here we connect to our endpoint url for alpaca markets 

 api = trade_api.REST('PK9XK16R99YK604A8TSX','LBNhFfbK4L0Ax3U7FeZvcDnmaxdzyl6b88sS3bvQ',alpaca_endpoint) #This is our key and our secret id key 

 #Here we are going to want to test our account connection. 
 account = api.get_account()
 print(account.status)  # Tells us if our Connection to the account is active or not

 class Account(object):
     def init(self): 
         self.key ='PK9XK16R99YK604A8TSX'
         self.secret_key  = 'LBNhFfbK4L0Ax3U7FeZvcDnmaxdzyl6b88sS3bvQ'
         self.alpaca_endpoint = 'https://paper-api.alpaca.markets'
         self.api = trade_api.REST(self.key,self.secret_key,self.alpaca_endpoint)
         self.trade_symbol = '  ' #chooses what we want to trade
         self.current_order = None
         self.last_price = 1  



 # Daily OHLCV dataframe
 #aapl_daily = api.polygon.historic_agg('day','AAPL', limit=1000).df
 #print(aapl_daily)
 def market_open_or_close(): #checks to see if the market is open or not
    clock = api.get_clock() 
    print('The market is {}'.format('open' if clock.is_open else'closed'))
    return 

 def check_buying_power(): # this will check your buying power and how much you can spend currently. 
    if account.trading_blocked:
        print('accoutn blocked')
        return False
    else:
        print('${} is your buying power'.format(account.buying_power)) 
        return True 

 def buy(Symbol, qty, side , type, time_in_force): 
     self.alpaca.submit_order(Symbol,qty,side,type,time_in_force)
     print('{} ordered.',Symbol)

 market_open_or_close()

 check_buying_power()