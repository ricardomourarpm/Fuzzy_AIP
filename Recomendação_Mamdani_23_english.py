# -*- coding: utf-8 -*-
"""
Created on Fri May  7 12:47:36 2021

@author: user
"""

from os import name
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Input characteristics - variables
# Variable efficiency (%)
efficiency = ctrl.Antecedent(np.arange(0, 101, 1), 'Efficiency')

efficiency['Very Poor'] = fuzz.gauss2mf(efficiency.universe, 0, 8, 8, 8)
efficiency['Poor'] = fuzz.gauss2mf(efficiency.universe, 27, 8, 42, 8)
efficiency['Good'] = fuzz.gauss2mf(efficiency.universe, 60, 7, 73, 7)
efficiency['Very Good'] = fuzz.gauss2mf(efficiency.universe, 90, 7, 100, 7)

#efficiency.view()

# Input characteristics - variables
# Variable power
power = ctrl.Antecedent(np.arange(0, 10, 0.1), 'Power')

power['Very Poor'] = fuzz.gauss2mf(power.universe, 0, 0.8, 0.8, 0.8)
power['Poor'] = fuzz.gauss2mf(power.universe, 2.7, 0.8, 4.2, 0.8)
power['Good'] = fuzz.gauss2mf(power.universe, 6.0, 0.7, 7.3, 0.7)
power['Very Good'] = fuzz.gauss2mf(power.universe, 9.0, 0.7, 10, 0.7)

#power.view()

# Input characteristics - variables
# Variable acoustic_signature
acoustic_signature = ctrl.Antecedent(np.arange(0, 10, 0.1), 'Acoustic Signature')

acoustic_signature['Very Low'] = fuzz.gauss2mf(acoustic_signature.universe, 0, 0.8, 0.8, 0.8)
acoustic_signature['Low'] = fuzz.gauss2mf(acoustic_signature.universe, 2.7, 0.8, 4.2, 0.8)
acoustic_signature['High'] = fuzz.gauss2mf(acoustic_signature.universe, 6.0, 0.7, 7.3, 0.7)
acoustic_signature['Very High'] = fuzz.gauss2mf(acoustic_signature.universe, 9.0, 0.7, 10, 0.7)

#acoustic_signature.view()

# Input characteristics - variables
# Variable acquisition_cost
acquisition_cost = ctrl.Antecedent(np.arange(0, 10, 0.1), 'Acquisition Cost')

acquisition_cost['Very Low'] = fuzz.gauss2mf(acquisition_cost.universe, 0, 0.8, 0.8, 0.8)
acquisition_cost['Low'] = fuzz.gauss2mf(acquisition_cost.universe, 2.7, 0.8, 4.2, 0.8)
acquisition_cost['High'] = fuzz.gauss2mf(acquisition_cost.universe, 6.0, 0.7, 7.3, 0.7)
acquisition_cost['Very High'] = fuzz.gauss2mf(acquisition_cost.universe, 9.0, 0.7, 10, 0.7)

#acquisition_cost.view()

# Input characteristics - variables
# Variable maintenance_cost
maintenance_cost = ctrl.Antecedent(np.arange(0, 10, 0.1), 'Maintenance Cost')

maintenance_cost['Very Low'] = fuzz.gauss2mf(maintenance_cost.universe, 0, 0.8, 0.8, 0.8)
maintenance_cost['Low'] = fuzz.gauss2mf(maintenance_cost.universe, 2.7, 0.8, 4.2, 0.8)
maintenance_cost['High'] = fuzz.gauss2mf(maintenance_cost.universe, 6.0, 0.7, 7.3, 0.7)
maintenance_cost['Very High'] = fuzz.gauss2mf(maintenance_cost.universe, 9.0, 0.7, 10, 0.7)

#maintenance_cost.view()

# Input characteristics - variables
# Variable operation_cost
operation_cost = ctrl.Antecedent(np.arange(0, 10, 0.1), 'Operation Cost')

operation_cost['Very Low'] = fuzz.gauss2mf(operation_cost.universe, 0, 0.8, 0.8, 0.8)
operation_cost['Low'] = fuzz.gauss2mf(operation_cost.universe, 2.7, 0.8, 4.2, 0.8)
operation_cost['High'] = fuzz.gauss2mf(operation_cost.universe, 6.0, 0.7, 7.3, 0.7)
operation_cost['Very High'] = fuzz.gauss2mf(operation_cost.universe, 9.0, 0.7, 10, 0.7)

#operation_cost.view()

# Input characteristics - variables
# Variable thermal_emission
thermal_emission = ctrl.Antecedent(np.arange(0, 900, 1), 'Thermal Emission')

thermal_emission['Very Low'] = fuzz.gauss2mf(thermal_emission.universe, 0, 80, 60, 80)
thermal_emission['Low'] = fuzz.gauss2mf(thermal_emission.universe, 250, 80, 350, 80)
thermal_emission['High'] = fuzz.gauss2mf(thermal_emission.universe, 530, 70, 630, 70)
thermal_emission['Very High'] = fuzz.gauss2mf(thermal_emission.universe, 800, 70, 900, 70)

#thermal_emission.view()

# Input characteristics - variables
# Variable byproduct
byproduct = ctrl.Antecedent(np.arange(0, 10, 0.1), 'Byproduct')

byproduct['Low Pollutant'] = fuzz.gauss2mf(byproduct.universe, 0, 0.8, 0.8, 0.8)
byproduct['Pollutant'] = fuzz.gauss2mf(byproduct.universe, 2.7, 0.8, 4.2, 0.8)
byproduct['Highly Pollutant'] = fuzz.gauss2mf(byproduct.universe, 6.0, 0.7, 7.3, 0.7)
byproduct['Extremely Pollutant'] = fuzz.gauss2mf(byproduct.universe, 9.0, 0.7, 10, 0.7)

#byproduct.view()

# Input characteristics - variables
# Variable size
size = ctrl.Antecedent(np.arange(0, 10, 0.1), 'Size')

size['Very Low'] = fuzz.gauss2mf(size.universe, 0, 0.8, 0.8, 0.8)
size['Low'] = fuzz.gauss2mf(size.universe, 2.7, 0.8, 4.2, 0.8)
size['High'] = fuzz.gauss2mf(size.universe, 6.0, 0.7, 7.3, 0.7)
size['Very High'] = fuzz.gauss2mf(size.universe, 9.0, 0.7, 10, 0.7)

#size.view()

# Creation of subcategories for consequence

# Subcategory - Operational Dimension

operational_dimension = ctrl.Consequent(np.arange(0, 101, 1), 'Operational Dimension')

operational_dimension['Low'] = fuzz.gauss2mf(operational_dimension.universe, 0, 10, 15, 10)
operational_dimension['Medium'] = fuzz.gauss2mf(operational_dimension.universe, 38, 8, 62, 8)
operational_dimension['High'] = fuzz.gauss2mf(operational_dimension.universe, 85, 10, 100, 10)

#operational_dimension.view()

# Subcategory - Economic Dimension

economic_dimension = ctrl.Consequent(np.arange(0, 101, 1), 'Economic Dimension')

