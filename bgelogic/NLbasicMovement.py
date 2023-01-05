# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    CON0000 = nodes.ConditionAnd()
    CON0001 = nodes.ObjectPropertyOperator()
    ACT0002 = nodes.ActionSetGameObjectVisibility()
    ACT0003 = nodes.ActionSetGameObjectVisibility()
    CON0004 = nodes.ObjectPropertyOperator()
    ACT0005 = nodes.ActionSetGameObjectVisibility()
    ACT0006 = nodes.ActionSetGameObjectVisibility()
    CON0007 = nodes.ConditionOr()
    CON0008 = nodes.ObjectPropertyOperator()
    CON0009 = nodes.ObjectPropertyOperator()
    ACT0010 = nodes.ActionSetGameObjectVisibility()
    ACT0011 = nodes.ActionSetGameObjectVisibility()
    ACT0012 = nodes.ActionSetGameObjectGameProperty()
    ACT0013 = nodes.ActionSetGameObjectGameProperty()
    CON0014 = nodes.ConditionAnd()
    CON0015 = nodes.ConditionAnd()
    ACT0016 = nodes.ActionSetGameObjectGameProperty()
    CON0017 = nodes.ConditionAnd()
    ACT0018 = nodes.ActionSetGameObjectGameProperty()
    CON0019 = nodes.ConditionAnd()
    ACT0020 = nodes.ActionSetGameObjectGameProperty()
    CON0021 = nodes.ConditionAnd()
    ACT0022 = nodes.ActionSetGameObjectGameProperty()
    CON0023 = nodes.ObjectPropertyOperator()
    CON0024 = nodes.ObjectPropertyOperator()
    CON0025 = nodes.ObjectPropertyOperator()
    CON0026 = nodes.ObjectPropertyOperator()
    CON0027 = nodes.ObjectPropertyOperator()
    CON0028 = nodes.ObjectPropertyOperator()
    CON0029 = nodes.ObjectPropertyOperator()
    CON0030 = nodes.ObjectPropertyOperator()
    CON0031 = nodes.ObjectPropertyOperator()
    CON0032 = nodes.ObjectPropertyOperator()
    CON0033 = nodes.ObjectPropertyOperator()
    PAR0034 = nodes.ParameterObjectAttribute()
    PAR0035 = nodes.ParameterObjectAttribute()
    PAR0036 = nodes.ParameterObjectAttribute()
    PAR0037 = nodes.ParameterObjectAttribute()
    PAR0038 = nodes.ParameterObjectAttribute()
    ACT0039 = nodes.ActionSetGameObjectGameProperty()
    CON0040 = nodes.ObjectPropertyOperator()
    CON0041 = nodes.ObjectPropertyOperator()
    CON0042 = nodes.ObjectPropertyOperator()
    CON0043 = nodes.ConditionOrList()
    ACT0044 = nodes.ActionTimeFilter()
    ACT0045 = nodes.ActionRayPick()
    CON0046 = nodes.ConditionOnUpdate()
    PAR0047 = nodes.ParameterObjectAttribute()
    PAR0048 = nodes.ParameterObjectAttribute()
    CON0049 = nodes.ConditionNot()
    ACT0050 = nodes.ActionAlignAxisToVector()
    ACT0051 = nodes.ActionSetObjectAttribute()
    CON0052 = nodes.ConditionOr()
    ACT0053 = nodes.ActionRotateTo()
    CON0054 = nodes.ConditionKeyPressed()
    CON0055 = nodes.ObjectPropertyOperator()
    CON0056 = nodes.ConditionOrList()
    CON0057 = nodes.ConditionKeyPressed()
    CON0058 = nodes.ConditionKeyPressed()
    CON0059 = nodes.ConditionKeyPressed()
    PAR0060 = nodes.ParameterObjectProperty()
    PAR0061 = nodes.ParameterVector3Simple()
    PAR0062 = nodes.ParameterArithmeticOp()
    ACT0063 = nodes.ActionApplyLocation()
    CON0064 = nodes.ConditionAnd()
    CON0065 = nodes.ConditionOr()
    CON0066 = nodes.ConditionOr()
    ACT0067 = nodes.ActionApplyForce()
    CON0068 = nodes.ObjectPropertyOperator()
    CON0069 = nodes.ObjectPropertyOperator()
    CON0070 = nodes.ConditionAndList()
    CON0071 = nodes.ConditionNot()
    CON0072 = nodes.ConditionCollision()
    CON0073 = nodes.ConditionCollision()
    CON0074 = nodes.ConditionAnd()
    ACT0075 = nodes.ActionSetGameObjectGameProperty()
    CON0076 = nodes.ConditionAnd()
    ACT0077 = nodes.ActionSetGameObjectGameProperty()
    ACT0078 = nodes.ActionSetGameObjectGameProperty()
    CON0079 = nodes.ObjectPropertyOperator()
    CON0080 = nodes.ConditionAnd()
    ACT0081 = nodes.ActionSetGameObjectGameProperty()
    CON0082 = nodes.ObjectPropertyOperator()
    ACT0083 = nodes.ActionSetGameObjectGameProperty()
    ACT0084 = nodes.ActionAddToGameObjectGameProperty()
    ACT0085 = nodes.ActionSetGameObjectGameProperty()
    CON0086 = nodes.ConditionKeyPressed()
    CON0087 = nodes.ObjectPropertyOperator()
    CON0088 = nodes.ConditionOr()
    CON0089 = nodes.ConditionAnd()
    ACT0090 = nodes.ActionApplyForce()
    CON0091 = nodes.ConditionGamepadButtons()
    CON0092 = nodes.ConditionOr()
    CON0093 = nodes.ConditionKeyPressed()
    ACT0094 = nodes.ActionSetGameObjectGameProperty()
    CON0095 = nodes.ConditionAnd()
    ACT0096 = nodes.ActionSetGameObjectGameProperty()
    ACT0097 = nodes.ActionSetGameObjectGameProperty()
    CON0098 = nodes.ConditionAnd()
    ACT0099 = nodes.ActionApplyForce()
    CON0100 = nodes.ObjectPropertyOperator()
    CON0101 = nodes.ConditionAnd()
    CON0102 = nodes.ObjectPropertyOperator()
    CON0103 = nodes.ConditionGamepadButtons()
    CON0104 = nodes.ConditionKeyPressed()
    CON0105 = nodes.ConditionKeyPressed()
    CON0106 = nodes.ConditionKeyPressed()
    CON0107 = nodes.ConditionOrList()
    CON0108 = nodes.ConditionAnd()
    CON0109 = nodes.ConditionKeyPressed()
    CON0110 = nodes.ConditionAnd()
    ACT0111 = nodes.ActionAddToGameObjectGameProperty()
    CON0112 = nodes.ConditionOrList()
    CON0113 = nodes.ConditionNot()
    ACT0114 = nodes.ActionSetGameObjectGameProperty()
    ACT0115 = nodes.ActionSetGameObjectGameProperty()
    CON0116 = nodes.ConditionAnd()
    CON0117 = nodes.ConditionAnd()
    CON0118 = nodes.ConditionAnd()
    CON0119 = nodes.ConditionAnd()
    CON0120 = nodes.ConditionAnd()
    CON0121 = nodes.ObjectPropertyOperator()
    ACT0122 = nodes.ActionTimeFilter()
    ACT0123 = nodes.ActionTimeFilter()
    CON0124 = nodes.ObjectPropertyOperator()
    ACT0125 = nodes.ActionAddToGameObjectGameProperty()
    ACT0126 = nodes.ActionSetGameObjectGameProperty()
    CON0127 = nodes.ObjectPropertyOperator()
    ACT0128 = nodes.ActionSetGameObjectGameProperty()
    ACT0129 = nodes.ActionSetGameObjectGameProperty()
    PAR0130 = nodes.ParameterObjectProperty()
    CON0131 = nodes.ObjectPropertyOperator()
    ACT0132 = nodes.ActionSetGameObjectGameProperty()
    CON0133 = nodes.ObjectPropertyOperator()
    CON0134 = nodes.ObjectPropertyOperator()
    CON0135 = nodes.ConditionNot()
    ACT0136 = nodes.ActionSetGameObjectGameProperty()
    ACT0137 = nodes.ActionSetGameObjectGameProperty()
    ACT0138 = nodes.ActionAddToGameObjectGameProperty()
    CON0139 = nodes.ConditionAndList()
    ACT0140 = nodes.ActionRotateTo()
    ACT0141 = nodes.ActionRotateTo()
    ACT0142 = nodes.ActionRotateTo()
    ACT0143 = nodes.ActionRotateTo()
    ACT0144 = nodes.ActionRotateTo()
    ACT0145 = nodes.ActionRotateTo()
    PAR0146 = nodes.ParameterObjectAttribute()
    PAR0147 = nodes.ParameterObjectAttribute()
    CON0148 = nodes.ObjectPropertyOperator()
    CON0149 = nodes.ObjectPropertyOperator()
    CON0150 = nodes.ObjectPropertyOperator()
    CON0151 = nodes.ObjectPropertyOperator()
    ACT0152 = nodes.ActionRotateTo()
    PAR0153 = nodes.ParameterObjectProperty()
    PAR0154 = nodes.ParameterObjectAttribute()
    CON0000.condition_a = CON0008
    CON0000.condition_b = CON0009
    CON0001.game_object = "NLO:CharacterController"
    CON0001.property_name = "isStomping"
    CON0001.compare_value = True
    CON0001.operator = 0
    ACT0002.condition = CON0000
    ACT0002.game_object = "NLO:SonicBall"
    ACT0002.visible = True
    ACT0002.recursive = False
    ACT0003.condition = CON0000
    ACT0003.game_object = "NLO:chr_Sonic_HD.001"
    ACT0003.visible = False
    ACT0003.recursive = False
    CON0004.game_object = "NLO:CharacterController"
    CON0004.property_name = "isJumping"
    CON0004.compare_value = False
    CON0004.operator = 0
    ACT0005.condition = CON0007
    ACT0005.game_object = "NLO:chr_Sonic_HD.001"
    ACT0005.visible = True
    ACT0005.recursive = False
    ACT0006.condition = CON0007
    ACT0006.game_object = "NLO:SonicBall"
    ACT0006.visible = False
    ACT0006.recursive = False
    CON0007.condition_a = CON0004
    CON0007.condition_b = CON0001
    CON0008.game_object = "NLO:CharacterController"
    CON0008.property_name = "isStomping"
    CON0008.compare_value = False
    CON0008.operator = 0
    CON0009.game_object = "NLO:CharacterController"
    CON0009.property_name = "isJumping"
    CON0009.compare_value = True
    CON0009.operator = 0
    ACT0010.condition = CON0000
    ACT0010.game_object = "NLO:chr_Sonic_HD.002"
    ACT0010.visible = False
    ACT0010.recursive = False
    ACT0011.condition = CON0007
    ACT0011.game_object = "NLO:chr_Sonic_HD.002"
    ACT0011.visible = True
    ACT0011.recursive = False
    ACT0012.condition = CON0015
    ACT0012.game_object = "NLO:CharacterController"
    ACT0012.property_name = "rotSpeed"
    ACT0012.property_value = 2.0
    ACT0013.condition = CON0014
    ACT0013.game_object = "NLO:CharacterController"
    ACT0013.property_name = "rotSpeed"
    ACT0013.property_value = 4.0
    CON0014.condition_a = CON0025
    CON0014.condition_b = CON0026
    CON0015.condition_a = CON0027
    CON0015.condition_b = CON0028
    ACT0016.condition = CON0017
    ACT0016.game_object = "NLO:CharacterController"
    ACT0016.property_name = "rotSpeed"
    ACT0016.property_value = 3.0
    CON0017.condition_a = CON0031
    CON0017.condition_b = CON0032
    ACT0018.condition = CON0033
    ACT0018.game_object = "NLO:CharacterController"
    ACT0018.property_name = "rotSpeed"
    ACT0018.property_value = 1.0
    CON0019.condition_a = CON0023
    CON0019.condition_b = CON0024
    ACT0020.condition = CON0021
    ACT0020.game_object = "NLO:CharacterController"
    ACT0020.property_name = "rotSpeed"
    ACT0020.property_value = 5.0
    CON0021.condition_a = CON0029
    CON0021.condition_b = CON0030
    ACT0022.condition = CON0019
    ACT0022.game_object = "NLO:CharacterController"
    ACT0022.property_name = "rotSpeed"
    ACT0022.property_value = 3.0
    CON0023.game_object = "NLO:CharacterController"
    CON0023.property_name = "Speed"
    CON0023.compare_value = 0.10000000149011612
    CON0023.operator = 5
    CON0024.game_object = "NLO:CharacterController"
    CON0024.property_name = "Speed"
    CON0024.compare_value = 0.0
    CON0024.operator = 2
    CON0025.game_object = "NLO:CharacterController"
    CON0025.property_name = "Speed"
    CON0025.compare_value = 0.3199999928474426
    CON0025.operator = 5
    CON0026.game_object = "NLO:CharacterController"
    CON0026.property_name = "Speed"
    CON0026.compare_value = 0.1599999964237213
    CON0026.operator = 2
    CON0027.game_object = "NLO:CharacterController"
    CON0027.property_name = "Speed"
    CON0027.compare_value = 0.6399999856948853
    CON0027.operator = 5
    CON0028.game_object = "NLO:CharacterController"
    CON0028.property_name = "Speed"
    CON0028.compare_value = 0.47999998927116394
    CON0028.operator = 2
    CON0029.game_object = "NLO:CharacterController"
    CON0029.property_name = "Speed"
    CON0029.compare_value = 0.1599999964237213
    CON0029.operator = 5
    CON0030.game_object = "NLO:CharacterController"
    CON0030.property_name = "Speed"
    CON0030.compare_value = 0.10000000149011612
    CON0030.operator = 2
    CON0031.game_object = "NLO:CharacterController"
    CON0031.property_name = "Speed"
    CON0031.compare_value = 0.47999998927116394
    CON0031.operator = 5
    CON0032.game_object = "NLO:CharacterController"
    CON0032.property_name = "Speed"
    CON0032.compare_value = 0.3199999928474426
    CON0032.operator = 2
    CON0033.game_object = "NLO:CharacterController"
    CON0033.property_name = "Speed"
    CON0033.compare_value = 0.6399999856948853
    CON0033.operator = 2
    PAR0034.game_object = "NLO:SD"
    PAR0034.attribute_name = "worldPosition"
    PAR0035.game_object = "NLO:AS"
    PAR0035.attribute_name = "worldPosition"
    PAR0036.game_object = "NLO:DW"
    PAR0036.attribute_name = "worldPosition"
    PAR0037.game_object = "NLO:WA"
    PAR0037.attribute_name = "worldPosition"
    PAR0038.game_object = "NLO:D"
    PAR0038.attribute_name = "worldPosition"
    ACT0039.condition = ACT0044
    ACT0039.game_object = "NLO:CharacterController"
    ACT0039.property_name = "idle"
    ACT0039.property_value = 0.0
    CON0040.game_object = "NLO:CharacterController"
    CON0040.property_name = "Speed"
    CON0040.compare_value = 0.029999999329447746
    CON0040.operator = 2
    CON0041.game_object = "NLO:CharacterController"
    CON0041.property_name = "isFalling"
    CON0041.compare_value = True
    CON0041.operator = 2
    CON0042.game_object = "NLO:CharacterController"
    CON0042.property_name = "isJumping"
    CON0042.compare_value = True
    CON0042.operator = 2
    CON0043.ca = CON0040
    CON0043.cb = CON0042
    CON0043.cc = CON0041
    CON0043.cd = CON0071
    CON0043.ce = None
    CON0043.cf = None
    ACT0044.condition = CON0043
    ACT0044.delay = 0.0
    ACT0045.condition = CON0046
    ACT0045.origin = PAR0047
    ACT0045.destination = PAR0048
    ACT0045.local = False
    ACT0045.property_name = ""
    ACT0045.xray = False
    ACT0045.custom_dist = False
    ACT0045.distance = 0.0
    ACT0045.visualize = False
    PAR0047.game_object = "NLO:CharacterController"
    PAR0047.attribute_name = "worldPosition"
    PAR0048.game_object = "NLO:RayRotate"
    PAR0048.attribute_name = "worldPosition"
    CON0049.condition = ACT0045
    ACT0050.local = True
    ACT0050.condition = ACT0045
    ACT0050.game_object = "NLO:CharacterController"
    ACT0050.vector = ACT0045.NORMAL
    ACT0050.axis = 2
    ACT0050.factor = 1.0
    ACT0051.condition = CON0049
    ACT0051.xyz = {'x': True, 'y': True, 'z': False}
    ACT0051.game_object = "NLO:CharacterController"
    ACT0051.attribute_value = mathutils.Vector((0.0, 0.0, 0.0))
    ACT0051.value_type = 'worldOrientation'
    CON0052.condition_a = None
    CON0052.condition_b = None
    ACT0053.condition = CON0116
    ACT0053.moving_object = "NLO:CharacterController"
    ACT0053.target_point = PAR0037
    ACT0053.speed = PAR0153
    ACT0053.rot_axis = 2
    ACT0053.front_axis = 1
    CON0054.key_code = bge.events.DKEY
    CON0054.pulse = True
    CON0055.game_object = "NLO:CharacterController"
    CON0055.property_name = "Speed"
    CON0055.compare_value = 0.029999999329447746
    CON0055.operator = 2
    CON0056.ca = CON0059
    CON0056.cb = CON0058
    CON0056.cc = CON0057
    CON0056.cd = CON0054
    CON0056.ce = None
    CON0056.cf = None
    CON0057.key_code = bge.events.AKEY
    CON0057.pulse = True
    CON0058.key_code = bge.events.SKEY
    CON0058.pulse = True
    CON0059.key_code = bge.events.WKEY
    CON0059.pulse = True
    PAR0060.game_object = "NLO:CharacterController"
    PAR0060.property_name = "Speed"
    PAR0061.input_x = 0.0
    PAR0061.input_y = CON0148
    PAR0061.input_z = 0.0
    PAR0062.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0062.operand_a = PAR0061.OUTV
    PAR0062.operand_b = PAR0060
    ACT0063.local = True
    ACT0063.condition = CON0055
    ACT0063.game_object = "NLO:CharacterController"
    ACT0063.movement = PAR0062
    CON0064.condition_a = CON0056
    CON0064.condition_b = CON0149
    CON0065.condition_a = CON0064
    CON0065.condition_b = CON0066
    CON0066.condition_a = CON0150
    CON0066.condition_b = CON0151
    ACT0067.local = True
    ACT0067.condition = CON0070
    ACT0067.game_object = "NLO:CharacterController"
    ACT0067.force = mathutils.Vector((0.0, 1500.0, 0.0))
    CON0068.game_object = "NLO:CharacterController"
    CON0068.property_name = "jump"
    CON0068.compare_value = 2
    CON0068.operator = 0
    CON0069.game_object = "NLO:CharacterController"
    CON0069.property_name = "isHommiable"
    CON0069.compare_value = False
    CON0069.operator = 0
    CON0070.ca = CON0088
    CON0070.cb = CON0068
    CON0070.cc = CON0069
    CON0070.cd = True
    CON0070.ce = True
    CON0070.cf = True
    CON0071.condition = CON0072
    CON0072.game_object = "NLO:groundSensor"
    CON0072.use_mat = False
    CON0072.prop = "obstacle"
    CON0072.material = None
    CON0072.pulse = True
    CON0073.game_object = "NLO:groundSensor"
    CON0073.use_mat = False
    CON0073.prop = "obstacle"
    CON0073.material = None
    CON0073.pulse = False
    CON0074.condition_a = CON0049
    CON0074.condition_b = CON0004
    ACT0075.condition = CON0074
    ACT0075.game_object = "NLO:CharacterController"
    ACT0075.property_name = "isFalling"
    ACT0075.property_value = True
    CON0076.condition_a = CON0082
    CON0076.condition_b = CON0071
    ACT0077.condition = CON0072
    ACT0077.game_object = "NLO:CharacterController"
    ACT0077.property_name = "isFalling"
    ACT0077.property_value = False
    ACT0078.condition = CON0076
    ACT0078.game_object = "NLO:CharacterController"
    ACT0078.property_name = "jump"
    ACT0078.property_value = 2
    CON0079.game_object = "NLO:CharacterController"
    CON0079.property_name = "jump"
    CON0079.compare_value = 2
    CON0079.operator = 4
    CON0080.condition_a = CON0079
    CON0080.condition_b = CON0073
    ACT0081.condition = CON0080
    ACT0081.game_object = "NLO:CharacterController"
    ACT0081.property_name = "isJumping"
    ACT0081.property_value = False
    CON0082.game_object = "NLO:CharacterController"
    CON0082.property_name = "jump"
    CON0082.compare_value = 1
    CON0082.operator = 0
    ACT0083.condition = CON0088
    ACT0083.game_object = "NLO:CharacterController"
    ACT0083.property_name = "isJumping"
    ACT0083.property_value = True
    ACT0084.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("ADD")
    ACT0084.condition = CON0088
    ACT0084.game_object = "NLO:CharacterController"
    ACT0084.property_name = "jump"
    ACT0084.property_value = 1.0
    ACT0085.condition = CON0072
    ACT0085.game_object = "NLO:CharacterController"
    ACT0085.property_name = "jump"
    ACT0085.property_value = 1
    CON0086.key_code = bge.events.SPACEKEY
    CON0086.pulse = False
    CON0087.game_object = "NLO:CharacterController"
    CON0087.property_name = "jump"
    CON0087.compare_value = 1
    CON0087.operator = 0
    CON0088.condition_a = CON0086
    CON0088.condition_b = CON0091.BUTTON
    CON0089.condition_a = CON0087
    CON0089.condition_b = CON0088
    ACT0090.local = True
    ACT0090.condition = CON0089
    ACT0090.game_object = "NLO:CharacterController"
    ACT0090.force = mathutils.Vector((0.0, 0.0, 1500.0))
    CON0091.index = 0
    CON0091.pulse = False
    CON0091.button = 0
    CON0092.condition_a = CON0103.BUTTON
    CON0092.condition_b = CON0093
    CON0093.key_code = bge.events.FKEY
    CON0093.pulse = False
    ACT0094.condition = CON0095
    ACT0094.game_object = "NLO:CharacterController"
    ACT0094.property_name = "isFalling"
    ACT0094.property_value = False
    CON0095.condition_a = CON0092
    CON0095.condition_b = CON0071
    ACT0096.condition = CON0101
    ACT0096.game_object = "NLO:CharacterController"
    ACT0096.property_name = "isStomping"
    ACT0096.property_value = False
    ACT0097.condition = CON0095
    ACT0097.game_object = "NLO:CharacterController"
    ACT0097.property_name = "isStomping"
    ACT0097.property_value = True
    CON0098.condition_a = CON0092
    CON0098.condition_b = CON0100
    ACT0099.local = True
    ACT0099.condition = CON0098
    ACT0099.game_object = "NLO:CharacterController"
    ACT0099.force = mathutils.Vector((0.0, 0.0, -2000.0))
    CON0100.game_object = "NLO:CharacterController"
    CON0100.property_name = "jump"
    CON0100.compare_value = 2
    CON0100.operator = 4
    CON0101.condition_a = CON0073
    CON0101.condition_b = CON0102
    CON0102.game_object = "NLO:CharacterController"
    CON0102.property_name = "isStomping"
    CON0102.compare_value = True
    CON0102.operator = 4
    CON0103.index = 0
    CON0103.pulse = False
    CON0103.button = 1
    CON0104.key_code = bge.events.SKEY
    CON0104.pulse = False
    CON0105.key_code = bge.events.AKEY
    CON0105.pulse = False
    CON0106.key_code = bge.events.DKEY
    CON0106.pulse = False
    CON0107.ca = CON0109
    CON0107.cb = CON0104
    CON0107.cc = CON0105
    CON0107.cd = CON0106
    CON0107.ce = CON0110
    CON0107.cf = CON0108
    CON0108.condition_a = CON0105
    CON0108.condition_b = CON0106
    CON0109.key_code = bge.events.WKEY
    CON0109.pulse = False
    CON0110.condition_a = CON0109
    CON0110.condition_b = CON0104
    ACT0111.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("SUB")
    ACT0111.condition = CON0107
    ACT0111.game_object = "NLO:CharacterController"
    ACT0111.property_name = "Speed"
    ACT0111.property_value = 0.10000000149011612
    CON0112.ca = CON0116
    CON0112.cb = CON0117
    CON0112.cc = CON0119
    CON0112.cd = CON0118
    CON0112.ce = None
    CON0112.cf = None
    CON0113.condition = CON0120
    ACT0114.condition = CON0120
    ACT0114.game_object = "NLO:CharacterController"
    ACT0114.property_name = "max"
    ACT0114.property_value = 1.0
    ACT0115.condition = CON0113
    ACT0115.game_object = "NLO:CharacterController"
    ACT0115.property_name = "max"
    ACT0115.property_value = 1.0
    CON0116.condition_a = CON0059
    CON0116.condition_b = CON0057
    CON0117.condition_a = CON0059
    CON0117.condition_b = CON0054
    CON0118.condition_a = CON0058
    CON0118.condition_b = CON0054
    CON0119.condition_a = CON0058
    CON0119.condition_b = CON0057
    CON0120.condition_a = CON0112
    CON0120.condition_b = CON0121
    CON0121.game_object = "NLO:CharacterController"
    CON0121.property_name = "isBoosting"
    CON0121.compare_value = False
    CON0121.operator = 0
    ACT0122.condition = CON0124
    ACT0122.delay = 0.019999999552965164
    ACT0123.condition = CON0065
    ACT0123.delay = 0.019999999552965164
    CON0124.game_object = "NLO:CharacterController"
    CON0124.property_name = "Speed"
    CON0124.compare_value = 0.029999999329447746
    CON0124.operator = 2
    ACT0125.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("SUB")
    ACT0125.condition = ACT0122
    ACT0125.game_object = "NLO:CharacterController"
    ACT0125.property_name = "Speed"
    ACT0125.property_value = 0.009999999776482582
    ACT0126.condition = ACT0125.OUT
    ACT0126.game_object = "NLO:U_O"
    ACT0126.property_name = "isAccelerating"
    ACT0126.property_value = False
    CON0127.game_object = "NLO:CharacterController"
    CON0127.property_name = "Speed"
    CON0127.compare_value = 0.0
    CON0127.operator = 3
    ACT0128.condition = CON0127
    ACT0128.game_object = "NLO:CharacterController"
    ACT0128.property_name = "Speed"
    ACT0128.property_value = 0.029999999329447746
    ACT0129.condition = CON0135
    ACT0129.game_object = "NLO:CharacterController"
    ACT0129.property_name = "max"
    ACT0129.property_value = 1.0
    PAR0130.game_object = "NLO:CharacterController"
    PAR0130.property_name = "max"
    CON0131.game_object = "NLO:CharacterController"
    CON0131.property_name = "Speed"
    CON0131.compare_value = PAR0130
    CON0131.operator = 2
    ACT0132.condition = CON0139
    ACT0132.game_object = "NLO:CharacterController"
    ACT0132.property_name = "Speed"
    ACT0132.property_value = PAR0130
    CON0133.game_object = "NLO:CharacterController"
    CON0133.property_name = "isBoosting"
    CON0133.compare_value = False
    CON0133.operator = 0
    CON0134.game_object = "NLO:CharacterController"
    CON0134.property_name = "isAccelerating"
    CON0134.compare_value = True
    CON0134.operator = 0
    CON0135.condition = CON0134
    ACT0136.condition = ACT0138.OUT
    ACT0136.game_object = "NLO:U_O"
    ACT0136.property_name = "isAccelerating"
    ACT0136.property_value = True
    ACT0137.condition = ACT0136.OUT
    ACT0137.game_object = "NLO:U_O"
    ACT0137.property_name = "max"
    ACT0137.property_value = 1.0
    ACT0138.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("ADD")
    ACT0138.condition = ACT0123
    ACT0138.game_object = "NLO:CharacterController"
    ACT0138.property_name = "Speed"
    ACT0138.property_value = 0.029999999329447746
    CON0139.ca = CON0131
    CON0139.cb = CON0133
    CON0139.cc = CON0134
    CON0139.cd = True
    CON0139.ce = True
    CON0139.cf = True
    ACT0140.condition = CON0058
    ACT0140.moving_object = "NLO:CharacterController"
    ACT0140.target_point = PAR0146
    ACT0140.speed = PAR0153
    ACT0140.rot_axis = 2
    ACT0140.front_axis = 1
    ACT0141.condition = CON0057
    ACT0141.moving_object = "NLO:CharacterController"
    ACT0141.target_point = PAR0147
    ACT0141.speed = PAR0153
    ACT0141.rot_axis = 2
    ACT0141.front_axis = 1
    ACT0142.condition = CON0054
    ACT0142.moving_object = "NLO:CharacterController"
    ACT0142.target_point = PAR0038
    ACT0142.speed = PAR0153
    ACT0142.rot_axis = 2
    ACT0142.front_axis = 1
    ACT0143.condition = CON0117
    ACT0143.moving_object = "NLO:CharacterController"
    ACT0143.target_point = PAR0036
    ACT0143.speed = PAR0153
    ACT0143.rot_axis = 2
    ACT0143.front_axis = 1
    ACT0144.condition = CON0118
    ACT0144.moving_object = "NLO:CharacterController"
    ACT0144.target_point = PAR0034
    ACT0144.speed = PAR0153
    ACT0144.rot_axis = 2
    ACT0144.front_axis = 1
    ACT0145.condition = CON0119
    ACT0145.moving_object = "NLO:CharacterController"
    ACT0145.target_point = PAR0035
    ACT0145.speed = PAR0153
    ACT0145.rot_axis = 2
    ACT0145.front_axis = 1
    PAR0146.game_object = "NLO:S"
    PAR0146.attribute_name = "worldPosition"
    PAR0147.game_object = "NLO:A"
    PAR0147.attribute_name = "worldPosition"
    CON0148.game_object = "NLO:CharacterController"
    CON0148.property_name = "Speed"
    CON0148.compare_value = 0.029999999329447746
    CON0148.operator = 2
    CON0149.game_object = "NLO:CharacterController"
    CON0149.property_name = "isBoosting"
    CON0149.compare_value = False
    CON0149.operator = 0
    CON0150.game_object = "NLO:U_O"
    CON0150.property_name = "value_updown"
    CON0150.compare_value = 0.0
    CON0150.operator = 1
    CON0151.game_object = "NLO:CharacterController"
    CON0151.property_name = "value_leftright"
    CON0151.compare_value = 0.0
    CON0151.operator = 1
    ACT0152.condition = CON0059
    ACT0152.moving_object = "NLO:CharacterController"
    ACT0152.target_point = PAR0154
    ACT0152.speed = PAR0153
    ACT0152.rot_axis = 2
    ACT0152.front_axis = 1
    PAR0153.game_object = "NLO:CharacterController"
    PAR0153.property_name = "rotSpeed"
    PAR0154.game_object = "NLO:W"
    PAR0154.attribute_name = "worldPosition"
    network.add_cell(CON0001)
    network.add_cell(CON0004)
    network.add_cell(CON0007)
    network.add_cell(CON0009)
    network.add_cell(ACT0011)
    network.add_cell(CON0023)
    network.add_cell(CON0025)
    network.add_cell(CON0027)
    network.add_cell(CON0029)
    network.add_cell(CON0031)
    network.add_cell(CON0033)
    network.add_cell(PAR0035)
    network.add_cell(PAR0037)
    network.add_cell(CON0040)
    network.add_cell(CON0042)
    network.add_cell(CON0046)
    network.add_cell(PAR0048)
    network.add_cell(CON0052)
    network.add_cell(CON0054)
    network.add_cell(CON0057)
    network.add_cell(CON0059)
    network.add_cell(CON0068)
    network.add_cell(CON0072)
    network.add_cell(ACT0077)
    network.add_cell(CON0079)
    network.add_cell(CON0082)
    network.add_cell(ACT0085)
    network.add_cell(CON0087)
    network.add_cell(CON0091)
    network.add_cell(CON0093)
    network.add_cell(CON0100)
    network.add_cell(CON0102)
    network.add_cell(CON0104)
    network.add_cell(CON0106)
    network.add_cell(CON0109)
    network.add_cell(CON0116)
    network.add_cell(CON0121)
    network.add_cell(CON0124)
    network.add_cell(CON0127)
    network.add_cell(PAR0130)
    network.add_cell(CON0133)
    network.add_cell(PAR0146)
    network.add_cell(CON0148)
    network.add_cell(CON0150)
    network.add_cell(PAR0153)
    network.add_cell(ACT0005)
    network.add_cell(CON0008)
    network.add_cell(ACT0018)
    network.add_cell(CON0024)
    network.add_cell(CON0028)
    network.add_cell(CON0032)
    network.add_cell(PAR0036)
    network.add_cell(CON0041)
    network.add_cell(PAR0047)
    network.add_cell(ACT0053)
    network.add_cell(CON0058)
    network.add_cell(PAR0061)
    network.add_cell(CON0069)
    network.add_cell(CON0071)
    network.add_cell(CON0076)
    network.add_cell(CON0086)
    network.add_cell(CON0103)
    network.add_cell(CON0110)
    network.add_cell(CON0117)
    network.add_cell(CON0119)
    network.add_cell(ACT0122)
    network.add_cell(ACT0125)
    network.add_cell(ACT0128)
    network.add_cell(CON0131)
    network.add_cell(CON0134)
    network.add_cell(CON0139)
    network.add_cell(ACT0143)
    network.add_cell(ACT0145)
    network.add_cell(CON0149)
    network.add_cell(PAR0154)
    network.add_cell(CON0000)
    network.add_cell(ACT0003)
    network.add_cell(ACT0010)
    network.add_cell(CON0015)
    network.add_cell(CON0017)
    network.add_cell(CON0026)
    network.add_cell(PAR0034)
    network.add_cell(CON0043)
    network.add_cell(ACT0045)
    network.add_cell(ACT0050)
    network.add_cell(CON0055)
    network.add_cell(PAR0060)
    network.add_cell(CON0073)
    network.add_cell(ACT0078)
    network.add_cell(CON0088)
    network.add_cell(CON0092)
    network.add_cell(CON0095)
    network.add_cell(ACT0097)
    network.add_cell(CON0101)
    network.add_cell(CON0118)
    network.add_cell(ACT0126)
    network.add_cell(ACT0132)
    network.add_cell(ACT0140)
    network.add_cell(ACT0144)
    network.add_cell(CON0151)
    network.add_cell(ACT0002)
    network.add_cell(ACT0012)
    network.add_cell(CON0014)
    network.add_cell(CON0019)
    network.add_cell(ACT0022)
    network.add_cell(PAR0038)
    network.add_cell(ACT0044)
    network.add_cell(CON0056)
    network.add_cell(CON0064)
    network.add_cell(CON0066)
    network.add_cell(CON0070)
    network.add_cell(CON0080)
    network.add_cell(ACT0083)
    network.add_cell(CON0089)
    network.add_cell(ACT0094)
    network.add_cell(CON0098)
    network.add_cell(CON0105)
    network.add_cell(CON0108)
    network.add_cell(CON0112)
    network.add_cell(CON0120)
    network.add_cell(CON0135)
    network.add_cell(ACT0142)
    network.add_cell(ACT0152)
    network.add_cell(ACT0006)
    network.add_cell(ACT0016)
    network.add_cell(CON0030)
    network.add_cell(CON0049)
    network.add_cell(PAR0062)
    network.add_cell(CON0065)
    network.add_cell(CON0074)
    network.add_cell(ACT0081)
    network.add_cell(ACT0090)
    network.add_cell(ACT0099)
    network.add_cell(CON0113)
    network.add_cell(ACT0115)
    network.add_cell(ACT0129)
    network.add_cell(PAR0147)
    network.add_cell(ACT0013)
    network.add_cell(CON0021)
    network.add_cell(ACT0051)
    network.add_cell(ACT0067)
    network.add_cell(ACT0084)
    network.add_cell(CON0107)
    network.add_cell(ACT0114)
    network.add_cell(ACT0141)
    network.add_cell(ACT0020)
    network.add_cell(ACT0063)
    network.add_cell(ACT0096)
    network.add_cell(ACT0123)
    network.add_cell(ACT0138)
    network.add_cell(ACT0039)
    network.add_cell(ACT0111)
    network.add_cell(ACT0075)
    network.add_cell(ACT0136)
    network.add_cell(ACT0137)
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
