from app.model import *
import random
import statistics

def run_model():
    all_states = []
    for j in range(100):
        model = WorldModel(46)
        for i in range(40):
            model.step()
            for agent in model.schedule.agents:
                all_states.append((i, agent.nation_name, agent.state))
    return all_states

# wellbeing_list=[]
# wb_list_2 = []
# for i in all_states:
#     wellbeing_list.append(i[2])
#     for j in wellbeing_list:
#         wb_list_2.append(j)
#     print(max(wb_list_2) - min(wb_list_2))