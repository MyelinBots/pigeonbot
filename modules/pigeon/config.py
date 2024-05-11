class Config:
    def __init__(self, **kwargs):
        self._interval = int(kwargs.get("interval", 5))

    def interval(self) -> int:
        return self._interval
