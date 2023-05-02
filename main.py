import pandas as pd
import glob

#VARIABLE
path_input = "input_files/"
filepaths = glob.glob(path_input+"invoices/*.xlsx")
print(filepaths)

#list comprehension
for i,filepath in enumerate(filepaths):
    num= i+1
    print(f"\n\nfilepath: {filepath}")
    exec(f"df_{num}=pd.read_excel(filepath,sheet_name='Sheet 1')")
    exec(f"print(df_{num})")

#    df = pd.read_excel(filepath,sheet_name="Sheet 1")
#    print(f"df: \n {df}")
print("Pippo")
print(df_1)