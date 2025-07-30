class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: float | "Distance") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        return self

    def __mul__(self, multiplier: float) -> "Distance":
        return Distance(self.km * multiplier)

    def __truediv__(self, other: float | "Distance") -> "Distance":
        if isinstance(other, Distance):
            return Distance(round(self.km / other.km, 2))
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return False

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __lt__(self, other: "Distance") -> bool:
        return self.km < other.km

    def __le__(self, other: "Distance") -> bool:
        return self.km <= other.km

    def __gt__(self, other: "Distance") -> bool:
        return self.km > other.km

    def __ge__(self, other: "Distance") -> bool:
        return self.km >= other.km
