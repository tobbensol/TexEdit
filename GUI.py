import tkinter as tk
from PIL import ImageTk
import tex_channel_copier
import numpy as np

class TexEdit:
    def __init__(self):
        self.root = tk.Tk()
        self.background_colour = "gray20"
        self.text_colour = "white"

        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open Tex")
        menubar.add_cascade(menu=filemenu, label="File")

        self.root.geometry("1280x720")
        self.root.title("TexEdit")
        self.root.configure(bg=self.background_colour)
        self.root.config(menu=menubar)

        label = tk.Label(self.root, text= "test", font=("Arial", 20), bg=self.background_colour, foreground=self.text_colour)
        label.grid(row=0, column=0, columnspan=2)

        img_tex = tex_channel_copier.get_tex("target.tex")
        img_hdr = img_tex.hdr
        img_data = tex_channel_copier.get_data(img_tex)
        img = tex_channel_copier.get_image(img_data, img_hdr.height, img_hdr.width)

        
        canvas = ImageTk.PhotoImage(img)

        self.image1 = tk.Label(self.root, image=canvas, background="black")
        self.image1.grid(row=1, column=0, padx=5, pady= 10)
        self.image2 = tk.Label(self.root, image=canvas, background="black")
        self.image2.grid(row=1, column=1, padx=5, pady= 10)


        entryframe = tk.Frame(self.root)
        self.rows, self.cols = (4,2)
        self.text_var = np.identity(max(self.rows, self.cols))[:self.rows, :self.cols].tolist()
        entries = np.empty(shape = (self.rows, self.cols)).tolist()

        for i in range(self.rows):
            for j in range(self.cols):
                # append your StringVar and Entry
                self.text_var[i][j] = tk.StringVar(value=self.text_var[i][j])
                entries[i][j] = tk.Entry(entryframe, width=10, textvariable=self.text_var[i][j])
                entries[i][j].grid(row= i,column = j)

        entryframe.grid(row=2, column=0)
        button= tk.Button(self.root,text="Submit", bg='bisque3', width=15, command=self.get_mat)
        button.grid(row=3, column=0)


        self.root.mainloop()

    def get_mat(self):
        matrix = np.empty(shape=(self.rows, self.cols)).tolist()
        for i in range(self.rows):
            for j in range(self.cols):
                try:
                    matrix[i][j] = float(self.text_var[i][j].get())
                except ValueError:
                    raise ValueError("entry must contain a number")


        print(matrix)

if __name__ == "__main__":
    TexEdit()