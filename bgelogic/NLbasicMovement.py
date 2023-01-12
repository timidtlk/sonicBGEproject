# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    PAR0000 = nodes.ParameterObjectAttribute()
    PAR0001 = nodes.ParameterObjectAttribute()
    ACT0002 = nodes.ActionRotateTo()
    ACT0003 = nodes.ActionRotateTo()
    ACT0004 = nodes.ActionRotateTo()
    ACT0005 = nodes.ActionRotateTo()
    ACT0006 = nodes.ActionRotateTo()
    ACT0007 = nodes.ActionRotateTo()
    PAR0008 = nodes.ParameterObjectAttribute()
    PAR0009 = nodes.ParameterObjectAttribute()
    PAR0010 = nodes.ParameterObjectAttribute()
    PAR0011 = nodes.ParameterObjectAttribute()
    PAR0012 = nodes.ParameterObjectAttribute()
    PAR0013 = nodes.ParameterObjectProperty()
    PAR0014 = nodes.ParameterObjectAttribute()
    ACT0015 = nodes.ActionRotateTo()
    CON0016 = nodes.ConditionOrList()
    CON0017 = nodes.ConditionNot()
    ACT0018 = nodes.ActionSetGameObjectGameProperty()
    CON0019 = nodes.ConditionAnd()
    CON0020 = nodes.ConditionAnd()
    CON0021 = nodes.ConditionAnd()
    CON0022 = nodes.ConditionAnd()
    CON0023 = nodes.ConditionAnd()
    CON0024 = nodes.ObjectPropertyOperator()
    ACT0025 = nodes.ActionSetGameObjectGameProperty()
    ACT0026 = nodes.ActionSetGameObjectGameProperty()
    ACT0027 = nodes.ActionSetGameObjectGameProperty()
    ACT0028 = nodes.ActionAddToGameObjectGameProperty()
    ACT0029 = nodes.ActionTimeFilter()
    ACT0030 = nodes.ActionSetGameObjectGameProperty()
    ACT0031 = nodes.ActionSetPhysics()
    ACT0032 = nodes.ActionSetPhysics()
    CON0033 = nodes.ConditionAnd()
    CON0034 = nodes.ConditionNot()
    ACT0035 = nodes.ActionApplyLocation()
    CON0036 = nodes.ObjectPropertyOperator()
    ACT0037 = nodes.ActionSetGameObjectGameProperty()
    ACT0038 = nodes.ActionSetGameObjectGameProperty()
    CON0039 = nodes.ObjectPropertyOperator()
    ACT0040 = nodes.ActionSetGameObjectGameProperty()
    CON0041 = nodes.ObjectPropertyOperator()
    ACT0042 = nodes.ActionSetGameObjectGameProperty()
    CON0043 = nodes.ObjectPropertyOperator()
    ACT0044 = nodes.ActionSetGameObjectGameProperty()
    CON0045 = nodes.ObjectPropertyOperator()
    CON0046 = nodes.ObjectPropertyOperator()
    CON0047 = nodes.ConditionAndList()
    CON0048 = nodes.ObjectPropertyOperator()
    CON0049 = nodes.ObjectPropertyOperator()
    CON0050 = nodes.ConditionAndList()
    CON0051 = nodes.ObjectPropertyOperator()
    CON0052 = nodes.ConditionAndList()
    CON0053 = nodes.ObjectPropertyOperator()
    CON0054 = nodes.ConditionAndList()
    CON0055 = nodes.ConditionAndList()
    CON0056 = nodes.ObjectPropertyOperator()
    CON0057 = nodes.ObjectPropertyOperator()
    CON0058 = nodes.ObjectPropertyOperator()
    ACT0059 = nodes.ActionSetGameObjectGameProperty()
    CON0060 = nodes.ObjectPropertyOperator()
    ACT0061 = nodes.ActionApplyForce()
    ACT0062 = nodes.ActionSetGameObjectGameProperty()
    ACT0063 = nodes.ActionSetGameObjectGameProperty()
    CON0064 = nodes.ConditionNot()
    CON0065 = nodes.ConditionAndList()
    CON0066 = nodes.ObjectPropertyOperator()
    CON0067 = nodes.ObjectPropertyOperator()
    PAR0068 = nodes.ParameterObjectProperty()
    CON0069 = nodes.ObjectPropertyOperator()
    CON0070 = nodes.ObjectPropertyOperator()
    CON0071 = nodes.ObjectPropertyOperator()
    ACT0072 = nodes.ActionSetGameObjectGameProperty()
    ACT0073 = nodes.ActionSetGameObjectGameProperty()
    ACT0074 = nodes.ActionTimeDelay()
    CON0075 = nodes.ConditionOr()
    ACT0076 = nodes.ActionRotateTo()
    ACT0077 = nodes.ActionTimeFilter()
    CON0078 = nodes.ObjectPropertyOperator()
    ACT0079 = nodes.ActionAddToGameObjectGameProperty()
    CON0080 = nodes.ConditionOnUpdate()
    CON0081 = nodes.ObjectPropertyOperator()
    CON0082 = nodes.ConditionOr()
    CON0083 = nodes.ConditionAnd()
    PAR0084 = nodes.ParameterArithmeticOp()
    PAR0085 = nodes.ParameterVector3Simple()
    PAR0086 = nodes.ParameterObjectProperty()
    CON0087 = nodes.ConditionKeyPressed()
    CON0088 = nodes.ConditionKeyPressed()
    CON0089 = nodes.ConditionKeyPressed()
    CON0090 = nodes.ConditionOrList()
    CON0091 = nodes.ObjectPropertyOperator()
    CON0092 = nodes.ConditionKeyPressed()
    CON0093 = nodes.ObjectPropertyOperator()
    CON0094 = nodes.ObjectPropertyOperator()
    CON0095 = nodes.ObjectPropertyOperator()
    CON0096 = nodes.ConditionOr()
    CON0097 = nodes.ConditionAndList()
    CON0098 = nodes.ObjectPropertyOperator()
    CON0099 = nodes.ObjectPropertyOperator()
    ACT0100 = nodes.ActionSetGameObjectGameProperty()
    PAR0101 = nodes.GESetOverlayCollection()
    CON0102 = nodes.ConditionCollision()
    CON0103 = nodes.ObjectPropertyOperator()
    PAR0104 = nodes.ParameterObjectAttribute()
    PAR0105 = nodes.ParameterObjectAttribute()
    CON0106 = nodes.ConditionOnUpdate()
    ACT0107 = nodes.ActionRayPick()
    ACT0108 = nodes.ActionSetGameObjectGameProperty()
    CON0109 = nodes.ConditionAnd()
    ACT0110 = nodes.ActionSetGameObjectGameProperty()
    PAR0000.game_object = "NLO:A"
    PAR0000.attribute_name = "worldPosition"
    PAR0001.game_object = "NLO:S"
    PAR0001.attribute_name = "worldPosition"
    ACT0002.condition = CON0022
    ACT0002.moving_object = "NLO:CharacterController"
    ACT0002.target_point = PAR0011
    ACT0002.speed = PAR0013
    ACT0002.rot_axis = 2
    ACT0002.front_axis = 1
    ACT0003.condition = CON0020
    ACT0003.moving_object = "NLO:CharacterController"
    ACT0003.target_point = PAR0010
    ACT0003.speed = PAR0013
    ACT0003.rot_axis = 2
    ACT0003.front_axis = 1
    ACT0004.condition = CON0092
    ACT0004.moving_object = "NLO:CharacterController"
    ACT0004.target_point = PAR0008
    ACT0004.speed = PAR0013
    ACT0004.rot_axis = 2
    ACT0004.front_axis = 1
    ACT0005.condition = CON0089
    ACT0005.moving_object = "NLO:CharacterController"
    ACT0005.target_point = PAR0000
    ACT0005.speed = PAR0013
    ACT0005.rot_axis = 2
    ACT0005.front_axis = 1
    ACT0006.condition = CON0088
    ACT0006.moving_object = "NLO:CharacterController"
    ACT0006.target_point = PAR0001
    ACT0006.speed = PAR0013
    ACT0006.rot_axis = 2
    ACT0006.front_axis = 1
    ACT0007.condition = CON0019
    ACT0007.moving_object = "NLO:CharacterController"
    ACT0007.target_point = PAR0009
    ACT0007.speed = PAR0013
    ACT0007.rot_axis = 2
    ACT0007.front_axis = 1
    PAR0008.game_object = "NLO:D"
    PAR0008.attribute_name = "worldPosition"
    PAR0009.game_object = "NLO:WA"
    PAR0009.attribute_name = "worldPosition"
    PAR0010.game_object = "NLO:DW"
    PAR0010.attribute_name = "worldPosition"
    PAR0011.game_object = "NLO:AS"
    PAR0011.attribute_name = "worldPosition"
    PAR0012.game_object = "NLO:SD"
    PAR0012.attribute_name = "worldPosition"
    PAR0013.game_object = "NLO:CharacterController"
    PAR0013.property_name = "rotSpeed"
    PAR0014.game_object = "NLO:W"
    PAR0014.attribute_name = "worldPosition"
    ACT0015.condition = CON0087
    ACT0015.moving_object = "NLO:CharacterController"
    ACT0015.target_point = PAR0014
    ACT0015.speed = PAR0013
    ACT0015.rot_axis = 2
    ACT0015.front_axis = 1
    CON0016.ca = CON0019
    CON0016.cb = CON0020
    CON0016.cc = CON0022
    CON0016.cd = CON0021
    CON0016.ce = None
    CON0016.cf = None
    CON0017.condition = CON0023
    ACT0018.condition = CON0023
    ACT0018.game_object = "NLO:CharacterController"
    ACT0018.property_name = "max"
    ACT0018.property_value = 1.0
    CON0019.condition_a = CON0087
    CON0019.condition_b = CON0089
    CON0020.condition_a = CON0087
    CON0020.condition_b = CON0092
    CON0021.condition_a = CON0088
    CON0021.condition_b = CON0092
    CON0022.condition_a = CON0088
    CON0022.condition_b = CON0089
    CON0023.condition_a = CON0016
    CON0023.condition_b = CON0024
    CON0024.game_object = "NLO:CharacterController"
    CON0024.property_name = "isBoosting"
    CON0024.compare_value = False
    CON0024.operator = 0
    ACT0025.condition = ACT0079.OUT
    ACT0025.game_object = "NLO:U_O"
    ACT0025.property_name = "isAccelerating"
    ACT0025.property_value = False
    ACT0026.condition = ACT0028.OUT
    ACT0026.game_object = "NLO:U_O"
    ACT0026.property_name = "isAccelerating"
    ACT0026.property_value = True
    ACT0027.condition = ACT0026.OUT
    ACT0027.game_object = "NLO:U_O"
    ACT0027.property_name = "max"
    ACT0027.property_value = 1.0
    ACT0028.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("ADD")
    ACT0028.condition = ACT0029
    ACT0028.game_object = "NLO:CharacterController"
    ACT0028.property_name = "Speed"
    ACT0028.property_value = 0.029999999329447746
    ACT0029.condition = CON0097
    ACT0029.delay = 0.019999999552965164
    ACT0030.condition = CON0017
    ACT0030.game_object = "NLO:CharacterController"
    ACT0030.property_name = "max"
    ACT0030.property_value = 1.0
    ACT0031.condition = None
    ACT0031.game_object = "NLO:Plane"
    ACT0031.activate = False
    ACT0031.free_const = False
    ACT0032.condition = CON0033
    ACT0032.game_object = "NLO:Plane"
    ACT0032.activate = True
    ACT0032.free_const = False
    CON0033.condition_a = CON0034
    CON0033.condition_b = CON0060
    CON0034.condition = CON0102
    ACT0035.local = True
    ACT0035.condition = CON0091
    ACT0035.game_object = "NLO:CharacterController"
    ACT0035.movement = PAR0084
    CON0036.game_object = "NLO:CharacterController"
    CON0036.property_name = "Speed"
    CON0036.compare_value = 0.1599999964237213
    CON0036.operator = 2
    ACT0037.condition = CON0050
    ACT0037.game_object = "NLO:CharacterController"
    ACT0037.property_name = "rotSpeed"
    ACT0037.property_value = 9.0
    ACT0038.condition = CON0052
    ACT0038.game_object = "NLO:CharacterController"
    ACT0038.property_name = "rotSpeed"
    ACT0038.property_value = 9.0
    CON0039.game_object = "NLO:CharacterController"
    CON0039.property_name = "Speed"
    CON0039.compare_value = 0.6399999856948853
    CON0039.operator = 5
    ACT0040.condition = CON0054
    ACT0040.game_object = "NLO:CharacterController"
    ACT0040.property_name = "rotSpeed"
    ACT0040.property_value = 9.0
    CON0041.game_object = "NLO:CharacterController"
    CON0041.property_name = "Speed"
    CON0041.compare_value = 0.10000000149011612
    CON0041.operator = 5
    ACT0042.condition = CON0047
    ACT0042.game_object = "NLO:CharacterController"
    ACT0042.property_name = "rotSpeed"
    ACT0042.property_value = 10.0
    CON0043.game_object = "NLO:CharacterController"
    CON0043.property_name = "Speed"
    CON0043.compare_value = 0.6399999856948853
    CON0043.operator = 2
    ACT0044.condition = CON0043
    ACT0044.game_object = "NLO:CharacterController"
    ACT0044.property_name = "rotSpeed"
    ACT0044.property_value = 8.0
    CON0045.game_object = "NLO:CharacterController"
    CON0045.property_name = "Speed"
    CON0045.compare_value = 0.1599999964237213
    CON0045.operator = 5
    CON0046.game_object = "NLO:CharacterController"
    CON0046.property_name = "Speed"
    CON0046.compare_value = 0.10000000149011612
    CON0046.operator = 2
    CON0047.ca = CON0045
    CON0047.cb = CON0046
    CON0047.cc = CON0058
    CON0047.cd = True
    CON0047.ce = True
    CON0047.cf = True
    CON0048.game_object = "NLO:CharacterController"
    CON0048.property_name = "Speed"
    CON0048.compare_value = 0.47999998927116394
    CON0048.operator = 5
    CON0049.game_object = "NLO:CharacterController"
    CON0049.property_name = "Speed"
    CON0049.compare_value = 0.3199999928474426
    CON0049.operator = 2
    CON0050.ca = CON0048
    CON0050.cb = CON0049
    CON0050.cc = CON0058
    CON0050.cd = True
    CON0050.ce = True
    CON0050.cf = True
    CON0051.game_object = "NLO:CharacterController"
    CON0051.property_name = "Speed"
    CON0051.compare_value = 0.3199999928474426
    CON0051.operator = 5
    CON0052.ca = CON0051
    CON0052.cb = CON0036
    CON0052.cc = CON0058
    CON0052.cd = True
    CON0052.ce = True
    CON0052.cf = True
    CON0053.game_object = "NLO:CharacterController"
    CON0053.property_name = "Speed"
    CON0053.compare_value = 0.47999998927116394
    CON0053.operator = 2
    CON0054.ca = CON0039
    CON0054.cb = CON0053
    CON0054.cc = CON0058
    CON0054.cd = True
    CON0054.ce = True
    CON0054.cf = True
    CON0055.ca = CON0041
    CON0055.cb = CON0056
    CON0055.cc = CON0058
    CON0055.cd = True
    CON0055.ce = True
    CON0055.cf = True
    CON0056.game_object = "NLO:CharacterController"
    CON0056.property_name = "Speed"
    CON0056.compare_value = 0.0
    CON0056.operator = 2
    CON0057.game_object = "NLO:CharacterController"
    CON0057.property_name = "isSliding"
    CON0057.compare_value = True
    CON0057.operator = 0
    CON0058.game_object = "NLO:CharacterController"
    CON0058.property_name = "isSliding"
    CON0058.compare_value = False
    CON0058.operator = 0
    ACT0059.condition = CON0057
    ACT0059.game_object = "NLO:CharacterController"
    ACT0059.property_name = "rotSpeed"
    ACT0059.property_value = 2.0
    CON0060.game_object = "NLO:U_O"
    CON0060.property_name = "object"
    CON0060.compare_value = 2.0
    CON0060.operator = 4
    ACT0061.local = False
    ACT0061.condition = ACT0031.OUT
    ACT0061.game_object = "NLO:U_O"
    ACT0061.force = mathutils.Vector((0.0, 0.0, 500.0))
    ACT0062.condition = CON0064
    ACT0062.game_object = "NLO:CharacterController"
    ACT0062.property_name = "max"
    ACT0062.property_value = 1.0
    ACT0063.condition = CON0065
    ACT0063.game_object = "NLO:CharacterController"
    ACT0063.property_name = "Speed"
    ACT0063.property_value = PAR0068
    CON0064.condition = CON0066
    CON0065.ca = CON0069
    CON0065.cb = CON0067
    CON0065.cc = CON0066
    CON0065.cd = True
    CON0065.ce = True
    CON0065.cf = True
    CON0066.game_object = "NLO:CharacterController"
    CON0066.property_name = "isAccelerating"
    CON0066.compare_value = True
    CON0066.operator = 0
    CON0067.game_object = "NLO:CharacterController"
    CON0067.property_name = "isBoosting"
    CON0067.compare_value = False
    CON0067.operator = 0
    PAR0068.game_object = "NLO:CharacterController"
    PAR0068.property_name = "max"
    CON0069.game_object = "NLO:CharacterController"
    CON0069.property_name = "Speed"
    CON0069.compare_value = PAR0068
    CON0069.operator = 2
    CON0070.game_object = "NLO:CharacterController"
    CON0070.property_name = "Speed"
    CON0070.compare_value = 0.0
    CON0070.operator = 3
    CON0071.game_object = "NLO:CharacterController"
    CON0071.property_name = "Speed"
    CON0071.compare_value = 0.029999999329447746
    CON0071.operator = 5
    ACT0072.condition = CON0070
    ACT0072.game_object = "NLO:CharacterController"
    ACT0072.property_name = "Speed"
    ACT0072.property_value = 0.029999999329447746
    ACT0073.condition = ACT0074
    ACT0073.game_object = "NLO:CharacterController"
    ACT0073.property_name = "isSliding"
    ACT0073.property_value = False
    ACT0074.condition = CON0071
    ACT0074.delay = 0.20000000298023224
    CON0075.condition_a = None
    CON0075.condition_b = None
    ACT0076.condition = CON0021
    ACT0076.moving_object = "NLO:CharacterController"
    ACT0076.target_point = PAR0012
    ACT0076.speed = PAR0013
    ACT0076.rot_axis = 2
    ACT0076.front_axis = 1
    ACT0077.condition = CON0078
    ACT0077.delay = 0.019999999552965164
    CON0078.game_object = "NLO:CharacterController"
    CON0078.property_name = "Speed"
    CON0078.compare_value = 0.029999999329447746
    CON0078.operator = 2
    ACT0079.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("SUB")
    ACT0079.condition = ACT0077
    ACT0079.game_object = "NLO:CharacterController"
    ACT0079.property_name = "Speed"
    ACT0079.property_value = 0.009999999776482582
    CON0081.game_object = "NLO:CharacterController"
    CON0081.property_name = "Speed"
    CON0081.compare_value = 0.029999999329447746
    CON0081.operator = 2
    CON0082.condition_a = CON0094
    CON0082.condition_b = CON0093
    CON0083.condition_a = CON0090
    CON0083.condition_b = CON0095
    PAR0084.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0084.operand_a = PAR0085.OUTV
    PAR0084.operand_b = PAR0086
    PAR0085.input_x = 0.0
    PAR0085.input_y = CON0081
    PAR0085.input_z = 0.0
    PAR0086.game_object = "NLO:CharacterController"
    PAR0086.property_name = "Speed"
    CON0087.key_code = bge.events.WKEY
    CON0087.pulse = True
    CON0088.key_code = bge.events.SKEY
    CON0088.pulse = True
    CON0089.key_code = bge.events.AKEY
    CON0089.pulse = True
    CON0090.ca = CON0087
    CON0090.cb = CON0088
    CON0090.cc = CON0089
    CON0090.cd = CON0092
    CON0090.ce = None
    CON0090.cf = None
    CON0091.game_object = "NLO:CharacterController"
    CON0091.property_name = "Speed"
    CON0091.compare_value = 0.029999999329447746
    CON0091.operator = 2
    CON0092.key_code = bge.events.DKEY
    CON0092.pulse = True
    CON0093.game_object = "NLO:CharacterController"
    CON0093.property_name = "value_leftright"
    CON0093.compare_value = 0.0
    CON0093.operator = 1
    CON0094.game_object = "NLO:U_O"
    CON0094.property_name = "value_updown"
    CON0094.compare_value = 0.0
    CON0094.operator = 1
    CON0095.game_object = "NLO:CharacterController"
    CON0095.property_name = "isBoosting"
    CON0095.compare_value = False
    CON0095.operator = 0
    CON0096.condition_a = CON0083
    CON0096.condition_b = CON0082
    CON0097.ca = CON0096
    CON0097.cb = CON0099
    CON0097.cc = True
    CON0097.cd = True
    CON0097.ce = True
    CON0097.cf = True
    CON0098.game_object = "NLO:CharacterController"
    CON0098.property_name = "isStomping"
    CON0098.compare_value = False
    CON0098.operator = 0
    CON0099.game_object = "NLO:CharacterController"
    CON0099.property_name = "isSliding"
    CON0099.compare_value = False
    CON0099.operator = 0
    ACT0100.condition = CON0055
    ACT0100.game_object = "NLO:CharacterController"
    ACT0100.property_name = "rotSpeed"
    ACT0100.property_value = 10.0
    PAR0101.condition = CON0080
    PAR0101.camera = "NLO:Camera"
    PAR0101.collection = "infront"
    CON0102.game_object = "NLO:groundSensor"
    CON0102.use_mat = False
    CON0102.prop = "preventclipping"
    CON0102.material = None
    CON0102.pulse = True
    CON0103.game_object = "NLO:CharacterController"
    CON0103.property_name = "Speed"
    CON0103.compare_value = 0.20000000298023224
    CON0103.operator = 2
    PAR0104.game_object = "NLO:CharacterController"
    PAR0104.attribute_name = "worldPosition"
    PAR0105.game_object = "NLO:RayFrente"
    PAR0105.attribute_name = "worldPosition"
    ACT0107.condition = CON0106
    ACT0107.origin = PAR0104
    ACT0107.destination = PAR0105
    ACT0107.local = False
    ACT0107.property_name = "obstacle"
    ACT0107.xray = False
    ACT0107.custom_dist = False
    ACT0107.distance = 100.0
    ACT0107.visualize = False
    ACT0108.condition = CON0109
    ACT0108.game_object = "NLO:CharacterController"
    ACT0108.property_name = "Speed"
    ACT0108.property_value = 0.20000000298023224
    CON0109.condition_a = ACT0107
    CON0109.condition_b = CON0103
    ACT0110.condition = CON0109
    ACT0110.game_object = "NLO:CharacterController"
    ACT0110.property_name = "isBoosting"
    ACT0110.property_value = False
    network.add_cell(PAR0000)
    network.add_cell(PAR0008)
    network.add_cell(PAR0010)
    network.add_cell(PAR0012)
    network.add_cell(PAR0014)
    network.add_cell(CON0024)
    network.add_cell(ACT0031)
    network.add_cell(CON0036)
    network.add_cell(CON0039)
    network.add_cell(CON0041)
    network.add_cell(CON0043)
    network.add_cell(CON0045)
    network.add_cell(CON0048)
    network.add_cell(CON0051)
    network.add_cell(CON0053)
    network.add_cell(CON0056)
    network.add_cell(CON0058)
    network.add_cell(CON0060)
    network.add_cell(CON0066)
    network.add_cell(PAR0068)
    network.add_cell(CON0070)
    network.add_cell(ACT0072)
    network.add_cell(CON0075)
    network.add_cell(CON0078)
    network.add_cell(CON0080)
    network.add_cell(PAR0086)
    network.add_cell(CON0088)
    network.add_cell(CON0091)
    network.add_cell(CON0093)
    network.add_cell(CON0095)
    network.add_cell(CON0098)
    network.add_cell(PAR0101)
    network.add_cell(CON0103)
    network.add_cell(PAR0105)
    network.add_cell(PAR0001)
    network.add_cell(PAR0009)
    network.add_cell(PAR0013)
    network.add_cell(ACT0044)
    network.add_cell(CON0049)
    network.add_cell(CON0052)
    network.add_cell(CON0055)
    network.add_cell(ACT0061)
    network.add_cell(CON0064)
    network.add_cell(CON0067)
    network.add_cell(CON0071)
    network.add_cell(ACT0074)
    network.add_cell(ACT0077)
    network.add_cell(CON0081)
    network.add_cell(PAR0085)
    network.add_cell(CON0089)
    network.add_cell(CON0092)
    network.add_cell(CON0099)
    network.add_cell(CON0102)
    network.add_cell(CON0106)
    network.add_cell(ACT0004)
    network.add_cell(ACT0006)
    network.add_cell(PAR0011)
    network.add_cell(CON0021)
    network.add_cell(CON0034)
    network.add_cell(ACT0038)
    network.add_cell(CON0046)
    network.add_cell(CON0050)
    network.add_cell(CON0057)
    network.add_cell(ACT0062)
    network.add_cell(CON0069)
    network.add_cell(ACT0076)
    network.add_cell(PAR0084)
    network.add_cell(CON0094)
    network.add_cell(ACT0100)
    network.add_cell(ACT0005)
    network.add_cell(CON0022)
    network.add_cell(CON0033)
    network.add_cell(ACT0037)
    network.add_cell(CON0047)
    network.add_cell(ACT0059)
    network.add_cell(CON0065)
    network.add_cell(ACT0079)
    network.add_cell(CON0087)
    network.add_cell(PAR0104)
    network.add_cell(ACT0002)
    network.add_cell(ACT0015)
    network.add_cell(CON0019)
    network.add_cell(ACT0025)
    network.add_cell(ACT0032)
    network.add_cell(ACT0042)
    network.add_cell(ACT0063)
    network.add_cell(CON0082)
    network.add_cell(CON0090)
    network.add_cell(ACT0107)
    network.add_cell(CON0109)
    network.add_cell(ACT0007)
    network.add_cell(CON0020)
    network.add_cell(ACT0035)
    network.add_cell(CON0054)
    network.add_cell(CON0083)
    network.add_cell(ACT0108)
    network.add_cell(ACT0003)
    network.add_cell(ACT0040)
    network.add_cell(CON0096)
    network.add_cell(ACT0110)
    network.add_cell(CON0016)
    network.add_cell(CON0023)
    network.add_cell(ACT0073)
    network.add_cell(CON0017)
    network.add_cell(ACT0030)
    network.add_cell(ACT0018)
    network.add_cell(CON0097)
    network.add_cell(ACT0029)
    network.add_cell(ACT0028)
    network.add_cell(ACT0026)
    network.add_cell(ACT0027)
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