economic_dimension['Low'] = fuzz.gauss2mf(economic_dimension.universe, 0, 10, 15, 10)
economic_dimension['Medium'] = fuzz.gauss2mf(economic_dimension.universe, 38, 8, 62, 8)
economic_dimension['High'] = fuzz.gauss2mf(economic_dimension.universe, 85, 10, 100, 10)

#economic_dimension.view()

# Subcategory - Environmental Dimension

environmental_dimension = ctrl.Consequent(np.arange(0, 101, 1), 'Environmental Dimension')

environmental_dimension['Low'] = fuzz.gauss2mf(environmental_dimension.universe, 0, 10, 15, 10)
environmental_dimension['Medium'] = fuzz.gauss2mf(environmental_dimension.universe, 38, 8, 62, 8)
environmental_dimension['High'] = fuzz.gauss2mf(environmental_dimension.universe, 85, 10, 100, 10)

#environmental_dimension.view()

# Creating fuzzy decision rules
# Defining dimensions through variables

# Operational dimension case

rule1 = ctrl.Rule(efficiency['Very Poor'] & power['Very Poor'] & acoustic_signature['Very Low'], operational_dimension['Medium'])
rule2 = ctrl.Rule(efficiency['Very Poor'] & power['Very Poor'] & acoustic_signature['Low'], operational_dimension['Low'])
rule3 = ctrl.Rule(efficiency['Very Poor'] & power['Very Poor'] & acoustic_signature['High'], operational_dimension['Low'])
rule4 = ctrl.Rule(efficiency['Very Poor'] & power['Very Poor'] & acoustic_signature['Very High'], operational_dimension['Low'])

rule5 = ctrl.Rule(efficiency['Very Poor'] & power['Poor'] & acoustic_signature['Very Low'], operational_dimension['Medium'])
rule6 = ctrl.Rule(efficiency['Very Poor'] & power['Poor'] & acoustic_signature['Low'], operational_dimension['Medium'])
rule7 = ctrl.Rule(efficiency['Very Poor'] & power['Poor'] & acoustic_signature['High'], operational_dimension['Low'])
rule8 = ctrl.Rule(efficiency['Very Poor'] & power['Poor'] & acoustic_signature['Very High'], operational_dimension['Low'])

rule9 = ctrl.Rule(efficiency['Very Poor'] & power['Good'] & acoustic_signature['Very Low'], operational_dimension['Medium'])
rule10 = ctrl.Rule(efficiency['Very Poor'] & power['Good'] & acoustic_signature['Low'], operational_dimension['Medium'])
rule11 = ctrl.Rule(efficiency['Very Poor'] & power['Good'] & acoustic_signature['High'], operational_dimension['Low'])
rule12 = ctrl.Rule(efficiency['Very Poor'] & power['Good'] & acoustic_signature['Very High'], operational_dimension['Low'])

rule13 = ctrl.Rule(efficiency['Very Poor'] & power['Very Good'] & acoustic_signature['Very Low'], operational_dimension['High'])
rule14 = ctrl.Rule(efficiency['Very Poor'] & power['Very Good'] & acoustic_signature['Low'], operational_dimension['Medium'])
rule15 = ctrl.Rule(efficiency['Very Poor'] & power['Very Good'] & acoustic_signature['High'], operational_dimension['Medium'])
rule16 = ctrl.Rule(efficiency['Very Poor'] & power['Very Good'] & acoustic_signature['Very High'], operational_dimension['Low'])

rule17 = ctrl.Rule(efficiency['Poor'] & power['Very Poor'] & acoustic_signature['Very Low'], operational_dimension['Medium'])
rule18 = ctrl.Rule(efficiency['Poor'] & power['Very Poor'] & acoustic_signature['Low'], operational_dimension['Medium'])
rule19 = ctrl.Rule(efficiency['Poor'] & power['Very Poor'] & acoustic_signature['High'], operational_dimension['Low'])
rule20 = ctrl.Rule(efficiency['Poor'] & power['Very Poor'] & acoustic_signature['Very High'], operational_dimension['Low'])

rule21 = ctrl.Rule(efficiency['Poor'] & power['Poor'] & acoustic_signature['Very Low'], operational_dimension['Medium'])
rule22 = ctrl.Rule(efficiency['Poor'] & power['Poor'] & acoustic_signature['Low'], operational_dimension['Medium'])
rule23 = ctrl.Rule(efficiency['Poor'] & power['Poor'] & acoustic_signature['High'], operational_dimension['Medium'])
rule24 = ctrl.Rule(efficiency['Poor'] & power['Poor'] & acoustic_signature['Very High'], operational_dimension['Low'])

rule25 = ctrl.Rule(efficiency['Poor'] & power['Good'] & acoustic_signature['Very Low'], operational_dimension['High'])
rule26 = ctrl.Rule(efficiency['Poor'] & power['Good'] & acoustic_signature['Low'], operational_dimension['Medium'])
rule27 = ctrl.Rule(efficiency['Poor'] & power['Good'] & acoustic_signature['High'], operational_dimension['Medium'])
rule28 = ctrl.Rule(efficiency['Poor'] & power['Good'] & acoustic_signature['Very High'], operational_dimension['Low'])

rule29 = ctrl.Rule(efficiency['Poor'] & power['Very Good'] & acoustic_signature['Very Low'], operational_dimension['High'])
rule30 = ctrl.Rule(efficiency['Poor'] & power['Very Good'] & acoustic_signature['Low'], operational_dimension['Medium'])
rule31 = ctrl.Rule(efficiency['Poor'] & power['Very Good'] & acoustic_signature['High'], operational_dimension['Medium'])
rule32 = ctrl.Rule(efficiency['Poor'] & power['Very Good'] & acoustic_signature['Very High'], operational_dimension['Medium'])

rule33 = ctrl.Rule(efficiency['Good'] & power['Very Poor'] & acoustic_signature['Very Low'], operational_dimension['Medium'])
rule34 = ctrl.Rule(efficiency['Good'] & power['Very Poor'] & acoustic_signature['Low'], operational_dimension['Medium'])
rule35 = ctrl.Rule(efficiency['Good'] & power['Very Poor'] & acoustic_signature['High'], operational_dimension['Medium'])
rule36 = ctrl.Rule(efficiency['Good'] & power['Very Poor'] & acoustic_signature['Very High'], operational_dimension['Low'])

rule37 = ctrl.Rule(efficiency['Good'] & power['Poor'] & acoustic_signature['Very Low'], operational_dimension['High'])
rule38 = ctrl.Rule(efficiency['Good'] & power['Poor'] & acoustic_signature['Low'], operational_dimension['Medium'])
rule39 = ctrl.Rule(efficiency['Good'] & power['Poor'] & acoustic_signature['High'], operational_dimension['Medium'])
rule40 = ctrl.Rule(efficiency['Good'] & power['Poor'] & acoustic_signature['Very High'], operational_dimension['Low'])

rule41 = ctrl.Rule(efficiency['Good'] & power['Good'] & acoustic_signature['Very Low'], operational_dimension['High'])
rule42 = ctrl.Rule(efficiency['Good'] & power['Good'] & acoustic_signature['Low'], operational_dimension['Medium'])
rule43 = ctrl.Rule(efficiency['Good'] & power['Good'] & acoustic_signature['High'], operational_dimension['Medium'])
rule44 = ctrl.Rule(efficiency['Good'] & power['Good'] & acoustic_signature['Very High'], operational_dimension['Medium'])

