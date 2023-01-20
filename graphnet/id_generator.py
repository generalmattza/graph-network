class IDGenerator:
    def __init__(self):
        self.last_id = -1

    def get_new_id(self) -> str:
        self.last_id += 1
        return str(self.last_id).zfill(4)


def test_IDGenerator():
    _ids = IDGenerator()
    for _ in range(10):
        print(_ids.get_new_id())


if __name__ == "__main__":
    test_IDGenerator()
