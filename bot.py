import tkinter
import tkinter.messagebox
import customtkinter
import difflib
from datetime import datetime
from teste import perguntas_respostas

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("orange.json")  # Themes: "blue" (standard), "green", "dark-blue", "orange.json" (ConnectMuseum)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.iconbitmap('images/logo.ico')

        self.perguntas_respostas = perguntas_respostas

        # configure window
        self.title("Núcleo Multidimensional de Gestão do Patrimônio.")
        self.geometry(f"{500}x{300}")  # Aumentando o tamanho da janela de login

        # create login frame with widgets
        self.login_frame = customtkinter.CTkFrame(self, width=300, corner_radius=0)
        self.login_frame.pack(expand=True, fill='both')

        customtkinter.CTkLabel(self.login_frame, text="Login de Usuário", font=customtkinter.CTkFont(size=16, weight="bold")).pack(pady=10)

        customtkinter.CTkLabel(self.login_frame, text="Nome de Usuário:").pack(pady=5)
        self.username_entry = customtkinter.CTkEntry(self.login_frame)
        self.username_entry.pack()

        customtkinter.CTkLabel(self.login_frame, text="Senha:").pack(pady=5)
        self.password_entry = customtkinter.CTkEntry(self.login_frame, show="*")
        self.password_entry.pack()

        # Botão para confirmar o login
        customtkinter.CTkButton(self.login_frame, text="Login", command=self.verificar_login).pack(pady=10)

        # Botão para cadastrar novo usuário
        customtkinter.CTkButton(self.login_frame, text="Cadastrar Novo Usuário", command=self.abrir_janela_cadastro).pack(pady=5)

        # Dicionário para armazenar usuários cadastrados
        self.usuarios_cadastrados = {"Escobar": "nugepbot"}

    def verificar_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.usuarios_cadastrados and self.usuarios_cadastrados[username] == password:
            self.abrir_chatbot(username)
        else:
            tkinter.messagebox.showerror("Erro de Login", "Nome de usuário ou senha incorretos.")

    def abrir_chatbot(self, username):
        self.login_frame.destroy()
        # Código para abrir o chatbot
        chatbot_window = ChatbotWindow(username)
        chatbot_window.mainloop()


    def abrir_janela_cadastro(self):
        cadastro_frame = customtkinter.CTkToplevel(self)
        cadastro_frame.title("Cadastro de usuário")
        cadastro_frame.geometry(f"{500}x{300}")

        cadastro_frame = customtkinter.CTkFrame(cadastro_frame, width=300, corner_radius=0)
        cadastro_frame.pack(expand=True, fill='both')
        

        customtkinter.CTkLabel(cadastro_frame, text="Nome de Usuário:").pack(pady=5)
        self.novo_username_entry = customtkinter.CTkEntry(cadastro_frame)
        self.novo_username_entry.pack()

        customtkinter.CTkLabel(cadastro_frame, text="Senha:").pack(pady=5)
        self.nova_password_entry = customtkinter.CTkEntry(cadastro_frame, show="*")
        self.nova_password_entry.pack()

        customtkinter.CTkButton(cadastro_frame, text="Salvar", command=self.salvar_usuario).pack(pady=10)

    def salvar_usuario(self):
        novo_username = self.novo_username_entry.get()
        nova_password = self.nova_password_entry.get()

        # Adiciona o novo usuário ao dicionário de usuários cadastrados
        self.usuarios_cadastrados[novo_username] = nova_password

        tkinter.messagebox.showinfo("Cadastro de Usuário", "Usuário cadastrado com sucesso!")

    def usernames_cadastrados(self):
        return self.usuarios_cadastrados.keys()
    