rule45 = ctrl.Rule(efficiency['Good'] & power['Very Good'] & acoustic_signature['Very Low'], operational_dimension['High'])
rule46 = ctrl.Rule(efficiency['Good'] & power['Very Good'] & acoustic_signature['Low'], operational_dimension['High'])
rule47 = ctrl.Rule(efficiency['Good'] & power['Very Good'] & acoustic_signature['High'], operational_dimension['Medium'])
rule48 = ctrl.Rule(efficiency['Good'] & power['Very Good'] & acoustic_signature['Very High'], operational_dimension['Medium'])

rule49 = ctrl.Rule(efficiency['Very Good'] & power['Very Poor'] & acoustic_signature['Very Low'], operational_dimension['High'])
rule50 = ctrl.Rule(efficiency['Very Good'] & power['Very Poor'] & acoustic_signature['Low'], operational_dimension['Medium'])
rule51 = ctrl.Rule(efficiency['Very Good'] & power['Very Poor'] & acoustic_signature['High'], operational_dimension['Medium'])
rule52 = ctrl.Rule(efficiency['Very Good'] & power['Very Poor'] & acoustic_signature['Very High'], operational_dimension['Low'])

rule53 = ctrl.Rule(efficiency['Very Good'] & power['Poor'] & acoustic_signature['Very Low'], operational_dimension['High'])
rule54 = ctrl.Rule(efficiency['Very Good'] & power['Poor'] & acoustic_signature['Low'], operational_dimension['High'])
rule55 = ctrl.Rule(efficiency['Very Good'] & power['Poor'] & acoustic_signature['High'], operational_dimension['Medium'])
rule56 = ctrl.Rule(efficiency['Very Good'] & power['Poor'] & acoustic_signature['Very High'], operational_dimension['Medium'])

rule57 = ctrl.Rule(efficiency['Very Good'] & power['Good'] & acoustic_signature['Very Low'], operational_dimension['High'])
rule58 = ctrl.Rule(efficiency['Very Good'] & power['Good'] & acoustic_signature['Low'], operational_dimension['High'])
rule59 = ctrl.Rule(efficiency['Very Good'] & power['Good'] & acoustic_signature['High'], operational_dimension['Medium'])
rule60 = ctrl.Rule(efficiency['Very Good'] & power['Good'] & acoustic_signature['Very High'], operational_dimension['Medium'])

rule61 = ctrl.Rule(efficiency['Very Good'] & power['Very Good'] & acoustic_signature['Very Low'], operational_dimension['High'])
rule62 = ctrl.Rule(efficiency['Very Good'] & power['Very Good'] & acoustic_signature['Low'], operational_dimension['High'])
rule63 = ctrl.Rule(efficiency['Very Good'] & power['Very Good'] & acoustic_signature['High'], operational_dimension['High'])
rule64 = ctrl.Rule(efficiency['Very Good'] & power['Very Good'] & acoustic_signature['Very High'], operational_dimension['Medium'])

# Economic dimension case
rule65 = ctrl.Rule(acquisition_cost['Very Low'] & maintenance_cost['Very Low'] & operation_cost['Very Low'], economic_dimension['High'])
rule66 = ctrl.Rule(acquisition_cost['Very Low'] & maintenance_cost['Very Low'] & operation_cost['Low'], economic_dimension['High'])
rule67 = ctrl.Rule(acquisition_cost['Very Low'] & maintenance_cost['Very Low'] & operation_cost['High'], economic_dimension['High'])
rule68 = ctrl.Rule(acquisition_cost['Very Low'] & maintenance_cost['Very Low'] & operation_cost['Very High'], economic_dimension['Medium'])

rule69 = ctrl.Rule(acquisition_cost['Very Low'] & maintenance_cost['Low'] & operation_cost['Very Low'], economic_dimension['High'])
rule70 = ctrl.Rule(acquisition_cost['Very Low'] & maintenance_cost['Low'] & operation_cost['Low'], economic_dimension['High'])
rule71 = ctrl.Rule(acquisition_cost['Very Low'] & maintenance_cost['Low'] & operation_cost['High'], economic_dimension['Medium'])
rule72 = ctrl.Rule(acquisition_cost['Very Low'] & maintenance_cost['Low'] & operation_cost['Very High'], economic_dimension['Medium'])

rule73 = ctrl.Rule(acquisition_cost['Very Low'] & maintenance_cost['High'] & operation_cost['Very Low'], economic_dimension['High'])
rule74 = ctrl.Rule(acquisition_cost['Very Low'] & maintenance_cost['High'] & operation_cost['Low'], economic_dimension['Medium'])
rule75 = ctrl.Rule(acquisition_cost['Very Low'] & maintenance_cost['High'] & operation_cost['High'], economic_dimension['Medium'])
rule76 = ctrl.Rule(acquisition_cost['Very Low'] & maintenance_cost['High'] & operation_cost['Very High'], economic_dimension['Medium'])

rule77 = ctrl.Rule(acquisition_cost['Very Low'] & maintenance_cost['Very High'] & operation_cost['Very Low'], economic_dimension['Medium'])
rule78 = ctrl.Rule(acquisition_cost['Very Low'] & maintenance_cost['Very High'] & operation_cost['Low'], economic_dimension['Medium'])
rule79 = ctrl.Rule(acquisition_cost['Very Low'] & maintenance_cost['Very High'] & operation_cost['High'], economic_dimension['Medium'])
rule80 = ctrl.Rule(acquisition_cost['Very Low'] & maintenance_cost['Very High'] & operation_cost['Very High'], economic_dimension['Low'])

rule81 = ctrl.Rule(acquisition_cost['Low'] & maintenance_cost['Very Low'] & operation_cost['Very Low'], economic_dimension['High'])
rule82 = ctrl.Rule(acquisition_cost['Low'] & maintenance_cost['Very Low'] & operation_cost['Low'], economic_dimension['High'])
rule83 = ctrl.Rule(acquisition_cost['Low'] & maintenance_cost['Very Low'] & operation_cost['High'], economic_dimension['High'])
rule84 = ctrl.Rule(acquisition_cost['Low'] & maintenance_cost['Very Low'] & operation_cost['Very High'], economic_dimension['Medium'])

rule85 = ctrl.Rule(acquisition_cost['Low'] & maintenance_cost['Low'] & operation_cost['Very Low'], economic_dimension['High'])
rule86 = ctrl.Rule(acquisition_cost['Low'] & maintenance_cost['Low'] & operation_cost['Low'], economic_dimension['Medium'])
rule87 = ctrl.Rule(acquisition_cost['Low'] & maintenance_cost['Low'] & operation_cost['High'], economic_dimension['Medium'])
rule88 = ctrl.Rule(acquisition_cost['Low'] & maintenance_cost['Low'] & operation_cost['Very High'], economic_dimension['Medium'])

rule89 = ctrl.Rule(acquisition_cost['Low'] & maintenance_cost['High'] & operation_cost['Very Low'], economic_dimension['Medium'])
rule90 = ctrl.Rule(acquisition_cost['Low'] & maintenance_cost['High'] & operation_cost['Low'], economic_dimension['Medium'])
rule91 = ctrl.Rule(acquisition_cost['Low'] & maintenance_cost['High'] & operation_cost['High'], economic_dimension['Medium'])
rule92 = ctrl.Rule(acquisition_cost['Low'] & maintenance_cost['High'] & operation_cost['Very High'], economic_dimension['Low'])

