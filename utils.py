def singleton(cls):
    _instances = {}

    def inner():
        if cls not in _instances:
            _instances[cls] = cls()
        return _instances[cls]
    return inner