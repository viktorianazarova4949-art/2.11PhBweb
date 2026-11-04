
class SoftAssert:
    def __init__(self) -> None:
        self._errors: list[str] = []

    def assert_true(self, condition: bool, message: str) -> None:
        if not condition:
            self._errors.append(message)

    def assert_all(self) -> None:
        if self._errors:
            raise AssertionError("Soft assertion failures:\n - " + "\n - ".join(self._errors))


def get_property():
    return None