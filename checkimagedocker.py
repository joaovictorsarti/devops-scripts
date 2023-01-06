import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


repositorios = {
  'repo1': 'https://urlnexus.com/repo',
  'repo2': 'https://urlnexus.com/repo',
  'repo3': 'https://urlnexus.com/repo',
  'repo4': 'http://urlnexus.com/repo'
 }

with open('imagens.txt', 'r') as f:

  for linha in f:

    linha = linha.strip()

    nome_imagem, tag = linha.rsplit(':', 1)

    repositorios_encontrados = []

    for nome, url in repositorios.items():

      resposta = requests.get(f'{url}/v2/{nome_imagem}/manifests/{tag}', verify=False)

      if resposta.status_code == 200:
        repositorios_encontrados.append(nome)

    if repositorios_encontrados:
      print(f'Imagem {bcolors.FAIL}{nome_imagem}:{tag}{bcolors.ENDC} {bcolors.OKGREEN}ENCONTRADA{bcolors.ENDC} nos repositórios {bcolors.WARNING}{", ".join(repositorios_encontrados)}{bcolors.ENDC}')
    else:
      print(f'Imagem {nome_imagem}:{tag} {bcolors.FAIL}NÃO{bcolors.ENDC} encontrada em nenhum repositório')