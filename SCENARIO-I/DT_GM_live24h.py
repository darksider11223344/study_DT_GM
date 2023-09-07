import traci
import time

sumoCmd = ["sumo-gui", "-c", "DT_GM_live24h.sumocfg"]

traci.start(sumoCmd)
step = 0

while(traci.simulation.getMinExpectedNumber() > 0):
    traci.simulationStep()
    print(step)

    step+=1
    time.sleep(0.1)

traci.close()