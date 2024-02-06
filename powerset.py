'''modules installed'''
import time as t
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
from matplotlib import pyplot as plt
import ece6397_pasunuri_helper_headerfooter as h
ca1=h.Header("Aravind Reddy","Pasunuri","Assignment 8","Air Conditioner Controller")
for i in range(2):
    ca1.horizontal_line()
ca1.student_name()
ca1.ca_name()
ca1.horizontal_line()
ca1.description()
Start_time=t.time()
print("START RUN")
ca1.horizontal_line()
#set the input variables
outside_temperature_input= int(input("enter the outside temperature"))
room_humidity_input=int(input("enter the room humidity"))
room_occupancy_input=int(input("enter the room_occupancy"))
temperature_desired=input("enter the desired_temperature")



# Define input variables
room_occupancy=ctrl.Antecedent(np.arange(0, 101, 1), 'Occupancy')
room_occupancy.view()
room_humidity=ctrl.Antecedent(np.arange(0, 101, 1), 'Humidity')
outside_temperature=ctrl.Antecedent(np.arange(0, 101, 1), 'Outside Temperature')
error_temperature= ctrl.Antecedent(np.arange(0,101,1), 'Error')
# Define output variable
ac_power = ctrl.Consequent(np.arange(0, 101, 1), 'AC Power Consumption')

# Define membership functions for input variables
room_occupancy['low'] = fuzz.trimf(room_occupancy.universe, [0, 0, 50])
room_occupancy['medium'] = fuzz.trimf(room_occupancy.universe, [0, 50, 100])
room_occupancy['high'] = fuzz.trimf(room_occupancy.universe, [50, 100, 100])

room_humidity['low'] = fuzz.trimf(room_humidity.universe, [0, 0, 50])
room_humidity['medium'] = fuzz.trimf(room_humidity.universe, [0, 50, 100])
room_humidity['high'] = fuzz.trimf(room_humidity.universe, [50, 100, 100])

outside_temperature['cold'] = fuzz.trimf(outside_temperature.universe, [0, 0, 60])
outside_temperature['moderate'] = fuzz.trimf(outside_temperature.universe, [60, 75, 85])
outside_temperature['hot'] = fuzz.trimf(outside_temperature.universe, [80, 100, 100])

error_temperature['low'] = fuzz.trimf(error_temperature.universe, [0, 0, 50])
error_temperature['moderate'] = fuzz.trimf(error_temperature.universe, [0, 50, 100])
error_temperature['high'] = fuzz.trimf(error_temperature.universe, [50, 100, 100])

fig, (ax0, ax1, ax2) = plt.subplots (nrows=3, figsize=(10, 8))
ax0.plot(np.arange(0, 101, 1), fuzz.trimf(outside_temperature.universe,
                                           [0, 0, 50]), 'b', linewidth=1.5, label='Cold')
ax0.plot(np.arange(0, 101, 1), fuzz.trimf(outside_temperature.universe,
                                           [30, 60, 70]), 'g', linewidth=1.5, label='Mild')
ax0.plot(np.arange(0, 101, 1), fuzz.trimf(outside_temperature.universe,
                                           [70, 100, 100]), 'r', linewidth=1.5, label='Hot')
ax0.set_title ('Membership Function of Outside Temperature')
ax0.set_xlabel('Outside Temperature')
ax0.set_ylabel('U_ot')
ax0.legend()


ax1.plot(np.arange(0, 101, 1), fuzz.trimf(room_humidity.universe, [0, 0, 50]),
          'b', linewidth=1.5, label='dry')
ax1.plot(np.arange(0, 101, 1), fuzz.trimf(room_humidity.universe, [0, 50, 100]),
          'g', linewidth=1.5, label='Normal')
ax1.plot(np.arange(0, 101, 1), fuzz.trimf(room_humidity.universe, [50, 100, 100]),
          'r', linewidth=1.5, label='Humid')
ax1.set_title ('Membership Function of Room Humidity')
ax1.set_xlabel('Room humidity percentage')
ax1.set_ylabel('U_rh')
ax1.legend()

