import unittest
import nlc

class TestNlc(unittest.TestCase):
    def test_plus(self):
        result = nlc.process_string("fifty three plus twenty one")[1]
        self.assertEqual(74, result)
        
    def test_minus(self):
        result = nlc.process_string("fifty three minus twenty one")[1]
        self.assertEqual(32, result)
        
    def test_multiply(self):
        result = nlc.process_string("fifty three multiply twenty one")[1]
        self.assertEqual(1113, result)
        
    def test_divide(self):
        result = nlc.process_string("fifty four divide twenty seven")[1]
        self.assertEqual(2, result)
        
    def test_mod(self):
        result = nlc.process_string("fifty three mod twenty one")[1]
        self.assertEqual(11, result)
        
    def test_decimals(self):
        nstring = 'two point one three plus four dot zero seven one'
        result = nlc.process_string(nstring)[1]
        self.assertEqual(6.201, result)
        
    def test_spacing(self):
        nstring = 'twohundredthousandninehundredandfourminussixtysix'
        result = nlc.process_string(nstring)[1]
        self.assertEqual(200838, result)    
        
    def test_mixed(self):
        nstring = '30 thousand 800 seventy four'
        result = nlc.process_string(nstring)[1]
        self.assertEqual(30874, result)
        
    def test_unordered(self):
        nstring = 'four million three hundred thousand one hundred and seventy four'
        result = nlc.process_string(nstring)[1]
        self.assertEqual(4300174, result)
        
    def test_places(self):
        nstring = 'two trillion four billion eighty eight million nine thousand five hundred ninety two'
        result = nlc.process_string(nstring)[1]
        self.assertEqual(2004088009592, result)
        
    def test_order_of_operations(self):
        nstring = 'three ** (four minus two) * one plus two'
        result = nlc.process_string(nstring)[1]
        self.assertEqual(11, result)  
        
    def test_alphabetic_to_digits(self):
        unsplit_input = ''
        for ndict in nlc.NUMBERS:
            for n in ndict:
                unsplit_input += n
        raw_token_list = nlc.split_tokens(unsplit_input)
        token_list = nlc.alphabetic_to_digit(raw_token_list)
        result = True
        for t in token_list:
            if not t.isdigit():
                result = False
                break
        self.assertTrue(result)
         
        
if __name__ == "__main__":
    unittest.main()