# Python_pytest

# Execute below mentioned command to run the test case
pytest
pytest test_game.py
# Execute below mentioned command to run the test case
pytest --cov

# Execute below mentioned command for unit test coverage
python3 -m coverage run -m unittest
python3 -m coverage run -m unittest test_stringcase.py

# once it's done run below mentioned command
python3 -m coverage report -m


# run below mentioned method for test
python3 -c "import quize;quize.quize()" 
python3 -c "import gamequiz;gamequiz.quiz()"

