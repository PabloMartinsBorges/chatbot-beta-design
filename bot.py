import tkinter as tk
from tkinter import Tk, Label, Menu, ttk, Scrollbar, Text, Button
from ttkbootstrap import Style
from ttkthemes import ThemedStyle
import difflib
from teste import perguntas_respostas

class Chatbot:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Núcleo Multidimensional de Gestão do Patrimônio.")
        self.perguntas_respostas = perguntas_respostas

        # Adiciona campos em um frame novo
        self.notebook = ttk.Notebook(janela)
        self.notebook.pack(fill='both', expand='yes')

        # Adiciona um campo de texo
        self.conversa = tk.Text(janela, width=50, height=20, font='Arial 10', relief='groove')
        self.conversa.insert(tk.END,"Bem vindo ao Chatbot do Núcleo Multidimensional de Gestão do Patrimônio!\nTodas as informações sobre o acervo de cultura popular que foram e são pesquisadas estão aqui.\nAtualmente possuimos um acervo com mais de 90 obras de cultura popular localizadas no Rio de Janeiro.\nPara uma melhor experiência tente ser específico quanto as perguntas.\nAproveite!\n\n")
        self.conversa.configure(state='disabled')
        self.conversa.pack(fill='both', expand='yes', padx=10, pady=5, side='top')

        scrollbar = ttk.Scrollbar(janela, command=self.conversa.yview)
        scrollbar.pack(side="right", fill="y")
        self.conversa.config(yscrollcommand=scrollbar.set)

        # Adiciona um texto indicando onde escrever a mensagem
        self.label = Label(text="Digite aqui sua mensagem:", font='Arial 15', relief='groove')
        self.label.pack(pady=10, padx=10)

        # wdiget para a entrada do usuário
        self.mensagem = tk.Entry(janela, width=50, font='Arial 10', relief='groove')
        self.mensagem.pack(padx=10, pady=10)
        self.mensagem.bind("<Return>", self.enviar_mensagem)

        #Menu Chat
        self.chat_frame = tk.Frame(self.notebook)
        self.notebook.add(self.chat_frame, text="Chat")

        # Adiciona um texo para indicar a conversa do chatbot - CHAT
        tk.Label(self.chat_frame, text="NUGEP Bot", font="Courier 40").pack(fill='both', expand='yes', padx=10, pady=5, side='top')
        self.chat_bot = tk.Label(self.chat_frame, font="Arial 10")
        self.chat_bot.pack()

        #Menu Cadastro
        self.cadastro_frame = tk.Frame(self.notebook)
        self.notebook.add(self.cadastro_frame, text="Cadastro")

        #Botão de cadastrar - CADASTRO
        self.botao_cadastro = tk.Button(self.cadastro_frame, text="Cadastrar usuário",command=self.abrir_janela_cadastro)
        self.botao_cadastro.grid(row=0, pady=10)

        #Menu História
        self.planilha_frame = tk.Frame(self.notebook)
        self.notebook.add(self.planilha_frame, text="Sua História")

        # Adiciona botão para abrir janela de cadastro - HISTÓRIA
        self.botao_history = tk.Button(self.planilha_frame, text="Cadastrar história",command=self.abrir_janela_history)
        self.botao_history.grid(row=0, pady=10)

        #Menu - Informação
        self.dados_frame = tk.Frame(self.notebook)
        self.notebook.add(self.dados_frame, text='Informações')

        self.label_dados = tk.Label(self.dados_frame, text='Aqui estão disponibilizadas os relatórios de uso do chatbot', font="Arial 10", relief='raised')
        self.label_dados.grid(row=0, column=0)

        self.botao_dados = tk.Button(self.dados_frame, text="Gerar relatório", command=self.abrir_gerar_relatorio)
        self.botao_dados.grid(row=0,column=1,  pady=10)

    def abrir_janela_cadastro(self):
        janela_cadastro = tk.Toplevel(self.janela)
        janela_cadastro.title("Cadastro de usuário")
        janela_cadastro.geometry("500x400")
        janela_cadastro.resizable(True, True)

        tk.Label(janela_cadastro, text="Nome:").grid(row=1, column=0)
        self.nome_entry = tk.Entry(janela_cadastro)
        self.nome_entry.grid(row=1, column=1)

        tk.Label(janela_cadastro, text="Idade:").grid(row=2, column=0)
        self.idade_entry = tk.Entry(janela_cadastro)
        self.idade_entry.grid(row=2, column=1)

        tk.Label(janela_cadastro, text="Email:").grid(row=3, column=0)
        self.email_entry = tk.Entry(janela_cadastro)
        self.email_entry.grid(row=3, column=1)

        tk.Label(janela_cadastro, height=0, text="Endereço:").grid(row=4, column=0)
        self.endereco_entry = tk.Entry(janela_cadastro)
        self.endereco_entry.grid(row=4, column=1)

        botao_salvar_cadastro = ttk.Button(janela_cadastro, text="Salvar", command=self.salvar_usuario)
        botao_salvar_cadastro.grid(row=5, column=3, pady=10)

        self.conversa_cadastro_label = tk.Label(janela_cadastro, text='Janela de Usuários:', font="Arial 20", relief='groove')
        self.conversa_cadastro_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.conversa_cadastro = tk.Text(janela_cadastro, width=30, height=10, font='Arial 10', relief='groove')
        self.conversa_cadastro.configure(state='disabled')
        self.conversa_cadastro.grid(row=6, column=0, columnspan=2, padx=10, pady=10)


    def abrir_gerar_relatorio(self):
        janela_relatorio = tk.Toplevel(self.janela)
        janela_relatorio.title("Relatórios de uso")
        janela_relatorio.geometry("400x450")
        janela_relatorio.resizable(True, True)

        self.label_relatorio = tk.Text(janela_relatorio, font='Verdana 10')
        self.label_relatorio.pack()

        botao_relatorio = tk.Button(janela_relatorio, text="Dashboard",font="Verdana 10")
        botao_relatorio.pack(pady=15)
        #FALTA UMA FUNÇÃO PARA MOSTRAR OS DADOS - CADASTRO, HISTÓRIA E CONVERSAS

    def abrir_janela_history(self):
        janela_history = tk.Toplevel(self.janela)
        janela_history.title("Cadastro de história")
        janela_history.geometry("400x400")
        janela_history.resizable(True, True)

        tk.Label(janela_history, text="Conte aqui:").pack()
        self.history_text = tk.Entry(janela_history, font='Arial 10', relief='groove')
        self.history_text.pack()

        self.history_cadastro = tk.Text(janela_history, width=50, height=10, pady=20, padx=20, font='Arial 10', relief='groove')
        self.history_cadastro.configure(state='disabled')
        self.history_cadastro.pack(pady=15)

        botao_salvar_history = tk.Button(janela_history, text="Salvar", command=self.salvar_history,font="Verdana 10")
        botao_salvar_history.pack(pady=15)

    def salvar_history(self):
        self.history_cadastro.configure(state='normal')
        history = self.history_text.get()
        self.history_cadastro.insert(tk.END, f'História Cadastrada com Sucesso.\nRelato: {history}\n')
        self.history_cadastro.configure(state='disabled')

    def salvar_usuario(self):
        self.conversa_cadastro.configure(state='normal')
        nome = self.nome_entry.get()
        idade = self.idade_entry.get()
        email = self.email_entry.get()
        endereco = self.endereco_entry.get()

        self.conversa_cadastro.insert(tk.END,f'Cadastrado com sucesso: Nome {nome},' f'Idade: {idade},' f'Email: {email},' f'Endereço: {endereco}')
        self.conversa_cadastro.configure(state='disabled')

    def enviar_mensagem(self, event):
        self.conversa.configure(state='normal')
        mensagem_usuario = self.mensagem.get()

        self.mensagem.delete(0, tk.END)
        resposta_chatbot = self.processar_mensagem(mensagem_usuario)

        self.conversa.insert(tk.END, "Usuário: " + mensagem_usuario + "\n")
        self.conversa.insert(tk.END, "Chatbot: " + resposta_chatbot + "\n")
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

estilo = Style(theme="darkly")
janela = estilo.master
janela.title("Núcleo Multidimensional de Gestão do Patrimônio.")
janela.geometry('750x600')
chatbot = Chatbot(janela)

janela.mainloop()