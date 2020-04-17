#!/usr/bin/python3

import sys
import pytest

sys.path.insert(1, './../src')
#print(sys.path)
from softdes import lambda_handler

f1 = open("desafio1.py", "r")
f2 = open("desafio2.py", "r")

def test_lambda_wrong():
    lambdaObj = {}
    lambdaObj['code'] = f1.read()
    lambdaObj['ndes'] = 1
    lambdaObj['args'] = [[1], [2], [3]]
    lambdaObj['resp'] = [0, 0, 0]
    lambdaObj['diag'] = ['a', 'b', 'c']
    resp = lambda_handler(lambdaObj, None)
    assert resp == 'a b c'

    f1.close()

def test_lambda_correct():
    lambdaObj = {}
    lambdaObj['code'] = f2.read()
    lambdaObj['ndes'] = 1
    lambdaObj['args'] = [[1], [2], [3]]
    lambdaObj['resp'] = [0, 0, 0]
    lambdaObj['diag'] = ['a', 'b', 'c']
    resp = lambda_handler(lambdaObj, None)
    assert len(resp) == 0

    f2.close()
