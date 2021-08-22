#!/usr/bin/env python3
# coding: utf8
import os, sys, csv, json, datetime, locale
from string import Template
from collections import namedtuple
class Null:
    @staticmethod
    def default(*args, **kwargs):
        for arg in args:
            if arg is not None: return arg
#            以下だと数値の0までNone扱いしてしまう
#            if not arg: return arg
    @staticmethod
    def throw(*args, **kwargs): # 関数名が raise だと SyntaxError: invalid syntax
        v = Null.default(*args, **kwargs)
        if v is None: raise ValueError('すべての値がNoneです。非Noneの値を1つ以上用意してください。')
#        以下だと数値の0までNone扱いしてしまう
#        if not v: raise ValueError('すべての値がNoneです。非Noneの値を1つ以上用意してください。')
        else: return v
    @staticmethod
    def exept(f):
        def _wrapper(*args, **kwargs):
            try: return f(*args, **kwargs)
            except: return None
        return _wrapper
class NullEmpty:
    @staticmethod
    def default(*args): # None, '', [], (,), {}, ...
        for arg in args:
            if arg is not None:
                try:
                    if 0 == len(arg): continue
                except: pass
                return arg
#            if arg is not None and (0 < len(arg) if hasattr(arg, 'len') else True): return arg
#            以下だと[],(,),{}などは対象外
#            if arg is not None and '' == arg.strip(): return arg
#            以下だと数値の0までNone扱いしてしまう
#            if not arg: return arg
    @staticmethod
    def throw(*args, **kwargs):
        v = NullEmpty.default(*args, **kwargs)
        if v is None: raise ValueError('すべての値がNoneまたは空文字列です。それ以外の値を1つ以上用意してください。')
        else: return v
    @staticmethod
    def exept(f):
        def _wrapper(*args, **kwargs):
            try: return f(*args, **kwargs)
            except: return None
        return _wrapper

