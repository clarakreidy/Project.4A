import pandas as pd
import numpy as np
import glob
import os

# path to the directory where the csv files are
path = f'{os.getcwd()}/'
all_files = glob.glob(path + "*.csv")

li = []

# reading each csv one by one and adding them to list
for filename in all_files:
    df = pd.read_csv(filename)

    df.replace(to_replace='*', value=np.nan, inplace=True)
    df.dropna(subset=['BE'], inplace=True)

    df['annee'] = pd.to_datetime(df['annee'], format='%Y')
    df['BE'] = pd.to_numeric(df['BE'], downcast='integer')
    df['NOMBE'] = pd.Series(df['NOMBE'], dtype=pd.StringDtype())
    df['Famille_met'] = pd.Series(df['Famille_met'], dtype=pd.StringDtype())
    df['Lbl_fam_met'] = pd.Series(df['Lbl_fam_met'], dtype=pd.StringDtype())
    df['metier'] = pd.Series(df['metier'], dtype=pd.StringDtype())
    df['nommetier'] = pd.Series(df['nommetier'], dtype=pd.StringDtype())
    df['Dept'] = pd.Series(df['Dept'], dtype=pd.StringDtype())
    df['NomDept'] = pd.Series(df['NomDept'], dtype=pd.StringDtype())
    df['met'] = pd.Series(df['met'], dtype=pd.Float32Dtype())
    df['xmet'] = pd.Series(df['xmet'], dtype=pd.Float32Dtype())
    df['smet'] = pd.Series(df['smet'], dtype=pd.Float32Dtype())
    df['REG'] = pd.to_numeric(df['REG'], downcast='integer')
    df['NOM_REG'] = pd.Series(df['NOM_REG'], dtype=pd.StringDtype())

    # df.info()

    df.to_csv(path_or_buf=filename, index=False)

# concatenate all dataframes form each csv into one
# frame = pd.concat(li, axis=0, ignore_index=True)

# replace * value present in met, xmet and smet fields with None
# frame.replace(to_replace='*', value=np.nan, inplace=True)
#
# frame['annee'] = pd.to_datetime(frame['annee'], format='%Y')
# frame['BE'] = pd.Series(frame['BE'], dtype=pd.StringDtype())
# frame['NOMBE'] = pd.Series(frame['NOMBE'], dtype=pd.StringDtype())
# frame['Famille_met'] = pd.Series(frame['Famille_met'], dtype=pd.StringDtype())
# frame['Lbl_fam_met'] = pd.Series(frame['Lbl_fam_met'], dtype=pd.StringDtype())
# frame['metier'] = pd.Series(frame['metier'], dtype=pd.StringDtype())
# frame['nommetier'] = pd.Series(frame['nommetier'], dtype=pd.StringDtype())
# frame['Dept'] = pd.Series(frame['Dept'], dtype=pd.StringDtype())
# frame['NomDept'] = pd.Series(frame['NomDept'], dtype=pd.StringDtype())
# frame['met'] = pd.Series(frame['met'], dtype=pd.Float32Dtype())
# frame['xmet'] = pd.Series(frame['xmet'], dtype=pd.Float32Dtype())
# frame['smet'] = pd.Series(frame['smet'], dtype=pd.Float32Dtype())
# frame['REG'] = pd.Series(frame['REG'], dtype=pd.StringDtype())
# frame['NOM_REG'] = pd.Series(frame['NOM_REG'], dtype=pd.StringDtype())

