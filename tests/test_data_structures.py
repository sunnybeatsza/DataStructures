import unittest
from data_structures import *

class MyTestCase(unittest.TestCase):
     
    #Tests for generate_random_list
    def test_list_length(self):
        length = 10
        result = generate_random_list(length)
        self.assertEqual(len(result), length)
    
    def test_values_in_range(self):
        length = 10
        result = generate_random_list(length)
        for number in result:
            self.assertGreaterEqual(number, 0)
            self.assertLessEqual(number, 100)
    
    def test_output_type(self):
        length = 5
        result = generate_random_list(length)
        self.assertIsInstance(result, list)
        for number in result:
            self.assertIsInstance(number, int)

    #Tests for find max
    def test_find_max(self):
        list = [31, 60, 79, 73, 82]
        result = find_max(list)
        self.assertEqual(result, 82)

    def test_find_max_negative(self):
        list = [-3, -1, -7, -4]
        result = find_max(list)
        self.assertEqual(result, -1)
        
    def test_max_mixed_numbers(self):
        list = [-3, 10, -7, 4]
        result = find_max(list)
        self.assertEqual(result, 10)

    #Tests for find min
    def test_find_min(self):
        list = [31, 60, 79, 73, 82]
        result = find_min(list)
        self.assertEqual(result, 31)

    def test_find_min_negative(self):
        list = [-3, -1, -7, -4]
        result = find_min(list)
        self.assertEqual(result, -7)

    def test_min_mixed_numbers(self):
        list = [-3, 10, -7, 4]
        result = find_min(list)
        self.assertEqual(result, -7)

    #Tests for find average
    def test_find_average(self): 
        numbers = [1, 2, 3, 4, 5]
        result = find_average(numbers)
        self.assertEqual(result, 3.0)
    
    def test_output_average(self):
        numbers = [1, 2, 3, 4, 5]
        result = find_average(numbers)
        self.assertIsInstance(result, float)

    def test_average_of_negative_numbers(self):
        numbers = [-1, -2, -3, -4, -5]
        result = find_average(numbers)
        self.assertEqual(result, -3.0)

    #Tests for find number of even numbers
    def test_find_even_mixed(self):
        numbers = [1, 2, 3, 4, 5]
        result = find_number_of_even_numbers(numbers)
        self.assertEqual(result, 2,)

    def test_no_even_numbers(self):
        numbers = [1, 3, 5, 7, 9]
        result = find_number_of_even_numbers(numbers)
        self.assertEqual(result, 0, )

    def test_all_even_numbers(self):
        numbers = [2, 4, 6, 8, 10]
        result = find_number_of_even_numbers(numbers)
        self.assertEqual(result, 5, )

    #Tests for find number of odd numbers
    def test_find_odd_mixed(self):
        numbers = [1, 2, 3, 4, 5]
        result = find_number_of_odd_numbers(numbers)
        self.assertEqual(result, 3)

    def test_no_odd_numbers(self):
        numbers = [2, 4, 6, 8, 10]
        result = find_number_of_odd_numbers(numbers)
        self.assertEqual(result, 0, )

    def test_all_odd_numbers(self):
        numbers = [1, 3, 5, 7, 9]
        result = find_number_of_odd_numbers(numbers)
        self.assertEqual(result, 5, )

    def test_even_numbers_total(self):
        numbers = [1, 2, 3, 4, 5]
        result = find_even_numbers(numbers)
        self.assertEqual(result, (2, 4))

    def test_no_even_numbers_total(self):
        numbers = [1, 3, 5, 7, 9]
        result = find_even_numbers(numbers)
        self.assertEqual(result, ())

    def test_all_even_numbers_total(self):
        numbers = [2, 4, 6, 8, 10]
        result = find_even_numbers(numbers)
        self.assertEqual(result, (2, 4, 6, 8, 10))

 # Tests for find_odd_numbers
    def test_find_odd_numbers_mixed(self):
        self.assertEqual(find_odd_numbers([1, 2, 3, 4, 5]), (1, 3, 5))

    def test_find_odd_numbers_none(self):
        self.assertEqual(find_odd_numbers([2, 4, 6]), ())

    def test_find_odd_numbers_all_odd(self):
        self.assertEqual(find_odd_numbers([1, 3, 5, 7]), (1, 3, 5, 7))

    # Tests for return_list_stats
    def test_return_list_stats_basic(self):
        stats = return_list_stats([1, 2, 3, 4, 5])
        self.assertEqual(stats['min'], 1)
        self.assertEqual(stats['max'], 5)
        self.assertEqual(stats['average'], 3.0)

    def test_return_list_stats_even_odd_counts(self):
        stats = return_list_stats([1, 2, 3, 4, 5])
        self.assertEqual(stats['number_of_even_numbers'], 2)
        self.assertEqual(stats['number_of_odd_numbers'], 3)

    def test_return_list_stats_unique_numbers(self):
        stats = return_list_stats([1, 1, 2, 3, 3])
        self.assertEqual(stats['unique_numbers'], {1, 2, 3})

    # Tests for process_characters
    def test_process_characters_mixed(self):
        result = process_characters(['a', '1', 'b', '3', 'c', '@', '5', 'd', 'e'])
        self.assertEqual(result, (['a', 'b', 'c', 'd', 'e'], [1, 3, 5]))

    def test_process_characters_only_numbers(self):
        result = process_characters(['1', '2', '3', '4'])
        self.assertEqual(result, ([], [1, 2, 3, 4]))

    def test_process_characters_only_letters(self):
        result = process_characters(['x', 'y', 'z'])
        self.assertEqual(result, (['x', 'y', 'z'], []))

    # Tests for generate_squared_dict
    def test_generate_squared_dict_basic(self):
        self.assertEqual(generate_squared_dict(3), {1: 1, 2: 4, 3: 9})

    def test_generate_squared_dict_zero(self):
        self.assertEqual(generate_squared_dict(0), {})

    def test_generate_squared_dict_negative(self):
        self.assertEqual(generate_squared_dict(-5), {-5: 25, -4: 16, -3: 9, -2: 4, -1: 1})

    # Tests for convert_to_word_list
    def test_convert_to_word_list_sentence(self):
        result = convert_to_word_list("Hello, world!")
        self.assertEqual(result, ["hello", "world"])

    def test_convert_to_word_list_with_punctuation(self):
        result = convert_to_word_list("Let's test, with punctuation")
        self.assertEqual(result, ["lets", "test", "with", "punctuation"])

    def test_convert_to_word_list_empty_string(self):
        result = convert_to_word_list("")
        self.assertEqual(result, [])

    # Tests for letters_count_map
    def test_letters_count_map_basic(self):
        result = letters_count_map("hello")
        self.assertEqual(result['h'], 1)
        self.assertEqual(result['e'], 1)
        self.assertEqual(result['l'], 2)
        self.assertEqual(result['o'], 1)

    def test_letters_count_map_case_insensitive(self):
        result = letters_count_map("HelloHELLO")
        self.assertEqual(result['h'], 2)
        self.assertEqual(result['e'], 2)
        self.assertEqual(result['l'], 4)
        self.assertEqual(result['o'], 2)

    def test_letters_count_map_missing_letter(self):
        result = letters_count_map("abc")
        self.assertEqual(result['z'], 0)

    # Tests for text_to_morse
    def test_text_to_morse_basic(self):
        result = text_to_morse("SOS")
        self.assertEqual(result, "... --- ...")

    def test_text_to_morse_numbers(self):
        result = text_to_morse("123")
        self.assertEqual(result, ".---- ..--- ...--")
