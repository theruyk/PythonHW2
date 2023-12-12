import sys
# Добавляем путь к каталогу, где находится модуль HW9
sys.path.append('/Users/the_ryuk/Desktop/PythonHW2/')
from HW9.checking_text import checking_text
import pytest

folder_in = '/Users/the_ryuk/Desktop/PythonHW2/HW10/folder_in'
folder_out = '/Users/the_ryuk/Desktop/PythonHW2/HW10/folder_out'
folder_ex = '/Users/the_ryuk/Desktop/PythonHW2/HW10/folder_ex'

def test_step_1():
    assert checking_text(f"cd {folder_in}; 7z a {folder_out}/archive_1 *", "Everything is Ok")

def test_step_2():
    assert checking_text(f"cd {folder_out}; 7z x archive_1.7z -o{folder_ex}", "Everything is Ok")

def test_step3():
    expected_files = ["file1.txt", "file2.txt"]
    for file in expected_files:
        res = checking_text(f"cd {folder_out}; 7z l archive_1.7z", file)
        assert res, f"{file} not found"



if __name__=='__main__':
    pytest.main(['-vv'])



#pytest -vv /Users/the_ryuk/Desktop/PythonHW2/HW10/Task1.py