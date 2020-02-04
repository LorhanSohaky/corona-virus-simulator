from models import *
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

def agent_portrayal(agent):
    portrayal = {
      "Shape": "circle",
      "Color": "red" if agent.infected else "blue",
      "Filled": "true",
      "Layer": 0,
      "infected":agent.infected,
      "r": 0.5
    }

    return portrayal

grid = CanvasGrid(agent_portrayal, 5, 5, 500, 500)

server = ModularServer(HumanModel,
                       [grid],
                       "Human Model",
                       {"N":3, "width":5, "height":5})

server.port = 8521 # The default
server.launch()
