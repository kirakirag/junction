import pandas as pd

xls = pd.ExcelFile('uber_hackathon_v2_mock_data.xlsx')
print('Sheet names:', xls.sheet_names)
print()

for name in xls.sheet_names:
    df = pd.read_excel('uber_hackathon_v2_mock_data.xlsx', sheet_name=name, nrows=2)
    print(f'\n{name}:')
    print(f'Columns: {list(df.columns)}')
    print(df.head())
