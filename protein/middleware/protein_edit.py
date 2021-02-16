# ppar = +203
# pgc1 = -166
import pandas as pd
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo


def edit_dat(dat_file):
    lines = open(dat_file, "r")
    new_text = ""
    for line in lines:
        # itens - 09 10 11 = +203
        # itens - 21 22 23 = -166

        item1 = line[9:12]
        item2 = line[21:24]

        edit = "".join((line[:9],
                        str(int(item1)+203),
                        line[12:21],
                        str(int(item2)-166),
                        line[24:]
                        ))
        new_text += edit

    new_filename = f"{dat_file}edited.dat"
    text_file = open(new_filename, "w")
    text_file.write(new_text)
    text_file.close()
    return new_filename



def sort_by_contact(dat_file_edited):

    lines = open(dat_file_edited, "r")

    ppar = []
    pgc1 = []
    contact = []

    for line in lines:
        item1 = line[9:12]
        item2 = line[21:24]
        item3 = line[26:37]

        ppar.append(item1)
        pgc1.append(item2)
        contact.append(float(item3))


    data = {
        "ppar": ppar,
        "pgc1": pgc1,
        "contact": contact
    }
    df = pd.DataFrame(data)
    df = df.sort_values("contact")
    df = df.reset_index(drop=True)

    print(df.head())
    new_csv_name = f"{dat_file_edited}_sorted.csv"
    df.to_csv(new_csv_name)
    return new_csv_name
        

if __name__ == "__main__":
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    showinfo(title="Protein Editing", message="Selecione o arquivo .dat no padrao!")
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    dat_file_edited = edit_dat(filename)
    new_csv_name = sort_by_contact(dat_file_edited)
    showinfo(title="Protein Editing", message=f"Arquivos gerados!\n.dat : {dat_file_edited}\n.csv : {new_csv_name}")




