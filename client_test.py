import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertEqual(stock, quote['stock'])
        self.assertEqual(bid_price, quote['top_bid']['price'])
        self.assertEqual(ask_price, quote['top_ask']['price'])
        self.assertEqual(price, (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertEqual(stock, quote['stock'])
        self.assertEqual(bid_price, quote['top_bid']['price'])
        self.assertEqual(ask_price, quote['top_ask']['price'])
        self.assertEqual(price, (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)

  """ ------------ Add more unit tests ------------ """
  #When the bid and ask price are the same
  def test_getDataPoint_identicalBidAsk(self):
      quotes = [
          {'top_ask': {'price': 120.5, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.5, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
      ]
      for quote in quotes:
          stock, bid_price, ask_price, price = getDataPoint(quote)
          self.assertEqual(stock, quote['stock'])
          self.assertEqual(bid_price, quote['top_bid']['price'])
          self.assertEqual(ask_price, quote['top_ask']['price'])
          self.assertEqual(price, quote['top_bid']['price'])  # Since bid and ask are the same

  #When data is missing
  def test_getDataPoint_missingData(self):
      quotes = [
          {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {}, 'id': '0.109974697771', 'stock': 'ABC'},
          {'top_ask': {}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
      ]
      for quote in quotes:
          stock, bid_price, ask_price, price = getDataPoint(quote)
          self.assertEqual(stock, quote['stock'])
          self.assertEqual(bid_price, quote['top_bid'].get('price', None))
          self.assertEqual(ask_price, quote['top_ask'].get('price', None))
          if bid_price is not None and ask_price is not None:
              self.assertEqual(price, (bid_price + ask_price) / 2)
          else:
              self.assertIsNone(price)

  #When the price is 0
  def test_getDataPoint_zeroPrices(self):
      quotes = [
          {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
      ]
      for quote in quotes:
          stock, bid_price, ask_price, price = getDataPoint(quote)
          self.assertEqual(stock, quote['stock'])
          self.assertEqual(bid_price, 0)
          self.assertEqual(ask_price, 0)
          self.assertEqual(price, 0)



if __name__ == '__main__':
    unittest.main()
