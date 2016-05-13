class Map:
    
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise Exception('bad size');
        self.width = width;
        self.height = height;
   
    def onMap(self, mower):
        return (mower.x >= 0 and mower.x <= self.width and mower.y >= 0 and mower.y <= self.height);

