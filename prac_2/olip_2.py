def check_winners(scores: list, student_score: int) -> None:
    """Печатает, вошёл ли Стас в тройку победителей.

    Args:
        scores: список баллов всех участников.
        student_score: балл Стаса.
    """
    top3 = sorted(scores, reverse=True)[:3]

    if student_score in top3:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")

check_winners({76, 23, 3, 98, 86, 100, 70}, 100)