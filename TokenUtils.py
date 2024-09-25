"""
The TokenUtils class provides methods to parse a string and get the string frequency
"""
from collections import Counter
from typing import List
import re


class TokenUtils:
    def __init__(self, split_pattern=r'\W+'):
        self.split_pattern = split_pattern

    """
    TODO: Implement this function to take input as a string and split the string into words.
    return a list of words. e.g. input text = "Hello world", output list = ["Hello", "world"]
    """
    def get_tokens(self, text: str) -> List[str]:
        #TODO

    """
    TODO: Implement the below function to return the most frequent N words.
    e.g. input: text = "red blue green green" and n=1. this should return ["green"] since green occurs
     more than the other words. 
    """
    def get_topn_tokens(self, text: str, n: int) -> List[str]:
        #TODO
