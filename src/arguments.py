# File: arguments.py
"""
This file contains functions to parse command line arguments
"""

import argparse 

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log-level', dest='log_level', default='WARNING',
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help='Set the logging level (default: %(default)s)')
    parser.add_argument("--DEBUG", action="store_true", help="Run the program in debug mode")
    parser.add_argument("-i", "--input", dest='input_file', help="Input file name", default=None)
    parser.add_argument("-o", "--output", dest='output_file', help="Output file name", default=None)
    return parser.parse_args()