ax2.plot(np.arange(0, 101, 1), fuzz.trimf(room_occupancy.universe, [0, 0, 50]),
          'b', linewidth=1.5, label='low')
ax2.plot(np.arange(0, 101, 1), fuzz.trimf(room_occupancy.universe, [0, 50, 100]),
          'g', linewidth=1.5, label='Medium')
ax2.plot(np.arange(0, 101, 1), fuzz.trimf(room_occupancy.universe, [50, 100, 100]),
          'r', linewidth=1.5, label='High')
ax2.set_title ('Membership Function of Room occupancy')
ax2.set_xlabel('Room occupancy ')
ax2.set_ylabel('U_ro')
ax2.legend()



# Define membership functions for output variable
ac_power['very low'] = fuzz.trimf(ac_power.universe, [0, 0, 25])
ac_power['low'] = fuzz.trimf(ac_power.universe, [0, 25, 40])
ac_power['low_medium'] = fuzz.trimf(ac_power.universe, [25, 40, 60])
ac_power['high_medium'] = fuzz.trimf(ac_power.universe, [40,70,75])
ac_power['high'] = fuzz.trimf(ac_power.universe, [70,80,90])
ac_power['very high'] = fuzz.trimf(ac_power.universe, [80,100,100])

ac_power_list=[]
temperature_list = []
sensor_list=[]
error_temperature_list=[]


# Define rules for the controller
rule1 = ctrl.Rule(room_occupancy['low'] & room_humidity['low'] & error_temperature['low']
                  , ac_power['very low'])
rule2 = ctrl.Rule(room_occupancy['low'] & room_humidity['low'] & error_temperature['moderate'] ,
                   ac_power['low_medium'])
rule3 = ctrl.Rule(room_occupancy['low'] & room_humidity['low'] & error_temperature['high'],
                   ac_power['high'])
rule4 = ctrl.Rule(room_occupancy['low'] & room_humidity['medium'] & error_temperature['low'],
                   ac_power['low'])
rule5 = ctrl.Rule(room_occupancy['low'] & room_humidity['medium'] & error_temperature['moderate'],
                   ac_power['low_medium'])
rule6 = ctrl.Rule(room_occupancy['low'] & room_humidity['medium'] & error_temperature['high'],
                   ac_power['high'])
rule7 = ctrl.Rule(room_occupancy['low'] & room_humidity['high'] & error_temperature['low'],
                   ac_power['low_medium'])
rule8 = ctrl.Rule(room_occupancy['low'] & room_humidity['high'] & error_temperature['moderate'],
                   ac_power['high_medium'])
rule9 = ctrl.Rule(room_occupancy['low'] & room_humidity['high'] & error_temperature['high'],
                   ac_power['high'])
rule10 = ctrl.Rule(room_occupancy['medium'] & room_humidity['low'] & error_temperature['low'] ,
                    ac_power['low'])
rule11 = ctrl.Rule(room_occupancy['medium'] & room_humidity['low'] & error_temperature['moderate'] ,
                    ac_power['low_medium'])
rule12= ctrl.Rule(room_occupancy['medium'] & room_humidity['low'] & error_temperature['high'],
                   ac_power['high'])
rule13= ctrl.Rule(room_occupancy['medium'] & room_humidity['medium'] & error_temperature['low'],
                   ac_power['low_medium'])
rule14= ctrl.Rule(room_occupancy['medium'] & room_humidity['medium'] &
                  error_temperature['moderate'],
                   ac_power['high_medium'])
rule15= ctrl.Rule(room_occupancy['medium'] & room_humidity['medium'] & error_temperature['high'],
                   ac_power['high'])
rule16= ctrl.Rule(room_occupancy['medium'] & room_humidity['high'] & error_temperature['low'],
                   ac_power['low_medium'])
rule17= ctrl.Rule(room_occupancy['medium'] & room_humidity['high'] & error_temperature['moderate'],
                   ac_power['high_medium'])
rule18= ctrl.Rule(room_occupancy['medium'] & room_humidity['high'] & error_temperature['high'],
                   ac_power['very high'])
