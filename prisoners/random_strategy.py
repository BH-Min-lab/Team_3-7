import random
from drawer import shuffled_drawers, prisoners, OPEN_LIMIT, DRAWER_COUNT

def random_success(drawers, prisoner):
    picks = random.sample(range(DRAWER_COUNT), OPEN_LIMIT)
    return any(drawers[idx] == prisoner for idx in picks)

def play_random(trials = 100_000):
    wins = 0
    for _ in range(trials):
        drawers = shuffled_drawers()
        if all(random_success(drawers, p) for p in prisoners()):
            wins += 1
    return wins / trials * 100.0
