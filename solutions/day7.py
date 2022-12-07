from typing import List, Dict
from collections import defaultdict


def dir_size(data: List[str]) -> Dict[str, int]:
    cwd: List[str] = []
    sizes: Dict[str, int] = defaultdict(lambda: 0)

    for cmd in data:
        if cmd.startswith("$ cd "):
            _cwd = cmd.removeprefix("$ cd").strip()
            if _cwd == "..":
                cwd.pop()
            else:
                abs_path = _cwd if len(cwd) < 1 else cwd[-1] + "/" + _cwd
                cwd.append(abs_path)
        elif not cmd.startswith("$ ls") and not cmd.startswith("dir"):
            size = int(cmd.split(" ")[0])
            for d in cwd:
                sizes[d] += size
    return sizes


def day7_a(data: List[str]):
    sizes = dir_size(data=data)
    return sum([d for d in sizes.values() if d <= 100_000])


def day7_b(data: List[str]) -> int:
    sizes = dir_size(data=data)
    used_space = sizes["/"]
    unused_space = 70000000 - used_space
    required_space = 30000000 - unused_space
    deleted_bytes = 0

    for key, value in sizes.items():
        if value >= required_space and (value < deleted_bytes or deleted_bytes == 0):
            deleted_bytes = value

    return deleted_bytes
