class SimpleReflexVacuumAgent:
    def _init_(self):
        self.location = [1, 1]  
        self.world = [[0, 0], [0, 0]]  

    def move_right(self):
        if self.location == [1, 1]:
            self.location = [1, 2]
        elif self.location == [1, 2]:
            self.location = [1, 1]
        else:
            raise ValueError("Invalid location")

    def move_down(self):
        if self.location == [1, 1]:
            self.location = [2, 1]
        elif self.location == [2, 1]:
            self.location = [1, 1]
        else:
            raise ValueError("Invalid location")

    def update_world(self, row, col, value):
        self.world[row-1][col-1] = value

    def act(self):
        if self.location == [1, 1]:
            if self.world[0][0] == 1:  
                self.update_world(1, 1, 0)  
                return "Cleaned"
            else:
                self.move_right()
                return "Moved right"
        elif self.location == [1, 2]:
            if self.world[0][1] == 1:  
                self.update_world(1, 2, 0)  
                return "Cleaned"
            else:
                self.move_down()
                return "Moved down"
        elif self.location == [2, 1]:
            if self.world[1][0] == 1:  
                self.update_world(2, 1, 0) 
                return "Cleaned"
            else:
                self.move_right()
                return "Moved right"
        else:
            raise ValueError("Invalid location")


agent = SimpleReflexVacuumAgent()
agent.update_world(1, 1, 1)  
print(agent.act()) 
print(agent.world)  