rule93 = ctrl.Rule(acquisition_cost['Low'] & maintenance_cost['Very High'] & operation_cost['Very Low'], economic_dimension['Medium'])
rule94 = ctrl.Rule(acquisition_cost['Low'] & maintenance_cost['Very High'] & operation_cost['Low'], economic_dimension['Medium'])
rule95 = ctrl.Rule(acquisition_cost['Low'] & maintenance_cost['Very High'] & operation_cost['High'], economic_dimension['Low'])
rule96 = ctrl.Rule(acquisition_cost['Low'] & maintenance_cost['Very High'] & operation_cost['Very High'], economic_dimension['Low'])

rule97 = ctrl.Rule(acquisition_cost['High'] & maintenance_cost['Very Low'] & operation_cost['Very Low'], economic_dimension['High'])
rule98 = ctrl.Rule(acquisition_cost['High'] & maintenance_cost['Very Low'] & operation_cost['Low'], economic_dimension['High'])
rule99 = ctrl.Rule(acquisition_cost['High'] & maintenance_cost['Very Low'] & operation_cost['High'], economic_dimension['Medium'])
rule100 = ctrl.Rule(acquisition_cost['High'] & maintenance_cost['Very Low'] & operation_cost['Very High'], economic_dimension['Medium'])

rule101 = ctrl.Rule(acquisition_cost['High'] & maintenance_cost['Low'] & operation_cost['Very Low'], economic_dimension['High'])
rule102 = ctrl.Rule(acquisition_cost['High'] & maintenance_cost['Low'] & operation_cost['Low'], economic_dimension['Medium'])
rule103 = ctrl.Rule(acquisition_cost['High'] & maintenance_cost['Low'] & operation_cost['High'], economic_dimension['Medium'])
rule104 = ctrl.Rule(acquisition_cost['High'] & maintenance_cost['Low'] & operation_cost['Very High'], economic_dimension['Medium'])

rule105 = ctrl.Rule(acquisition_cost['High'] & maintenance_cost['High'] & operation_cost['Very Low'], economic_dimension['Medium'])
rule106 = ctrl.Rule(acquisition_cost['High'] & maintenance_cost['High'] & operation_cost['Low'], economic_dimension['Medium'])
rule107 = ctrl.Rule(acquisition_cost['High'] & maintenance_cost['High'] & operation_cost['High'], economic_dimension['Medium'])
rule108 = ctrl.Rule(acquisition_cost['High'] & maintenance_cost['High'] & operation_cost['Very High'], economic_dimension['Low'])

rule109 = ctrl.Rule(acquisition_cost['High'] & maintenance_cost['Very High'] & operation_cost['Very Low'], economic_dimension['Medium'])
rule110 = ctrl.Rule(acquisition_cost['High'] & maintenance_cost['Very High'] & operation_cost['Low'], economic_dimension['Low'])
rule111 = ctrl.Rule(acquisition_cost['High'] & maintenance_cost['Very High'] & operation_cost['High'], economic_dimension['Low'])
rule112 = ctrl.Rule(acquisition_cost['High'] & maintenance_cost['Very High'] & operation_cost['Very High'], economic_dimension['Low'])

rule113 = ctrl.Rule(acquisition_cost['Very High'] & maintenance_cost['Very Low'] & operation_cost['Very Low'], economic_dimension['High'])
rule114 = ctrl.Rule(acquisition_cost['Very High'] & maintenance_cost['Very Low'] & operation_cost['Low'], economic_dimension['Medium'])
rule115 = ctrl.Rule(acquisition_cost['Very High'] & maintenance_cost['Very Low'] & operation_cost['High'], economic_dimension['Medium'])
rule116 = ctrl.Rule(acquisition_cost['Very High'] & maintenance_cost['Very Low'] & operation_cost['Very High'], economic_dimension['Medium'])

rule117 = ctrl.Rule(acquisition_cost['Very High'] & maintenance_cost['Low'] & operation_cost['Very Low'], economic_dimension['Medium'])
rule118 = ctrl.Rule(acquisition_cost['Very High'] & maintenance_cost['Low'] & operation_cost['Low'], economic_dimension['Medium'])
rule119 = ctrl.Rule(acquisition_cost['Very High'] & maintenance_cost['Low'] & operation_cost['High'], economic_dimension['Medium'])
rule120 = ctrl.Rule(acquisition_cost['Very High'] & maintenance_cost['Low'] & operation_cost['Very High'], economic_dimension['Low'])

rule121 = ctrl.Rule(acquisition_cost['Very High'] & maintenance_cost['High'] & operation_cost['Very Low'], economic_dimension['Medium'])
rule122 = ctrl.Rule(acquisition_cost['Very High'] & maintenance_cost['High'] & operation_cost['Low'], economic_dimension['Medium'])
rule123 = ctrl.Rule(acquisition_cost['Very High'] & maintenance_cost['High'] & operation_cost['High'], economic_dimension['Low'])
rule124 = ctrl.Rule(acquisition_cost['Very High'] & maintenance_cost['High'] & operation_cost['Very High'], economic_dimension['Low'])

rule125 = ctrl.Rule(acquisition_cost['Very High'] & maintenance_cost['Very High'] & operation_cost['Very Low'], economic_dimension['Medium'])
rule126 = ctrl.Rule(acquisition_cost['Very High'] & maintenance_cost['Very High'] & operation_cost['Low'], economic_dimension['Low'])
rule127 = ctrl.Rule(acquisition_cost['Very High'] & maintenance_cost['Very High'] & operation_cost['High'], economic_dimension['Low'])
rule128 = ctrl.Rule(acquisition_cost['Very High'] & maintenance_cost['Very High'] & operation_cost['Very High'], economic_dimension['Low'])
# Environmental dimension case

# Rules for Very Low thermal_emission
rule129 = ctrl.Rule(thermal_emission['Very Low'] & byproduct['Low Pollutant'] & size['Very Low'], environmental_dimension['High'])
rule130 = ctrl.Rule(thermal_emission['Very Low'] & byproduct['Low Pollutant'] & size['Low'], environmental_dimension['High'])
rule131 = ctrl.Rule(thermal_emission['Very Low'] & byproduct['Low Pollutant'] & size['High'], environmental_dimension['High'])
rule132 = ctrl.Rule(thermal_emission['Very Low'] & byproduct['Low Pollutant'] & size['Very High'], environmental_dimension['Medium'])

rule133 = ctrl.Rule(thermal_emission['Very Low'] & byproduct['Pollutant'] & size['Very Low'], environmental_dimension['High'])
rule134 = ctrl.Rule(thermal_emission['Very Low'] & byproduct['Pollutant'] & size['Low'], environmental_dimension['High'])
rule135 = ctrl.Rule(thermal_emission['Very Low'] & byproduct['Pollutant'] & size['High'], environmental_dimension['Medium'])
rule136 = ctrl.Rule(thermal_emission['Very Low'] & byproduct['Pollutant'] & size['Very High'], environmental_dimension['Medium'])

