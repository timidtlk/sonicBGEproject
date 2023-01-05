# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionSetGameObjectGameProperty()
    ACT0001 = nodes.ActionSetGameObjectGameProperty()
    ACT0002 = nodes.ActionSetObjectAttribute()
    PAR0003 = nodes.ParameterObjectProperty()
    PAR0004 = nodes.ParameterObjectProperty()
    PAR0005 = nodes.ParameterVector3Simple()
    PAR0006 = nodes.ParameterObjectAttribute()
    PAR0007 = nodes.ParameterArithmeticOp()
    PAR0008 = nodes.ParameterArithmeticOp()
    CON0009 = nodes.ObjectPropertyOperator()
    CON0010 = nodes.ObjectPropertyOperator()
    CON0011 = nodes.ConditionOr()
    PAR0012 = nodes.ConditionGamepadSticks()
    ACT0013 = nodes.ActionRotateTo()
    CON0014 = nodes.ConditionOnUpdate()
    PAR0015 = nodes.ParameterMathFun()
    PAR0016 = nodes.ParameterObjectProperty()
    PAR0017 = nodes.ParameterMathFun()
    PAR0018 = nodes.ParameterMathFun()
    ACT0019 = nodes.ActionSetGameObjectGameProperty()
    ACT0020 = nodes.ActionSetGameObjectGameProperty()
    PAR0021 = nodes.ParameterObjectProperty()
    ACT0022 = nodes.ActionSetGameObjectGameProperty()
    PAR0023 = nodes.ParameterObjectProperty()
    PAR0024 = nodes.ParameterObjectProperty()
    ACT0025 = nodes.ActionSetGameObjectGameProperty()
    ACT0026 = nodes.ActionSetGameObjectGameProperty()
    CON0027 = nodes.ConditionAnd()
    ACT0028 = nodes.ActionSetGameObjectGameProperty()
    CON0029 = nodes.ConditionAnd()
    CON0030 = nodes.ConditionAnd()
    CON0031 = nodes.ConditionNot()
    CON0032 = nodes.ConditionAnd()
    CON0033 = nodes.ConditionNot()
    CON0034 = nodes.ConditionAnd()
    CON0035 = nodes.ConditionNot()
    CON0036 = nodes.ConditionAnd()
    CON0037 = nodes.ObjectPropertyOperator()
    CON0038 = nodes.ObjectPropertyOperator()
    PAR0039 = nodes.ParameterObjectProperty()
    PAR0040 = nodes.ParameterObjectProperty()
    PAR0041 = nodes.ParameterArithmeticOp()
    ACT0042 = nodes.ActionSetGameObjectGameProperty()
    CON0043 = nodes.GEKeyboardActive()
    CON0044 = nodes.ConditionNot()
    ACT0045 = nodes.ActionSetGameObjectGameProperty()
    CON0046 = nodes.ObjectPropertyOperator()
    ACT0000.condition = CON0014
    ACT0000.game_object = "NLO:U_O"
    ACT0000.property_name = "value_updown"
    ACT0000.property_value = PAR0007
    ACT0001.condition = CON0014
    ACT0001.game_object = "NLO:U_O"
    ACT0001.property_name = "value_leftright"
    ACT0001.property_value = PAR0008
    ACT0002.condition = CON0014
    ACT0002.xyz = {'x': True, 'y': True, 'z': False}
    ACT0002.game_object = "NLO:joystick_forward"
    ACT0002.attribute_value = PAR0005.OUTV
    ACT0002.value_type = 'localPosition'
    PAR0003.game_object = "NLO:U_O"
    PAR0003.property_name = "value_leftright"
    PAR0004.game_object = "NLO:U_O"
    PAR0004.property_name = "value_updown"
    PAR0005.input_x = PAR0003
    PAR0005.input_y = PAR0004
    PAR0005.input_z = 0.0
    PAR0006.game_object = "NLO:joystick_forward"
    PAR0006.attribute_name = "worldPosition"
    PAR0007.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0007.operand_a = PAR0012.Y
    PAR0007.operand_b = 4.0
    PAR0008.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0008.operand_a = PAR0012.X
    PAR0008.operand_b = -4.0
    CON0009.game_object = "NLO:U_O"
    CON0009.property_name = "value_updown"
    CON0009.compare_value = 0.0
    CON0009.operator = 1
    CON0010.game_object = "NLO:CharacterController"
    CON0010.property_name = "value_leftright"
    CON0010.compare_value = 0.0
    CON0010.operator = 1
    CON0011.condition_a = CON0009
    CON0011.condition_b = CON0010
    PAR0012.inverted = False
    PAR0012.index = 0
    PAR0012.sensitivity = 1.0
    PAR0012.threshold = 0.10000000149011612
    PAR0012.axis = 0
    ACT0013.condition = CON0011
    ACT0013.moving_object = "NLO:U_O"
    ACT0013.target_point = PAR0006
    ACT0013.speed = 2.0
    ACT0013.rot_axis = 2
    ACT0013.front_axis = 1
    PAR0015.formula = "abs(a)"
    PAR0015.a = PAR0041
    PAR0015.b = 0.0
    PAR0016.game_object = "NLO:U_O"
    PAR0016.property_name = "absup"
    PAR0017.formula = "abs(a)"
    PAR0017.a = PAR0039
    PAR0017.b = 0.0
    PAR0018.formula = "abs(a)"
    PAR0018.a = PAR0040
    PAR0018.b = 0.0
    ACT0019.condition = CON0014
    ACT0019.game_object = "NLO:U_O"
    ACT0019.property_name = "absleft"
    ACT0019.property_value = PAR0018
    ACT0020.condition = CON0014
    ACT0020.game_object = "NLO:U_O"
    ACT0020.property_name = "absup"
    ACT0020.property_value = PAR0017
    PAR0021.game_object = "NLO:CharacterController"
    PAR0021.property_name = "A"
    ACT0022.condition = None
    ACT0022.game_object = "NLO:U_O"
    ACT0022.property_name = "A"
    ACT0022.property_value = PAR0023
    PAR0023.game_object = "NLO:U_O"
    PAR0023.property_name = "absleft"
    PAR0024.game_object = "NLO:U_O"
    PAR0024.property_name = "absup"
    ACT0025.condition = CON0027
    ACT0025.game_object = "NLO:U_O"
    ACT0025.property_name = "A"
    ACT0025.property_value = CON0046.VAL
    ACT0026.condition = CON0029
    ACT0026.game_object = "NLO:U_O"
    ACT0026.property_name = "A"
    ACT0026.property_value = CON0037.VAL
    CON0027.condition_a = CON0046
    CON0027.condition_b = CON0035
    ACT0028.condition = CON0030
    ACT0028.game_object = "NLO:U_O"
    ACT0028.property_name = "A"
    ACT0028.property_value = CON0038.VAL
    CON0029.condition_a = CON0037
    CON0029.condition_b = CON0033
    CON0030.condition_a = CON0038
    CON0030.condition_b = CON0031
    CON0031.condition = CON0032
    CON0032.condition_a = CON0046
    CON0032.condition_b = CON0037
    CON0033.condition = CON0034
    CON0034.condition_a = CON0046
    CON0034.condition_b = CON0038
    CON0035.condition = CON0036
    CON0036.condition_a = CON0037
    CON0036.condition_b = CON0038
    CON0037.game_object = "NLO:U_O"
    CON0037.property_name = "absleft"
    CON0037.compare_value = PAR0024
    CON0037.operator = 2
    CON0038.game_object = "NLO:U_O"
    CON0038.property_name = "absup"
    CON0038.compare_value = PAR0023
    CON0038.operator = 2
    PAR0039.game_object = "NLO:U_O"
    PAR0039.property_name = "value_updown"
    PAR0040.game_object = "NLO:U_O"
    PAR0040.property_name = "value_leftright"
    PAR0041.operator = nodes.ParameterArithmeticOp.op_by_code("DIV")
    PAR0041.operand_a = PAR0021
    PAR0041.operand_b = 4.0
    ACT0042.condition = CON0043
    ACT0042.game_object = "NLO:U_O"
    ACT0042.property_name = "max"
    ACT0042.property_value = 1.0
    CON0044.condition = CON0043
    ACT0045.condition = CON0044
    ACT0045.game_object = "NLO:U_O"
    ACT0045.property_name = "max"
    ACT0045.property_value = PAR0015
    CON0046.game_object = "NLO:U_O"
    CON0046.property_name = "absleft"
    CON0046.compare_value = PAR0024
    CON0046.operator = 0
    network.add_cell(PAR0003)
    network.add_cell(PAR0006)
    network.add_cell(CON0009)
    network.add_cell(PAR0012)
    network.add_cell(CON0014)
    network.add_cell(PAR0016)
    network.add_cell(PAR0021)
    network.add_cell(PAR0023)
    network.add_cell(CON0038)
    network.add_cell(PAR0040)
    network.add_cell(CON0043)
    network.add_cell(PAR0004)
    network.add_cell(PAR0007)
    network.add_cell(CON0010)
    network.add_cell(PAR0018)
    network.add_cell(ACT0022)
    network.add_cell(PAR0039)
    network.add_cell(ACT0042)
    network.add_cell(ACT0000)
    network.add_cell(PAR0005)
    network.add_cell(CON0011)
    network.add_cell(PAR0017)
    network.add_cell(ACT0020)
    network.add_cell(PAR0041)
    network.add_cell(ACT0002)
    network.add_cell(ACT0013)
    network.add_cell(ACT0019)
    network.add_cell(CON0044)
    network.add_cell(PAR0008)
    network.add_cell(PAR0024)
    network.add_cell(CON0037)
    network.add_cell(CON0046)
    network.add_cell(ACT0001)
    network.add_cell(CON0032)
    network.add_cell(CON0034)
    network.add_cell(CON0036)
    network.add_cell(PAR0015)
    network.add_cell(CON0031)
    network.add_cell(CON0035)
    network.add_cell(CON0027)
    network.add_cell(CON0030)
    network.add_cell(ACT0045)
    network.add_cell(ACT0025)
    network.add_cell(ACT0028)
    network.add_cell(CON0033)
    network.add_cell(CON0029)
    network.add_cell(ACT0026)
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
