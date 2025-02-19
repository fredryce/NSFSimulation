import traci
import traci.constants as tc
from settings import Settings
import os
from random import choice

#sumo_path = os.path.join(Settings.default, Settings.sumo_config)


traci.start(["sumo", "-c", Settings.sumo_config]) 

'''
junctionID_list = traci.junction.getIDList()

junctionID = choice(junctionID_list)

traci.junction.subscribeContext(junctionID, tc.CMD_GET_VEHICLE_VARIABLE, 42, [tc.VAR_SPEED])



stepLength = traci.simulation.getDeltaT() 
while True:
	traci.simulationStep()
	scResults = traci.junction.getContextSubscriptionResults(junctionID)
	if scResults:
		for d in scResults.values():
			print(d[tc.VAR_SPEED])
		break
	junctionID = choice(junctionID_list)
	print('testing junction ', junctionID)
'''

'''
print(traci.junction.getContextSubscriptionResults(junctionID))
for step in range(3):
   print("step", step)
   traci.simulationStep()
   print(traci.junction.getContextSubscriptionResults(junctionID))
traci.close()

'''
print('len is ', len(traci.vehicle.getIDList()))
print(type(traci.vehicle.getIDList()))
'''
while True: 
    for veh_id in traci.simulation.getDepartedIDList():
    	traci.vehicle.subscribe(veh_id, [traci.constants.VAR_POSITION])
    positions = traci.vehicle.getAllSubscriptionResults()
    traci.simulationStep()
    if positions:
    	print(positions)
'''
traci.close()