rule137 = ctrl.Rule(thermal_emission['Very Low'] & byproduct['Highly Pollutant'] & size['Very Low'], environmental_dimension['High'])
rule138 = ctrl.Rule(thermal_emission['Very Low'] & byproduct['Highly Pollutant'] & size['Low'], environmental_dimension['High'])
rule139 = ctrl.Rule(thermal_emission['Very Low'] & byproduct['Highly Pollutant'] & size['High'], environmental_dimension['Medium'])
rule140 = ctrl.Rule(thermal_emission['Very Low'] & byproduct['Highly Pollutant'] & size['Very High'], environmental_dimension['Medium'])

rule141 = ctrl.Rule(thermal_emission['Very Low'] & byproduct['Extremely Pollutant'] & size['Very Low'], environmental_dimension['High'])
rule142 = ctrl.Rule(thermal_emission['Very Low'] & byproduct['Extremely Pollutant'] & size['Low'], environmental_dimension['Medium'])
rule143 = ctrl.Rule(thermal_emission['Very Low'] & byproduct['Extremely Pollutant'] & size['High'], environmental_dimension['Medium'])
rule144 = ctrl.Rule(thermal_emission['Very Low'] & byproduct['Extremely Pollutant'] & size['Very High'], environmental_dimension['Low'])

# Rules for Low thermal_emission
rule145 = ctrl.Rule(thermal_emission['Low'] & byproduct['Low Pollutant'] & size['Very Low'], environmental_dimension['High'])
rule146 = ctrl.Rule(thermal_emission['Low'] & byproduct['Low Pollutant'] & size['Low'], environmental_dimension['High'])
rule147 = ctrl.Rule(thermal_emission['Low'] & byproduct['Low Pollutant'] & size['High'], environmental_dimension['Medium'])
rule148 = ctrl.Rule(thermal_emission['Low'] & byproduct['Low Pollutant'] & size['Very High'], environmental_dimension['Medium'])

rule149 = ctrl.Rule(thermal_emission['Low'] & byproduct['Pollutant'] & size['Very Low'], environmental_dimension['High'])
rule150 = ctrl.Rule(thermal_emission['Low'] & byproduct['Pollutant'] & size['Low'], environmental_dimension['Medium'])
rule151 = ctrl.Rule(thermal_emission['Low'] & byproduct['Pollutant'] & size['High'], environmental_dimension['Medium'])
rule152 = ctrl.Rule(thermal_emission['Low'] & byproduct['Pollutant'] & size['Very High'], environmental_dimension['Medium'])

rule153 = ctrl.Rule(thermal_emission['Low'] & byproduct['Highly Pollutant'] & size['Very Low'], environmental_dimension['High'])
rule154 = ctrl.Rule(thermal_emission['Low'] & byproduct['Highly Pollutant'] & size['Low'], environmental_dimension['Medium'])
rule155 = ctrl.Rule(thermal_emission['Low'] & byproduct['Highly Pollutant'] & size['High'], environmental_dimension['Medium'])
rule156 = ctrl.Rule(thermal_emission['Low'] & byproduct['Highly Pollutant'] & size['Very High'], environmental_dimension['Low'])

rule157 = ctrl.Rule(thermal_emission['Low'] & byproduct['Extremely Pollutant'] & size['Very Low'], environmental_dimension['Medium'])
rule158 = ctrl.Rule(thermal_emission['Low'] & byproduct['Extremely Pollutant'] & size['Low'], environmental_dimension['Medium'])
rule159 = ctrl.Rule(thermal_emission['Low'] & byproduct['Extremely Pollutant'] & size['High'], environmental_dimension['Medium'])
rule160 = ctrl.Rule(thermal_emission['Low'] & byproduct['Extremely Pollutant'] & size['Very High'], environmental_dimension['Low'])

# Rules for High thermal_emission
rule161 = ctrl.Rule(thermal_emission['High'] & byproduct['Low Pollutant'] & size['Very Low'], environmental_dimension['High'])
rule162 = ctrl.Rule(thermal_emission['High'] & byproduct['Low Pollutant'] & size['Low'], environmental_dimension['Medium'])
rule163 = ctrl.Rule(thermal_emission['High'] & byproduct['Low Pollutant'] & size['High'], environmental_dimension['Medium'])
rule164 = ctrl.Rule(thermal_emission['High'] & byproduct['Low Pollutant'] & size['Very High'], environmental_dimension['Medium'])

rule165 = ctrl.Rule(thermal_emission['High'] & byproduct['Pollutant'] & size['Very Low'], environmental_dimension['High'])
rule166 = ctrl.Rule(thermal_emission['High'] & byproduct['Pollutant'] & size['Low'], environmental_dimension['Medium'])
rule167 = ctrl.Rule(thermal_emission['High'] & byproduct['Pollutant'] & size['High'], environmental_dimension['Medium'])
rule168 = ctrl.Rule(thermal_emission['High'] & byproduct['Pollutant'] & size['Very High'], environmental_dimension['Low'])

rule169 = ctrl.Rule(thermal_emission['High'] & byproduct['Highly Pollutant'] & size['Very Low'], environmental_dimension['Medium'])
rule170 = ctrl.Rule(thermal_emission['High'] & byproduct['Highly Pollutant'] & size['Low'], environmental_dimension['Medium'])
rule171 = ctrl.Rule(thermal_emission['High'] & byproduct['Highly Pollutant'] & size['High'], environmental_dimension['Low'])
rule172 = ctrl.Rule(thermal_emission['High'] & byproduct['Highly Pollutant'] & size['Very High'], environmental_dimension['Low'])

rule173 = ctrl.Rule(thermal_emission['High'] & byproduct['Extremely Pollutant'] & size['Very Low'], environmental_dimension['Medium'])
rule174 = ctrl.Rule(thermal_emission['High'] & byproduct['Extremely Pollutant'] & size['Low'], environmental_dimension['Medium'])
rule175 = ctrl.Rule(thermal_emission['High'] & byproduct['Extremely Pollutant'] & size['High'], environmental_dimension['Low'])
rule176 = ctrl.Rule(thermal_emission['High'] & byproduct['Extremely Pollutant'] & size['Very High'], environmental_dimension['Low'])

# Rules for Very High thermal_emission
rule177 = ctrl.Rule(thermal_emission['Very High'] & byproduct['Low Pollutant'] & size['Very Low'], environmental_dimension['High'])
rule178 = ctrl.Rule(thermal_emission['Very High'] & byproduct['Low Pollutant'] & size['Low'], environmental_dimension['Medium'])
rule179 = ctrl.Rule(thermal_emission['Very High'] & byproduct['Low Pollutant'] & size['High'], environmental_dimension['Medium'])
rule180 = ctrl.Rule(thermal_emission['Very High'] & byproduct['Low Pollutant'] & size['Very High'], environmental_dimension['Low'])

rule181 = ctrl.Rule(thermal_emission['Very High'] & byproduct['Pollutant'] & size['Very Low'], environmental_dimension['Medium'])
rule182 = ctrl.Rule(thermal_emission['Very High'] & byproduct['Pollutant'] & size['Low'], environmental_dimension['Medium'])
rule183 = ctrl.Rule(thermal_emission['Very High'] & byproduct['Pollutant'] & size['High'], environmental_dimension['Low'])
rule184 = ctrl.Rule(thermal_emission['Very High'] & byproduct['Pollutant'] & size['Very High'], environmental_dimension['Low'])

