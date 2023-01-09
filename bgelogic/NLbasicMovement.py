# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    CON0000 = nodes.ConditionOr()
    CON0001 = nodes.ObjectPropertyOperator()
    CON0002 = nodes.ObjectPropertyOperator()
    CON0003 = nodes.ObjectPropertyOperator()
    CON0004 = nodes.ObjectPropertyOperator()
    CON0005 = nodes.ConditionOr()
    CON0006 = nodes.ConditionOr()
    CON0007 = nodes.ConditionAnd()
    ACT0008 = nodes.ActionApplyLocation()
    PAR0009 = nodes.ParameterArithmeticOp()
    PAR0010 = nodes.ParameterVector3Simple()
    PAR0011 = nodes.ParameterObjectProperty()
    CON0012 = nodes.ConditionKeyPressed()
    CON0013 = nodes.ConditionKeyPressed()
    CON0014 = nodes.ConditionKeyPressed()
    CON0015 = nodes.ConditionOrList()
    CON0016 = nodes.ObjectPropertyOperator()
    CON0017 = nodes.ConditionKeyPressed()
    CON0018 = nodes.ObjectPropertyOperator()
    CON0019 = nodes.ConditionAnd()
    CON0020 = nodes.ConditionAnd()
    CON0021 = nodes.ConditionAnd()
    CON0022 = nodes.ConditionAnd()
    CON0023 = nodes.ConditionAnd()
    CON0024 = nodes.ConditionOrList()
    CON0025 = nodes.ConditionNot()
    ACT0026 = nodes.ActionSetGameObjectGameProperty()
    ACT0027 = nodes.ActionSetGameObjectGameProperty()
    CON0028 = nodes.ConditionAnd()
    CON0029 = nodes.ConditionAnd()
    CON0030 = nodes.ConditionAnd()
    CON0031 = nodes.ConditionAnd()
    CON0032 = nodes.ConditionAnd()
    CON0033 = nodes.ObjectPropertyOperator()
    ACT0034 = nodes.ActionTimeFilter()
    ACT0035 = nodes.ActionTimeFilter()
    CON0036 = nodes.ObjectPropertyOperator()
    ACT0037 = nodes.ActionAddToGameObjectGameProperty()
    ACT0038 = nodes.ActionSetGameObjectGameProperty()
    ACT0039 = nodes.ActionSetGameObjectGameProperty()
    ACT0040 = nodes.ActionSetGameObjectGameProperty()
    ACT0041 = nodes.ActionAddToGameObjectGameProperty()
    ACT0042 = nodes.ActionSetGameObjectGameProperty()
    ACT0043 = nodes.ActionSetGameObjectGameProperty()
    PAR0044 = nodes.ParameterObjectProperty()
    CON0045 = nodes.ObjectPropertyOperator()
    ACT0046 = nodes.ActionSetGameObjectGameProperty()
    CON0047 = nodes.ObjectPropertyOperator()
    CON0048 = nodes.ObjectPropertyOperator()
    CON0049 = nodes.ConditionNot()
    CON0050 = nodes.ConditionAndList()
    CON0051 = nodes.ObjectPropertyOperator()
    CON0052 = nodes.ObjectPropertyOperator()
    CON0053 = nodes.ObjectPropertyOperator()
    CON0054 = nodes.ObjectPropertyOperator()
    CON0055 = nodes.ObjectPropertyOperator()
    CON0056 = nodes.ObjectPropertyOperator()
    ACT0057 = nodes.ActionSetGameObjectGameProperty()
    ACT0058 = nodes.ActionSetGameObjectGameProperty()
    ACT0059 = nodes.ActionSetGameObjectGameProperty()
    CON0060 = nodes.ObjectPropertyOperator()
    ACT0061 = nodes.ActionSetGameObjectGameProperty()
    CON0062 = nodes.ObjectPropertyOperator()
    CON0063 = nodes.ObjectPropertyOperator()
    ACT0064 = nodes.ActionSetGameObjectGameProperty()
    CON0065 = nodes.ObjectPropertyOperator()
    CON0066 = nodes.ObjectPropertyOperator()
    ACT0067 = nodes.ActionSetGameObjectGameProperty()
    PAR0068 = nodes.ParameterObjectAttribute()
    PAR0069 = nodes.ParameterObjectAttribute()
    ACT0070 = nodes.ActionRotateTo()
    ACT0071 = nodes.ActionRotateTo()
    ACT0072 = nodes.ActionRotateTo()
    ACT0073 = nodes.ActionRotateTo()
    ACT0074 = nodes.ActionRotateTo()
    ACT0075 = nodes.ActionRotateTo()
    ACT0076 = nodes.ActionRotateTo()
    PAR0077 = nodes.ParameterObjectAttribute()
    PAR0078 = nodes.ParameterObjectAttribute()
    PAR0079 = nodes.ParameterObjectAttribute()
    PAR0080 = nodes.ParameterObjectAttribute()
    PAR0081 = nodes.ParameterObjectAttribute()
    PAR0082 = nodes.ParameterObjectProperty()
    PAR0083 = nodes.ParameterObjectAttribute()
    ACT0084 = nodes.ActionRotateTo()
    CON0000.condition_a = None
    CON0000.condition_b = None
    CON0001.game_object = "NLO:CharacterController"
    CON0001.property_name = "value_leftright"
    CON0001.compare_value = 0.0
    CON0001.operator = 1
    CON0002.game_object = "NLO:U_O"
    CON0002.property_name = "value_updown"
    CON0002.compare_value = 0.0
    CON0002.operator = 1
    CON0003.game_object = "NLO:CharacterController"
    CON0003.property_name = "isBoosting"
    CON0003.compare_value = False
    CON0003.operator = 0
    CON0004.game_object = "NLO:CharacterController"
    CON0004.property_name = "Speed"
    CON0004.compare_value = 0.029999999329447746
    CON0004.operator = 2
    CON0005.condition_a = CON0002
    CON0005.condition_b = CON0001
    CON0006.condition_a = CON0007
    CON0006.condition_b = CON0005
    CON0007.condition_a = CON0015
    CON0007.condition_b = CON0003
    ACT0008.local = True
    ACT0008.condition = CON0016
    ACT0008.game_object = "NLO:CharacterController"
    ACT0008.movement = PAR0009
    PAR0009.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0009.operand_a = PAR0010.OUTV
    PAR0009.operand_b = PAR0011
    PAR0010.input_x = 0.0
    PAR0010.input_y = CON0004
    PAR0010.input_z = 0.0
    PAR0011.game_object = "NLO:CharacterController"
    PAR0011.property_name = "Speed"
    CON0012.key_code = bge.events.WKEY
    CON0012.pulse = True
    CON0013.key_code = bge.events.SKEY
    CON0013.pulse = True
    CON0014.key_code = bge.events.AKEY
    CON0014.pulse = True
    CON0015.ca = CON0012
    CON0015.cb = CON0013
    CON0015.cc = CON0014
    CON0015.cd = CON0017
    CON0015.ce = None
    CON0015.cf = None
    CON0016.game_object = "NLO:CharacterController"
    CON0016.property_name = "Speed"
    CON0016.compare_value = 0.029999999329447746
    CON0016.operator = 2
    CON0017.key_code = bge.events.DKEY
    CON0017.pulse = True
    CON0018.game_object = "NLO:CharacterController"
    CON0018.property_name = "Speed"
    CON0018.compare_value = 0.3199999928474426
    CON0018.operator = 2
    CON0019.condition_a = CON0052
    CON0019.condition_b = CON0053
    CON0020.condition_a = CON0065
    CON0020.condition_b = CON0066
    CON0021.condition_a = CON0054
    CON0021.condition_b = CON0018
    CON0022.condition_a = CON0062
    CON0022.condition_b = CON0063
    CON0023.condition_a = CON0060
    CON0023.condition_b = CON0055
    CON0024.ca = CON0028
    CON0024.cb = CON0029
    CON0024.cc = CON0031
    CON0024.cd = CON0030
    CON0024.ce = None
    CON0024.cf = None
    CON0025.condition = CON0032
    ACT0026.condition = CON0032
    ACT0026.game_object = "NLO:CharacterController"
    ACT0026.property_name = "max"
    ACT0026.property_value = 1.0
    ACT0027.condition = CON0025
    ACT0027.game_object = "NLO:CharacterController"
    ACT0027.property_name = "max"
    ACT0027.property_value = 1.0
    CON0028.condition_a = CON0012
    CON0028.condition_b = CON0014
    CON0029.condition_a = CON0012
    CON0029.condition_b = CON0017
    CON0030.condition_a = CON0013
    CON0030.condition_b = CON0017
    CON0031.condition_a = CON0013
    CON0031.condition_b = CON0014
    CON0032.condition_a = CON0024
    CON0032.condition_b = CON0033
    CON0033.game_object = "NLO:CharacterController"
    CON0033.property_name = "isBoosting"
    CON0033.compare_value = False
    CON0033.operator = 0
    ACT0034.condition = CON0036
    ACT0034.delay = 0.019999999552965164
    ACT0035.condition = CON0006
    ACT0035.delay = 0.019999999552965164
    CON0036.game_object = "NLO:CharacterController"
    CON0036.property_name = "Speed"
    CON0036.compare_value = 0.029999999329447746
    CON0036.operator = 2
    ACT0037.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("SUB")
    ACT0037.condition = ACT0034
    ACT0037.game_object = "NLO:CharacterController"
    ACT0037.property_name = "Speed"
    ACT0037.property_value = 0.009999999776482582
    ACT0038.condition = ACT0037.OUT
    ACT0038.game_object = "NLO:U_O"
    ACT0038.property_name = "isAccelerating"
    ACT0038.property_value = False
    ACT0039.condition = ACT0041.OUT
    ACT0039.game_object = "NLO:U_O"
    ACT0039.property_name = "isAccelerating"
    ACT0039.property_value = True
    ACT0040.condition = ACT0039.OUT
    ACT0040.game_object = "NLO:U_O"
    ACT0040.property_name = "max"
    ACT0040.property_value = 1.0
    ACT0041.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("ADD")
    ACT0041.condition = ACT0035
    ACT0041.game_object = "NLO:CharacterController"
    ACT0041.property_name = "Speed"
    ACT0041.property_value = 0.029999999329447746
    ACT0042.condition = CON0051
    ACT0042.game_object = "NLO:CharacterController"
    ACT0042.property_name = "Speed"
    ACT0042.property_value = 0.029999999329447746
    ACT0043.condition = CON0049
    ACT0043.game_object = "NLO:CharacterController"
    ACT0043.property_name = "max"
    ACT0043.property_value = 1.0
    PAR0044.game_object = "NLO:CharacterController"
    PAR0044.property_name = "max"
    CON0045.game_object = "NLO:CharacterController"
    CON0045.property_name = "Speed"
    CON0045.compare_value = PAR0044
    CON0045.operator = 2
    ACT0046.condition = CON0050
    ACT0046.game_object = "NLO:CharacterController"
    ACT0046.property_name = "Speed"
    ACT0046.property_value = PAR0044
    CON0047.game_object = "NLO:CharacterController"
    CON0047.property_name = "isBoosting"
    CON0047.compare_value = False
    CON0047.operator = 0
    CON0048.game_object = "NLO:CharacterController"
    CON0048.property_name = "isAccelerating"
    CON0048.compare_value = True
    CON0048.operator = 0
    CON0049.condition = CON0048
    CON0050.ca = CON0045
    CON0050.cb = CON0047
    CON0050.cc = CON0048
    CON0050.cd = True
    CON0050.ce = True
    CON0050.cf = True
    CON0051.game_object = "NLO:CharacterController"
    CON0051.property_name = "Speed"
    CON0051.compare_value = 0.0
    CON0051.operator = 3
    CON0052.game_object = "NLO:CharacterController"
    CON0052.property_name = "Speed"
    CON0052.compare_value = 0.1599999964237213
    CON0052.operator = 5
    CON0053.game_object = "NLO:CharacterController"
    CON0053.property_name = "Speed"
    CON0053.compare_value = 0.10000000149011612
    CON0053.operator = 2
    CON0054.game_object = "NLO:CharacterController"
    CON0054.property_name = "Speed"
    CON0054.compare_value = 0.47999998927116394
    CON0054.operator = 5
    CON0055.game_object = "NLO:CharacterController"
    CON0055.property_name = "Speed"
    CON0055.compare_value = 0.1599999964237213
    CON0055.operator = 2
    CON0056.game_object = "NLO:CharacterController"
    CON0056.property_name = "Speed"
    CON0056.compare_value = 0.6399999856948853
    CON0056.operator = 2
    ACT0057.condition = CON0019
    ACT0057.game_object = "NLO:CharacterController"
    ACT0057.property_name = "rotSpeed"
    ACT0057.property_value = 10.0
    ACT0058.condition = CON0021
    ACT0058.game_object = "NLO:CharacterController"
    ACT0058.property_name = "rotSpeed"
    ACT0058.property_value = 9.0
    ACT0059.condition = CON0056
    ACT0059.game_object = "NLO:CharacterController"
    ACT0059.property_name = "rotSpeed"
    ACT0059.property_value = 8.0
    CON0060.game_object = "NLO:CharacterController"
    CON0060.property_name = "Speed"
    CON0060.compare_value = 0.3199999928474426
    CON0060.operator = 5
    ACT0061.condition = CON0023
    ACT0061.game_object = "NLO:CharacterController"
    ACT0061.property_name = "rotSpeed"
    ACT0061.property_value = 9.0
    CON0062.game_object = "NLO:CharacterController"
    CON0062.property_name = "Speed"
    CON0062.compare_value = 0.6399999856948853
    CON0062.operator = 5
    CON0063.game_object = "NLO:CharacterController"
    CON0063.property_name = "Speed"
    CON0063.compare_value = 0.47999998927116394
    CON0063.operator = 2
    ACT0064.condition = CON0022
    ACT0064.game_object = "NLO:CharacterController"
    ACT0064.property_name = "rotSpeed"
    ACT0064.property_value = 9.0
    CON0065.game_object = "NLO:CharacterController"
    CON0065.property_name = "Speed"
    CON0065.compare_value = 0.10000000149011612
    CON0065.operator = 5
    CON0066.game_object = "NLO:CharacterController"
    CON0066.property_name = "Speed"
    CON0066.compare_value = 0.0
    CON0066.operator = 2
    ACT0067.condition = CON0020
    ACT0067.game_object = "NLO:CharacterController"
    ACT0067.property_name = "rotSpeed"
    ACT0067.property_value = 10.0
    PAR0068.game_object = "NLO:A"
    PAR0068.attribute_name = "worldPosition"
    PAR0069.game_object = "NLO:S"
    PAR0069.attribute_name = "worldPosition"
    ACT0070.condition = CON0031
    ACT0070.moving_object = "NLO:CharacterController"
    ACT0070.target_point = PAR0080
    ACT0070.speed = PAR0082
    ACT0070.rot_axis = 2
    ACT0070.front_axis = 1
    ACT0071.condition = CON0030
    ACT0071.moving_object = "NLO:CharacterController"
    ACT0071.target_point = PAR0081
    ACT0071.speed = PAR0082
    ACT0071.rot_axis = 2
    ACT0071.front_axis = 1
    ACT0072.condition = CON0029
    ACT0072.moving_object = "NLO:CharacterController"
    ACT0072.target_point = PAR0079
    ACT0072.speed = PAR0082
    ACT0072.rot_axis = 2
    ACT0072.front_axis = 1
    ACT0073.condition = CON0017
    ACT0073.moving_object = "NLO:CharacterController"
    ACT0073.target_point = PAR0077
    ACT0073.speed = PAR0082
    ACT0073.rot_axis = 2
    ACT0073.front_axis = 1
    ACT0074.condition = CON0014
    ACT0074.moving_object = "NLO:CharacterController"
    ACT0074.target_point = PAR0068
    ACT0074.speed = PAR0082
    ACT0074.rot_axis = 2
    ACT0074.front_axis = 1
    ACT0075.condition = CON0013
    ACT0075.moving_object = "NLO:CharacterController"
    ACT0075.target_point = PAR0069
    ACT0075.speed = PAR0082
    ACT0075.rot_axis = 2
    ACT0075.front_axis = 1
    ACT0076.condition = CON0028
    ACT0076.moving_object = "NLO:CharacterController"
    ACT0076.target_point = PAR0078
    ACT0076.speed = PAR0082
    ACT0076.rot_axis = 2
    ACT0076.front_axis = 1
    PAR0077.game_object = "NLO:D"
    PAR0077.attribute_name = "worldPosition"
    PAR0078.game_object = "NLO:WA"
    PAR0078.attribute_name = "worldPosition"
    PAR0079.game_object = "NLO:DW"
    PAR0079.attribute_name = "worldPosition"
    PAR0080.game_object = "NLO:AS"
    PAR0080.attribute_name = "worldPosition"
    PAR0081.game_object = "NLO:SD"
    PAR0081.attribute_name = "worldPosition"
    PAR0082.game_object = "NLO:CharacterController"
    PAR0082.property_name = "rotSpeed"
    PAR0083.game_object = "NLO:W"
    PAR0083.attribute_name = "worldPosition"
    ACT0084.condition = CON0012
    ACT0084.moving_object = "NLO:CharacterController"
    ACT0084.target_point = PAR0083
    ACT0084.speed = PAR0082
    ACT0084.rot_axis = 2
    ACT0084.front_axis = 1
    network.add_cell(CON0000)
    network.add_cell(CON0002)
    network.add_cell(CON0004)
    network.add_cell(PAR0010)
    network.add_cell(CON0012)
    network.add_cell(CON0014)
    network.add_cell(CON0016)
    network.add_cell(CON0018)
    network.add_cell(CON0028)
    network.add_cell(CON0033)
    network.add_cell(CON0036)
    network.add_cell(PAR0044)
    network.add_cell(CON0047)
    network.add_cell(CON0051)
    network.add_cell(CON0053)
    network.add_cell(CON0055)
    network.add_cell(CON0060)
    network.add_cell(CON0062)
    network.add_cell(CON0065)
    network.add_cell(PAR0068)
    network.add_cell(PAR0077)
    network.add_cell(PAR0079)
    network.add_cell(PAR0081)
    network.add_cell(PAR0083)
    network.add_cell(CON0001)
    network.add_cell(CON0005)
    network.add_cell(PAR0011)
    network.add_cell(CON0017)
    network.add_cell(CON0023)
    network.add_cell(CON0029)
    network.add_cell(ACT0034)
    network.add_cell(ACT0037)
    network.add_cell(ACT0042)
    network.add_cell(CON0045)
    network.add_cell(CON0048)
    network.add_cell(CON0050)
    network.add_cell(CON0054)
    network.add_cell(ACT0061)
    network.add_cell(CON0066)
    network.add_cell(PAR0069)
    network.add_cell(PAR0078)
    network.add_cell(PAR0082)
    network.add_cell(CON0003)
    network.add_cell(PAR0009)
    network.add_cell(CON0020)
    network.add_cell(ACT0038)
    network.add_cell(ACT0046)
    network.add_cell(CON0052)
    network.add_cell(CON0063)
    network.add_cell(ACT0067)
    network.add_cell(ACT0072)
    network.add_cell(ACT0074)
    network.add_cell(ACT0076)
    network.add_cell(ACT0084)
    network.add_cell(ACT0008)
    network.add_cell(CON0019)
    network.add_cell(CON0022)
    network.add_cell(CON0049)
    network.add_cell(ACT0057)
    network.add_cell(ACT0064)
    network.add_cell(ACT0073)
    network.add_cell(PAR0080)
    network.add_cell(CON0013)
    network.add_cell(CON0021)
    network.add_cell(CON0030)
    network.add_cell(ACT0043)
    network.add_cell(ACT0058)
    network.add_cell(ACT0071)
    network.add_cell(CON0015)
    network.add_cell(CON0031)
    network.add_cell(CON0056)
    network.add_cell(ACT0070)
    network.add_cell(CON0007)
    network.add_cell(ACT0059)
    network.add_cell(CON0006)
    network.add_cell(ACT0035)
    network.add_cell(ACT0041)
    network.add_cell(CON0024)
    network.add_cell(CON0032)
    network.add_cell(ACT0075)
    network.add_cell(CON0025)
    network.add_cell(ACT0027)
    network.add_cell(ACT0026)
    network.add_cell(ACT0039)
    network.add_cell(ACT0040)
    owner["IGNLTree_basicMovement"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__basicMovement')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_basicMovement")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
