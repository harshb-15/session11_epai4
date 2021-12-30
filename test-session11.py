import os
import pytest
import inspect
import re

from session11 import Polygon
from session11 import PolygonSeq


def test_session11_readme_exists():
    assert os.path.isfile("README.md"), "README.md file not found!"


def test_session11_readme_500_words():
    readme_words = [word for line in open('README.md', 'r', encoding="utf-8") for word in line.split()]
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add at least 500 words"


def test_session11_readme_file_for_more_than_10_hashes():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10, "You have not described all the functions/classes well in your README.md file"


def test_session11_function_name_had_cap_letter():
    functions = inspect.getmembers(Polygon, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

    functions = inspect.getmembers(PolygonSeq, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"




