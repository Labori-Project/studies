from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo

# protein a +203

# protein b +106 

def change_protein_value(filename):
    lines = open(filename, "r")
    text = ""
    for line in lines:
        # 
        new_line = line
        print(line[-2])

        if line[-2] == "A":
            item_a_line = "".join((line[:23],
            str(int(line[23:26]) + 203),
            line[27:]))
            text += item_a_line

        elif line[-2] == "B":
            item_a_line = "".join((line[:23],
            str(int(line[23:26]) + 106),
            line[27:]))
            text += item_a_line

        else: 
            text += new_line
    
    new_filename = filename.split(".")
    new_filename = f"{new_filename[0]}_edited.{new_filename[1]}"
    text_file = open(new_filename, "w")
    text_file.write(text)
    text_file.close()
    return new_filename

if __name__ == "__main__":
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    showinfo(title="Protein Editing", message="Selecione o arquivo .pdb no padrao!")
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    new_filename = change_protein_value(filename)
    showinfo(title="Protein Editing", message=f"Arquivo {new_filename} salvo!")
