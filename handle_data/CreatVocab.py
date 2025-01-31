# -*- coding: utf-8 -*-

import numpy as np
from collections import Counter
import torch
import random

torch.manual_seed(233)
random.seed(233)

UNK = 1
PAD = 0
PAD_S, UNK_S = '<pad>', '<unk>'


def create_vocabularies(data, vocab_size,src_word_counter,tgt_word_counter):

    # 这个是按照出现频率由高到低的顺序的
    src_most_common = [ite for ite, it in src_word_counter.most_common(vocab_size)]
    tgt_most_common = [ite for ite, it in tgt_word_counter.most_common(vocab_size)]

    src_vocab = VocabSrc(src_most_common)
    tgt_vocab = VocabTgt(tgt_most_common)
    print(tgt_vocab)

    return src_vocab, tgt_vocab


class VocabSrc:
    def __init__(self, word_list):
        self._id2extword = [PAD_S, UNK_S]

        self.i2w = [PAD_S, UNK_S] + word_list
        self.w2i = {}
        for idx, word in enumerate(self.i2w):
            self.w2i[word] = idx

        if len(self.w2i) != len(self.i2w):
            print("serious bug: words dumplicated, please check!")
            self.copydict()

    def copydict(self):
        w2i = self.i2w
        return w2i
    def word2id(self, xx):
        if isinstance(xx, list):
            return [self.w2i.get(word,UNK) for word in xx]
        return self.w2i.get(xx, UNK)

    def id2word(self, xx):
        if isinstance(xx, list):
            return [self.i2w[idx] for idx in xx]
        return self.i2w[xx]

    @property
    def size(self):
        return len(self.i2w)

    @property
    def embed_size(self):
        return len(self._id2extword)

       


class VocabTgt:
    def __init__(self, word_list):
        self.i2w = word_list
        self.w2i = {}
        for idx, word in enumerate(self.i2w):
            self.w2i[word] = idx
        if len(self.w2i) != len(self.i2w):
            print("serious bug: words dumplicated, please check!")

    def word2id(self, xx):
        if isinstance(xx, list):
            return [self.w2i[word] for word in xx]
        return self.w2i[xx]

    def id2word(self, xx):
        if isinstance(xx, list):
            return [self.i2w[idx] for idx in xx]
        return self.i2w[xx]

    @property
    def size(self):
        return len(self.i2w)