rule185 = ctrl.Rule(thermal_emission['Very High'] & byproduct['Highly Pollutant'] & size['Very Low'], environmental_dimension['Medium'])
rule186 = ctrl.Rule(thermal_emission['Very High'] & byproduct['Highly Pollutant'] & size['Low'], environmental_dimension['Medium'])
rule187 = ctrl.Rule(thermal_emission['Very High'] & byproduct['Highly Pollutant'] & size['High'], environmental_dimension['Low'])
rule188 = ctrl.Rule(thermal_emission['Very High'] & byproduct['Highly Pollutant'] & size['Very High'], environmental_dimension['Low'])

rule189 = ctrl.Rule(thermal_emission['Very High'] & byproduct['Extremely Pollutant'] & size['Very Low'], environmental_dimension['Medium'])
rule190 = ctrl.Rule(thermal_emission['Very High'] & byproduct['Extremely Pollutant'] & size['Low'], environmental_dimension['Low'])
rule191 = ctrl.Rule(thermal_emission['Very High'] & byproduct['Extremely Pollutant'] & size['High'], environmental_dimension['Low'])
rule192 = ctrl.Rule(thermal_emission['Very High'] & byproduct['Extremely Pollutant'] & size['Very High'], environmental_dimension['Low'])

# Creating control systems and simulations
# Operational Dimension

operational_dimension_ctrl = ctrl.ControlSystem([
    rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
    rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20,
    rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30,
    rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40,
    rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50,
    rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60,
    rule61, rule62, rule63, rule64
])
operational_dimension_sim = ctrl.ControlSystemSimulation(operational_dimension_ctrl)

# Economic Dimension

economic_dimension_ctrl = ctrl.ControlSystem([
    rule65, rule66, rule67, rule68, rule69, rule70, rule71, rule72, rule73, rule74,
    rule75, rule76, rule77, rule78, rule79, rule80, rule81, rule82, rule83, rule84,
    rule85, rule86, rule87, rule88, rule89, rule90, rule91, rule92, rule93, rule94,
    rule95, rule96, rule97, rule98, rule99, rule100, rule101, rule102, rule103,
    rule104, rule105, rule106, rule107, rule108, rule109, rule110, rule111, rule112,
    rule113, rule114, rule115, rule116, rule117, rule118, rule119, rule120, rule121,
    rule122, rule123, rule124, rule125, rule126, rule127, rule128
])
economic_dimension_sim = ctrl.ControlSystemSimulation(economic_dimension_ctrl)

# Environmental Dimension

environmental_dimension_ctrl = ctrl.ControlSystem([
    rule129, rule130, rule131, rule132, rule133, rule134, rule135, rule136, rule137,
    rule138, rule139, rule140, rule141, rule142, rule143, rule144, rule145, rule146,
    rule147, rule148, rule149, rule150, rule151, rule152, rule153, rule154, rule155,
    rule156, rule157, rule158, rule159, rule160, rule161, rule162, rule163, rule164,
    rule165, rule166, rule167, rule168, rule169, rule170, rule171, rule172, rule173,
    rule174, rule175, rule176, rule177, rule178, rule179, rule180, rule181, rule182,
    rule183, rule184, rule185, rule186, rule187, rule188, rule189, rule190, rule191,
    rule192
])
environmental_dimension_sim = ctrl.ControlSystemSimulation(environmental_dimension_ctrl)

# Adding values for the characteristics of different systems
# (Fuel Cells, Stirling Engines, Steam Turbines, Diesel Engines)
# for the operational dimension

operational_dimension_sim.input['Efficiency'] = 30  # set the corresponding value
operational_dimension_sim.input['Power'] = 6       # set the corresponding value
operational_dimension_sim.input['Acoustic Signature'] = 9  # set the corresponding value

# Calculating the values for the operational dimension, based on
# the adopted values for efficiency, power, and acoustic signature across the four systems

operational_dimension_sim.compute()
print(operational_dimension_sim.output)

# To display the graph for the operational dimension reached by different systems

operational_dimension.view(sim=operational_dimension_sim)

# Loop to compute operational dimension output across a range of input values

for i in range(11):
    operational_dimension_sim.input['Efficiency'] = i * 10  # set the corresponding value
    operational_dimension_sim.input['Power'] = i            # set the corresponding value
    operational_dimension_sim.input['Acoustic Signature'] = 10 - i  # set the corresponding value
    operational_dimension_sim.compute()
    print(operational_dimension_sim.output)

# Now, adding values for the economic dimension for the different systems
# Setting the input values for acquisition, maintenance, and operation costs

economic_dimension_sim.input['Acquisition Cost'] = 3  # set the corresponding value
economic_dimension_sim.input['Maintenance Cost'] = 5  # set the corresponding value
economic_dimension_sim.input['Operation Cost'] = 3    # set the corresponding value

# Calculating the values for the economic dimension based on the input values
# for acquisition, maintenance, and operation costs across the four systems

economic_dimension_sim.compute()
print(economic_dimension_sim.output)

# To display the graph for the economic dimension reached by different systems

economic_dimension.view(sim=economic_dimension_sim)

# Loop to compute economic dimension output across a range of input values

for i in range(11):
    economic_dimension_sim.input['Acquisition Cost'] = i  # set the corresponding value
    economic_dimension_sim.input['Maintenance Cost'] = i  # set the corresponding value
    economic_dimension_sim.input['Operation Cost'] = i    # set the corresponding value
    economic_dimension_sim.compute()
    print(economic_dimension_sim.output)

# Adding values for the environmental dimension for the different systems
# Setting the input values for thermal emission, byproducts, and size

environmental_dimension_sim.input['Thermal Emission'] = 500  # set the corresponding value
environmental_dimension_sim.input['Byproduct'] = 8           # set the corresponding value
environmental_dimension_sim.input['Size'] = 3                # set the corresponding value

# Calculating the values for the environmental dimension based on the input values
# for thermal emission, byproducts, and size across the four systems

environmental_dimension_sim.compute()
print(environmental_dimension_sim.output)

# To display the graph for the environmental dimension reached by different systems

environmental_dimension.view(sim=environmental_dimension_sim)

# Creating antecedents (input) for the recommendation level
# Subcategory - Operational Dimension
operational_dimension_level = ctrl.Antecedent(np.arange(0, 101, 1), 'Operational Dimension Level')
operational_dimension_level['Low'] = fuzz.gauss2mf(operational_dimension_level.universe, 0, 10, 15, 10)
operational_dimension_level['Medium'] = fuzz.gauss2mf(operational_dimension_level.universe, 38, 8, 62, 8)
operational_dimension_level['High'] = fuzz.gauss2mf(operational_dimension_level.universe, 90, 10, 100, 10)

# Subcategory - Economic Dimension
economic_dimension_level = ctrl.Antecedent(np.arange(0, 101, 1), 'Economic Dimension Level')
economic_dimension_level['Low'] = fuzz.gauss2mf(economic_dimension_level.universe, 0, 10, 15, 10)
economic_dimension_level['Medium'] = fuzz.gauss2mf(economic_dimension_level.universe, 38, 8, 62, 8)
economic_dimension_level['High'] = fuzz.gauss2mf(economic_dimension_level.universe, 90, 10, 100, 10)

