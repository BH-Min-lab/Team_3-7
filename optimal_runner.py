from prisoners.drawer import shuffled_drawers, prisoners
from prisoners.optimal_core import cycle_success

def play_optimal(trials: int = 100_000) -> float:
    """최적(사이클) 전략의 생존 확률(%)"""
    wins = 0
    for _ in range(trials):
        drawers = shuffled_drawers()
        if all(cycle_success(drawers, p) for p in prisoners()):
            wins += 1
    return wins / trials * 100.0

