"""
Program: file_compare.py
Author:  Tara Heeren
Date: 7/25/2020

This is the main program that compares two comma delimited files and outputs the differences
"""
import csv
import os as os
from file_compare import row_compare as rc


def open_file(file):
    try:
        return open(file)
    except IOError:
        print('File open error: ' + str(file) + ' does not exist.')


def write_to_file(file_name, message):
    file_dir = os.path.dirname(__file__)
    # print(str(file_name))  # debug
    try:
        f = open(os.path.join(file_dir, file_name), "a")
        f.write(message + '\n')
    except IOError:
        print('Error writing to ' + str(file_name))


def close_file(file):
    try:
        file.close()
    except IOError:
        print('Error closing file(s)')


def compare_file(file1, file2, user_delimiter, file_name_input='output.txt'):
    file_name = file_name_input
    #print(str(file_name)) # debug
    source_data = open_file(file1)
    #source_data = open_file(r'C:\Users\TaraH\DMACC\Python\FinalProject\files\file1.txt')
    sd = csv.reader(source_data, delimiter=user_delimiter)
    exported_data = open_file(file2)
    #exported_data = open_file(r'C:\Users\TaraH\DMACC\Python\FinalProject\files\file2.txt')
    ed = csv.reader(exported_data, delimiter=user_delimiter)
    column_names_file_1 = source_data.readline().strip().split(user_delimiter)
    column_names_file_2 = exported_data.readline().strip().split(user_delimiter)
    counter = 0
    # print(str(column_names_file_1)) # debug
    # print(str(column_names_file_2)) # debug

    for sourceDataRow, exportedDataRow in zip(sd, ed):
        compare_object = rc.RowCompare(sourceDataRow, exportedDataRow)
        comparison_result = None
        comparison_result = rc.RowCompare.row_element_compare(compare_object)
        #print(str(comparison_result)) # debug
        counter += 1

        if comparison_result is not None:  # comparison_result is the column index at which the mismatch occurred
            #print('counter ' + str(counter)) # debug
            #print('comparison result ' + str(comparison_result)) # debug
            #print('Mismatch in row number %d, column %s, source value %s, target value %s' % (counter, column_names_file_1[int(str(comparison_result))], sourceDataRow[int(str(comparison_result))], exportedDataRow[int(str(comparison_result))]))
            write_to_file(str(file_name), ('Mismatch in row number %d, column %s, source value %s, target value %s' % (counter, column_names_file_1[int(str(comparison_result))], sourceDataRow[int(str(comparison_result))], exportedDataRow[int(str(comparison_result))])))

    print('\nFile comparison complete')

    close_file(source_data)
    close_file(exported_data)
    #print('Files closed')
