from add import calculate_add

def test_positive_numbers():
    assert calculate_add(2, 3) == 10

def test_zero():
    assert calculate_add(50, 0) == -10

def test_negative_numbers():
    assert calculate_add(-50,10) == -40