from mesa_geo.visualization.ModularVisualization import ModularServer
from mesa_geo.visualization.MapModule import MapModule

from models import GeoModel


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
                       "Coronavirus simulator")

server.port = 8521 # The default
server.launch()
profile.run(server.launch())
