"""
ExcelFile class:
-uses xlrd, openpyxl pkgs (install these pkgs!)

to use:
1. create ExcelFile install
2. pass in path name with extension .xls or .xlsx
"""

import pandas as pd

# # example using ExcelFile
# # **note: 'data.xls' isn't an available
# #         sample dataset!; sample code only
xls_file=pd.ExcelFile("data.xls")
# data in one sheet read into DataFrame
table=xls_file.parse("Sheet1")
# print table
