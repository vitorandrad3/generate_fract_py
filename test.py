import pytest
from main import search_integer_period_and_not_period
from main import transform_to_fraction


def test_search_integer_period_and_not_period():
    assert search_integer_period_and_not_period('0.1') == ('0','1', '')
    assert search_integer_period_and_not_period('0.12') == ('0','12','')
    assert search_integer_period_and_not_period('1.3434') == ('1','34','')
    assert search_integer_period_and_not_period('0.13434') == ('0','34','1')
    assert search_integer_period_and_not_period('3.1212') == ('3','12','')
    assert search_integer_period_and_not_period('1.133') == ('1','3','1')
    assert search_integer_period_and_not_period('1.123123') == ('1','123','')

def test_tranform_to_fraction():
    assert transform_to_fraction('0.1') == '1/9'
    assert transform_to_fraction('0.333') == '1/3'
    assert transform_to_fraction('0.666') == '2/3'
    assert transform_to_fraction('0.0833') == '1/12'
    assert transform_to_fraction('0.818181') == '9/11'
    assert transform_to_fraction('0.1666') == '1/6'
    assert transform_to_fraction('0.272727') == '3/11'
    assert transform_to_fraction('62.53777') == '14071/225'
    assert transform_to_fraction('1.133') == '17/15'

     
    
    

