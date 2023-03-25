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

chars = set()

for input_text in inputs + outputs:
    for char in input_text:
        if char not in chars:
            chars.add(char)

char2idx = {}
idx2char = {}

for i, char in enumerate(chars):
    char2idx[char] = i
    idx2char[i] = char

max_seq_length = max([len(x) for x in inputs])

print('Number of chars:', len(chars))
print('Max sequence length:', max_seq_length)

input_data_one_hot = np.zeros((len(inputs), max_seq_length, len(chars)), dtype='int32')
for i, input_text in enumerate(inputs):
    for k, char in enumerate(input_text):
        input_data_one_hot[i, k, char2idx[char]] = 1.0

input_data_sparse = np.zeros((len(inputs), max_seq_length), dtype='int32')

for i, input_text in enumerate(inputs):
    for k, char in enumerate(input_text):
        input_data_sparse[i, k] = char2idx[char]

# Output data

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
model.add(Embedding(len(chars), 64))
model.add(LSTM(128, return_sequences=True))
model.add(Dense(len(output_data), activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

model.summary()
