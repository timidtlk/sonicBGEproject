# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    PAR0000 = nodes.ParameterVector3Split()
    PAR0001 = nodes.ParameterMatrixToVector()
    PAR0002 = nodes.ParameterMatrixToVector()
    PAR0003 = nodes.ParameterObjectAttribute()
    PAR0004 = nodes.ParameterObjectAttribute()
    CON0005 = nodes.ConditionOnUpdate()
    PAR0006 = nodes.ParameterVector3Split()
    ACT0007 = nodes.ActionSetGameObjectVisibility()
    ACT0008 = nodes.ActionSetGameObjectVisibility()
    ACT0009 = nodes.ActionSetGameObjectVisibility()
    ACT0010 = nodes.ActionSetGameObjectVisibility()
    ACT0011 = nodes.ActionSetGameObjectGameProperty()
    PAR0012 = nodes.ParameterArithmeticOp()
    ACT0013 = nodes.AbsoluteValue()
    CON0014 = nodes.ObjectPropertyOperator()
    CON0015 = nodes.ConditionAndList()
    CON0016 = nodes.ObjectPropertyOperator()
    CON0017 = nodes.ConditionAndList()
    CON0018 = nodes.ObjectPropertyOperator()
    CON0019 = nodes.ObjectPropertyOperator()
    PAR0000.input_v = PAR0001.OUT
    PAR0001.input_m = PAR0003
    PAR0002.input_m = PAR0004
    PAR0003.game_object = "NLO:cameraController"
    PAR0003.attribute_name = "localOrientation"
    PAR0004.game_object = "NLO:CharacterController"
    PAR0004.attribute_name = "localOrientation"
    PAR0006.input_v = PAR0002.OUT
    ACT0007.condition = CON0015
    ACT0007.game_object = "NLO:chr_Sonic_HD.002"
    ACT0007.visible = False
    ACT0007.recursive = False
    ACT0008.condition = CON0015
    ACT0008.game_object = "NLO:chr_Sonic_HD.003"
    ACT0008.visible = True
    ACT0008.recursive = False
    ACT0009.condition = CON0017
    ACT0009.game_object = "NLO:chr_Sonic_HD.002"
    ACT0009.visible = True
    ACT0009.recursive = False
    ACT0010.condition = CON0017
    ACT0010.game_object = "NLO:chr_Sonic_HD.003"
    ACT0010.visible = False
    ACT0010.recursive = False
    ACT0011.condition = CON0005
    ACT0011.game_object = "NLO:U_O"
    ACT0011.property_name = "mouth_side"
    ACT0011.property_value = ACT0013.OUT
    PAR0012.operator = nodes.ParameterArithmeticOp.op_by_code("SUB")
    PAR0012.operand_a = PAR0000.OUTZ
    PAR0012.operand_b = PAR0006.OUTZ
    ACT0013.value = PAR0012
    CON0014.game_object = "NLO:U_O"
    CON0014.property_name = "mouth_side"
    CON0014.compare_value = 3.1415927410125732
    CON0014.operator = 3
    CON0015.ca = CON0014
    CON0015.cb = CON0018
    CON0015.cc = True
    CON0015.cd = True
    CON0015.ce = True
    CON0015.cf = True
    CON0016.game_object = "NLO:U_O"
    CON0016.property_name = "mouth_side"
    CON0016.compare_value = 3.1415927410125732
    CON0016.operator = 2
    CON0017.ca = CON0016
    CON0017.cb = CON0019
    CON0017.cc = True
    CON0017.cd = True
    CON0017.ce = True
    CON0017.cf = True
    CON0018.game_object = "NLO:CharacterController"
    CON0018.property_name = "isJumping"
    CON0018.compare_value = False
    CON0018.operator = 0
    CON0019.game_object = "NLO:CharacterController"
    CON0019.property_name = "isJumping"
    CON0019.compare_value = False
    CON0019.operator = 0
    network.add_cell(PAR0003)
    network.add_cell(CON0005)
    network.add_cell(CON0014)
    network.add_cell(CON0016)
    network.add_cell(CON0018)
    network.add_cell(PAR0001)
    network.add_cell(PAR0004)
    network.add_cell(CON0015)
    network.add_cell(CON0019)
    network.add_cell(PAR0000)
    network.add_cell(ACT0007)
    network.add_cell(CON0017)
    network.add_cell(PAR0002)
    network.add_cell(ACT0008)
    network.add_cell(ACT0010)
    network.add_cell(PAR0006)
    network.add_cell(PAR0012)
    network.add_cell(ACT0009)
    network.add_cell(ACT0013)
    network.add_cell(ACT0011)
    owner["IGNLTree_face_side"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__face_side')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_face_side")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
