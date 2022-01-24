import os
import glob
import pandas as pd


path = f'{os.getcwd()}/data/'

extension = 'csv'
all_filenames = [i for i in glob.glob(f'{path}*.{extension}')]

# combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
# export to csv
combined_csv.to_csv("data.csv", index=False, encoding='utf-8')
