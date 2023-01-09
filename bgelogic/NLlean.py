# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionSetGameObjectGameProperty()
    ACT0001 = nodes.ActionTimeFilter()
    PAR0002 = nodes.ParameterObjectProperty()
    ACT0003 = nodes.ActionSetGameObjectGameProperty()
    PAR0004 = nodes.ParameterVector3Split()
    PAR0005 = nodes.ParameterObjectAttribute()
    PAR0006 = nodes.ParameterMatrixToVector()
    PAR0007 = nodes.ParameterObjectProperty()
    PAR0008 = nodes.ParameterObjectProperty()
    ACT0009 = nodes.ActionSetGameObjectGameProperty()
    PAR0010 = nodes.ParameterArithmeticOp()
    CON0011 = nodes.ConditionOnUpdate()
    ACT0012 = nodes.ActionSetGameObjectGameProperty()
    CON0013 = nodes.ObjectPropertyOperator()
    ACT0014 = nodes.ActionSetGameObjectGameProperty()
    CON0015 = nodes.ObjectPropertyOperator()
    CON0016 = nodes.ObjectPropertyOperator()
    ACT0017 = nodes.ActionSetGameObjectGameProperty()
    ACT0000.condition = CON0011
    ACT0000.game_object = "NLO:U_O"
    ACT0000.property_name = "rotation_z"
    ACT0000.property_value = PAR0004.OUTZ
    ACT0001.condition = CON0011
    ACT0001.delay = 0.10000000149011612
    PAR0002.game_object = "NLO:U_O"
    PAR0002.property_name = "rotation_z"
    ACT0003.condition = ACT0001
    ACT0003.game_object = "NLO:U_O"
    ACT0003.property_name = "rotation_lasttick"
    ACT0003.property_value = PAR0002
    PAR0004.input_v = PAR0006.OUT
    PAR0005.game_object = "NLO:U_O"
    PAR0005.attribute_name = "worldOrientation"
    PAR0006.input_m = PAR0005
    PAR0007.game_object = "NLO:U_O"
    PAR0007.property_name = "rotation_lasttick"
    PAR0008.game_object = "NLO:U_O"
    PAR0008.property_name = "rotation_z"
    ACT0009.condition = CON0011
    ACT0009.game_object = "NLO:U_O"
    ACT0009.property_name = "subtract_result"
    ACT0009.property_value = PAR0010
    PAR0010.operator = nodes.ParameterArithmeticOp.op_by_code("SUB")
    PAR0010.operand_a = PAR0008
    PAR0010.operand_b = PAR0007
    ACT0012.condition = CON0013
    ACT0012.game_object = "NLO:chr_Sonic_HD"
    ACT0012.property_name = "lean_direction"
    ACT0012.property_value = "left"
    CON0013.game_object = "NLO:U_O"
    CON0013.property_name = "subtract_result"
    CON0013.compare_value = 0.0
    CON0013.operator = 2
    ACT0014.condition = CON0015
    ACT0014.game_object = "NLO:chr_Sonic_HD"
    ACT0014.property_name = "lean_direction"
    ACT0014.property_value = "center"
    CON0015.game_object = "NLO:U_O"
    CON0015.property_name = "subtract_result"
    CON0015.compare_value = 0.0
    CON0015.operator = 0
    CON0016.game_object = "NLO:U_O"
    CON0016.property_name = "subtract_result"
    CON0016.compare_value = 0.0
    CON0016.operator = 3
    ACT0017.condition = CON0016
    ACT0017.game_object = "NLO:chr_Sonic_HD"
    ACT0017.property_name = "lean_direction"
    ACT0017.property_value = "right"
    network.add_cell(PAR0002)
    network.add_cell(PAR0005)
    network.add_cell(PAR0007)
    network.add_cell(CON0011)
    network.add_cell(CON0013)
    network.add_cell(CON0015)
    network.add_cell(ACT0001)
    network.add_cell(PAR0006)
    network.add_cell(ACT0012)
    network.add_cell(CON0016)
    network.add_cell(ACT0003)
    network.add_cell(PAR0008)
    network.add_cell(PAR0010)
    network.add_cell(ACT0017)
    network.add_cell(PAR0004)
    network.add_cell(ACT0014)
    network.add_cell(ACT0000)
    network.add_cell(ACT0009)
    owner["IGNLTree_lean"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__lean')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_lean")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
