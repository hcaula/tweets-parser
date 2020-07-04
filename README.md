# tweets-parser
Esse projeto facilita o processamento de _tweets_ buscados a partir da Search API do Twitter, possibilitando:
1. Transformar o retorno da API em um arquivo JSON bem formatado;
2. Transformar o arquivo JSON gerado em CSV.

## Instruções

### O que você precisa
#### Para consumir a API  do Twitter
1. Uma [conta no Twitter](https://twitter.com/i/flow/signup);
2. Uma [conta de desenvolvedor](https://developer.twitter.com/en/apply-for-access) do Twitter;
3. Um [aplicativo](https://developer.twitter.com/en/apps) em sua conta de desenvolvedor do Twitter;
4. Um [ambiente de desenvolvimento](https://developer.twitter.com/en/account/environments) para consumir _tweets_ sem limite de período (Search Tweets: Full Archive).
	- OBS.: Nomeie o ambiente de desenvolvimento de "prod".

#### Para requisitar os dados da API
1. [Instalar Python](https://realpython.com/installing-python/) em sua máquina (linha de comando);
	- Python já vem instalado em Mac OSX.
	- Você pode verificar se Python já está instalado em sua máquina, abra o terminal, digite `python --version`. Se estiver instalado, esse comando lhe dará a versão instalada em sua máquina (ex.: `Python 3.7.3`).
2. Instalar a biblioteca Python [search-tweets](https://github.com/twitterdev/search-tweets-python).
	- Você pode instalar facilmente executando `pip install searchtweets` em seu terminal.

#### Para instalar este projeto
1. Clone este repositório.
	- Em seu terminal, execute `git clone https://github.com/hcaula/tweets-parser`. Isso criará um diretório chamado `tweets-parser` com os arquivos deste projeto.
2. Pelo terminal, entre no diretório desse projeto executando `cd tweets-parser`.
	- Para verificar que você está no repositório certo, execute `ls`. Esse comando lista os arquivos e diretórios do diretório atual. A saída deve conter todos os arquivos desse repositório. Se tudo ocorrer bem, você já instalou este projeto!