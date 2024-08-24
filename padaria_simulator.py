#CASSINO

#========================#IMPORTS#========================#
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os
#========================#IMAGENS#========================#

current_dir = os.path.dirname(os.path.abspath(__file__))

#image1 = Image.open('pao_jogo.png')
#image1 = image1.resize((200, 150))
#image2 = Image.open('pao_frances.png')
#image2 = image2.resize((150, 150))

image_path1 = os.path.join(current_dir, 'padaria_images', 'pao_jogo.png')
image_path2 = os.path.join(current_dir, 'padaria_images', 'pao_frances.png')

img1 = Image.open(image_path1)
img2 = Image.open(image_path2)

image1 = img1.resize((200,150))
image2 = img2.resize((150,150))

#========================#GAME.VARIABLES#========================#
pao = 0
paes_produzidos = 0
producao_de_paes = 1
nivel_forno = 1
quantidade_padeiros = 0
preço_forno = 30
preço_padeiro = 45
rate_producao_padeiro = 1
preço_melhoria_padeiros = 250
melhoria_padeiros_int = 1
melhoria_padeiros_str = 'Curso técnico pros padeiros'
melhoria_final_comprada = False

#========================#FUNCTIONS#========================#
def abrir_creditos():
  janela_creditos.deiconify()
def fechar_creditos():
  janela_creditos.withdraw()

def jogar():
  janela.withdraw()
  global janela_gameplay
  janela_gameplay = tk.Toplevel()
  janela_gameplay.title('Padaria Simulator')
  janela_gameplay.geometry('400x600')

  janela_gameplay.columnconfigure(0, minsize=125)
  janela_gameplay.columnconfigure(1, minsize=150)
  janela_gameplay.columnconfigure(2, minsize=125)
  janela_gameplay.rowconfigure(0, minsize=75)
  janela_gameplay.rowconfigure(1, minsize=225)
  janela_gameplay.rowconfigure(2, minsize=75)
  janela_gameplay.rowconfigure(3, minsize=30)
  janela_gameplay.rowconfigure(4, minsize=30)
  janela_gameplay.rowconfigure(5, minsize=30)
  janela_gameplay.rowconfigure(6, minsize=25)
  janela_gameplay.rowconfigure(7, minsize=30)

  global contador_de_pao
  contador_de_pao = tk.Label(janela_gameplay, text=f'Pães: {pao}\np/s: {quantidade_padeiros * rate_producao_padeiro}', font=('Arial', 19))
  contador_de_pao.grid(row=0, column=1)

  pao_botao = tk.Button(janela_gameplay, image=pao_frances, command=gerar_paes)
  pao_botao.grid(row=1, column=1)

  loja_botao = tk.Button(janela_gameplay, text="Loja", width='15', height='3', bg='#b8b8b8', command=abrir_loja)
  loja_botao.grid(row=2, column=1)

  stats_botao = tk.Button(janela_gameplay, text="Estatísticas", width='15', height='3', bg='#b8b8b8', command=abrir_stats)
  stats_botao.grid(row=4, column=1)

  gerar_paes_padeiros()

  

def gerar_paes():
  global pao
  global paes_produzidos

  pao += producao_de_paes
  paes_produzidos += producao_de_paes
  contador_de_pao.config(text=f'Pães: {pao}\np/s: {quantidade_padeiros * rate_producao_padeiro}')

def gerar_paes_padeiros():
  global pao
  global contador_de_pao
  global paes_produzidos

  pao += rate_producao_padeiro * quantidade_padeiros
  paes_produzidos += rate_producao_padeiro * quantidade_padeiros
  contador_de_pao.config(text=f'Pães: {pao}\np/s: {quantidade_padeiros * rate_producao_padeiro}')
  contador_de_pao.after(1000, gerar_paes_padeiros)

