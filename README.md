# TRADUTOR DE ÁUDIO.

#### autor: alysson c. c. cordeiro.
###### ENGENHEIRO DA COMPUTAÇÃO - M8 - INTELI.

## Objetivo
Este projeto é uma aplicação que integra um tradutor de texto, uma aplicação de speech-to-text (transcrição de fala para texto) e uma aplicação de text-to-speech (conversão de texto para fala). A ferramenta de terminal criada é capaz de receber como argumento o caminho para um arquivo de áudio contendo fala e transformá-lo em texto, traduzir esse texto para outro idioma e, em seguida, converter o texto traduzido de volta para áudio, reproduzindo-o para o usuário.

## Como faço para instalar?

Primieiro, clone o repositório:

```python
git clone https://github.com/alyssoncastro/projeto-ponderada8-m8.git
```
Abra no caminho:

```python
cd projeto-ponderada8-m8/ponderada8
```

Dependêcias:

```python
pip install whisper googletrans gtts pygame
```
## Como faço para executar?

Para executar o programa, use o seguinte comando no terminal, substituindo <caminho_do_arquivo> pelo caminho do seu arquivo de áudio e <codigo_do_idioma> pelo código do idioma para tradução (por exemplo, 'en' para inglês, 'pt' para português):

```python
python3 locutor.py -f <caminho_do_arquivo> -l <codigo_do_idioma>
```

meu exemplo de uso:

```python
python3 locutor.py -f /Modulo8/projeto-ponderada8-m8/ponderada8/audio1.ogg -l en
```

*obs: você poderá fr, pt, ja, ou qualquer outro idioma.*

## Funcionalidades:

- Transcrição de Áudio para Texto: Usa o Whisper para converter a fala do arquivo de áudio em texto.
- Tradução de Texto: Traduz o texto transcrito para o idioma escolhido.
- Text-to-Speech: Converte o texto traduzido de volta para áudio e o reproduz.

## VÍDEO DEMONSTRATIVO: (clique na imagem)

[![Texto alternativo](ponderada8/tradutor.jpeg))](https://youtu.be/_wM9MnzV5eI?si=u5LcMroWEjQ8Clsf)

