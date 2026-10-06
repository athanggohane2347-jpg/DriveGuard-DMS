from collections import deque


class FatigueTrend:
    def __init__(self, maxlen: int = 120) -> None:
        self.values: deque[float] = deque(maxlen=maxlen)

    def add(self, fatigue_score: float) -> str:
        self.values.append(fatigue_score)
        if len(self.values) < 10:
            return "STABLE"
        early = sum(list(self.values)[:5]) / 5
        late = sum(list(self.values)[-5:]) / 5
        if late - early > 12:
            return "INCREASING"
        if early - late > 12:
            return "DECREASING"
        return "STABLE"