def comprar_forno_melhor():
  global nivel_forno
  global producao_de_paes
  global pao
  global preço_forno

  if pao >= preço_forno:
    pao -= preço_forno
    nivel_forno += 1
    preço_forno *= 2
    producao_de_paes += 1
    loja_comprar_forno_titulo.config(text=f'Forno Nível {nivel_forno + 1}\nPreço: {preço_forno} pães', font=('Arial', 15))
  else:
    messagebox.showinfo(title="Pães insuficientes", message="Você não tem pães o suficiente para comprar isso.")
  contador_de_pao.config(text=f'Pães: {pao}\np/s: {quantidade_padeiros * rate_producao_padeiro}')

def contratar_padeiro():
  global quantidade_padeiros
  global pao
  global preço_padeiro

  if pao >= preço_padeiro:
    quantidade_padeiros += 1
    pao -= preço_padeiro
    preço_padeiro += preço_padeiro + 15
    contador_de_pao.config(text=f'Pães: {pao}\np/s: {quantidade_padeiros * rate_producao_padeiro}')
    loja_comprar_padeiros_titulo.config(text=f"Contratar padeiro ({rate_producao_padeiro}p/s)\nPreço: {preço_padeiro} pães")
  else:
    messagebox.showinfo(title="Pães insuficientes", message="Você não tem pães o suficiente para comprar isso.")

def melhorar_padeiro():
  global melhoria_padeiros_str
  global pao
  global rate_producao_padeiro
  global melhoria_padeiros_int
  global loja_melhorar_padeiros_titulo
  global preço_melhoria_padeiros
  global loja_comprar_padeiros_titulo


  if quantidade_padeiros == 0:
    messagebox.showinfo(title="Sem padeiros", message="Você não tem padeiros para melhorar.")
  elif pao >= preço_melhoria_padeiros:
    pao -= preço_melhoria_padeiros
    rate_producao_padeiro *= 2
    preço_melhoria_padeiros *= 4
    melhoria_padeiros_int += 1
    if melhoria_padeiros_int == 1:
      melhoria_padeiros_str = 'Curso técnico pros padeiros'
    elif melhoria_padeiros_int == 2:
      melhoria_padeiros_str = 'Batedeira ergonômica'
    elif melhoria_padeiros_int == 3:
      melhoria_padeiros_str = 'Trigo importado'
    elif melhoria_padeiros_int == 4:
      melhoria_padeiros_str = 'Bancadas de aço inox'
    elif melhoria_padeiros_int == 5:
      melhoria_padeiros_str = 'Padeiros Grão-mestres'
    elif melhoria_padeiros_int == 6:
      melhoria_padeiros_str = 'Padeiros Grão-mestres'
      janela_loja.withdraw()

    loja_melhorar_padeiros_titulo.config(text=f'{melhoria_padeiros_str}\nPreço: {preço_melhoria_padeiros} pães')
    loja_comprar_padeiros_titulo.config(text=f"Contratar padeiro ({rate_producao_padeiro}p/s)\nPreço: {preço_padeiro} pães")
    contador_de_pao.config(text=f'Pães: {pao}\np/s: {quantidade_padeiros * rate_producao_padeiro}')
  else:
    messagebox.showinfo(title="Pães insuficientes", message="Você não tem pães o suficiente para comprar isso.")

def comprar_melhoria_final():
  global producao_de_paes
  global rate_producao_padeiro
  global pao
  global melhoria_final_comprada

  if pao >= 250000:
    pao -= 250000
    producao_de_paes += 100
    rate_producao_padeiro += 250
    loja_melhoria_final_botao.config(text='Comprar', state=tk.DISABLED)
    melhoria_final_comprada = True
    janela_loja.withdraw()

    global janela_gameplay
    if melhoria_final_comprada:
      botao_minigame_final = tk.Button(janela_gameplay, text='PERIGO!', width='15', height='3', bg='#960000', fg='yellow', font=('Helvetica', 10, 'bold'), command=jogar_minigame_final)
      botao_minigame_final.grid(row=7, column=1)

