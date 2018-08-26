#! /usr/bin/python
# -*- coding: utf-8 -*-

import tensorflow as tf

from tensorlayer.layers.core import Layer

from tensorlayer.layers.utils.quantization import quantize

from tensorlayer.decorators import auto_parse_inputs
from tensorlayer.decorators import deprecated_alias
from tensorlayer.decorators import deprecated_args

__all__ = [
    'SignLayer',
]


class SignLayer(Layer):
    """The :class:`SignLayer` class is for quantizing the layer outputs to -1 or 1 while inferencing.

    Parameters
    ----------
    prev_layer : :class:`Layer`
        Previous layer.
    name : a str
        A unique layer name.

    """
    def __init__(
        self,
        name='sign',
    ):

        self.name = name

        super(SignLayer, self).__init__()

    @auto_parse_inputs
    def compile(self, prev_layer, is_train=True):

        with tf.variable_scope(self.name):
            self._temp_data['outputs'] = quantize(self._temp_data['inputs'])
