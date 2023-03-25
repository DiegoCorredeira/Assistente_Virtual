import yaml
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.utils import to_categorical

data = yaml.safe_load(open('train.yml', 'r', encoding='utf-8').read())

inputs, outputs = [], []

for command in data['commands']:
    inputs.append(command['input'].lower())
    outputs.append('{}\{}'.format(command['entidade'], command['acao']))

max_seq_length = max([len(bytes(x.encode('utf-8'))) for x in inputs])

print('Max sequence length:', max_seq_length)

input_data_one_hot = np.zeros((len(inputs), max_seq_length, 256), dtype='float32')
for i, input_text in enumerate(inputs):
    for k, char in enumerate(bytes(input_text.encode('utf-8'))):
        input_data_one_hot[i, k, int(char)] = 1.0

# input_data_sparse = np.zeros((len(inputs), max_seq_length), dtype='int32')
#
# for i, input_text in enumerate(inputs):
#     for k, char in enumerate(input_text):
#         input_data_sparse[i, k] = char2idx[char]


labels = set(outputs)

label2idx = {}
idx2label = {}

for k, label in enumerate(labels):
    label2idx[label] = k
    idx2label[k] = label

output_data = []

for output in outputs:
    output_data.append(label2idx[output])

output_data = to_categorical(output_data, len(output_data))

print(output_data[0])

model = Sequential()
model.add(LSTM(128))
model.add(Dense(len(output_data), activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
model.fit(input_data_one_hot, output_data, epochs=128)


def classificandoTexto(texto):
    x = np.zeros((1, 48, 256), dtype='float32')

    for k, ch in enumerate(bytes(text.encode('utf-8'))):
        x[0, k, int(ch)] = 1.0

    out = model.predict(x)
    idx = out.argmax()
    print(idx2label[idx])


while True:
    text = input('Digite algo: ')
    classificandoTexto(text)
