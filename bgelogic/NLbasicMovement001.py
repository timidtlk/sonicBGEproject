# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionRotateTo()
    ACT0001 = nodes.ActionRotateTo()
    ACT0002 = nodes.ActionRotateTo()
    ACT0003 = nodes.ActionRotateTo()
    ACT0004 = nodes.ActionRotateTo()
    ACT0005 = nodes.ActionRotateTo()
    ACT0006 = nodes.ActionRotateTo()
    ACT0007 = nodes.ActionRotateTo()
    PAR0008 = nodes.ParameterObjectAttribute()
    PAR0009 = nodes.ParameterObjectAttribute()
    PAR0010 = nodes.ParameterObjectAttribute()
    PAR0011 = nodes.ParameterObjectProperty()
    PAR0012 = nodes.ParameterObjectAttribute()
    PAR0013 = nodes.ParameterObjectAttribute()
    PAR0014 = nodes.ParameterObjectAttribute()
    PAR0015 = nodes.ParameterObjectAttribute()
    PAR0016 = nodes.ParameterObjectAttribute()
    CON0017 = nodes.ConditionAnd()
    CON0018 = nodes.ConditionAnd()
    CON0019 = nodes.ConditionAnd()
    CON0020 = nodes.ConditionAnd()
    CON0021 = nodes.ConditionOrList()
    CON0022 = nodes.ConditionNot()
    ACT0023 = nodes.ActionSetGameObjectGameProperty()
    ACT0024 = nodes.ActionSetGameObjectGameProperty()
    CON0025 = nodes.ConditionKeyPressed()
    CON0026 = nodes.ConditionKeyPressed()
    CON0027 = nodes.ConditionKeyPressed()
    CON0028 = nodes.ConditionOrList()
    CON0029 = nodes.ConditionAnd()
    CON0030 = nodes.ConditionKeyPressed()
    CON0031 = nodes.ConditionAnd()
    ACT0032 = nodes.ActionAddToGameObjectGameProperty()
    ACT0033 = nodes.ActionSetGameObjectGameProperty()
    CON0034 = nodes.ObjectPropertyOperator()
    ACT0035 = nodes.ActionSetGameObjectGameProperty()
    CON0036 = nodes.ObjectPropertyOperator()
    PAR0037 = nodes.ParameterObjectProperty()
    ACT0038 = nodes.ActionAddToGameObjectGameProperty()
    ACT0039 = nodes.ActionAddToGameObjectGameProperty()
    ACT0040 = nodes.ActionTimeFilter()
    CON0041 = nodes.ConditionNot()
    ACT0042 = nodes.ActionTimeFilter()
    PAR0043 = nodes.ParameterVector3Simple()
    CON0044 = nodes.ConditionOrList()
    PAR0045 = nodes.ParameterArithmeticOp()
    CON0046 = nodes.ConditionKeyPressed()
    CON0047 = nodes.ConditionKeyPressed()
    CON0048 = nodes.ConditionKeyPressed()
    CON0049 = nodes.ConditionKeyPressed()
    PAR0050 = nodes.ParameterObjectProperty()
    CON0051 = nodes.ObjectPropertyOperator()
    ACT0052 = nodes.ActionApplyLocation()
    CON0053 = nodes.ObjectPropertyOperator()
    ACT0054 = nodes.ActionSetGameObjectGameProperty()
    CON0055 = nodes.ObjectPropertyOperator()
    ACT0056 = nodes.ActionSetGameObjectGameProperty()
    CON0057 = nodes.ObjectPropertyOperator()
    CON0058 = nodes.ObjectPropertyOperator()
    CON0059 = nodes.ConditionAnd()
    CON0060 = nodes.ConditionAnd()
    CON0061 = nodes.ObjectPropertyOperator()
    ACT0062 = nodes.ActionSetGameObjectGameProperty()
    CON0063 = nodes.ObjectPropertyOperator()
    CON0064 = nodes.ConditionAnd()
    CON0065 = nodes.ObjectPropertyOperator()
    ACT0066 = nodes.ActionSetGameObjectGameProperty()
    ACT0067 = nodes.ActionSetGameObjectGameProperty()
    CON0068 = nodes.ObjectPropertyOperator()
    CON0069 = nodes.ObjectPropertyOperator()
    CON0070 = nodes.ConditionAnd()
    CON0071 = nodes.ObjectPropertyOperator()
    CON0072 = nodes.ConditionAnd()
    ACT0073 = nodes.ActionSetGameObjectGameProperty()
    CON0074 = nodes.ObjectPropertyOperator()
    CON0075 = nodes.ObjectPropertyOperator()
    CON0076 = nodes.ConditionAnd()
    ACT0077 = nodes.ActionSetObjectAttribute()
    ACT0078 = nodes.ActionAlignAxisToVector()
    CON0079 = nodes.ConditionNot()
    ACT0080 = nodes.ActionRayPick()
    PAR0081 = nodes.ParameterObjectAttribute()
    PAR0082 = nodes.ParameterObjectAttribute()
    CON0083 = nodes.ConditionOnUpdate()
    ACT0084 = nodes.ActionSetGameObjectGameProperty()
    CON0085 = nodes.ObjectPropertyOperator()
    CON0086 = nodes.ObjectPropertyOperator()
    CON0087 = nodes.ObjectPropertyOperator()
    CON0088 = nodes.ConditionOrList()
    ACT0089 = nodes.ActionTimeFilter()
    CON0090 = nodes.ConditionAnd()
    ACT0091 = nodes.ActionApplyForce()
    CON0092 = nodes.ObjectPropertyOperator()
    CON0093 = nodes.ConditionKeyPressed()
    ACT0094 = nodes.ActionSetGameObjectVisibility()
    ACT0095 = nodes.ActionSetGameObjectVisibility()
    CON0096 = nodes.ObjectPropertyOperator()
    CON0097 = nodes.ConditionAnd()
    ACT0098 = nodes.ActionApplyForce()
    CON0099 = nodes.ConditionAnd()
    CON0100 = nodes.ConditionKeyPressed()
    ACT0101 = nodes.ActionApplyForce()
    ACT0102 = nodes.ActionSetGameObjectGameProperty()
    ACT0103 = nodes.ActionSetGameObjectGameProperty()
    CON0104 = nodes.ConditionAnd()
    CON0105 = nodes.ObjectPropertyOperator()
    CON0106 = nodes.ConditionAnd()
    CON0107 = nodes.ObjectPropertyOperator()
    ACT0108 = nodes.ActionSetGameObjectVisibility()
    ACT0109 = nodes.ActionSetGameObjectGameProperty()
    ACT0110 = nodes.ActionAddToGameObjectGameProperty()
    ACT0111 = nodes.ActionSetGameObjectGameProperty()
    CON0112 = nodes.ObjectPropertyOperator()
    ACT0113 = nodes.ActionSetGameObjectGameProperty()
    CON0114 = nodes.ConditionAnd()
    CON0115 = nodes.ObjectPropertyOperator()
    ACT0116 = nodes.ActionSetGameObjectGameProperty()
    ACT0117 = nodes.ActionSetGameObjectGameProperty()
    CON0118 = nodes.ConditionAnd()
    ACT0119 = nodes.ActionSetGameObjectGameProperty()
    CON0120 = nodes.ConditionAnd()
    CON0121 = nodes.ConditionCollision()
    CON0122 = nodes.ConditionCollision()
    CON0123 = nodes.ConditionNot()
    ACT0124 = nodes.ActionSetGameObjectVisibility()
    CON0125 = nodes.ConditionOr()
    CON0126 = nodes.ObjectPropertyOperator()
    CON0127 = nodes.ObjectPropertyOperator()
    CON0128 = nodes.ObjectPropertyOperator()
    ACT0000.condition = CON0017
    ACT0000.moving_object = "NLO:CharacterController.001"
    ACT0000.target_point = PAR0014
    ACT0000.speed = PAR0011
    ACT0000.rot_axis = 2
    ACT0000.front_axis = 1
    ACT0001.condition = CON0019
    ACT0001.moving_object = "NLO:CharacterController.001"
    ACT0001.target_point = PAR0016
    ACT0001.speed = PAR0011
    ACT0001.rot_axis = 2
    ACT0001.front_axis = 1
    ACT0002.condition = CON0018
    ACT0002.moving_object = "NLO:CharacterController.001"
    ACT0002.target_point = PAR0013
    ACT0002.speed = PAR0011
    ACT0002.rot_axis = 2
    ACT0002.front_axis = 1
    ACT0003.condition = CON0020
    ACT0003.moving_object = "NLO:CharacterController.001"
    ACT0003.target_point = PAR0012
    ACT0003.speed = PAR0011
    ACT0003.rot_axis = 2
    ACT0003.front_axis = 1
    ACT0004.condition = CON0047
    ACT0004.moving_object = "NLO:CharacterController.001"
    ACT0004.target_point = PAR0010
    ACT0004.speed = PAR0011
    ACT0004.rot_axis = 2
    ACT0004.front_axis = 1
    ACT0005.condition = CON0046
    ACT0005.moving_object = "NLO:CharacterController.001"
    ACT0005.target_point = PAR0009
    ACT0005.speed = PAR0011
    ACT0005.rot_axis = 2
    ACT0005.front_axis = 1
    ACT0006.condition = CON0048
    ACT0006.moving_object = "NLO:CharacterController.001"
    ACT0006.target_point = PAR0008
    ACT0006.speed = PAR0011
    ACT0006.rot_axis = 2
    ACT0006.front_axis = 1
    ACT0007.condition = CON0049
    ACT0007.moving_object = "NLO:CharacterController.001"
    ACT0007.target_point = PAR0015
    ACT0007.speed = PAR0011
    ACT0007.rot_axis = 2
    ACT0007.front_axis = 1
    PAR0008.game_object = "NLO:S.001"
    PAR0008.attribute_name = "worldPosition"
    PAR0009.game_object = "NLO:A.001"
    PAR0009.attribute_name = "worldPosition"
    PAR0010.game_object = "NLO:D.001"
    PAR0010.attribute_name = "worldPosition"
    PAR0011.game_object = "NLO:CharacterController.001"
    PAR0011.property_name = "rotSpeed"
    PAR0012.game_object = "NLO:WA.001"
    PAR0012.attribute_name = "worldPosition"
    PAR0013.game_object = "NLO:DW.001"
    PAR0013.attribute_name = "worldPosition"
    PAR0014.game_object = "NLO:AS.001"
    PAR0014.attribute_name = "worldPosition"
    PAR0015.game_object = "NLO:W.001"
    PAR0015.attribute_name = "worldPosition"
    PAR0016.game_object = "NLO:SD.001"
    PAR0016.attribute_name = "worldPosition"
    CON0017.condition_a = CON0048
    CON0017.condition_b = CON0046
    CON0018.condition_a = CON0049
    CON0018.condition_b = CON0047
    CON0019.condition_a = CON0048
    CON0019.condition_b = CON0047
    CON0020.condition_a = CON0049
    CON0020.condition_b = CON0046
    CON0021.ca = CON0020
    CON0021.cb = CON0018
    CON0021.cc = CON0017
    CON0021.cd = CON0019
    CON0021.ce = None
    CON0021.cf = None
    CON0022.condition = CON0021
    ACT0023.condition = CON0021
    ACT0023.game_object = "NLO:CharacterController.001"
    ACT0023.property_name = "max"
    ACT0023.property_value = 0.800000011920929
    ACT0024.condition = CON0022
    ACT0024.game_object = "NLO:CharacterController.001"
    ACT0024.property_name = "max"
    ACT0024.property_value = 0.800000011920929
    CON0025.key_code = bge.events.SKEY
    CON0025.pulse = False
    CON0026.key_code = bge.events.AKEY
    CON0026.pulse = False
    CON0027.key_code = bge.events.DKEY
    CON0027.pulse = False
    CON0028.ca = CON0030
    CON0028.cb = CON0025
    CON0028.cc = CON0026
    CON0028.cd = CON0027
    CON0028.ce = CON0031
    CON0028.cf = CON0029
    CON0029.condition_a = CON0026
    CON0029.condition_b = CON0027
    CON0030.key_code = bge.events.WKEY
    CON0030.pulse = False
    CON0031.condition_a = CON0030
    CON0031.condition_b = CON0025
    ACT0032.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("SUB")
    ACT0032.condition = CON0028
    ACT0032.game_object = "NLO:CharacterController.001"
    ACT0032.property_name = "Speed"
    ACT0032.property_value = 0.10000000149011612
    ACT0033.condition = CON0034
    ACT0033.game_object = "NLO:CharacterController.001"
    ACT0033.property_name = "Speed"
    ACT0033.property_value = PAR0037
    CON0034.game_object = "NLO:CharacterController.001"
    CON0034.property_name = "Speed"
    CON0034.compare_value = PAR0037
    CON0034.operator = 2
    ACT0035.condition = CON0036
    ACT0035.game_object = "NLO:CharacterController.001"
    ACT0035.property_name = "Speed"
    ACT0035.property_value = 0.029999999329447746
    CON0036.game_object = "NLO:CharacterController.001"
    CON0036.property_name = "Speed"
    CON0036.compare_value = 0.0
    CON0036.operator = 3
    PAR0037.game_object = "NLO:CharacterController.001"
    PAR0037.property_name = "max"
    ACT0038.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("SUB")
    ACT0038.condition = ACT0040
    ACT0038.game_object = "NLO:CharacterController.001"
    ACT0038.property_name = "Speed"
    ACT0038.property_value = 0.009999999776482582
    ACT0039.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("ADD")
    ACT0039.condition = ACT0042
    ACT0039.game_object = "NLO:CharacterController.001"
    ACT0039.property_name = "Speed"
    ACT0039.property_value = 0.019999999552965164
    ACT0040.condition = CON0041
    ACT0040.delay = 0.019999999552965164
    CON0041.condition = CON0044
    ACT0042.condition = CON0044
    ACT0042.delay = 0.019999999552965164
    PAR0043.input_x = 0.0
    PAR0043.input_y = CON0044
    PAR0043.input_z = 0.0
    CON0044.ca = CON0049
    CON0044.cb = CON0048
    CON0044.cc = CON0046
    CON0044.cd = CON0047
    CON0044.ce = None
    CON0044.cf = None
    PAR0045.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0045.operand_a = PAR0043.OUTV
    PAR0045.operand_b = PAR0050
    CON0046.key_code = bge.events.AKEY
    CON0046.pulse = True
    CON0047.key_code = bge.events.DKEY
    CON0047.pulse = True
    CON0048.key_code = bge.events.SKEY
    CON0048.pulse = True
    CON0049.key_code = bge.events.WKEY
    CON0049.pulse = True
    PAR0050.game_object = "NLO:CharacterController.001"
    PAR0050.property_name = "Speed"
    CON0051.game_object = "NLO:CharacterController.001"
    CON0051.property_name = "Speed"
    CON0051.compare_value = 0.029999999329447746
    CON0051.operator = 2
    ACT0052.local = True
    ACT0052.condition = CON0051
    ACT0052.game_object = "NLO:CharacterController.001"
    ACT0052.movement = PAR0045
    CON0053.game_object = "NLO:CharacterController.001"
    CON0053.property_name = "Speed"
    CON0053.compare_value = 0.47999998927116394
    CON0053.operator = 2
    ACT0054.condition = CON0060
    ACT0054.game_object = "NLO:CharacterController.001"
    ACT0054.property_name = "rotSpeed"
    ACT0054.property_value = 2.0
    CON0055.game_object = "NLO:CharacterController.001"
    CON0055.property_name = "Speed"
    CON0055.compare_value = 0.6399999856948853
    CON0055.operator = 5
    ACT0056.condition = CON0059
    ACT0056.game_object = "NLO:CharacterController.001"
    ACT0056.property_name = "rotSpeed"
    ACT0056.property_value = 4.0
    CON0057.game_object = "NLO:CharacterController.001"
    CON0057.property_name = "Speed"
    CON0057.compare_value = 0.1599999964237213
    CON0057.operator = 2
    CON0058.game_object = "NLO:CharacterController.001"
    CON0058.property_name = "Speed"
    CON0058.compare_value = 0.3199999928474426
    CON0058.operator = 5
    CON0059.condition_a = CON0058
    CON0059.condition_b = CON0057
    CON0060.condition_a = CON0055
    CON0060.condition_b = CON0053
    CON0061.game_object = "NLO:CharacterController.001"
    CON0061.property_name = "Speed"
    CON0061.compare_value = 0.3199999928474426
    CON0061.operator = 2
    ACT0062.condition = CON0064
    ACT0062.game_object = "NLO:CharacterController.001"
    ACT0062.property_name = "rotSpeed"
    ACT0062.property_value = 3.0
    CON0063.game_object = "NLO:CharacterController.001"
    CON0063.property_name = "Speed"
    CON0063.compare_value = 0.47999998927116394
    CON0063.operator = 5
    CON0064.condition_a = CON0063
    CON0064.condition_b = CON0061
    CON0065.game_object = "NLO:CharacterController.001"
    CON0065.property_name = "Speed"
    CON0065.compare_value = 0.10000000149011612
    CON0065.operator = 5
    ACT0066.condition = CON0070
    ACT0066.game_object = "NLO:CharacterController.001"
    ACT0066.property_name = "rotSpeed"
    ACT0066.property_value = 3.0
    ACT0067.condition = CON0072
    ACT0067.game_object = "NLO:CharacterController.001"
    ACT0067.property_name = "rotSpeed"
    ACT0067.property_value = 1.0
    CON0068.game_object = "NLO:CharacterController.001"
    CON0068.property_name = "Speed"
    CON0068.compare_value = 0.0
    CON0068.operator = 2
    CON0069.game_object = "NLO:CharacterController.001"
    CON0069.property_name = "Speed"
    CON0069.compare_value = 0.6399999856948853
    CON0069.operator = 2
    CON0070.condition_a = CON0065
    CON0070.condition_b = CON0068
    CON0071.game_object = "NLO:CharacterController.001"
    CON0071.property_name = "Speed"
    CON0071.compare_value = 0.800000011920929
    CON0071.operator = 5
    CON0072.condition_a = CON0071
    CON0072.condition_b = CON0069
    ACT0073.condition = CON0076
    ACT0073.game_object = "NLO:CharacterController.001"
    ACT0073.property_name = "rotSpeed"
    ACT0073.property_value = 5.0
    CON0074.game_object = "NLO:CharacterController.001"
    CON0074.property_name = "Speed"
    CON0074.compare_value = 0.10000000149011612
    CON0074.operator = 2
    CON0075.game_object = "NLO:CharacterController.001"
    CON0075.property_name = "Speed"
    CON0075.compare_value = 0.1599999964237213
    CON0075.operator = 5
    CON0076.condition_a = CON0075
    CON0076.condition_b = CON0074
    ACT0077.condition = CON0079
    ACT0077.xyz = {'x': True, 'y': True, 'z': False}
    ACT0077.game_object = "NLO:CharacterController.001"
    ACT0077.attribute_value = mathutils.Vector((0.0, 0.0, 0.0))
    ACT0077.value_type = 'worldOrientation'
    ACT0078.local = True
    ACT0078.condition = ACT0080
    ACT0078.game_object = "NLO:CharacterController.001"
    ACT0078.vector = ACT0080.NORMAL
    ACT0078.axis = 2
    ACT0078.factor = 1.0
    CON0079.condition = ACT0080
    ACT0080.condition = CON0083
    ACT0080.origin = PAR0082
    ACT0080.destination = PAR0081
    ACT0080.local = False
    ACT0080.property_name = ""
    ACT0080.xray = False
    ACT0080.custom_dist = False
    ACT0080.distance = 0.0
    ACT0080.visualize = True
    PAR0081.game_object = "NLO:RayRotate.001"
    PAR0081.attribute_name = "worldPosition"
    PAR0082.game_object = "NLO:CharacterController.001"
    PAR0082.attribute_name = "worldPosition"
    ACT0084.condition = ACT0089
    ACT0084.game_object = "NLO:CharacterController.001"
    ACT0084.property_name = "idle"
    ACT0084.property_value = 0.0
    CON0085.game_object = "NLO:CharacterController.001"
    CON0085.property_name = "Speed"
    CON0085.compare_value = 0.029999999329447746
    CON0085.operator = 2
    CON0086.game_object = "NLO:CharacterController.001"
    CON0086.property_name = "isFalling"
    CON0086.compare_value = True
    CON0086.operator = 2
    CON0087.game_object = "NLO:CharacterController.001"
    CON0087.property_name = "isJumping"
    CON0087.compare_value = True
    CON0087.operator = 2
    CON0088.ca = CON0085
    CON0088.cb = CON0087
    CON0088.cc = CON0086
    CON0088.cd = CON0123
    CON0088.ce = None
    CON0088.cf = None
    ACT0089.condition = CON0088
    ACT0089.delay = 0.0
    CON0090.condition_a = CON0092
    CON0090.condition_b = CON0093
    ACT0091.local = True
    ACT0091.condition = CON0090
    ACT0091.game_object = "NLO:CharacterController.001"
    ACT0091.force = mathutils.Vector((0.0, 0.0, 800.0))
    CON0092.game_object = "NLO:CharacterController.001"
    CON0092.property_name = "jump"
    CON0092.compare_value = 1
    CON0092.operator = 0
    CON0093.key_code = bge.events.SPACEKEY
    CON0093.pulse = False
    ACT0094.condition = CON0128
    ACT0094.game_object = "NLO:SonicBall.001"
    ACT0094.visible = True
    ACT0094.recursive = False
    ACT0095.condition = CON0128
    ACT0095.game_object = "NLO:chr_Sonic_HD.003"
    ACT0095.visible = False
    ACT0095.recursive = False
    CON0096.game_object = "NLO:CharacterController.001"
    CON0096.property_name = "jump"
    CON0096.compare_value = 2
    CON0096.operator = 0
    CON0097.condition_a = CON0093
    CON0097.condition_b = CON0096
    ACT0098.local = True
    ACT0098.condition = CON0097
    ACT0098.game_object = "NLO:CharacterController.001"
    ACT0098.force = mathutils.Vector((0.0, 1500.0, 0.0))
    CON0099.condition_a = CON0100
    CON0099.condition_b = CON0105
    CON0100.key_code = bge.events.FKEY
    CON0100.pulse = False
    ACT0101.local = True
    ACT0101.condition = CON0099
    ACT0101.game_object = "NLO:CharacterController.001"
    ACT0101.force = mathutils.Vector((0.0, 0.0, -2000.0))
    ACT0102.condition = CON0104
    ACT0102.game_object = "NLO:CharacterController.001"
    ACT0102.property_name = "isStomping"
    ACT0102.property_value = True
    ACT0103.condition = CON0106
    ACT0103.game_object = "NLO:CharacterController.001"
    ACT0103.property_name = "isStomping"
    ACT0103.property_value = False
    CON0104.condition_a = CON0100
    CON0104.condition_b = CON0123
    CON0105.game_object = "NLO:CharacterController.001"
    CON0105.property_name = "jump"
    CON0105.compare_value = 2
    CON0105.operator = 4
    CON0106.condition_a = CON0121
    CON0106.condition_b = CON0107
    CON0107.game_object = "NLO:CharacterController.001"
    CON0107.property_name = "isStomping"
    CON0107.compare_value = True
    CON0107.operator = 4
    ACT0108.condition = CON0125
    ACT0108.game_object = "NLO:SonicBall.001"
    ACT0108.visible = False
    ACT0108.recursive = False
    ACT0109.condition = CON0122
    ACT0109.game_object = "NLO:CharacterController.001"
    ACT0109.property_name = "jump"
    ACT0109.property_value = 1
    ACT0110.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("ADD")
    ACT0110.condition = CON0093
    ACT0110.game_object = "NLO:CharacterController.001"
    ACT0110.property_name = "jump"
    ACT0110.property_value = 1.0
    ACT0111.condition = CON0093
    ACT0111.game_object = "NLO:CharacterController.001"
    ACT0111.property_name = "isJumping"
    ACT0111.property_value = True
    CON0112.game_object = "NLO:CharacterController.001"
    CON0112.property_name = "jump"
    CON0112.compare_value = 1
    CON0112.operator = 0
    ACT0113.condition = CON0114
    ACT0113.game_object = "NLO:CharacterController.001"
    ACT0113.property_name = "isJumping"
    ACT0113.property_value = False
    CON0114.condition_a = CON0115
    CON0114.condition_b = CON0121
    CON0115.game_object = "NLO:CharacterController.001"
    CON0115.property_name = "jump"
    CON0115.compare_value = 2
    CON0115.operator = 4
    ACT0116.condition = CON0118
    ACT0116.game_object = "NLO:CharacterController.001"
    ACT0116.property_name = "jump"
    ACT0116.property_value = 2
    ACT0117.condition = CON0122
    ACT0117.game_object = "NLO:CharacterController.001"
    ACT0117.property_name = "isFalling"
    ACT0117.property_value = False
    CON0118.condition_a = CON0112
    CON0118.condition_b = CON0123
    ACT0119.condition = CON0120
    ACT0119.game_object = "NLO:CharacterController.001"
    ACT0119.property_name = "isFalling"
    ACT0119.property_value = True
    CON0120.condition_a = CON0079
    CON0120.condition_b = CON0127
    CON0121.game_object = "NLO:groundSensor.001"
    CON0121.use_mat = False
    CON0121.prop = "obstacle"
    CON0121.material = None
    CON0121.pulse = False
    CON0122.game_object = "NLO:groundSensor.001"
    CON0122.use_mat = False
    CON0122.prop = "obstacle"
    CON0122.material = None
    CON0122.pulse = True
    CON0123.condition = CON0122
    ACT0124.condition = CON0125
    ACT0124.game_object = "NLO:chr_Sonic_HD.003"
    ACT0124.visible = True
    ACT0124.recursive = False
    CON0125.condition_a = CON0127
    CON0125.condition_b = CON0126
    CON0126.game_object = "NLO:CharacterController.001"
    CON0126.property_name = "isStomping"
    CON0126.compare_value = True
    CON0126.operator = 0
    CON0127.game_object = "NLO:CharacterController.001"
    CON0127.property_name = "isJumping"
    CON0127.compare_value = False
    CON0127.operator = 0
    CON0128.game_object = "NLO:CharacterController.001"
    CON0128.property_name = "isJumping"
    CON0128.compare_value = True
    CON0128.operator = 0
    network.add_cell(PAR0008)
    network.add_cell(PAR0010)
    network.add_cell(PAR0012)
    network.add_cell(PAR0014)
    network.add_cell(PAR0016)
    network.add_cell(CON0025)
    network.add_cell(CON0027)
    network.add_cell(CON0030)
    network.add_cell(CON0036)
    network.add_cell(CON0046)
    network.add_cell(CON0048)
    network.add_cell(PAR0050)
    network.add_cell(CON0053)
    network.add_cell(CON0055)
    network.add_cell(CON0057)
    network.add_cell(CON0060)
    network.add_cell(CON0063)
    network.add_cell(CON0065)
    network.add_cell(CON0068)
    network.add_cell(CON0070)
    network.add_cell(CON0074)
    network.add_cell(PAR0081)
    network.add_cell(CON0083)
    network.add_cell(CON0085)
    network.add_cell(CON0087)
    network.add_cell(CON0092)
    network.add_cell(CON0096)
    network.add_cell(CON0100)
    network.add_cell(CON0105)
    network.add_cell(CON0107)
    network.add_cell(CON0112)
    network.add_cell(CON0115)
    network.add_cell(CON0121)
    network.add_cell(CON0126)
    network.add_cell(CON0128)
    network.add_cell(PAR0009)
    network.add_cell(PAR0013)
    network.add_cell(CON0017)
    network.add_cell(CON0026)
    network.add_cell(CON0029)
    network.add_cell(ACT0035)
    network.add_cell(CON0047)
    network.add_cell(CON0051)
    network.add_cell(ACT0054)
    network.add_cell(CON0058)
    network.add_cell(CON0061)
    network.add_cell(CON0064)
    network.add_cell(CON0069)
    network.add_cell(CON0075)
    network.add_cell(PAR0082)
    network.add_cell(CON0086)
    network.add_cell(CON0093)
    network.add_cell(ACT0095)
    network.add_cell(CON0099)
    network.add_cell(CON0106)
    network.add_cell(ACT0110)
    network.add_cell(CON0114)
    network.add_cell(CON0122)
    network.add_cell(CON0127)
    network.add_cell(PAR0011)
    network.add_cell(CON0019)
    network.add_cell(CON0031)
    network.add_cell(PAR0037)
    network.add_cell(CON0049)
    network.add_cell(CON0059)
    network.add_cell(ACT0066)
    network.add_cell(CON0071)
    network.add_cell(CON0076)
    network.add_cell(ACT0080)
    network.add_cell(CON0090)
    network.add_cell(ACT0094)
    network.add_cell(ACT0101)
    network.add_cell(ACT0103)
    network.add_cell(ACT0109)
    network.add_cell(ACT0113)
    network.add_cell(ACT0117)
    network.add_cell(CON0123)
    network.add_cell(CON0125)
    network.add_cell(ACT0000)
    network.add_cell(ACT0004)
    network.add_cell(ACT0006)
    network.add_cell(PAR0015)
    network.add_cell(CON0020)
    network.add_cell(CON0028)
    network.add_cell(CON0034)
    network.add_cell(CON0044)
    network.add_cell(ACT0056)
    network.add_cell(CON0072)
    network.add_cell(ACT0078)
    network.add_cell(CON0088)
    network.add_cell(ACT0091)
    network.add_cell(CON0104)
    network.add_cell(ACT0111)
    network.add_cell(CON0118)
    network.add_cell(ACT0124)
    network.add_cell(ACT0001)
    network.add_cell(ACT0003)
    network.add_cell(ACT0007)
    network.add_cell(ACT0032)
    network.add_cell(CON0041)
    network.add_cell(PAR0043)
    network.add_cell(ACT0062)
    network.add_cell(ACT0073)
    network.add_cell(CON0079)
    network.add_cell(ACT0089)
    network.add_cell(ACT0102)
    network.add_cell(ACT0116)
    network.add_cell(CON0120)
    network.add_cell(ACT0005)
    network.add_cell(ACT0033)
    network.add_cell(ACT0040)
    network.add_cell(PAR0045)
    network.add_cell(ACT0067)
    network.add_cell(ACT0084)
    network.add_cell(ACT0108)
    network.add_cell(CON0018)
    network.add_cell(ACT0038)
    network.add_cell(ACT0042)
    network.add_cell(ACT0077)
    network.add_cell(ACT0119)
    network.add_cell(ACT0002)
    network.add_cell(ACT0039)
    network.add_cell(CON0097)
    network.add_cell(CON0021)
    network.add_cell(ACT0023)
    network.add_cell(ACT0052)
    network.add_cell(CON0022)
    network.add_cell(ACT0098)
    network.add_cell(ACT0024)
    owner["IGNLTree_basicMovement.001"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__basicMovement.001')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_basicMovement.001")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
