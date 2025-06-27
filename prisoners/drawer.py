import random
from typing import List

DRAWER_COUNT = 100 # 서랍/죄수 수
OPEN_LIMIT = DRAWER_COUNT // 2 # 50

def shuffled_drawers() -> List[int]:
    """0‥99 숫자를 무작위로 섞은 서랍 상태를 반환."""
    lst = list(range(DRAWER_COUNT))
    random.shuffle(lst)
    return lst

def prisoners() -> range:
    """죄수 번호(0‥99)를 순회하는 range 객체."""
    return range(DRAWER_COUNT)
