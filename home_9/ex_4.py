def change_word(f_string, changed_word, new_word, count: int) -> str:
    return f_string.replace(changed_word, new_word, count)


print(change_word('Good cars are makes by bmw,but audi still better than bmw', 'bmw', 'mercedes', 2))
