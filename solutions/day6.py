from more_itertools import windowed


def day6(data: str, window_size: int = 4) -> int:
    count = window_size
    for window in windowed(data, count):
        if len(set(window)) == len(window):
            return count
        count += 1
