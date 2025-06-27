from prisoners.drawer import OPEN_LIMIT, DRAWER_COUNT

def cycle_success(drawers: list[int], prisoner: int) -> bool:
    """
    최적 전략: 자기 번호 → 카드 → 인덱스 … 사이클을 따라가며
    50번 안에 자기 번호 카드를 찾으면 True.
    """
    idx = prisoner
    for _ in range(OPEN_LIMIT):
        card = drawers[idx]
        if card == prisoner:
            return True
        idx = card
    return False

