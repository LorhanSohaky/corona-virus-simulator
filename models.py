from mesa import Model
from mesa_geo import GeoSpace, GeoAgent, AgentCreator

class State(GeoAgent):
    def __init__(self, unique_id, model, shape):
        super().__init__(unique_id, model, shape)

class GeoModel(Model):
    def __init__(self):
        self.grid = GeoSpace()
        
        state_agent_kwargs = dict(model=self)
        AC = AgentCreator(agent_class=State, agent_kwargs=state_agent_kwargs)
        agents = AC.from_file('custom.geo.json',unique_id="labelrank")
        self.grid.add_agents(agents)