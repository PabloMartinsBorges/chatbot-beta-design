"""
Example script for testing the Azure ttk theme
Author: rdbende
License: MIT license
Source: https://github.com/rdbende/ttk-widget-factory
"""


import tkinter as tk
from tkinter import ttk



class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create value lists
        self.option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
        self.combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
        self.readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

        # Create control variables
        self.var_0 = tk.BooleanVar()
        self.var_1 = tk.BooleanVar(value=True)
        self.var_2 = tk.BooleanVar()
        self.var_3 = tk.IntVar(value=2)
        self.var_4 = tk.StringVar(value=self.option_menu_list[1])
        self.var_5 = tk.DoubleVar(value=75.0)

        # Create widgets :)
        self.setup_widgets()

    def setup_widgets(self):
        # Create a Frame for the Checkbuttons
        self.check_frame = ttk.LabelFrame(self, text="Outras Funções", padding=(20, 10))
        self.check_frame.grid(
            row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )

    # Button
        self.button1 = ttk.Button(self.check_frame, text="Gerar Relatório")
        self.button1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        self.button2 = ttk.Button(self.check_frame, text="Sua História")
        self.button2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

        self.button3 = ttk.Button(self.check_frame, text="Outros Projetos")
        self.button3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

        self.button7 = ttk.Button(self.check_frame, text="Conheça o Núcleo")
        self.button7.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

        

       
        # Separator
        self.separator = ttk.Separator(self)
        self.separator.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="ew")

        # Create a Frame for the Radiobuttons
        self.radio_frame = ttk.LabelFrame(self, text="Area do Usuario", padding=(20, 10))
        self.radio_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")


        # Button
        self.button4 = ttk.Button(self.radio_frame, text="Criar Conta")
        self.button4.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        self.button5 = ttk.Button(self.radio_frame, text="Log in")
        self.button5.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

    

       

        # Create a Frame for input widgets
        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(
            row=0, column=2, padx=10, pady=(30, 10), sticky="nsew", rowspan=3
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)
        """
        # Entry
        self.entry = ttk.Entry(self.widgets_frame)
        self.entry.insert(0, "TExto")
        self.entry.grid(row=0, column=0, padx=5, pady=(0, 5), sticky="ew")

        """
        
        self.label = ttk.Label(
            self.widgets_frame,
            text="Espaço Livre",
            justify="center",
            font=("-size", 15, "-weight", "bold"),
        )
        self.label.grid(row=1, column=0, padx=5, pady=(0, 5), sticky="ew")
        

        # Panedwindow
        self.paned = ttk.PanedWindow(self)
        self.paned.grid(row=0, column=1, pady=(25, 5), sticky="nsew", rowspan=3)


        # Pane #1
        self.pane_1 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_1, weight=2)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.pane_1)
        self.scrollbar.pack(side="right", fill="y")



         # Adiciona um campo de texto para a conversa
        self.conversa = tk.Text(self.pane_1, width=60, height=25, font='Arial 10', relief='groove')
        self.conversa.insert(tk.END, "Bem-vindo ao Chatbot do Núcleo Multidimensional de Gestão do Patrimônio!\n"
                                     "Todas as informações sobre o acervo de cultura popular que foram e são pesquisadas estão aqui.\n"
                                     "Atualmente possuímos um acervo com mais de 90 obras de cultura popular localizadas no Rio de Janeiro.\n"
                                     "Para uma melhor experiência, tente ser específico quanto às perguntas.\nAproveite!\n\n")
        self.conversa.configure(state='disabled')
        self.conversa.pack(fill='both', expand='yes', padx=10, pady=5, side='top')
        self.conversa.config(yscrollcommand=self.scrollbar.set)



        """
        # Treeview
        self.treeview = ttk.Treeview(
            self.pane_1,
            selectmode="browse",
            yscrollcommand=self.scrollbar.set,
            columns=(1, 2),
            height=10,
        )
        self.treeview.pack(expand=True, fill="both")
        self.scrollbar.config(command=self.treeview.yview)

        # Treeview columns
        self.treeview.column("#0", anchor="w", width=120)
        self.treeview.column(1, anchor="w", width=120)
        self.treeview.column(2, anchor="w", width=120)

        # Treeview headings
        self.treeview.heading("#0", text="Column 1", anchor="center")
        self.treeview.heading(1, text="Column 2", anchor="center")
        self.treeview.heading(2, text="Column 3", anchor="center")

        # Define treeview data
        treeview_data = [
            ("", 1, "Parent", ("Item 1", "Value 1")),
            (1, 2, "Child", ("Subitem 1.1", "Value 1.1")),
            (1, 3, "Child", ("Subitem 1.2", "Value 1.2")),
            (1, 4, "Child", ("Subitem 1.3", "Value 1.3")),
            (1, 5, "Child", ("Subitem 1.4", "Value 1.4")),
            ("", 6, "Parent", ("Item 2", "Value 2")),
            (6, 7, "Child", ("Subitem 2.1", "Value 2.1")),
            (6, 8, "Sub-parent", ("Subitem 2.2", "Value 2.2")),
            (8, 9, "Child", ("Subitem 2.2.1", "Value 2.2.1")),
            (8, 10, "Child", ("Subitem 2.2.2", "Value 2.2.2")),
            (8, 11, "Child", ("Subitem 2.2.3", "Value 2.2.3")),
            (6, 12, "Child", ("Subitem 2.3", "Value 2.3")),
            (6, 13, "Child", ("Subitem 2.4", "Value 2.4")),
            ("", 14, "Parent", ("Item 3", "Value 3")),
            (14, 15, "Child", ("Subitem 3.1", "Value 3.1")),
            (14, 16, "Child", ("Subitem 3.2", "Value 3.2")),
            (14, 17, "Child", ("Subitem 3.3", "Value 3.3")),
            (14, 18, "Child", ("Subitem 3.4", "Value 3.4")),
            ("", 19, "Parent", ("Item 4", "Value 4")),
            (19, 20, "Child", ("Subitem 4.1", "Value 4.1")),
            (19, 21, "Sub-parent", ("Subitem 4.2", "Value 4.2")),
            (21, 22, "Child", ("Subitem 4.2.1", "Value 4.2.1")),
            (21, 23, "Child", ("Subitem 4.2.2", "Value 4.2.2")),
            (21, 24, "Child", ("Subitem 4.2.3", "Value 4.2.3")),
            (19, 25, "Child", ("Subitem 4.3", "Value 4.3")),
        ]

        # Insert treeview data
        for item in treeview_data:
            self.treeview.insert(
                parent=item[0], index="end", iid=item[1], text=item[2], values=item[3]
            )
            if item[0] == "" or item[1] in {8, 21}:
                self.treeview.item(item[1], open=True)  # Open parents

        # Select and scroll
        self.treeview.selection_set(10)
        self.treeview.see(7)
        """
        # Notebook, pane #2
        self.pane_2 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_2, weight=3)
        """
        # Notebook, pane #2
        self.notebook = ttk.Notebook(self.pane_2)
        self.notebook.pack(fill="both", expand=True)

        # Tab #1
        self.tab_1 = ttk.Frame(self.notebook)
        for index in [0, 1]:
            self.tab_1.columnconfigure(index=index, weight=1)
            self.tab_1.rowconfigure(index=index, weight=1)
        self.notebook.add(self.tab_1, text="Tab 1")

        # Scale
        #self.scale = ttk.Scale(self.tab_1, from_=100, to=0, variable=self.var_5, command=lambda event: self.var_5.set(self.scale.get()),)
        #self.scale.grid(row=0, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")

        # Progressbar
       # self.progress = ttk.Progressbar(self.tab_1, value=0, variable=self.var_5,mode="determinate" )
        #self.progress.grid(row=0, column=1, padx=(10, 20), pady=(20, 0), sticky="ew")

        # Label
       # self.label = ttk.Label(
        #    self.tab_1,
         #   text="Azure theme for ttk",
          #  justify="center",
           # font=("-size", 15, "-weight", "bold"),
        #)

        """

        
        # Entry
        self.entry = ttk.Entry(self.pane_2, width=60)
        self.entry.insert(0, "Diga olá!")
        self.entry.grid(row=1, column=0, padx=10, pady=(0, 10), columnspan=3)

       # self.label.grid(row=1, column=0, pady=10, columnspan=2)

        """
        # Tab #2
        self.tab_2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_2, text="Tab 2")

        # Tab #3
        self.tab_3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_3, text="Tab 3")

        # Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))
        """
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("")
    

    # Simply set the theme
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    root.mainloop()
