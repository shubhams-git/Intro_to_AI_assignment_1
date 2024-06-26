import re

class FileReader:
    """
    Provides methods to read and parse configuration data from a file for a grid-based pathfinding simulation.
    """
    def __init__(self, filename):
        self.line = ""
        self.grid = ""
        self.agentpos = ""
        self.goal = ""
        self.walls = []
        self.filename = filename

    def read(self):
        """
        Reads the configuration from the file and stores grid size, agent position, goal position, and wall positions.
        """
        with open(self.filename, 'r') as file:
            lines = file.readlines()

        if len(lines) > 0:
            self.grid = lines[0].strip()
        if len(lines) > 1:
            self.agentpos = lines[1].strip()
        if len(lines) > 2:
            self.goal = lines[2].strip()
        if len(lines) > 3:
            self.walls = [line.strip() for line in lines[3:]]

    """
    Parses the text file.
    """

    def get_grid(self):
        return [int(value) for value in re.findall(r'\d+', self.grid)]

    def get_agent(self):
        return [int(value) for value in re.findall(r'\d+', self.agentpos)]

    def get_goal(self):
        return [int(value) for value in re.findall(r'\d+', self.goal)]

    def get_walls(self):
        wall_list = []
        for wall in self.walls:
            wall_list.append([int(value) for value in re.findall(r'\d+', wall)])
        return wall_list
