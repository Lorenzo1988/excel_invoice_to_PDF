import pandas as pd
import glob
from  fpdf import FPDF
from pathlib import Path

#VARIABLE
path_input = "input_files/"
path_output= "output_files/"
filepaths = glob.glob(path_input+"invoices/*.xlsx")

for i,filepath in enumerate(filepaths):

    nome_file = Path(filepath).stem # estreggo solo il nome file senza estensione
    numero_fattura,data_documento = str(nome_file).split("-")

    print(f"\n\nNOME FILE: {nome_file}")
    print(f"NUMERO_FATTURA: {numero_fattura}")
    print("###########")
    print(f"--> filepath: {filepath}")
#PDF FILE
    pdf = FPDF(orientation="P" , unit = "mm", format= "A4")

    pdf.add_page()
    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50,h=8,txt= f"Fattura numero: {numero_fattura}",ln=1)

    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50,h=8,txt= f"Data: {data_documento}",ln=1)


    # DATAFRAME
    #METODO CLASSICO
    df = pd.read_excel(filepath,sheet_name="Sheet 1")
    print(df)
    print("###########")
        #METODO CON exec(). Crea dataframe con nomi diversi
            # exec(f"df_{i+1}=pd.read_excel(filepath,sheet_name='Sheet 1')")
            # exec(f"print(df_{i+1})")

# RIGA DI HEADER
    #utilizzo la list comprehension per sostituire "_" con " "
    columns = [item.replace("_"," ").title() for item in df.columns]
    pdf.set_font(family="Times",size=10,style="B")
    pdf.set_text_color(0, 80, 80)

    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1,ln=1)

    # RIGHE CON I VALORI
    for index,row in df.iterrows():
        print(f"\tindex:{index}")
        print(f"\trow:{row}")
        pdf.set_font(family="Times",size=12,)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]),border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]),border=1,ln=1)

    pdf.output(path_output + "fattura_numero_" + nome_file + ".pdf")
