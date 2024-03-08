from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_demo():
        expected = 15
        actual = 15
        assert expected == actual        

def test_chance_shoud_return_sum_of_scores():
        d1,d2,d3,d4,d5 = 1,2,3,4,5
        
        score = Yatzy.chance(d1,d2,d3,d4,d5)
        
        assert score == 15

def test_yatzy_should_return_50_when_dice_same_numbers():
        dice = [1,1,1,1,1]
        
        score = Yatzy.yatzy(dice)
        
        assert score == 50
        
def test_yatzy_should_return_0_when_dice_same_numbers():
        dice = [1,1,1,2,1]
        
        score = Yatzy.yatzy(dice)
        
        assert score == 0

def test_yatzy_should_return_0_when_dice_same_numbers():
        dice = [1,1,1,2,1]
        
        score = Yatzy.yatzy(dice)
        
        assert score == 0

def test_yatzy_should_return_sum_of_ones():
        d1,d2,d3,d4,d5 = 1,1,3,4,5
        
        score = Yatzy.ones(d1,d2,d3,d4,d5)
        
        assert score == 2

def test_yatzy_should_return_sum_of_twos():
        d1,d2,d3,d4,d5 = 1,2,2,4,5
        
        score = Yatzy.twos(d1,d2,d3,d4,d5)
        
        assert score == 4

def test_yatzy_should_return_sum_of_threes():
        d1,d2,d3,d4,d5 = 1,2,3,3,5
        
        score = Yatzy.threes(d1,d2,d3,d4,d5)
        
        assert score == 6

def test_yatzy_should_return_sum_of_fours():
        d1,d2,d3,d4,d5 = 1,2,3,4,4
        yatzy = Yatzy(d1,d2,d3,d4,d5)
        score = yatzy.fours()
        
        assert score == 8

def test_yatzy_should_return_sum_of_fives():
        d1,d2,d3,d4,d5 = 1,2,3,5,5
        yatzy = Yatzy(d1,d2,d3,d4,d5)
        score = yatzy.fives()
        
        assert score == 10

def test_yatzy_should_return_sum_of_sixes():
        d1,d2,d3,d4,d5 = 1,2,3,6,6
        yatzy = Yatzy(d1,d2,d3,d4,d5)
        score = yatzy.sixes()
        
        assert score == 12


def test_ones_rule_should_return_0_score():
        d1,d2,d3,d4,d5 = 1,2,3,6,6
        yatzy = Yatzy(d1,d2,d3,d4,d5)
        score = yatzy.sixes()
        
        assert score == 12

def test_should_return_crazy_chance_score():
        dice = [2,4,3,5,6]
        
        expected = 52
        
        score = Yatzy.crazy_chance(dice)
        
        assert score == 52

def test_should_return_crazy_chance_score_when_all_pair():
        dice = [2,4,6,2,2]
        
        expected = 48
        
        score = Yatzy.crazy_chance(dice)
        
        assert score == expected

def test_should_return_crazy_chance_score_when_all_pair():
        dice = [1,1,3,5,5]
        
        expected = 30
        
        score = Yatzy.crazy_chance(dice)
        
        assert score == expected

