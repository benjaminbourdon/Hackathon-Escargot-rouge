from collections import defaultdict


class Escargot:
    # TAILLE_MAX = 32

    # possible = ["Up", "Right", "Left", "Down"]
    dir = {"Up": (1, 0), "Right": (0, 1), "Left": (0, -1), "Down": (-1, 0)}
    opp_dir = {"Up": "Down", "Right": "Left", "Down": "Up", "Left": "Right"}
    # already_explore = defaultdict(default_factory=defaultdict(default_factory=False))
    already_explore = [[False] * 70 for _ in range(70)]
    position = [35, 35]
    chemin = []
    to_explore = [[None] * 70 for _ in range(70)]
    last_dir = ""

    def move(self, directions):
        x, y = rouge.position

        if rouge.already_explore[x][y] == False:
            for direction in directions:
                if len(self.chemin)==0 or (len(self.chemin)>0 and direction != self.opp_dir[self.chemin[-1]]):
                    modif_x, modif_y = self.dir[direction]
                    if rouge.already_explore[x + modif_x][y + modif_y] == False:
                        if self.to_explore[x][y] is None:
                            self.to_explore[x][y] = []
                        self.to_explore[x][y].append(direction)

            rouge.already_explore[x][y] = True
        else:
            self.to_explore[x][y].remove(self.opp_dir[self.last_dir])

        if self.to_explore[x][y]:
            choosen_dir = self.to_explore[x][y][0]
            self.chemin.append(choosen_dir)
        else:
            last_dir = self.chemin.pop()
            choosen_dir = self.opp_dir[last_dir]

        modif_x, modif_y = self.dir[choosen_dir]
        self.position = [x + modif_x, y + modif_y]

        self.last_dir = choosen_dir
        return choosen_dir


rouge = Escargot()


def move(directions):
    return rouge.move(directions)


if __name__ == "__main__":
    list = []
    for i in range(30):
        list.append(move(["Up"]))
    list.append(move(["Down", "Right", "Left"]))
    list.append(move(["Left"]))
    list.append(move(["Down", "Right", "Left"]))
    print()
