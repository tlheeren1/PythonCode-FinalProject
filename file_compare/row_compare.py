"""
Program: row_compare.py
Author:  Tara Heeren
Date: 7/25/2020

This program creates a Row_Comparison class
Constructor:
:param: source_file_row - required
:param: output_file_row - required
:returns: row_number or none
"""


class RowCompare:
    # Constructor
    def __init__(self, source_row, exported_row):
        self.source_row = source_row
        self.exported_row = exported_row
        self.row_length = min(len(self.source_row), len(self.exported_row))
        self.return_data = None
        # print('source_row ' + str(self.source_row)) # debug
        # print('exported_row ' + str(self.exported_row)) # debug
        # print('row length ' + str(self.row_length))  # debug

    def row_element_compare(self):
        # print(str(self.source_row)) # debug
        # print(str(self.exported_row)) # debug
        # print(str(self.row_length))  # debug

        for i in range(self.row_length):
            if self.source_row[i] != self.exported_row[i]:
                self.return_data = i
        return self.return_data
