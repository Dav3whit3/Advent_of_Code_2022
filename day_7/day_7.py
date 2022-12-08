from utils import Input
from functools import reduce


class FileSystem:

    def __init__(self) -> None:
        self.tree = {"/": {"size": 0}, "small_dirs": []}
        self.parent = "/"
        self.current = "/"
        self.path = "/"

    def get_path_value(self, dictionary: dict, path: list[str]):
        return reduce(lambda dic, key: dic[key], path, dictionary)

    def set_path_value(self, d: dict, path: list[str], key: str, value: str | int | dict):
        d = self.get_path_value(d, path[:-1])
        d[path[-1]][key] = value

    def update_path_size(self, path: str, size: int, tree: dict):
        for index, _ in enumerate(path, start=1):
            node_path = path[0: index]
            dir_size = self.get_path_value(tree, list(node_path))["size"]
            self.set_path_value(tree, list(node_path), "size", dir_size + size)

            if dir_size + size >= 100000:
                tree["small_dirs"] = [*filter(lambda dir: dir != node_path, tree["small_dirs"])]

    def move(self, path: str, new_directoy: str, out: bool = False):
        new_path = path[:-1] if out else f"{path}{new_directoy}"
        try:
            parent = path[-2]
        except:
            parent = path[-1]

        return new_path, path[-1], parent

    def solve_part_1(self, data: list[str]):

        for cmd in data[1:]:

            # commands
            if cmd.startswith("$ cd "):

                new_directoy = cmd.split("$ cd ")[1]

                if new_directoy == "..":
                    self.path, self.current, self.parent = self.move(self.path, new_directoy, out=True)

                else:
                    self.path, self.current, self.parent = self.move(self.path, new_directoy)

                self.tree["small_dirs"].append(self.current)

            # dir info
            else:
                if cmd.startswith("dir"):
                    dir = cmd.split("dir ")[1]
                    self.set_path_value(self.tree, list(self.path), dir, {"size": 0})

                else:
                    file, size = cmd.split(" ")[1], cmd.split(" ")[0]
                    self.set_path_value(self. tree, list(self.path), file, size)
                    self.update_path_size(self.path, int(size), self.tree)

        print(set(self.tree["small_dirs"]))

#### main ####
if __name__ == "__main__":
    input = Input(day=7).get_list(split_by="\n")
    input = ['$ cd /',
            '$ ls',
            'dir a',
            '14848514 b.txt',
            '8504156 c.dat',
            'dir d',
            '$ cd a',
            '$ ls',
            'dir e',
            '29116 f',
            '2557 g',
            '62596 h.lst',
            '$ cd e',
            '$ ls',
            '584 i',
            '$ cd ..',
            '$ cd ..',
            '$ cd d',
            '$ ls',
            '4060174 j',
            '8033020 d.log',
            '5626152 d.ext',
            '7214296 k']
    input = [*filter(lambda cmd: "$ ls" not in cmd, input)]

    fs = FileSystem()
    fs.solve_part_1(input)