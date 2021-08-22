#!/usr/bin/env python3
# coding: utf8
import os,sys,pathlib,inspect
sys.path.append(str(pathlib.Path(__file__, '../../src').resolve()))
from collections import namedtuple
from null import NullEmpty
import unittest
class TestNullEmpty(unittest.TestCase):
    def test_default(self):
        for case in [
            ((None, 0), 0),
            (('', 0), 0),
            (((), 0), 0),
            (([], 0), 0),
            (({}, 0), 0),
            ((None, 'a'), 'a'),
            ((None, None, 0), 0),
            ((None, None, None, 0), 0),
            ((0, None), 0),
            (('a', None), 'a'),
            ((0, 'a', None), 0),
            ((0, 'a', None, 1), 0),
        ]:
            with self.subTest(case=case[0], expected=case[1]):
                self.assertEqual(NullEmpty.default(*case[0]), case[1])
    def test_default_all_none(self):
        for case in [
            ((None,), None),
            ((None, None), None),
            ((None, None, None), None),
        ]:
            with self.subTest(case=case[0], expected=case[1]):
                self.assertEqual(NullEmpty.default(*case[0]), case[1])
    def test_default_all_empty(self):
        T = namedtuple('T', '')
        for case in [
            ((), None),
            (('',), None),
            (([],), None),
            (({},), None),
            (((),), None),
            ((set(),), None),
            ((frozenset(),), None),
            ((str(),), None),
            ((list(),), None),
            ((dict(),), None),
            ((T(),), None),
            (('', [], {}, ()), None),
        ]:
            with self.subTest(case=case[0], expected=case[1]):
                self.assertEqual(NullEmpty.default(*case[0]), case[1])

    def test_default_exception_obj(self):
        ex = Exception()
        for case in [
            ((ex,), ex),
            ((None, ex), ex),
            ((None, None, ex), ex),
            ((None, None, ex, None), ex),
        ]:
            with self.subTest(case=case[0], expected=case[1]):
                self.assertEqual(NullEmpty.default(*case[0]), case[1])
    def test_throw(self):
        T = namedtuple('T', '')
        for case in [
            ((None,), None),
            ((None, None), None),
            ((None, None, None), None),
            ((), None),
            (('',), None),
            (([],), None),
            (({},), None),
            (((),), None),
            ((set(),), None),
            ((frozenset(),), None),
            ((str(),), None),
            ((list(),), None),
            ((dict(),), None),
            ((T(),), None),
            (('', [], {}, ()), None),
        ]:
            with self.subTest(case=case[0], expected=case[1]):
                with self.assertRaises(ValueError, msg='すべての値がNoneまたは空文字列です。それ以外の値を1つ以上用意してください。'):
                    NullEmpty.throw(*case[0])
    def test_throw_ok(self):
        for case in [
            ((None, 0), 0),
            ((None, 'a'), 'a'),
            ((None, None, 0), 0),
            ((None, None, None, 0), 0),
            ((0, None), 0),
            (('a', None), 'a'),
            ((0, 'a', None), 0),
            ((0, 'a', None, 1), 0),
        ]:
            with self.subTest(case=case[0], expected=case[1]):
                self.assertEqual(NullEmpty.throw(*case[0]), case[1])
    def test_except_function(self):
        @NullEmpty.exept
        def get(): raise Exception('なんかエラーです。')
        self.assertEqual(get(), None)
    def test_except_method(self):
        class C:
            @NullEmpty.exept
            def get(self): raise Exception('なんかエラーです。')
        self.assertEqual(C().get(), None)

if __name__ == "__main__":
    unittest.main()
