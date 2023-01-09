# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionSetGameObjectGameProperty()
    ACT0001 = nodes.ActionSetGameObjectGameProperty()
    PAR0002 = nodes.ParameterObjectProperty()
    PAR0003 = nodes.ParameterObjectProperty()
    PAR0004 = nodes.ParameterVector3Simple()
    PAR0005 = nodes.ParameterObjectAttribute()
    PAR0006 = nodes.ParameterArithmeticOp()
    PAR0007 = nodes.ParameterArithmeticOp()
    CON0008 = nodes.ObjectPropertyOperator()
    CON0009 = nodes.ObjectPropertyOperator()
    CON0010 = nodes.ConditionOr()
    PAR0011 = nodes.ConditionGamepadSticks()
    ACT0012 = nodes.ActionRotateTo()
    CON0013 = nodes.ConditionOnUpdate()
    PAR0014 = nodes.ParameterMathFun()
    PAR0015 = nodes.ParameterObjectProperty()
    PAR0016 = nodes.ParameterMathFun()
    PAR0017 = nodes.ParameterMathFun()
    ACT0018 = nodes.ActionSetGameObjectGameProperty()
    ACT0019 = nodes.ActionSetGameObjectGameProperty()
    PAR0020 = nodes.ParameterObjectProperty()
    ACT0021 = nodes.ActionSetGameObjectGameProperty()
    PAR0022 = nodes.ParameterObjectProperty()
    PAR0023 = nodes.ParameterObjectProperty()
    ACT0024 = nodes.ActionSetGameObjectGameProperty()
    ACT0025 = nodes.ActionSetGameObjectGameProperty()
    CON0026 = nodes.ConditionAnd()
    ACT0027 = nodes.ActionSetGameObjectGameProperty()
    CON0028 = nodes.ConditionAnd()
    CON0029 = nodes.ConditionAnd()
    CON0030 = nodes.ConditionNot()
    CON0031 = nodes.ConditionAnd()
    CON0032 = nodes.ConditionNot()
    CON0033 = nodes.ConditionAnd()
    CON0034 = nodes.ConditionNot()
    CON0035 = nodes.ConditionAnd()
    CON0036 = nodes.ObjectPropertyOperator()
    CON0037 = nodes.ObjectPropertyOperator()
    PAR0038 = nodes.ParameterObjectProperty()
    PAR0039 = nodes.ParameterObjectProperty()
    PAR0040 = nodes.ParameterArithmeticOp()
    ACT0041 = nodes.ActionSetGameObjectGameProperty()
    CON0042 = nodes.GEKeyboardActive()
    CON0043 = nodes.ConditionNot()
    ACT0044 = nodes.ActionSetGameObjectGameProperty()
    CON0045 = nodes.ObjectPropertyOperator()
    PAR0046 = nodes.ParameterObjectProperty()
    ACT0047 = nodes.ActionSetObjectAttribute()
    ACT0000.condition = CON0013
    ACT0000.game_object = "NLO:U_O"
    ACT0000.property_name = "value_updown"
    ACT0000.property_value = PAR0006
    ACT0001.condition = CON0013
    ACT0001.game_object = "NLO:U_O"
    ACT0001.property_name = "value_leftright"
    ACT0001.property_value = PAR0007
    PAR0002.game_object = "NLO:U_O"
    PAR0002.property_name = "value_leftright"
    PAR0003.game_object = "NLO:U_O"
    PAR0003.property_name = "value_updown"
    PAR0004.input_x = PAR0002
    PAR0004.input_y = PAR0003
    PAR0004.input_z = 0.0
    PAR0005.game_object = "NLO:joystick_forward"
    PAR0005.attribute_name = "worldPosition"
    PAR0006.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0006.operand_a = PAR0011.Y
    PAR0006.operand_b = 4.0
    PAR0007.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0007.operand_a = PAR0011.X
    PAR0007.operand_b = -4.0
    CON0008.game_object = "NLO:U_O"
    CON0008.property_name = "value_updown"
    CON0008.compare_value = 0.0
    CON0008.operator = 1
    CON0009.game_object = "NLO:CharacterController"
    CON0009.property_name = "value_leftright"
    CON0009.compare_value = 0.0
    CON0009.operator = 1
    CON0010.condition_a = CON0008
    CON0010.condition_b = CON0009
    PAR0011.inverted = False
    PAR0011.index = 0
    PAR0011.sensitivity = 1.0
    PAR0011.threshold = 0.10000000149011612
    PAR0011.axis = 0
    ACT0012.condition = CON0010
    ACT0012.moving_object = "NLO:U_O"
    ACT0012.target_point = PAR0005
    ACT0012.speed = PAR0046
    ACT0012.rot_axis = 2
    ACT0012.front_axis = 1
    PAR0014.formula = "abs(a)"
    PAR0014.a = PAR0040
    PAR0014.b = 0.0
    PAR0015.game_object = "NLO:U_O"
    PAR0015.property_name = "absup"
    PAR0016.formula = "abs(a)"
    PAR0016.a = PAR0038
    PAR0016.b = 0.0
    PAR0017.formula = "abs(a)"
    PAR0017.a = PAR0039
    PAR0017.b = 0.0
    ACT0018.condition = CON0013
    ACT0018.game_object = "NLO:U_O"
    ACT0018.property_name = "absleft"
    ACT0018.property_value = PAR0017
    ACT0019.condition = CON0013
    ACT0019.game_object = "NLO:U_O"
    ACT0019.property_name = "absup"
    ACT0019.property_value = PAR0016
    PAR0020.game_object = "NLO:CharacterController"
    PAR0020.property_name = "A"
    ACT0021.condition = None
    ACT0021.game_object = "NLO:U_O"
    ACT0021.property_name = "A"
    ACT0021.property_value = PAR0022
    PAR0022.game_object = "NLO:U_O"
    PAR0022.property_name = "absleft"
    PAR0023.game_object = "NLO:U_O"
    PAR0023.property_name = "absup"
    ACT0024.condition = CON0026
    ACT0024.game_object = "NLO:U_O"
    ACT0024.property_name = "A"
    ACT0024.property_value = CON0045.VAL
    ACT0025.condition = CON0028
    ACT0025.game_object = "NLO:U_O"
    ACT0025.property_name = "A"
    ACT0025.property_value = CON0036.VAL
    CON0026.condition_a = CON0045
    CON0026.condition_b = CON0034
    ACT0027.condition = CON0029
    ACT0027.game_object = "NLO:U_O"
    ACT0027.property_name = "A"
    ACT0027.property_value = CON0037.VAL
    CON0028.condition_a = CON0036
    CON0028.condition_b = CON0032
    CON0029.condition_a = CON0037
    CON0029.condition_b = CON0030
    CON0030.condition = CON0031
    CON0031.condition_a = CON0045
    CON0031.condition_b = CON0036
    CON0032.condition = CON0033
    CON0033.condition_a = CON0045
    CON0033.condition_b = CON0037
    CON0034.condition = CON0035
    CON0035.condition_a = CON0036
    CON0035.condition_b = CON0037
    CON0036.game_object = "NLO:U_O"
    CON0036.property_name = "absleft"
    CON0036.compare_value = PAR0023
    CON0036.operator = 2
    CON0037.game_object = "NLO:U_O"
    CON0037.property_name = "absup"
    CON0037.compare_value = PAR0022
    CON0037.operator = 2
    PAR0038.game_object = "NLO:U_O"
    PAR0038.property_name = "value_updown"
    PAR0039.game_object = "NLO:U_O"
    PAR0039.property_name = "value_leftright"
    PAR0040.operator = nodes.ParameterArithmeticOp.op_by_code("DIV")
    PAR0040.operand_a = PAR0020
    PAR0040.operand_b = 4.0
    ACT0041.condition = CON0042
    ACT0041.game_object = "NLO:U_O"
    ACT0041.property_name = "max"
    ACT0041.property_value = 1.0
    CON0043.condition = CON0042
    ACT0044.condition = CON0043
    ACT0044.game_object = "NLO:U_O"
    ACT0044.property_name = "max"
    ACT0044.property_value = PAR0014
    CON0045.game_object = "NLO:U_O"
    CON0045.property_name = "absleft"
    CON0045.compare_value = PAR0023
    CON0045.operator = 0
    PAR0046.game_object = "NLO:U_O"
    PAR0046.property_name = "rotSpeed"
    ACT0047.condition = CON0013
    ACT0047.xyz = {'x': True, 'y': True, 'z': False}
    ACT0047.game_object = "NLO:joystick_forward"
    ACT0047.attribute_value = PAR0004.OUTV
    ACT0047.value_type = 'localPosition'
    network.add_cell(PAR0002)
    network.add_cell(PAR0005)
    network.add_cell(CON0008)
    network.add_cell(PAR0011)
    network.add_cell(CON0013)
    network.add_cell(PAR0015)
    network.add_cell(PAR0020)
    network.add_cell(PAR0022)
    network.add_cell(CON0037)
    network.add_cell(PAR0039)
    network.add_cell(CON0042)
    network.add_cell(PAR0046)
    network.add_cell(PAR0003)
    network.add_cell(PAR0006)
    network.add_cell(CON0009)
    network.add_cell(PAR0017)
    network.add_cell(ACT0021)
    network.add_cell(PAR0038)
    network.add_cell(ACT0041)
    network.add_cell(ACT0000)
    network.add_cell(PAR0004)
    network.add_cell(CON0010)
    network.add_cell(PAR0016)
    network.add_cell(ACT0019)
    network.add_cell(PAR0040)
    network.add_cell(ACT0047)
    network.add_cell(PAR0007)
    network.add_cell(PAR0014)
    network.add_cell(PAR0023)
    network.add_cell(CON0036)
    network.add_cell(CON0045)
    network.add_cell(ACT0001)
    network.add_cell(ACT0018)
    network.add_cell(CON0031)
    network.add_cell(CON0033)
    network.add_cell(CON0035)
    network.add_cell(ACT0012)
    network.add_cell(CON0030)
    network.add_cell(CON0034)
    network.add_cell(CON0026)
    network.add_cell(CON0029)
    network.add_cell(CON0043)
    network.add_cell(ACT0024)
    network.add_cell(ACT0027)
    network.add_cell(CON0032)
    network.add_cell(CON0028)
    network.add_cell(ACT0025)
    network.add_cell(ACT0044)
    owner["IGNLTree_joystick"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__joystick')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_joystick")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
