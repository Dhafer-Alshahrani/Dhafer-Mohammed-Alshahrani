## I got teached By AI to understand the HW 
high_score_board = []


def record_game(player, *scores, bonus=0, multiplier=1.0):
    """
    player: name

    *scores:
       takes any number of round scores.

    bonus:
        optional

    multiplier:
        also optional
    """

    global high_score_board

    if len(scores) == 0:
        return f"{player}, 0, 0, no rounds played"

    for score in scores:
        if score < 0:
            return f"{player}, 0, 0, negative score not allowed"

    raw_total = sum(scores)
    total = (raw_total + bonus) * multiplier

    rounds = len(scores)

    high_score_board.append((player, total))

    sorted_board = sorted(
        high_score_board,
        key=lambda item: item[1],
        reverse=True
    )

    rank = sorted_board.index((player, total)) +1

    if rank == 1:
        status = "high score!"
    else:
        status = f"rank {rank}"

    return player, rounds, total, status


# print(record_game("Dhafer", 10, 20, 30))
print(record_game("Ahmed", 50, 40, bonus=10))
print(record_game("Dhafer", 10, 20, 30))
print(record_game("Tariq", 15, 15, 15, multiplier=2))

print("Leaderboard:")
print(high_score_board)