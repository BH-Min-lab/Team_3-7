import argparse, time
from random_strategy import play_random
from optimal_runner import play_optimal

def main():
    ap = argparse.ArgumentParser(description="100 Prisoners simulation")
    ap.add_argument("-n", "--trials", type=int, default=100_000,
    help="시뮬레이션 반복 횟수 (default: 100 000)")
    args = ap.parse_args()

    for label, fn in [("Random", play_random), ("Optimal", play_optimal)]:
        t0 = time.perf_counter()
        pct = fn(args.trials)
        dt  = time.perf_counter() - t0
        print(f"{label:7}: {pct:5.2f}%  (elapsed {dt:.2f}s)")

if __name__ == "__main__":
    main()