class ChatbotWindow(customtkinter.CTk):
    def __init__(self, username):
        super().__init__()
        self.iconbitmap('images/logo.ico')

        self.perguntas_respostas = perguntas_respostas

        # configure window
        self.title("Chatbot - Núcleo Multidimensional de Gestão do Patrimônio.")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Nugep\n Bot", font=customtkinter.CTkFont(size=40, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 30))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.abrir_janela_cadastro)
        self.sidebar_button_4.grid(row=6, column=0, padx=20, pady=10)
       
        # create main entry and button
        self.mensagem = customtkinter.CTkEntry(self, placeholder_text="Insira o sua mensagem")
        self.mensagem.grid(row=3, column=1, columnspan=2, rowspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.mensagem.bind("<Return>", self.enviar_mensagem)

        # create textbox
        self.conversa = customtkinter.CTkTextbox(self, width=250)
        self.conversa.grid(row=0, column=1, rowspan=3, padx=(20, 0), pady=(5, 0), sticky="nsew")
            
        self.sidebar_frame_dir = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame_dir.grid(row=0, column=3, padx =(20,0), rowspan=4, sticky="nsew")
        self.sidebar_frame_dir.grid_rowconfigure(4, weight=1)
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame_dir, text="Tema:", anchor="w")
        self.appearance_mode_label.grid(row=0, column=3, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame_dir, values=["Dark", "Light", "System"],
                                                                       command=self.change_appearance_mode_event)


        self.appearance_mode_optionemenu.grid(row=1, column=3, padx=20, pady=(10, 10))

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame_dir, text="Escala da Tela:", anchor="w")
        self.scaling_label.grid(row=2, column=3, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame_dir, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=3, column=3, padx=20, pady=(10, 20))

        # set default values
        self.sidebar_button_1.configure(text="Informações")
        self.sidebar_button_2.configure(text="Gerar Relatório")
        self.sidebar_button_3.configure(text="Feedbacks")
    
        self.conversa.insert("0.0", "Bem-vindo ao Chatbot do Núcleo Multidimensional de Gestão do Patrimônio!\n"
                                     "Todas as informações sobre o acervo de cultura popular que foram e são pesquisadas estão aqui.\n"
                                     "Atualmente possuímos um acervo com mais de 90 obras de cultura popular localizadas no Rio de Janeiro.\n"
                                     "Para uma melhor experiência, tente ser específico quanto às perguntas.\nAproveite!\n\n")
        
    #tesat se todos os butões estão funcionando
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def enviar_mensagem(self, event):
        self.conversa.configure(state='normal')
        mensagem_usuario = self.mensagem.get()

        self.mensagem.delete(0, customtkinter.END)
        resposta_chatbot = self.processar_mensagem(mensagem_usuario)

        self.conversa.insert(customtkinter.END, "Usuário: " + mensagem_usuario + "\n")
    
        self.conversa.insert(customtkinter.END, "Chatbot: " + resposta_chatbot + "\n")
        self.conversa.see(customtkinter.END)
        self.conversa.configure(state='disabled')

    def processar_mensagem(self, mensagem):
        mensagem = mensagem.lower()

        # Verifica se a mensagem é uma pergunta conhecida
        resposta = self.perguntas_respostas.get(mensagem)

        if resposta is not None:
            return resposta

        # Busca a pergunta mais próxima com base na similaridade de strings
        perguntas = list(self.perguntas_respostas.keys())
        matches = difflib.get_close_matches(mensagem, perguntas, n=1, cutoff=0.5)

        if matches:
            pergunta_correspondente = matches[0]
            resposta_correspondente = self.perguntas_respostas[pergunta_correspondente]
            return resposta_correspondente

        # Caso não encontre nenhuma correspondência, retorna uma mensagem padrão
        return "Desculpe, não entendi a pergunta. Tente novamente ou reformule a sua pergunta."

    def abrir_janela_cadastro(self):
        cadastro_frame = customtkinter.CTkToplevel(self)
        cadastro_frame.title("Cadastro de usuário")
        cadastro_frame.geometry(f"{500}x{300}")

        cadastro_frame = customtkinter.CTkFrame(cadastro_frame, width=300, corner_radius=0)
        cadastro_frame.pack(expand=True, fill='both')
        

        customtkinter.CTkLabel(cadastro_frame, text="Nome de Usuário:").pack(pady=5)
        self.novo_username_entry = customtkinter.CTkEntry(cadastro_frame)
        self.novo_username_entry.pack()

        customtkinter.CTkLabel(cadastro_frame, text="Senha:").pack(pady=5)
        self.nova_password_entry = customtkinter.CTkEntry(cadastro_frame, show="*")
        self.nova_password_entry.pack()

        customtkinter.CTkButton(cadastro_frame, text="Salvar", command=self.salvar_usuario).pack(pady=10)

    def salvar_usuario(self):
        novo_username = self.novo_username_entry.get()
        nova_password = self.nova_password_entry.get()

        # Adiciona o novo usuário ao dicionário de usuários cadastrados
        self.usuarios_cadastrados[novo_username] = nova_password

        tkinter.messagebox.showinfo("Cadastro de Usuário", "Usuário cadastrado com sucesso!")

if __name__ == "__main__":
    app = App()
    app.mainloop()
