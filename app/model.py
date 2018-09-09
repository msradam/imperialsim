# model.py
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
import random

class CountryAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = 1
        secure_random = random.SystemRandom()
        self.nation_name = random.choice(['US','CV','PT','IN','BR','MY','IR','PE','GY','GB','CO','EC','SL','AU','HT','ZA','EG','RS','LR','GR','DZ','AF','CN','DE','DO','BG','FR','CG','MZ','ZW','JP','SN','ET','BJ','TZ','MA','PR','CU','PH','BD','TD','SA','PG','SY','TR','RU'])

    def step(self):
        # The agent's step will go here.
        if self.state == 0:
            return  
        other_agent = random.choice(self.model.schedule.agents)
        if decision(10/37):
            other_agent.state -= 0
        else:
           other_agent.state -= 1
        
        if decision(10/37):
            self.state -=1
        else:
            self.state +=1
        

class WorldModel(Model):
    """A model with some number of agents."""
    def __init__(self, N):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = CountryAgent(i, self)
            self.schedule.add(a)

        self.datacollector = DataCollector(
            agent_reporters = {"States:": lambda a : (a.nation_name, a.state)})
    
    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()
        self.datacollector.collect(self)


def decision(probability):
    ''' Given a probability p, P(True) = p, 
    P(False) = 1-p '''
    return random.random() < probability
