from email_v2_141 import Email

def main():
   e1 = Email(1, 'joe@dcu.ie', 'Hi', 'a'*199 + 'A')
   e2 = Email(2, 'lou@dcu.ie', 'Big News', 'A' + 'a'*199)
   e3 = Email(1, 'joe@dcu.ie', 'Hi there', 'GET RICH! Now!')
   e4 = Email(2, 'bob@dcu.ie', 'Big News', 'CALL ME.')
   e5 = Email(3, 'zoe@dcu.ie', 'Hello you', 'A')

"""
    # There are 10 letters in the body. 8 are upper-case. That's 80%.
    assert(e1.spam_score() == 80)

    # All letters are upper-case. That's 100%.
    assert(e2.spam_score() == 100)

    # One third of letters are upper-case. That's 33%.
    assert(e3.spam_score() == 33)
"""


if __name__ == '__main__':
    main()
