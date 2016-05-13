class Mower:
    
    cardinalLetter = ['N', 'E', 'S', 'W'];
    cardinalVector = {
        'N': { 'x':  0, 'y':  1 },
        'E': { 'x':  1, 'y':  0 },
        'S': { 'x':  0, 'y': -1 },
        'W': { 'x': -1, 'y':  0 }
    };
    
    def __init__(self, x, y, direction):
        self.x = x;
        self.y = y;
        if self.x < 0 or self.y < 0:
            raise Exception('mower bad initial position')
        try:
            self.direction = Mower.cardinalLetter.index(direction);
        except:
            raise Exception('mower bad letter direction');
        
    def walk(self):
        vector = self.getDirectionVector();
        self.x += vector['x'];
        self.y += vector['y'];
        
    
    def back(self):
        vector = self.getDirectionVector();
        self.x -= vector['x'];
        self.y -= vector['y'];
    
    def left(self):
        self.direction = (self.direction - 1) % 4;
    
    def right(self):
        self.direction = (self.direction + 1) % 4;
        
    def getDirectionLetter(self):
        return Mower.cardinalLetter[self.direction];
    
    def getDirectionVector(self):
        return Mower.cardinalVector[self.getDirectionLetter()];
