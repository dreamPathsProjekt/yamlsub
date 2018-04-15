# import yaml, pprint, os
import replacements
import argparse

def parse_arguments():
    parser=argparse.ArgumentParser(description='Substite environment variables, user input or secrets to a file')
    parser.add_argument('field', type=str)
    parser.add_argument('original_value', type=str)
    parser.add_argument('value_to_replace', type=str)
    parser.add_argument('filename', type=str)
    parser.add_argument('-t', '--type', type=str, choices=['ini', 'prop', 'yml'], default='yml', help='the type of target file (default: %(default)s)')

    args = parser.parse_args()
    return args


