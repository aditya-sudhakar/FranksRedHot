# import PySpice.Logging.Logging as Logging
# logger = Logging.setup_logging()
#
#
# from PySpice.Spice.Netlist import Circuit, SubCircuit, SubCircuitFactory
# from PySpice.Unit import *
#
# class ParallelResistor(SubCircuitFactory):
#     __name__ = 'parallel_resistor'
#     __nodes__ = ('n1', 'n2')
#     def __init__(self, R1=1@u_Ω, R2=2@u_Ω):
#         super().__init__()
#         self.R(1, 'n1', 'n2', R1)
#         self.R(2, 'n1', 'n2', R2)
#
# circuit = Circuit('Test')
#
# circuit.subcircuit(ParallelResistor(R2=3@u_Ω))
# circuit.X('1', 'parallel_resistor', 1, circuit.gnd)
#
# print(circuit)

import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()


from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *


circuit = Circuit('Voltage Divider')

circuit.V('input', 1, circuit.gnd, 10@u_V)
circuit.R(1, 1, 2, 2@u_kΩ)
circuit.R(2, 2, circuit.gnd, 1@u_kΩ)

simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.operating_point()

for node in analysis.nodes.values():
    print('Node {}: {:5.2f} V'.format(str(node), float(node))) # Fixme: format value + unit
