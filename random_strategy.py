import random
from drawer import shuffled_drawers, prisoners, OPEN_LIMIT, DRAWER_COUNT

def random_success(drawers, prisoner):
#해당 죄수가 무작위 전략으로 성공했는지 반환.
    picks = random.sample(range(DRAWER_COUNT), OPEN_LIMIT)
    return any(drawers[idx] == prisoner for idx in picks)

def play_random(trials = 100_000):
#무작위 전략의 생존 확률(%)
    wins = 0
    for _ in range(trials):
        drawers = shuffled_drawers()
        if all(random_success(drawers, p) for p in prisoners()):
            wins += 1
    return wins / trials * 100.0
