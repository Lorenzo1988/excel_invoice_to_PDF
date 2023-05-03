import pandas as pd
import glob

#VARIABLE
path_input = "input_files/"
filepaths = glob.glob(path_input+"invoices/*.xlsx")
print(filepaths)

#list comprehension
for i,filepath in enumerate(filepaths):
    print("\n###########")
    print(f"--> filepath: {filepath}")
    #METODO CLASSICO
    df = pd.read_excel(filepath,sheet_name="Sheet 1")
    print(df)
    print("###########")

    #METODO CON exec(). Crea dataframe con nomi diversi
   # exec(f"df_{i+1}=pd.read_excel(filepath,sheet_name='Sheet 1')")
   # exec(f"print(df_{i+1})")



