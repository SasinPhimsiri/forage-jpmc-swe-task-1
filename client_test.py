import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock = quote['stock']
      bid_price = float(quote['top_bid']['price'])
      ask_price = float(quote['top_ask']['price'])
      price = (bid_price + ask_price) / 2
      self.assertEqual(getDataPoint(quote), (stock, bid_price, ask_price, price))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock = quote['stock']
      bid_price = float(quote['top_bid']['price'])
      ask_price = float(quote['top_ask']['price'])
      price = (bid_price + ask_price) / 2
      self.assertEqual(getDataPoint(quote), (stock, bid_price, ask_price, price))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_positiveValues(self):
      # Test when price_b is 0
      price_a = 10.0
      price_b = 0.0
      self.assertIsNone(getRatio(price_a, price_b))

      # Test when price_a and price_b are non-zero
      price_a = 5.0
      price_b = 2.5
      expected_ratio = price_a / price_b
      self.assertEqual(getRatio(price_a, price_b), expected_ratio)

      # Test when price_a and price_b are equal
      price_a = 5.0
      price_b = 5.0
      expected_ratio = 1.0
      self.assertEqual(getRatio(price_a, price_b), expected_ratio)

      # Test when price_a is 0 and price_b is non-zero
      price_a = 0.0
      price_b = 2.5
      expected_ratio = 0.0
      self.assertEqual(getRatio(price_a, price_b), expected_ratio)

  def test_getRatio_negativeValues(self):
      # Test when price_a and price_b are negative
      price_a = -5.0
      price_b = -2.5
      expected_ratio = price_a / price_b
      self.assertEqual(getRatio(price_a, price_b), expected_ratio)

      # Test when price_a is negative and price_b is positive
      price_a = -5.0
      price_b = 2.5
      expected_ratio = price_a / price_b
      self.assertEqual(getRatio(price_a, price_b), expected_ratio)

      # Test when price_a is positive and price_b is negative
      price_a = 5.0
      price_b = -2.5
      expected_ratio = price_a / price_b
      self.assertEqual(getRatio(price_a, price_b), expected_ratio)

  def test_getRatio_divisionByZero(self):
      # Test when both price_a and price_b are 0
      price_a = 0.0
      price_b = 0.0
      self.assertIsNone(getRatio(price_a, price_b))
      
  def test_getRatio_largeValues(self):
      # Test with large values
      price_a = 1.0e10
      price_b = 1.0e5
      expected_ratio = price_a / price_b
      self.assertEqual(getRatio(price_a, price_b), expected_ratio)

  def test_getRatio_smallValues(self):
      # Test with small values
      price_a = 1.0e-10
      price_b = 1.0e-5
      expected_ratio = price_a / price_b
      self.assertEqual(getRatio(price_a, price_b), expected_ratio)

if __name__ == '__main__':
    unittest.main()
