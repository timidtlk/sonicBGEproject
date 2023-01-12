# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    PAR0000 = nodes.ParameterArithmeticOp()
    PAR0001 = nodes.ParameterVector3Simple()
    ACT0002 = nodes.ActionTimeFilter()
    CON0003 = nodes.ConditionOnUpdate()
    PAR0004 = nodes.ParameterVector3Split()
    CON0005 = nodes.ConditionLogicOp()
    ACT0006 = nodes.ActionEndObject()
    PAR0007 = nodes.ParameterObjectAttribute()
    ACT0008 = nodes.ActionSetObjectAttribute()
    PAR0000.operator = nodes.ParameterArithmeticOp.op_by_code("SUB")
    PAR0000.operand_a = PAR0004.OUTX
    PAR0000.operand_b = 0.4000000059604645
    PAR0001.input_x = PAR0000
    PAR0001.input_y = PAR0000
    PAR0001.input_z = PAR0000
    ACT0002.condition = CON0003
    ACT0002.delay = 0.009999999776482582
    PAR0004.input_v = PAR0007
    CON0005.param_a = PAR0004.OUTX
    CON0005.param_b = 0.0
    CON0005.threshold = 0.0
    CON0005.operator = 5
    ACT0006.condition = CON0005
    ACT0006.game_object = "NLO:U_O"
    PAR0007.game_object = "NLO:U_O"
    PAR0007.attribute_name = "worldScale"
    ACT0008.condition = ACT0002
    ACT0008.xyz = {'x': True, 'y': True, 'z': True}
    ACT0008.game_object = "NLO:U_O"
    ACT0008.attribute_value = PAR0001.OUTV
    ACT0008.value_type = 'worldScale'
    network.add_cell(CON0003)
    network.add_cell(PAR0007)
    network.add_cell(ACT0002)
    network.add_cell(PAR0004)
    network.add_cell(PAR0000)
    network.add_cell(CON0005)
    network.add_cell(PAR0001)
    network.add_cell(ACT0008)
    network.add_cell(ACT0006)
    owner["IGNLTree_effect"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__effect')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_effect")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