# Subcategory - Environmental Dimension
environmental_dimension_level = ctrl.Antecedent(np.arange(0, 101, 1), 'Environmental Dimension Level')
environmental_dimension_level['Low'] = fuzz.gauss2mf(environmental_dimension_level.universe, 0, 10, 15, 10)
environmental_dimension_level['Medium'] = fuzz.gauss2mf(environmental_dimension_level.universe, 38, 8, 62, 8)
environmental_dimension_level['High'] = fuzz.gauss2mf(environmental_dimension_level.universe, 90, 10, 100, 10)

# Defining the final consequence - Recommendation Level
recommendation_level = ctrl.Consequent(np.arange(0, 101, 1), 'Recommendation Level')
recommendation_level['Very Low'] = fuzz.gauss2mf(recommendation_level.universe, 0, 5, 10, 5)
recommendation_level['Low'] = fuzz.gauss2mf(recommendation_level.universe, 23, 5, 33, 5)
recommendation_level['Medium'] = fuzz.gauss2mf(recommendation_level.universe, 45, 5, 55, 5)
recommendation_level['High'] = fuzz.gauss2mf(recommendation_level.universe, 68, 5, 78, 5)
recommendation_level['Very High'] = fuzz.gauss2mf(recommendation_level.universe, 90, 5, 100, 5)

# View the recommendation level
recommendation_level.view()

# Defining rules for the recommendation level based on operational, economic, and environmental dimensions
recommendation_rule_1 = ctrl.Rule(operational_dimension_level['Low'] & economic_dimension_level['Low'] & environmental_dimension_level['Low'], recommendation_level['Very Low'])
recommendation_rule_2 = ctrl.Rule(operational_dimension_level['Low'] & economic_dimension_level['Low'] & environmental_dimension_level['Medium'], recommendation_level['Very Low'])
recommendation_rule_3 = ctrl.Rule(operational_dimension_level['Low'] & economic_dimension_level['Low'] & environmental_dimension_level['High'], recommendation_level['Low'])

recommendation_rule_4 = ctrl.Rule(operational_dimension_level['Low'] & economic_dimension_level['Medium'] & environmental_dimension_level['Low'], recommendation_level['Very Low'])
recommendation_rule_5 = ctrl.Rule(operational_dimension_level['Low'] & economic_dimension_level['Medium'] & environmental_dimension_level['Medium'], recommendation_level['Low'])
recommendation_rule_6 = ctrl.Rule(operational_dimension_level['Low'] & economic_dimension_level['Medium'] & environmental_dimension_level['High'], recommendation_level['Medium'])

recommendation_rule_7 = ctrl.Rule(operational_dimension_level['Low'] & economic_dimension_level['High'] & environmental_dimension_level['Low'], recommendation_level['Low'])
recommendation_rule_8 = ctrl.Rule(operational_dimension_level['Low'] & economic_dimension_level['High'] & environmental_dimension_level['Medium'], recommendation_level['Medium'])
recommendation_rule_9 = ctrl.Rule(operational_dimension_level['Low'] & economic_dimension_level['High'] & environmental_dimension_level['High'], recommendation_level['Medium'])

recommendation_rule_10 = ctrl.Rule(operational_dimension_level['Medium'] & economic_dimension_level['Low'] & environmental_dimension_level['Low'], recommendation_level['Low'])
recommendation_rule_11 = ctrl.Rule(operational_dimension_level['Medium'] & economic_dimension_level['Low'] & environmental_dimension_level['Medium'], recommendation_level['Low'])
recommendation_rule_12 = ctrl.Rule(operational_dimension_level['Medium'] & economic_dimension_level['Low'] & environmental_dimension_level['High'], recommendation_level['Medium'])

recommendation_rule_13 = ctrl.Rule(operational_dimension_level['Medium'] & economic_dimension_level['Medium'] & environmental_dimension_level['Low'], recommendation_level['Low'])
recommendation_rule_14 = ctrl.Rule(operational_dimension_level['Medium'] & economic_dimension_level['Medium'] & environmental_dimension_level['Medium'], recommendation_level['Medium'])
recommendation_rule_15 = ctrl.Rule(operational_dimension_level['Medium'] & economic_dimension_level['Medium'] & environmental_dimension_level['High'], recommendation_level['High'])


recommendation_rule_16 = ctrl.Rule(operational_dimension_level['Medium'] & economic_dimension_level['High'] & environmental_dimension_level['Low'], recommendation_level['Medium'])
recommendation_rule_17 = ctrl.Rule(operational_dimension_level['Medium'] & economic_dimension_level['High'] & environmental_dimension_level['Medium'], recommendation_level['High'])
recommendation_rule_18 = ctrl.Rule(operational_dimension_level['Medium'] & economic_dimension_level['High'] & environmental_dimension_level['High'], recommendation_level['High'])

recommendation_rule_19 = ctrl.Rule(operational_dimension_level['High'] & economic_dimension_level['Low'] & environmental_dimension_level['Low'], recommendation_level['Medium'])
recommendation_rule_20 = ctrl.Rule(operational_dimension_level['High'] & economic_dimension_level['Low'] & environmental_dimension_level['Medium'], recommendation_level['Medium'])
recommendation_rule_21 = ctrl.Rule(operational_dimension_level['High'] & economic_dimension_level['Low'] & environmental_dimension_level['High'], recommendation_level['High'])

recommendation_rule_22 = ctrl.Rule(operational_dimension_level['High'] & economic_dimension_level['Medium'] & environmental_dimension_level['Low'], recommendation_level['Medium'])
recommendation_rule_23 = ctrl.Rule(operational_dimension_level['High'] & economic_dimension_level['Medium'] & environmental_dimension_level['Medium'], recommendation_level['High'])
recommendation_rule_24 = ctrl.Rule(operational_dimension_level['High'] & economic_dimension_level['Medium'] & environmental_dimension_level['High'], recommendation_level['Very High'])

recommendation_rule_25 = ctrl.Rule(operational_dimension_level['High'] & economic_dimension_level['High'] & environmental_dimension_level['Low'], recommendation_level['High'])
recommendation_rule_26 = ctrl.Rule(operational_dimension_level['High'] & economic_dimension_level['High'] & environmental_dimension_level['Medium'], recommendation_level['Very High'])
recommendation_rule_27 = ctrl.Rule(operational_dimension_level['High'] & economic_dimension_level['High'] & environmental_dimension_level['High'], recommendation_level['Very High'])

# Creating the control system and simulation for recommendation level
recommendation_ctrl = ctrl.ControlSystem([
    recommendation_rule_1, recommendation_rule_2, recommendation_rule_3, recommendation_rule_4, recommendation_rule_5,
    recommendation_rule_6, recommendation_rule_7, recommendation_rule_8, recommendation_rule_9, recommendation_rule_10,
    recommendation_rule_11, recommendation_rule_12, recommendation_rule_13, recommendation_rule_14, recommendation_rule_15,
    recommendation_rule_16, recommendation_rule_17, recommendation_rule_18, recommendation_rule_19, recommendation_rule_20,
    recommendation_rule_21, recommendation_rule_22, recommendation_rule_23, recommendation_rule_24, recommendation_rule_25,
    recommendation_rule_26, recommendation_rule_27
])
recommendation_sim = ctrl.ControlSystemSimulation(recommendation_ctrl)

