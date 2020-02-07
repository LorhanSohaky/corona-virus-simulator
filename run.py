
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.modules import ChartModule
from mesa_geo.visualization.ModularVisualization import ModularServer
from mesa_geo.visualization.MapModule import MapModule

# def agent_portrayal(agent):
#     portrayal = {
#       "Shape": "circle",
#       "Color": "red" if agent.infected else "blue",
#       "Filled": "true",
#       "Layer": 0,
#       "infected":agent.infected,
#       "r": 0.5
#     }

#     return portrayal

# grid = CanvasGrid(agent_portrayal, 5, 5, 500, 500)

# server = ModularServer(HumanModel,
#                        [grid],
#                        "Human Model",
#                        {"N":3, "width":5, "height":5})

# server.port = 8521 # The default
# server.launch()

from mesa_geo import GeoSpace, GeoAgent, AgentCreator
from mesa import Model

class State(GeoAgent):
    def __init__(self, unique_id, model, shape):
        super().__init__(unique_id, model, shape)

class GeoModel(Model):
    def __init__(self):
        self.grid = GeoSpace()
        
        state_agent_kwargs = dict(model=self)
        AC = AgentCreator(agent_class=State, agent_kwargs=state_agent_kwargs)
        agent = AC.create_agent([26.11,43.97],1)
        ##agents = AC.from_file('countries-land-10km.geo.json',unique_id="A3")
        self.grid.add_agents(agent)

m = GeoModel()

agent = m.grid.agents[0]
print(agent.unique_id)

def schelling_draw(agent):
    """
    Portrayal Method for canvas
    """
    portrayal = dict()
    portrayal["color"] = "Red"
    return portrayal

import profile


map_element = MapModule(schelling_draw, [52, 12], 4, 500, 500)
server = ModularServer(GeoModel,
                       [map_element],
                       "Human Model")

server.port = 8521 # The default
server.launch()
profile.run(server.launch())
