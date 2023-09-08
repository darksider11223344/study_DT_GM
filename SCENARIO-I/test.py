import traci
import time
import functions_DT_GM_live24h as fn

sumoCmd = ["sumo-gui", "-c", "DT_GM_live24h.sumocfg"]

hours = 24
run = 0
res_time = 1
step_length = 0.25

period_check_sim_speed = 10

while(run < hours):
    oldVehIDs_E_in = []

    oldVehIDs_out_E = []

    X_0224_03 = [0,0,0,0]
    X_0224_04 = [0,0,0,0]

    X_0272_01 = [0,0,0,0]
    X_0272_02 = [0,0,0,0]

    X_0200_04 = [0,0,0,0]
    X_0200_05 = [0,0,0,0]

    X_0224_01 = [0,0,0,0]
    X_0224_02 = [0,0,0,0]

    X_0200_06 = [0,0,0,0]

    X_0272_03 = [0,0,0,0]
    X_0272_04 = [0,0,0,0]

    X_0200_01 = [0,0,0,0]
    X_0200_02 = [0,0,0,0]
    X_0200_03 = [0,0,0,0]

    traci.start(sumoCmd)

    step = 0

    while(step <= hours * 3600 * (1 / step_length)):
    # while(traci.simulation.getMinExpectedNumber() > 0):
        traci.simulationStep()

        if step % (res_time * (1 / step_length)) == 0:
            print('1', step)
            #=======================
            # FLOW IN (measurements from SUMO)
            flow_E_in, speed_E_in, oldVehIDs_E_in, newVehIDs_E_in = \
            fn.edgeVehParameters('E_NS5', 'E_NS6', oldVehIDs_E_in)
            # print(flow_E_in, speed_E_in, oldVehIDs_E_in, newVehIDs_E_in)


            #================================
            # FLOW OUT (measurements from SUMO)
            flow_E, speed_E, oldVehIDs_out_E, newVehIDs_out_E =\
            fn.edgeVehParameters('SN_E5', 'SN_E6', oldVehIDs_out_E)
            # print(flow_E_in, speed_E_in, oldVehIDs_out_E, newVehIDs_out_E)


        if step % (period_check_sim_speed * (1 / step_length)) == 0 and step > 0:
            # print('2', step) ### 40, 80, 120
            pass


        if step % (60 * (1 / step_length)) == 0:
            print('--- 3', step)

            q1=X_0224_03[0]+X_0224_03[2]+X_0224_04[0]+X_0224_04[2]
            q3=X_0272_01[0]+X_0272_01[2]+X_0272_02[0]+X_0272_02[2]
            q5=X_0200_04[0]+X_0200_04[2]+X_0200_05[0]+X_0200_05[2]+X_0200_06[0]+X_0200_06[2]

            q2=X_0224_01[0]+X_0224_01[2]+X_0224_02[0]+X_0224_02[2]
            q4=X_0272_03[0]+X_0272_03[2]+X_0272_04[0]+X_0272_04[2]
            q6=X_0200_01[0]+X_0200_01[2]+X_0200_02[0]+X_0200_02[2]+X_0200_03[0]+X_0200_03[2]


        step += 1
        time.sleep(0.1)

    traci.close()
