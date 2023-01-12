# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    PAR0000 = nodes.ParameterObjectAttribute()
    ACT0001 = nodes.ActionSetObjectAttribute()
    PAR0002 = nodes.ParameterVector3Simple()
    CON0003 = nodes.ConditionLogicOp()
    PAR0004 = nodes.ParameterDistance()
    PAR0005 = nodes.ParameterObjectAttribute()
    PAR0006 = nodes.ParameterArithmeticOp()
    PAR0000.game_object = "NLO:aim"
    PAR0000.attribute_name = "worldPosition"
    ACT0001.condition = CON0003
    ACT0001.xyz = {'x': True, 'y': True, 'z': True}
    ACT0001.game_object = "NLO:aim"
    ACT0001.attribute_value = PAR0002.OUTV
    ACT0001.value_type = 'worldScale'
    PAR0002.input_x = PAR0006
    PAR0002.input_y = PAR0006
    PAR0002.input_z = 0.0
    CON0003.param_a = PAR0004
    CON0003.param_b = 10.0
    CON0003.threshold = 0.0
    CON0003.operator = 2
    PAR0004.parama = PAR0005
    PAR0004.paramb = PAR0000
    PAR0005.game_object = "NLO:camPos"
    PAR0005.attribute_name = "worldPosition"
    PAR0006.operator = nodes.ParameterArithmeticOp.op_by_code("DIV")
    PAR0006.operand_a = PAR0004
    PAR0006.operand_b = 5.0
    network.add_cell(PAR0000)
    network.add_cell(PAR0005)
    network.add_cell(PAR0004)
    network.add_cell(CON0003)
    network.add_cell(PAR0006)
    network.add_cell(PAR0002)
    network.add_cell(ACT0001)
    owner["IGNLTree_reticle"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__reticle')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_reticle")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