def abrir_loja():
  global janela_loja
  janela_loja = tk.Toplevel()
  janela_loja.title("Loja de Upgrades")
  janela_loja.geometry("400x600")

  janela_loja.columnconfigure(0, minsize=75)
  janela_loja.columnconfigure(1, minsize=250)
  janela_loja.columnconfigure(2, minsize=75)
  janela_loja.rowconfigure(0, minsize=75)
  janela_loja.rowconfigure(1, minsize=25)
  janela_loja.rowconfigure(2, minsize=25)
  janela_loja.rowconfigure(3, minsize=25)
  janela_loja.rowconfigure(4, minsize=25)
  janela_loja.rowconfigure(5, minsize=25)
  janela_loja.rowconfigure(6, minsize=25)
  janela_loja.rowconfigure(7, minsize=25)
  janela_loja.rowconfigure(8, minsize=25)
  janela_loja.rowconfigure(9, minsize=25)
  janela_loja.rowconfigure(10, minsize=25)
  janela_loja.rowconfigure(11, minsize=25)

  loja_titulo = tk.Label(janela_loja, text='Loja de Melhorias', font=('Helvetica', 20, 'underline', 'bold'), fg='blue')
  loja_titulo.grid(row=0, column=1)

  global preço_forno
  global loja_comprar_forno_titulo
  loja_comprar_forno_titulo = tk.Label(janela_loja, text=f'Forno Nível {nivel_forno + 1}\nPreço: {preço_forno} pães', font=('Arial', 15))
  loja_comprar_forno_titulo.grid(row=1, column=1)

  loja_comprar_forno_botao = tk.Button(janela_loja, text='Comprar', command=comprar_forno_melhor)
  loja_comprar_forno_botao.grid(row=2, column=1)

  global loja_comprar_padeiros_titulo
  loja_comprar_padeiros_titulo = tk.Label(janela_loja, text=f"Contratar padeiro ({rate_producao_padeiro}p/s)\nPreço: {preço_padeiro} pães", font=('Arial', 15))
  loja_comprar_padeiros_titulo.grid(row=4,column=1)

  loja_comprar_padeiros_botao = tk.Button(janela_loja, text='Comprar', command=contratar_padeiro)
  loja_comprar_padeiros_botao.grid(row=5, column=1)

  global melhoria_padeiros_str
  global melhoria_padeiros_int

  global loja_melhorar_padeiros_titulo
  global loja_melhorar_padeiros_botao

  if melhoria_padeiros_int == 6:
    loja_melhorar_padeiros_titulo = tk.Label(janela_loja, text=f'{melhoria_padeiros_str}\nPreço: ---', font=('Arial', 15), fg='gray')
    loja_melhorar_padeiros_botao = tk.Button(janela_loja, text='Comprar', state=tk.DISABLED)
  else:
    loja_melhorar_padeiros_titulo = tk.Label(janela_loja, text=f'{melhoria_padeiros_str}\nPreço: {preço_melhoria_padeiros} pães', font=('Arial', 15))
    loja_melhorar_padeiros_botao = tk.Button(janela_loja, text='Comprar', command=melhorar_padeiro)

  loja_melhorar_padeiros_titulo.grid(row=7, column=1)
  loja_melhorar_padeiros_botao.grid(row=8, column=1)

  global loja_melhoria_final_titulo
  global loja_melhoria_final_botao

  if melhoria_padeiros_int == 6 and not melhoria_final_comprada:
    loja_melhoria_final_titulo = tk.Label(janela_loja, text='INFRAESTRURA DE PONTA\nPreço: 250.000 pães', font=('Helvetica', 15, 'bold', 'underline'), fg='red')
    loja_melhoria_final_titulo.grid(row=10, column=1)

    loja_melhoria_final_botao = tk.Button(janela_loja, text='Comprar', command=comprar_melhoria_final)
    loja_melhoria_final_botao.grid(row=11, column=1)
  
  elif melhoria_padeiros_int == 6 and melhoria_final_comprada:
    loja_melhoria_final_titulo = tk.Label(janela_loja, text='INFRAESTRURA DE PONTA\nPreço: ---', font=('Helvetica', 15, 'bold', 'underline'), fg='gray')
    loja_melhoria_final_titulo.grid(row=10, column=1)

    loja_melhoria_final_botao = tk.Button(janela_loja, text='Comprar', state=tk.DISABLED)
    loja_melhoria_final_botao.grid(row=11, column=1)