rule19 = ctrl.Rule(room_occupancy['high'] & room_humidity['low'] & error_temperature['low'] ,
                    ac_power['high_medium'])
rule20 = ctrl.Rule(room_occupancy['high'] & room_humidity['low'] & error_temperature['moderate'] ,
                    ac_power['high'])
rule21= ctrl.Rule(room_occupancy['high'] & room_humidity['low'] & error_temperature['high'],
                   ac_power['very high'])
rule22= ctrl.Rule(room_occupancy['high'] & room_humidity['medium'] & error_temperature['low'],
                   ac_power['high_medium'])
rule23= ctrl.Rule(room_occupancy['high'] & room_humidity['medium'] & error_temperature['moderate'],
                   ac_power['high_medium'])
rule24= ctrl.Rule(room_occupancy['high'] & room_humidity['medium'] & error_temperature['high'],
                   ac_power['very high'])
rule25= ctrl.Rule(room_occupancy['high'] & room_humidity['high'] & error_temperature['low']
                  , ac_power['high_medium'])
rule26= ctrl.Rule(room_occupancy['high'] & room_humidity['high'] & error_temperature['moderate'],
                   ac_power['high'])
rule27= ctrl.Rule(room_occupancy['high'] & room_humidity['high'] & error_temperature['high'],
                   ac_power['very high'])


ac_controller = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5,
                                     rule6,rule7,rule8,rule9,rule10,
                                    rule11,rule12,rule13,rule14,rule15,rule16,
                                    rule17,rule18,rule19,rule20,rule21,
                                    rule22,rule23,rule24,rule25,rule26,rule27])
ac_simulator = ctrl.ControlSystemSimulation(ac_controller)

#for i in range(20):
    #if i==0:
        #error_temperature = temperature_desired - outside_temperature
    #else:
        #error_temperature = temperature_desired - ((1.58*y[i]+0.08*u[i])-(8.125*y[i]))
#help(ctrl.controlsystem.ControlSystemSimulation)
for i in range(20):
    if i==0:
        error_temperature_input = abs(int(temperature_desired))
        temperature_list.append(0.12*outside_temperature_input)
        sensor_list.append(0.12*outside_temperature_input)
        error_temperature_list.append(int(temperature_desired) - outside_temperature_input)
    else:
        temperature_list.append(1.58*float(temperature_list[i-1])+0.08*ac_power_list[i-1])
        sensor_list.append(0.12*temperature_list[i])
        #print(temperature_list[i],sensor_list[i])
        error_temperature_list.append(abs(float(temperature_desired) - (float(sensor_list[i]))))
        #print(error_temperature_list[i])
    ac_simulator.input['Humidity'] = int(room_humidity_input)
    ac_simulator.input['Occupancy'] = int(room_occupancy_input)
    #ac_simulator.input['Outside Temperature'] = int(outside_temperature_input)
    ac_simulator.input['Error'] = int(error_temperature_list[i])


    # Compute the output
    ac_simulator.compute()
    ac_power_list.append(float(ac_simulator.output['AC Power Consumption']))
    # Access the output variable
    ac_power_output = ac_simulator.output['AC Power Consumption']
    #print('AC Power Output:', ac_power_output)
#print(ac_power_list)
ac_power_list_ome=[]
ac_power_list_ome.append(ac_power_list[0])
for j in range(2,10):
    if ac_power_list[j]<ac_power_list[j-1]:
        ac_power_list_ome.append(ac_power_list[j])
    else:
        ac_power_list_ome.append(ac_power_list_ome[j-2]*0.5)

#print(error_temperature_list)
#print(ac_power_list_ome)
print("Sample K     ","desired temp     ","actual K     ","control effort")
LEN_K= len(ac_power_list_ome)
for k in range(LEN_K):
    print(str(k)+"              "+ str(temperature_desired)+"             "
          +str(sensor_list[k])+"       "+str(ac_power_list_ome[k]))

ca1.horizontal_line()
stop_time=t.time()
ca1=h.Footer((stop_time-Start_time))
ca1.run_time()
plt.show()
