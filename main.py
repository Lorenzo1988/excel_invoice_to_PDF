import pandas as pd
import glob
from  fpdf import FPDF
from pathlib import Path

#VARIABLE
path_input = "input_files/"
path_output="output_files/"
filepaths = glob.glob(path_input+"invoices/*.xlsx")


for i,filepath in enumerate(filepaths):
    nome_file = Path(filepath).stem # estreggo solo il nome file senza estensione
    numero_fattura,data_documento = str(nome_file).split("-")

    print(f"\n\nNOME FILE: {nome_file}")
    print(f"NUMERO_FATTURA: {numero_fattura}")
    print("###########")
    print(f"--> filepath: {filepath}")
# DATAFRAME
    #METODO CLASSICO
    df = pd.read_excel(filepath,sheet_name="Sheet 1")
    print(df)
    print("###########")
        #METODO CON exec(). Crea dataframe con nomi diversi
            # exec(f"df_{i+1}=pd.read_excel(filepath,sheet_name='Sheet 1')")
            # exec(f"print(df_{i+1})")
#PDF FILE
    pdf = FPDF(orientation="P" , unit = "mm", format= "A4")

    pdf.add_page()
    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50,h=8,txt= f"Fattura numero: {numero_fattura}",ln=1)

    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50,h=8,txt= f"Data: {data_documento}")

    pdf.output(path_output+"fattura_numero_"+nome_file+".pdf")

