import importlib.util
import sys
import os
import time


SO = sys.platform
arquivo = ''

while True:

  if importlib.util.find_spec('pygame') != None and importlib.util.find_spec('rich') != None:

    import pygame
    from rich.progress import track

    if SO == 'win32':
      os.system('cls')
    else:
      os.system('clear')

    print('\n')

    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('parabéns.mp3')
    pygame.mixer.music.play()

    for tempo_de_musica in track(range(100), 'Cantando Parabéns...'):
      time.sleep(58/100)

    break
  else:
    try:
      os.system('pip install pygame')
      os.system('pip install rich')
      
    except:
      print('[ERRO] falha ao tentar instalar os pacotes "pygame" e "rich" pelo instalador de pacotes "pip"')


pygame_escolha = input('\nDeseja desinstalar o pacote pygame utilizado na execução no programa?  [s]im  [n]ão\n>: ').lstrip().rstrip().lower()
rich_escolha = input('\nDeseja desinstalar o pacote rich utilizado na execução no programa?  [s]im  [n]ão\n>: ').lstrip().rstrip().lower()

if pygame_escolha == 's':
  os.system('pip uninstall pygame')
else:
  pass

if rich_escolha == 's':
  os.system('pip uninstall rich')
else:
  pass

if SO == 'win32':
  os.system('cls')
else:
  os.system('clear')

print('''

░░░░░░░░░░░░░░░░░░░░░░█████████
░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███
░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███
░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███
░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
░░████████████░░░█████████████████
''')

print('\n~~ Desenvolvido por Nícolas Carvalho [ P2 de Informática 2021.2 ]')