# Setting values for the operational, economic, and environmental dimensions
recommendation_sim.input['Operational Dimension Level'] = 18
recommendation_sim.input['Economic Dimension Level'] = 50
recommendation_sim.input['Environmental Dimension Level'] = 50

# Computing the recommendation level
recommendation_sim.compute()
recommendation_output = recommendation_sim.output['Recommendation Level']
print(recommendation_output)

# To visualize the recommendation level for different systems
recommendation_level.view(sim=recommendation_sim)

# Normalizing the output values
normalized_output = np.round((recommendation_output - 14.63) * 100 / (85.65 - 14.63), 1)
print(normalized_output)

# Data Validation - creating a 3D matrix to store the recommendation level outputs
output_matrix = np.zeros((11, 11, 11))

# Looping through different combinations of operational, economic, and environmental dimension levels
for k in range(11):
    for j in range(11):
        for i in range(11):
            recommendation_sim.input['Operational Dimension Level'] = i * 10  # Increment by 10 for each loop
            recommendation_sim.input['Economic Dimension Level'] = j * 10     # Increment by 10 for each loop
            recommendation_sim.input['Environmental Dimension Level'] = k * 10  # Increment by 10 for each loop
            recommendation_sim.compute()
            output_value = recommendation_sim.output['Recommendation Level']
            output_matrix[i, j, k] = output_value  # Store the computed recommendation level

# Visualization - Plotting 2D graphs for recommendation levels by economic and environmental dimensions

import matplotlib.pyplot as plt

# Creating subplots for visualizing recommendation levels with fixed operational dimension levels
fig, (ax1, ax2) = plt.subplots(2, 1)
fig.set_size_inches(8, 8)
fixed_operational_level = 50  # Fixed operational level for demonstration
fig.suptitle(f'Recommendation Values for Operational Dimension = {fixed_operational_level}%')

colormap = plt.cm.coolwarm  # Color map for the plots
colors = [colormap(i) for i in np.linspace(0, 1, 11)]

for j in range(11):
    loc = int(fixed_operational_level / 10)
    ax1.plot(np.array(range(11)) * 10, output_matrix[:, j, loc], label=j * 10, color=colors[j])
    ax2.plot(np.array(range(11)) * 10, output_matrix[:, loc, j], label=j * 10, color=colors[j])

ax1.legend(title='Economic Dimension', loc='best', ncol=3, shadow=True)
ax2.legend(title='Environmental Dimension', loc='best', ncol=3, shadow=True)
ax1.set_xlim(0, 100)
ax2.set_xlim(0, 100)
ax1.set_yticks([0, 20, 40, 60, 80, 100])
ax2.set_yticks([0, 20, 40, 60, 80, 100])
ax1.set_xlabel('Economic Dimension Values')
ax2.set_xlabel('Environmental Dimension Values')
plt.show()

# 3D Visualization for Recommendation Levels based on operational, economic, and environmental dimensions
from mpl_toolkits import mplot3d

# Looping over operational levels to generate multiple 3D surface plots
for i in range(11):
    x = np.zeros((11, 11))
    y = np.zeros((11, 11))
    z = np.zeros((11, 11))
    
    operational_level = i * 10  # Set fixed operational level for this plot
    idx = int(operational_level / 10)
    
    for j in range(11):
        for k in range(11):
            x[j, k] = j * 10
            y[j, k] = k * 10
            z[j, k] = output_matrix[idx, j, k]
    
    fig = plt.figure()
    fig.set_size_inches(8, 8)
    ax = plt.axes(projection='3d')
    
    ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')
    ax.set_title(f'Recommendation Values for Operational Dimension = {operational_level}%')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_zlim(0, 100)
    ax.set_xticks([0, 20, 40, 60, 80, 100])
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    ax.set_xlabel('Economic Dimension Values')
    ax.set_ylabel('Environmental Dimension Values')
    ax.set_zlabel('Recommendation Level')
    plt.savefig(f'3do_{i*10}.png')

# Looping over operational levels to generate multiple 3D surface plots
for i in range(11):
    x = np.zeros((11, 11))
    y = np.zeros((11, 11))
    z = np.zeros((11, 11))
    
    economic_level = i * 10  # Set fixed operational level for this plot
    idx = int(economic_level / 10)
    
    for j in range(11):
        for k in range(11):
            x[j, k] = j * 10
            y[j, k] = k * 10
            z[j, k] = output_matrix[j, idx, k]
    
    fig = plt.figure()
    fig.set_size_inches(8, 8)
    ax = plt.axes(projection='3d')
    
    ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')
    ax.set_title(f'Recommendation Values for Economic Dimension = {economic_level}%')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_zlim(0, 100)
    ax.set_xticks([0, 20, 40, 60, 80, 100])
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    ax.set_xlabel('Operational Dimension Values')
    ax.set_ylabel('Environmental Dimension Values')
    ax.set_zlabel('Recommendation Level')
    plt.savefig(f'3de_{i*10}.png')


# Looping over environmental levels to generate multiple 3D surface plots
for i in range(11):
    x = np.zeros((11, 11))
    y = np.zeros((11, 11))
    z = np.zeros((11, 11))
    
    environmental_level = i * 10  # Set fixed environmental level for this plot
    idx = int(environmental_level / 10)
    
    for j in range(11):
        for k in range(11):
            x[j, k] = j * 10  # Operational Dimension
            y[j, k] = k * 10  # Economic Dimension
            z[j, k] = output_matrix[j, k, idx]  # Fixed Environmental Dimension
    
    fig = plt.figure()
    fig.set_size_inches(8, 8)
    ax = plt.axes(projection='3d')
    
    ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')
    ax.set_title(f'Recommendation Values for Environmental Dimension = {environmental_level}%')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_zlim(0, 100)
    ax.set_xticks([0, 20, 40, 60, 80, 100])
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    ax.set_xlabel('Operational Dimension Values')
    ax.set_ylabel('Economic Dimension Values')
    ax.set_zlabel('Recommendation Level')
    plt.savefig(f'3den_{i*10}.png')


import matplotlib.pyplot as plt
import numpy as np

# Data for the star plot (excluding Recommendation)
labels = ['Operational', 'Economic', 'Environmental']
data = {
    "Fuel Cells": [79, 42, 79],
    "Stirling Engines": [50, 50, 42],
    "Steam Turbines": [48, 42, 16],
    "Diesel Engines": [18, 50, 50]
}

# Number of variables
num_vars = len(labels)

# Create the angles for the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Close the circle

# Create a radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each system's data
for system, values in data.items():
    values += values[:1]  # Close the circle
    ax.plot(angles, values, label=system, linewidth=2)
    ax.fill(angles, values, alpha=0.25)

# Add labels for each axis
ax.set_yticks([20, 40, 60, 80])
ax.set_yticklabels(['20', '40', '60', '80'])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

# Add legend and title
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
ax.set_title("Star Plot of AIP System Performance", size=16, weight='bold', position=(0.5, 1.1))

plt.show()
