from intervalos import mesclar_intervalos

def test_exemplo():
    assert mesclar_intervalos([(1, 3), (2, 6), (8, 10)]) == [(1, 6), (8, 10)]

def test_que_se_tocam():
    assert mesclar_intervalos([(1, 2), (2, 3)]) == [(1, 3)]

def test_desordenado():
    assert mesclar_intervalos([(5, 6), (1, 2)]) == [(1, 2), (5, 6)]

def test_contido():
    assert mesclar_intervalos([(1, 10), (2, 3)]) == [(1, 10)]

def test_vazio():
    assert mesclar_intervalos([]) == []
