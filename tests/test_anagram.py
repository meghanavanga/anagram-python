import pytest
from anagram import anagrams

test_data_dir = 'tests/data/test_dictionary.txt'
finder = anagrams.AnagramBase(test_data_dir)

def test_find_anagrams_for_stop():
    input_word="stop"
    expected_output = ["pots","tops","post","sopt","ptos","tsop"].sort()
    actual_output = finder.find_anagrams(input_word).sort()
    assert actual_output == expected_output

def test_find_anagrams_for_love():
    input_word="love"
    expected_output = ["love","evol","vole","velo"].sort()
    actual_output = finder.find_anagrams(input_word).sort()
    assert actual_output == expected_output

def test_found_no_anagrams():
    input_word="nothing"
    expected_output = None
    actual_output = finder.find_anagrams(input_word).sort()
    assert actual_output == expected_output

def test_find_num_anagrams_for_laugh():
    input_word="pet"
    expected_output = 2
    actual_output = finder.find_anagrams(input_word)
    assert len(actual_output) == expected_output

def test_wrong_input_filename():
    with pytest.raises(SystemExit) as excinfo:
        anagrams.AnagramBase('bad_file.txt')
    assert '9' in str(excinfo.value)


