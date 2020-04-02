# sprint-challenge-3.1 / acme_test.py

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    
    def test_default_weight(self):
        '''Test to ensure product weight is 20.'''
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability(self):
        '''Test to ensure that steal and explode are working properly.'''
        prod = Product('Test Product')
        self.assertEqual(prod.stealability(), 'Kinda Stealable...')

    def test_explode(self):
        '''Test to ensure that steal and explode are working properly.'''
        prod = Product('Test Product')
        self.assertEqual(prod.explode(), '...boom!')

class AcmeReportTests(unittest.TestCase):
    '''making these tests to pass this test'''
    def test_default_num_products(self):
        '''test to ensure that generate_products creates 30 products'''
        product_list = generate_products()
        self.assertEqual(len(product_list), 30)
    
    def test_legal_names(self):
        '''test to ensure that all product_list names are legal names'''
        product_list = generate_products()
        name = str(product_list[0].name)
        a, b = name.split()
        self.assertIn(a, ADJECTIVES)
        self.assertIn(b, NOUNS)       


if __name__ == '__main__':
    unittest.main()