from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from mesa.space import MultiGrid

class HumanAgent(Agent):
    def __init__(self, unique_id, model, infected):
        super().__init__(unique_id, model)
        self.infected = infected

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def infect(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = self.random.choice(cellmates)
            other.infected = True

    def step(self):
        self.move()
        if self.infected:
            self.infect()

class HumanModel(Model):
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True

        # Create a infected agent
        infectedHuman = HumanAgent(0, self, True)
        self.schedule.add(infectedHuman)
        x = 3
        y = 3
        self.grid.place_agent(infectedHuman, (x, y))

        for i in range(1,self.num_agents):
            a = HumanAgent(i, self, False)
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

    def step(self):
        self.schedule.step()
