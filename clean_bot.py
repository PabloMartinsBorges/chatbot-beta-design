import tkinter as tk
from ttkbootstrap import Style
from ttkthemes import ThemedStyle
import difflib
from teste import perguntas_respostas

class Chatbot:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Núcleo Multidimensional de Gestão do Patrimônio.")
        self.perguntas_respostas = perguntas_respostas

        # Adiciona um campo de texto para a conversa
        self.conversa = tk.Text(janela, width=50, height=10, font='Arial 10', relief='groove')
        self.conversa.insert(tk.END, "Bem-vindo ao Chatbot do Núcleo Multidimensional de Gestão do Patrimônio!\n"
                                     "Todas as informações sobre o acervo de cultura popular que foram e são pesquisadas estão aqui.\n"
                                     "Atualmente possuímos um acervo com mais de 90 obras de cultura popular localizadas no Rio de Janeiro.\n"
                                     "Para uma melhor experiência, tente ser específico quanto às perguntas.\nAproveite!\n\n")
        self.conversa.configure(state='disabled')
        self.conversa.pack(fill='both', expand='yes', padx=10, pady=5, side='top')

        # Adiciona um texto indicando onde escrever a mensagem
        self.label = tk.Label(text="Digite aqui sua mensagem:", font='Arial 15', relief='groove')
        self.label.pack(pady=10, padx=10)

        # Widget para a entrada do usuário
        self.mensagem = tk.Entry(janela, width=50, font='Arial 10', relief='groove')
        self.mensagem.pack(padx=10, pady=10)
        self.mensagem.bind("<Return>", self.enviar_mensagem)

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
