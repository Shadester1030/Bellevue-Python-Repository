#Stock Information
stocks = { "GOOGL" : 190, "AMZN" : 98, "PFE" : 1380, "FB" : 55, "APPL" : 10,
            "MRNA" : 30, "AESE" : 90, "CVX" : 9800, "PEP" : 832, "TSLA" : 5000 }

#Ticker Function
while(True):

    ticker = input('Please select a stock. Type stop to stop:')
    if ticker == 'stop':
        break
    if ticker in stocks:
        print('{} : {}'.format(ticker, stocks[ticker]))
    else:
        print(' {} not found'.format(ticker))