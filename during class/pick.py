def check_guess(guess, answer):
    difference= gues = answer
    if difference==0:
        return 0
    elif difference>0:
        print("guess is higher than answer")
        return 1
    elif difference<0:
        return -1

def test_check_guess():
    guess = 5
    answer = 4
    expected = 0
    
    actual = check_guess(guess, answer)
    
    assert expected==actual

def test_check_too_high():
    guess = 5
    answer = 4
    expected = 1
    
    actual = check_guess(guess, answer)
    
    assert expected==actual
def  test_check_too_low():
    guess = 5
    answer = 4
    expected = -1
    actual = check_guess(guess, answer)
    assert  expected==actual



#hometask slide 13 4.1.6
