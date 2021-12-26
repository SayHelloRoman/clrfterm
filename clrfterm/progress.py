from sys import stdout


JUMP_LEFT_SEQ = '\u001b[100D'
TEMPLATE = "|{}{}| {}/{}"


class Bar:
    def __init__(self, number_iterations: int) -> None:
        self.number_iterations = number_iterations
        self.i = 1

    def next(self) -> None:
        stdout.write(
            JUMP_LEFT_SEQ + TEMPLATE.format(
                "█" * self.i,
                " " * (self.number_iterations - self.i),
                self.i,
                self.number_iterations
            )
        )
        stdout.flush()
        self.i += 1
