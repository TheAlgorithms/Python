import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

#wash time depend on amount of dirt and grease
dirt = ctrl.Antecedent(np.arange(0, 100, 1), 'dirt') #scale
grease = ctrl.Antecedent(np.arange(0, 100, 1), 'grease') #scale
wash_time = ctrl.Consequent(np.arange(0, 60, 1), 'wash_time') #minutes
wash_time.defuzzify_method = 'mom'

#membership functions
dirt['ld'] = fuzz.trimf(dirt.universe, [0, 0, 50])
dirt['md'] = fuzz.trimf(dirt.universe, [0, 50, 100])
dirt['hd'] = fuzz.trimf(dirt.universe, [50, 100, 100])

grease['lg'] = fuzz.trimf(grease.universe, [0, 0, 50])
grease['mg'] = fuzz.trimf(grease.universe, [0, 50, 100])
grease['hg'] = fuzz.trimf(grease.universe, [50, 100, 100])

wash_time['vl'] = fuzz.trimf(wash_time.universe, [0, 0, 10])
wash_time['l']  = fuzz.trimf(wash_time.universe, [0, 10, 25])
wash_time['m']  = fuzz.trimf(wash_time.universe, [10, 25, 40])
wash_time['h']  = fuzz.trimf(wash_time.universe, [25, 40, 60])
wash_time['vh'] = fuzz.trimf(wash_time.universe, [40, 60, 60])

#Rules
r1 = ctrl.Rule(dirt['ld'] & grease['lg'], wash_time['vl'])
r2 = ctrl.Rule(dirt['ld'] & grease['mg'], wash_time['m'])
r3 = ctrl.Rule(dirt['ld'] & grease['hg'], wash_time['h'])
r4 = ctrl.Rule(dirt['md'] & grease['lg'], wash_time['l'])
r5 = ctrl.Rule(dirt['md'] & grease['mg'], wash_time['m'])
r6 = ctrl.Rule(dirt['md'] & grease['hg'], wash_time['vh'])
r7 = ctrl.Rule(dirt['hd'] & grease['lg'], wash_time['m'])
r8 = ctrl.Rule(dirt['hd'] & grease['mg'], wash_time['h'])
r9 = ctrl.Rule(dirt['hd'] & grease['hg'], wash_time['vh'])

wash_ctrl = ctrl.ControlSystem([r1, r2, r3, r4, r5, r6, r7, r8, r9])
machine = ctrl.ControlSystemSimulation(wash_ctrl)

machine.input['dirt'], machine.input['grease'] = 80, 90
machine.compute()
print('Wash time: ', machine.output['wash_time'])

dirt.view()
grease.view()
wash_time.view(sim=machine)