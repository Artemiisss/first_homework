def team_score(win, draw, lose) -> int:
    return win * 3 + draw - lose


print(team_score(3, 1, 1))
