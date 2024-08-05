class Deck:
    def __init__(self, row: int, column: int, is_alive: bool = True) -> None:
        self.row = row
        self.column = column
        self.is_alive = is_alive


class Ship:
    def __init__(
            self,
            start: tuple,
            end: tuple,
            is_drowned: bool = False
    ) -> None:
        self.start = start
        self.end = end
        self.is_drowned = is_drowned

        if start[0] == end[0]:
            self.decks = [
                Deck(start[0], index)
                for index in range(start[1], end[1] + 1)]
        else:
            self.decks = [
                Deck(j, start[1])
                for j in range(start[0], end[0] + 1)
            ]

    def get_deck(self, row: int, column: int) -> Deck | None:
        for index in self.decks:
            if index.column == column and index.row == row:
                return index
        return

    def fire(self, row: int, column: int) -> None:
        is_any_alive = False
        got_hit = False
        for index in self.decks:
            if index.column == column and index.row == row:
                index.is_alive = False
                got_hit = True
        for deck in self.decks:
            if deck.is_alive is True:
                is_any_alive = True
        if got_hit and not is_any_alive:
            self.is_drowned = True


class Battleship:
    def __init__(self, ships: list[tuple]) -> None:
        self.ships = ships
        self.field = {}

        for index in range(len(ships)):
            ship = Ship(self.ships[index][0], self.ships[index][1])
            for index in range(len(ship.decks)):
                self.field[ship.decks[index]] = ship

    def fire(self, location: tuple) -> str:
        keys = [(key.row, key.column) for key in self.field.keys()]
        if location not in keys:
            return "Miss!"
        for index, value in self.field.items():
            if location[0] == index.row and location[1] == index.column:
                value.fire(index.row, index.column)
                if value.is_drowned is True:
                    return "Sunk!"
                return "Hit!"
