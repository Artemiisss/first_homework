from typing import Sized


def longest_word(text) -> Sized:
    return max(text.split(), key=len)


print(longest_word('Mass Effect:2 is the best game that was introduce on E3 in 2010'))
