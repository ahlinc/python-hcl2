"""A parser for HCL2 implemented using the Lark parser"""
import os
from os.path import dirname
from hcl2.transformer import DictTransformer
from lark import Lark


LARK_CACHE_FILE = os.path.join(dirname(__file__), 'hcl2.lark.cache')
LARK_FILE = os.path.join(dirname(__file__), 'hcl2.lark')


def Lark_Cached(transformer=None, postlex=None):
  return Lark(open(LARK_FILE),
              parser="lalr", lexer="standard",
              transformer=transformer, postlex=postlex,
              cache=str(LARK_CACHE_FILE))


hcl2 = Lark_Cached(transformer=DictTransformer())
