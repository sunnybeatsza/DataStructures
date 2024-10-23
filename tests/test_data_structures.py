import unittest
from data_structures import *

class MyTestCase(unittest.TestCase):
    def test_find_max(self): pass

    def test_find_min(self): pass

    def test_find_average(self): pass

    def test_find_all_even_numbers(self): pass

    def test_find_all_odd_numbers(self): pass

    def test_find_total_number_of_even_numbers(self): pass

    def test_find_total_number_of_odd_numbers(self): pass

    def test_return_list_stats(self): pass
    
    def test_basic(self):
        input_list = ['a', '1', 'b', '3', 'c', '@', '5', 'd', 'e']
        result_alphabets, result_numbers = process_characters(input_list)

    def test_mixed_input(self):
        input_list = ['a', '1', 'b', '3', 'c', '2', '@', '5', 'd', 'e']
        result_alphabets, result_numbers = process_characters(input_list)


    def test_repeated_characters(self):
        input_list = ['1', 'b', 'a', 'c', 'c', 'b', 'a', '1']
        result_alphabets, result_numbers = process_characters(input_list)


    def test_special_characters(self):
        input_list = ['!', '@', '#', '1', '2', '3', '$', '%', '^']
        result_alphabets, result_numbers = process_characters(input_list)


    def test_more_special_characters(self):
        input_list = ['%', '&', '*', '4', '6', '8', '(', ')', '!', 'x']
        result_alphabets, result_numbers = process_characters(input_list)


    def test_generate_squared_dict(self):
        assert generate_squared_dict(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


    def test_convert_word_list_sentence(self): pass
 
    def test_convert_word_list_spaces(self): pass

    def test_letters_count_sentence(self): pass

    def test_alphanumeric_1(self): pass
    
    def test_alphanumeric_2(self): pass
    
    def test_alphanumeric_3(self): pass
    

