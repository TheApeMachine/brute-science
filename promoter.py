# PROMOTER
#
# Brute-forcing the values of a match scoring algorithm, with a little more
# finesse.

from resource import Resource

def main():
    keywords   = ['food']
    expansions = ['eat', 'restaurant', 'meal', 'alimentation', 'thought']
    resources  = Resource().small_test

    # Let's start with an actual assumption this time, not just random numbers.
    b   = 1   # Biases are cool
    kl0 = 0.9 # Keyword level 1
    kl1 = 0.6 # Keyword level 2
    fl1 = 0.9 # Category
    fl2 = 0.6 # Matchers
    fl3 = 0.6 # Title
    fl4 = 0.3 # Description
    fl5 = 0.3 # Tags

if __name__ == "__main__":
    main()
