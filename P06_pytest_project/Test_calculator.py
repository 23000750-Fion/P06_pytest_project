import pytest
from Calculator.Calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 5
        b = 3
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 2
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 2
        b = 5
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 10
        assert result == expected

    def test_divide(self):
        #arrange
        a=10
        b=2
        cal=Calculator()

        #Act 
        result=cal.divide(a,b)

        #Assert
        expected=5
        assert result == expected


    def test_divide_by_zero(self):
        #arrange
        a=4321
        b=0
        cal=Calculator()

        #Act and Assists
        with pytest.raises(ZeroDivisionError):
            cal.divide(a,b)

