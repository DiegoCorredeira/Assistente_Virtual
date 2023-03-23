# Projeto Alice - Assistente Virtual
Este código utiliza a biblioteca Vosk e a biblioteca pyttsx3 para criar um sistema de reconhecimento de voz em Python.
Requisitos

Para utilizar este código, você precisa ter as seguintes bibliotecas instaladas em seu ambiente Python:

    vosk: pode ser instalado com o comando pip install vosk
    pyaudio: pode ser instalado com o comando pip install pyaudio
    pyttsx3: pode ser instalado com o comando pip install pyttsx3

Além disso, é necessário ter um modelo de reconhecimento de voz. O modelo utilizado neste código está localizado no diretório 'model'.

# Uso

O código é dividido em duas partes: uma para reconhecimento de voz em tempo real, utilizando o modelo Vosk, e outra para sintetização de voz utilizando a biblioteca pyttsx3.

# Sintetização de Voz

A primeira parte do código utiliza a biblioteca pyttsx3 para sintetizar voz a partir de uma string. Ele inicializa a biblioteca pyttsx3, obtém as vozes disponíveis e define a voz utilizada como a primeira voz disponível.

Em seguida, ele define uma função chamada "sintese_voz" que recebe uma string e utiliza a biblioteca pyttsx3 para sintetizar essa string em voz. Para utilizar esta função, basta chamar sintese_voz("sua string aqui").

# Reconhecimento de Voz em Tempo Real

A segunda parte do código utiliza a biblioteca Vosk para reconhecimento de voz em tempo real. Ele define um modelo de reconhecimento de voz a partir dos dados presentes no diretório 'model', inicializa um gravador e inicia o fluxo de entrada de áudio.

Em seguida, ele entra em um loop infinito que lê blocos de áudio de 16000 bytes e os alimenta para o gravador. Se o gravador reconhecer um comando de voz, ele converte o resultado para um objeto JSON e verifica se o resultado é diferente de None.

Se o resultado não for None, ele extrai a string reconhecida do objeto JSON e a imprime na tela. Em seguida, ele verifica se a string reconhecida corresponde a algum comando pré-definido.

Se a string reconhecida corresponder a algum comando pré-definido, ele chama a função correspondente para sintetizar uma resposta em voz.

Atualmente, o código reconhece os seguintes comandos de voz:

    "me informe as horas" ou "que horas são"
    "qual é o seu nome" ou "como você se chama"
    "alice" (usado para testar se o sistema está funcionando)

Para adicionar novos comandos de voz, basta adicionar uma nova verificação no loop que verifica se a string reconhecida corresponde a algum comando pré-definido e criar uma nova função para tratar o comando.

### Esse repositório encontra-se em manutenção e atualmente está na versão 0.4