def abrir_stats():
  global janela_stats
  janela_stats = tk.Toplevel()
  janela_stats.title('Estatísticas')
  janela_stats.geometry('400x240')

  janela_stats.columnconfigure(0, minsize=50)
  janela_stats.columnconfigure(1, minsize=300)
  janela_stats.columnconfigure(2, minsize=50)

  janela_stats.rowconfigure(0, minsize=30)
  janela_stats.rowconfigure(1, minsize=30)
  janela_stats.rowconfigure(2, minsize=30)
  janela_stats.rowconfigure(3, minsize=30)
  janela_stats.rowconfigure(4, minsize=30)
  janela_stats.rowconfigure(5, minsize=30)
  janela_stats.rowconfigure(6, minsize=30)

  titulo_stats = tk.Label(janela_stats, text='Estatísticas', font=('Arial', 22, 'bold', 'underline'), fg='blue')
  titulo_stats.grid(row=0, column=1)

  global stats_paes_produzidos
  stats_paes_produzidos = tk.Label(janela_stats, text=f'Pães produzidos:     {paes_produzidos}', font=('Arial', 16))
  stats_paes_produzidos.grid(row=1, column=1, sticky='w')

  global stats_padeiros
  stats_padeiros = tk.Label(janela_stats, text=f'Padeiros:     {quantidade_padeiros}', font=('Arial', 16))
  stats_padeiros.grid(row=2, column=1, sticky='w')

  global stats_nivel_padeiros
  stats_nivel_padeiros = tk.Label(janela_stats, text=f'Nível dos padeiros:     {melhoria_padeiros_int}', font=('Arial', 16))
  stats_nivel_padeiros.grid(row=3, column=1, sticky='w')

  global stats_rate_padeiros
  stats_rate_padeiros = tk.Label(janela_stats, text=f'Taxa de produção (padeiros):     {rate_producao_padeiro}', font=('Arial', 16))
  stats_rate_padeiros.grid(row=4, column=1, sticky='w')

  global stats_nivel_forno
  stats_nivel_forno = tk.Label(janela_stats, text=f'Nível do forno:     {nivel_forno}', font=('Arial', 16))
  stats_nivel_forno.grid(row=5, column=1, sticky='w')

  global stats_rate_click
  stats_rate_click = tk.Label(janela_stats, text=f'Taxa de produção (clique):     {producao_de_paes}', font=('Arial', 16))
  stats_rate_click.grid(row=6, column=1, sticky='w')

def jogar_minigame_final():
  global minigame_janela
  minigame_janela = tk.Toplevel()
  minigame_janela.title('O mofo ataca!')
  minigame_janela.geometry('400x400')

  global label_1_minigame
  global label_2_minigame
  label_1_minigame = tk.Label(minigame_janela, text='O MOFO ATACA!', font=('Helvetica', 22, 'bold', 'underline'), fg='red')
  label_1_minigame.pack(pady=5,padx=5)
  label_2_minigame = tk.Label(minigame_janela, text='Durante a construção da infraestrutura de\nponta, algum dos trabalhadores sabotou\nsua padaria soltando mofo no seu estoque\nde pão, agora você terá que lutar contra\neles para salvar seu estabelecimento.', font=('Helvetica', 15) )
  label_2_minigame.pack(pady=5,padx=5)

  global botao_começar_minigame
  botao_começar_minigame = tk.Button(minigame_janela, text='LUTAR', font=('Times', 50), bg='#faa473', fg='#5c3c2a', command=começar_luta)
  botao_começar_minigame.pack(pady=5,padx=5)

def começar_luta():
  global label_1_minigame
  global label_2_minigame
  global botao_começar_minigame
  label_1_minigame.destroy()
  label_2_minigame.destroy()
  botao_começar_minigame.destroy()
  
  global mofos
  mofos = 20

  global tempo
  tempo = 15
  
  global tempo_label
  tempo_label = tk.Label(minigame_janela, text=f'Tempo: {tempo}', font=('Helvetica', 17))
  tempo_label.pack(pady=5)
  
  global mofos_label
  mofos_label = tk.Label(minigame_janela, text=f'Mofos: {mofos}', font=('Helvetica', 14), fg='#015e3e')
  mofos_label.pack(pady=5, padx=5)

  global botao_minigame
  botao_minigame = tk.Button(minigame_janela, text='Clique!', width='5', height='2', bg='yellow', command=clicar_botao)

  botao_minigame.place(x=random.randint(10,390), y=random.randint(10,390))
  minigame_janela.after(1000, tempo_passar)

