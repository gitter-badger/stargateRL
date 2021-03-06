class Tile:
    ''' Basic tile representation. '''
    def __init__(self, x, y, symbol, tags=[]):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.tags = tags
        self.entity = None

        # TODO: Create a basic list of tags and coresponding graphx

    def __repr__(self):
        return '''Tile(Position:({:3},{:3}),Symbol:{},{})\
               '''.format(self.x, self.y, self.symbol, self.entity)


class Map:
    ''' A set of tiles with helper methods. '''
    def __init__(self, size_x=0, size_y=0, tiles=[]):
        self.size_x = size_x
        self.size_y = size_y
        self.tiles = tiles

    def __repr__(self):
        _string = ''
        for col in self.tiles:
            for tile in col:
                _string += '\n' + str(tile)

        return 'Map(Size:({},{}),Tiles:({}))'.format(self.size_x,
                                                     self.size_y,
                                                     _string+'\n')

    def load(self, file_path, mode=0):
        with open(file_path, 'r') as file_map:
            if mode == 0:
                self.size_x = 0
                self.size_y = 0

                lines = file_map.readlines()
                for line in lines:
                    self.size_y += 1
                for char in line.strip('\n'):
                    self.size_x += 1
                self.tiles = [[None for _ in range(self.size_x)]
                              for _ in range(self.size_y)]

                for y, line in enumerate(reversed(lines)):
                    for x, char in enumerate(line):
                        if char != '\n':
                            self.set_tile(Tile(x, y, char,
                                               TAGS[char]))

    def get_tile(self, x, y):
        return self.tiles[y][x]

    def set_tile(self, tile):
        self.tiles[tile.y][tile.x] = tile

    def get_all(self):
        _tiles = []
        for row in self.tiles:
            for tile in row:
                _tiles.append(tile)
        return _tiles

    def check_tile(self, player_position, direction):
        if 'walkable' in self.get_tile(player_position[0] + direction[0],
                                       player_position[1] + direction[1]).tags:
            if self.get_tile(
                 player_position[0] + direction[0],
                 player_position[1] + direction[1]).entity is None:
                return True
            else:
                return False
        else:
            return False

    def display(self):
        for row in reversed(self.tiles):
            for tile in row:
                print tile.symbol,
            print

TAGS = {'#': [],
        '.': ['walkable'],
        ')': ['walkable'],
        ']': []}
