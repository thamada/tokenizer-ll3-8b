#!/usr/bin/env python3

import tokenizer

print ('Total: ', len(tokenizer.vocab.keys()))
print ('-' * 20)

prompt = ['this', 'is', 'a', 'pen', '.']

for token in prompt:
    print ('%5s, % 5d' % (token, tokenizer.vocab[token]))