def clicar_botao():
  global mofos
  if mofos == 1:
    mofos -= 1
    janela_gameplay.withdraw()
    minigame_janela.withdraw()
    janela_win = tk.Toplevel()
    janela_win.geometry('300x130')

    ganhou_label = tk.Label(janela_win, text='VOCÊ GANHOU!', font=('Arial', 25, 'bold'), fg='#1827f5')
    ganhou_label.pack(pady=5, padx=5)
    obrigado = tk.Label(janela_win, text='Obrigado por jogar :)', font=('Helvetica', 13))
    obrigado.pack(pady=5, padx=5)
    sair_win_botao = tk.Button(janela_win, text='Sair', bg='#bf3636', fg='yellow', width='3', command=janela.destroy)
    sair_win_botao.pack(pady=5, padx=10)

  else:
    global botao_minigame
    botao_minigame.place(x=random.randint(10,390), y=random.randint(10,390))

    mofos -= 1

    global mofos_label
    mofos_label.config(text=f'Mofos: {mofos}')
    minigame_janela.update_idletasks()

def tempo_passar():
  global tempo
  global mofos
  tempo -= 1
  if tempo > -1:
    minigame_janela.after(1000, tempo_passar)
  if tempo == -1 and mofos > 0:
    minigame_janela.withdraw()
    janela_loss = tk.Toplevel()
    janela_loss.geometry('300x110')

    perdeu_label = tk.Label(janela_loss, text='VOCÊ FALHOU!', font=('Arial', 24, 'bold'), fg='red')
    perdeu_label.pack(pady=5, padx=5)
    tentedenovo_label = tk.Label(janela_loss, text='Tente novamente', font=('Helvetica', 12))
    tentedenovo_label.pack(pady=5, padx=5)
  else:
    tempo_label.config(text=f'Tempo: {tempo}')
  minigame_janela.update_idletasks()

#========================#ROOT#========================#

janela = tk.Tk()

pao_jogo = ImageTk.PhotoImage(image1)
pao_frances = ImageTk.PhotoImage(image2)
janela.geometry('300x450')
janela.title("Padaria Simulator")

janela.columnconfigure(0, minsize=50)
janela.columnconfigure(1, minsize=200)
janela.columnconfigure(2, minsize=50)
janela.rowconfigure(0, minsize=50)
janela.rowconfigure(1, minsize=50)
janela.rowconfigure(2, minsize=30)
janela.rowconfigure(3, minsize=50)
janela.rowconfigure(4, minsize=50)
janela.rowconfigure(5, minsize=50)

#========================#WIDGETS#========================#

janela_creditos = tk.Toplevel(janela)
janela_creditos.title("Créditos")
janela_creditos.geometry('300x100')
janela_creditos.withdraw()

nome_do_criador = tk.Label(janela_creditos, text='Desenvolvedor:\n[Vinicin0] no Github', font=('Arial', '18'))
nome_do_criador.pack()
botao_fechar_creditos = tk.Button(janela_creditos, text='Fechar', command=fechar_creditos)
botao_fechar_creditos.pack()

titulo = tk.Label(janela, text="Padaria Simulator", font=('Arial', "18", 'bold', 'underline'), fg='red')
titulo.grid(row=0, column=1)

pao_menu =  tk.Label(janela, image=pao_jogo)
pao_menu.grid(row=1, column=1)

botao_start = tk.Button(janela, text='Começar', width='15', height='3', bg='#b8b8b8', command=jogar)
botao_start.grid(row=3, column=1)

botao_creditos = tk.Button(janela, text='Créditos', width='15', height='3', bg='#b8b8b8', command=abrir_creditos)
botao_creditos.grid(row=5, column=1)

janela.mainloop()