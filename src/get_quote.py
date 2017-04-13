import sys
from yahoo_finance import Share

def get_price(stockName):
    """
    gets stock data for given symbol
    """
    share = Share(stockName)
    if share.get_name() == '':
        print('Requested stock name does not exist')
        return
    print(share.get_price())
    return share.get_price()

def get_historic_data(stockName, dateStart, dateEnd):
    """
    gets historic stock data for given symbol and range of dates
    """
    share = Share(stockName)
    if share.get_name() == '':
        print('Requested stock name does not exist')
        return
    print(share.get_historical(dateStart, dateEnd))
    return share.get_historical(dateStart, dateEnd)

if len(sys.argv) == 2:
    stockName = str(sys.argv[1])
    get_price(stockName)

if len(sys.argv) == 4:
    stockName = str(sys.argv[1])
    dateStart = str(sys.argv[2])
    dateEnd = str(sys.argv[3])
    get_historic_data(stockName, dateStart, dateEnd)