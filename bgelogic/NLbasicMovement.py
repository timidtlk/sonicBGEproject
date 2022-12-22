# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    CON0000 = nodes.ConditionKeyPressed()
    CON0001 = nodes.ConditionKeyPressed()
    CON0002 = nodes.ConditionKeyPressed()
    CON0003 = nodes.ConditionOrList()
    CON0004 = nodes.ConditionAnd()
    CON0005 = nodes.ConditionKeyPressed()
    CON0006 = nodes.ConditionAnd()
    ACT0007 = nodes.ActionAddToGameObjectGameProperty()
    CON0008 = nodes.ObjectPropertyOperator()
    ACT0009 = nodes.ActionSaveVariable()
    ACT0010 = nodes.ActionPerformanceProfile()
    CON0011 = nodes.ConditionAnd()
    CON0012 = nodes.ObjectPropertyOperator()
    ACT0013 = nodes.ActionSetGameObjectVisibility()
    ACT0014 = nodes.ActionSetGameObjectVisibility()
    CON0015 = nodes.ObjectPropertyOperator()
    ACT0016 = nodes.ActionSetGameObjectVisibility()
    CON0017 = nodes.ConditionNot()
    CON0018 = nodes.ConditionCollision()
    CON0019 = nodes.ConditionCollision()
    CON0020 = nodes.ConditionAnd()
    ACT0021 = nodes.ActionSetGameObjectGameProperty()
    CON0022 = nodes.ConditionAnd()
    ACT0023 = nodes.ActionSetGameObjectGameProperty()
    ACT0024 = nodes.ActionSetGameObjectGameProperty()
    CON0025 = nodes.ObjectPropertyOperator()
    CON0026 = nodes.ConditionAnd()
    ACT0027 = nodes.ActionSetGameObjectGameProperty()
    CON0028 = nodes.ObjectPropertyOperator()
    ACT0029 = nodes.ActionSetGameObjectGameProperty()
    ACT0030 = nodes.ActionAddToGameObjectGameProperty()
    ACT0031 = nodes.ActionSetGameObjectGameProperty()
    CON0032 = nodes.ObjectPropertyOperator()
    CON0033 = nodes.ConditionAnd()
    CON0034 = nodes.ObjectPropertyOperator()
    ACT0035 = nodes.ActionApplyForce()
    CON0036 = nodes.ConditionKeyPressed()
    CON0037 = nodes.ConditionAnd()
    CON0038 = nodes.ObjectPropertyOperator()
    CON0039 = nodes.ConditionAnd()
    ACT0040 = nodes.ActionSetGameObjectVisibility()
    CON0041 = nodes.ConditionOr()
    CON0042 = nodes.ObjectPropertyOperator()
    CON0043 = nodes.ObjectPropertyOperator()
    ACT0044 = nodes.ActionSetGameObjectVisibility()
    ACT0045 = nodes.ActionSetGameObjectVisibility()
    CON0046 = nodes.ObjectPropertyOperator()
    PAR0047 = nodes.ParameterVector3Simple()
    PAR0048 = nodes.ParameterObjectProperty()
    ACT0049 = nodes.ActionSetGameObjectGameProperty()
    ACT0050 = nodes.ActionSetGameObjectGameProperty()
    CON0051 = nodes.ConditionAnd()
    CON0052 = nodes.ConditionAnd()
    ACT0053 = nodes.ActionSetGameObjectGameProperty()
    CON0054 = nodes.ConditionAnd()
    ACT0055 = nodes.ActionSetGameObjectGameProperty()
    CON0056 = nodes.ConditionAnd()
    ACT0057 = nodes.ActionSetGameObjectGameProperty()
    CON0058 = nodes.ConditionAnd()
    ACT0059 = nodes.ActionSetGameObjectGameProperty()
    CON0060 = nodes.ObjectPropertyOperator()
    CON0061 = nodes.ObjectPropertyOperator()
    CON0062 = nodes.ObjectPropertyOperator()
    CON0063 = nodes.ObjectPropertyOperator()
    CON0064 = nodes.ObjectPropertyOperator()
    CON0065 = nodes.ObjectPropertyOperator()
    CON0066 = nodes.ObjectPropertyOperator()
    CON0067 = nodes.ObjectPropertyOperator()
    CON0068 = nodes.ObjectPropertyOperator()
    CON0069 = nodes.ObjectPropertyOperator()
    CON0070 = nodes.ObjectPropertyOperator()
    PAR0071 = nodes.ParameterObjectAttribute()
    PAR0072 = nodes.ParameterObjectAttribute()
    PAR0073 = nodes.ParameterObjectAttribute()
    PAR0074 = nodes.ParameterObjectAttribute()
    PAR0075 = nodes.ParameterObjectAttribute()
    PAR0076 = nodes.ParameterObjectProperty()
    PAR0077 = nodes.ParameterObjectAttribute()
    PAR0078 = nodes.ParameterObjectAttribute()
    PAR0079 = nodes.ParameterObjectAttribute()
    ACT0080 = nodes.ActionRotateTo()
    ACT0081 = nodes.ActionRotateTo()
    ACT0082 = nodes.ActionRotateTo()
    ACT0083 = nodes.ActionRotateTo()
    ACT0084 = nodes.ActionRotateTo()
    ACT0085 = nodes.ActionRotateTo()
    ACT0086 = nodes.ActionRotateTo()
    ACT0087 = nodes.ActionRotateTo()
    CON0088 = nodes.ConditionKeyPressed()
    CON0089 = nodes.ObjectPropertyOperator()
    ACT0090 = nodes.ActionApplyLocation()
    PAR0091 = nodes.ParameterArithmeticOp()
    PAR0092 = nodes.ParameterObjectProperty()
    PAR0093 = nodes.ParameterVector3Simple()
    CON0094 = nodes.ConditionOrList()
    CON0095 = nodes.ConditionKeyPressed()
    CON0096 = nodes.ObjectPropertyOperator()
    CON0097 = nodes.ConditionKeyPressed()
    CON0098 = nodes.ConditionKeyPressed()
    CON0099 = nodes.ObjectPropertyOperator()
    CON0100 = nodes.ConditionAnd()
    ACT0101 = nodes.ActionAddToGameObjectGameProperty()
    ACT0102 = nodes.ActionTimeFilter()
    ACT0103 = nodes.ActionTimeFilter()
    CON0104 = nodes.ObjectPropertyOperator()
    ACT0105 = nodes.ActionAddToGameObjectGameProperty()
    ACT0106 = nodes.ActionSetGameObjectGameProperty()
    CON0107 = nodes.ObjectPropertyOperator()
    CON0108 = nodes.ConditionAnd()
    ACT0109 = nodes.ActionSetGameObjectGameProperty()
    PAR0110 = nodes.ParameterObjectProperty()
    CON0111 = nodes.ObjectPropertyOperator()
    CON0112 = nodes.ObjectPropertyOperator()
    ACT0113 = nodes.ActionSetGameObjectGameProperty()
    ACT0114 = nodes.ActionSetGameObjectGameProperty()
    CON0115 = nodes.ConditionAnd()
    ACT0116 = nodes.ActionSetGameObjectGameProperty()
    PAR0117 = nodes.ParameterArithmeticOp()
    ACT0118 = nodes.ActionSetGameObjectGameProperty()
    ACT0119 = nodes.ActionSetGameObjectGameProperty()
    CON0120 = nodes.ObjectPropertyOperator()
    CON0121 = nodes.ObjectPropertyOperator()
    CON0122 = nodes.ObjectPropertyOperator()
    CON0123 = nodes.ConditionOrList()
    ACT0124 = nodes.ActionTimeFilter()
    ACT0125 = nodes.ActionRayPick()
    CON0126 = nodes.ConditionOnUpdate()
    PAR0127 = nodes.ParameterObjectAttribute()
    PAR0128 = nodes.ParameterObjectAttribute()
    CON0129 = nodes.ConditionNot()
    ACT0130 = nodes.ActionAlignAxisToVector()
    ACT0131 = nodes.ActionSetObjectAttribute()
    ACT0132 = nodes.ActionApplyForce()
    CON0133 = nodes.ConditionKeyPressed()
    ACT0134 = nodes.ActionApplyForce()
    CON0135 = nodes.ConditionAndList()
    CON0136 = nodes.ObjectPropertyOperator()
    CON0137 = nodes.ObjectPropertyOperator()
    CON0138 = nodes.ConditionOrList()
    CON0139 = nodes.ConditionNot()
    ACT0140 = nodes.ActionSetGameObjectGameProperty()
    ACT0141 = nodes.ActionSetGameObjectGameProperty()
    CON0142 = nodes.ConditionAnd()
    CON0143 = nodes.ConditionAnd()
    CON0144 = nodes.ConditionAnd()
    CON0145 = nodes.ConditionAnd()
    CON0146 = nodes.ConditionAnd()
    CON0147 = nodes.ObjectPropertyOperator()
    PAR0148 = nodes.ParameterObjectAttribute()
    ACT0149 = nodes.ActionSetGameObjectGameProperty()
    CON0150 = nodes.ObjectPropertyOperator()
    ACT0151 = nodes.ActionSetGameObjectGameProperty()
    CON0152 = nodes.ObjectPropertyOperator()
    ACT0153 = nodes.ActionSetDynamics()
    ACT0154 = nodes.ActionMoveTo()
    ACT0155 = nodes.ActionRotateTo()
    PAR0156 = nodes.ParameterObjectAttribute()
    CON0157 = nodes.ConditionNot()
    ACT0158 = nodes.ActionSetGameObjectGameProperty()
    ACT0159 = nodes.ActionSetGameObjectGameProperty()
    CON0160 = nodes.ConditionAndList()
    CON0161 = nodes.ConditionKeyPressed()
    CON0162 = nodes.ObjectPropertyOperator()
    CON0163 = nodes.ConditionAnd()
    ACT0164 = nodes.ActionSetGameObjectGameProperty()
    ACT0165 = nodes.ActionSetGameObjectGameProperty()
    CON0166 = nodes.ObjectPropertyOperator()
    CON0167 = nodes.ObjectPropertyOperator()
    CON0168 = nodes.ConditionCollision()
    CON0169 = nodes.ConditionCollision()
    CON0170 = nodes.ConditionDistanceCheck()
    PAR0171 = nodes.ParameterObjectAttribute()
    CON0000.key_code = bge.events.SKEY
    CON0000.pulse = False
    CON0001.key_code = bge.events.AKEY
    CON0001.pulse = False
    CON0002.key_code = bge.events.DKEY
    CON0002.pulse = False
    CON0003.ca = CON0005
    CON0003.cb = CON0000
    CON0003.cc = CON0001
    CON0003.cd = CON0002
    CON0003.ce = CON0006
    CON0003.cf = CON0004
    CON0004.condition_a = CON0001
    CON0004.condition_b = CON0002
    CON0005.key_code = bge.events.WKEY
    CON0005.pulse = False
    CON0006.condition_a = CON0005
    CON0006.condition_b = CON0000
    ACT0007.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("SUB")
    ACT0007.condition = CON0003
    ACT0007.game_object = "NLO:CharacterController"
    ACT0007.property_name = "Speed"
    ACT0007.property_value = 0.10000000149011612
    CON0008.game_object = "NLO:CharacterController"
    CON0008.property_name = "idle"
    CON0008.compare_value = 10.0
    CON0008.operator = 0
    ACT0009.path = '//saves'
    ACT0009.file_name = 'profile'
    ACT0009.condition = CON0008
    ACT0009.name = "profile"
    ACT0009.val = ACT0010.DATA
    ACT0010.condition = CON0008
    ACT0010.print_profile = True
    ACT0010.check_evaluated_cells = True
    ACT0010.check_average_cells_per_sec = True
    ACT0010.check_cells_per_tick = True
    CON0011.condition_a = CON0042
    CON0011.condition_b = CON0043
    CON0012.game_object = "NLO:CharacterController"
    CON0012.property_name = "isStomping"
    CON0012.compare_value = True
    CON0012.operator = 0
    ACT0013.condition = CON0011
    ACT0013.game_object = "NLO:SonicBall"
    ACT0013.visible = True
    ACT0013.recursive = False
    ACT0014.condition = CON0011
    ACT0014.game_object = "NLO:chr_Sonic_HD.001"
    ACT0014.visible = False
    ACT0014.recursive = False
    CON0015.game_object = "NLO:CharacterController"
    CON0015.property_name = "isJumping"
    CON0015.compare_value = False
    CON0015.operator = 0
    ACT0016.condition = CON0041
    ACT0016.game_object = "NLO:chr_Sonic_HD.001"
    ACT0016.visible = True
    ACT0016.recursive = False
    CON0017.condition = CON0018
    CON0018.game_object = "NLO:groundSensor"
    CON0018.use_mat = False
    CON0018.prop = "obstacle"
    CON0018.material = None
    CON0018.pulse = True
    CON0019.game_object = "NLO:groundSensor"
    CON0019.use_mat = False
    CON0019.prop = "obstacle"
    CON0019.material = None
    CON0019.pulse = False
    CON0020.condition_a = CON0129
    CON0020.condition_b = CON0015
    ACT0021.condition = CON0020
    ACT0021.game_object = "NLO:CharacterController"
    ACT0021.property_name = "isFalling"
    ACT0021.property_value = True
    CON0022.condition_a = CON0028
    CON0022.condition_b = CON0017
    ACT0023.condition = CON0018
    ACT0023.game_object = "NLO:CharacterController"
    ACT0023.property_name = "isFalling"
    ACT0023.property_value = False
    ACT0024.condition = CON0022
    ACT0024.game_object = "NLO:CharacterController"
    ACT0024.property_name = "jump"
    ACT0024.property_value = 2
    CON0025.game_object = "NLO:CharacterController"
    CON0025.property_name = "jump"
    CON0025.compare_value = 2
    CON0025.operator = 4
    CON0026.condition_a = CON0025
    CON0026.condition_b = CON0019
    ACT0027.condition = CON0026
    ACT0027.game_object = "NLO:CharacterController"
    ACT0027.property_name = "isJumping"
    ACT0027.property_value = False
    CON0028.game_object = "NLO:CharacterController"
    CON0028.property_name = "jump"
    CON0028.compare_value = 1
    CON0028.operator = 0
    ACT0029.condition = CON0133
    ACT0029.game_object = "NLO:CharacterController"
    ACT0029.property_name = "isJumping"
    ACT0029.property_value = True
    ACT0030.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("ADD")
    ACT0030.condition = CON0133
    ACT0030.game_object = "NLO:CharacterController"
    ACT0030.property_name = "jump"
    ACT0030.property_value = 1.0
    ACT0031.condition = CON0018
    ACT0031.game_object = "NLO:CharacterController"
    ACT0031.property_name = "jump"
    ACT0031.property_value = 1
    CON0032.game_object = "NLO:CharacterController"
    CON0032.property_name = "isStomping"
    CON0032.compare_value = True
    CON0032.operator = 4
    CON0033.condition_a = CON0019
    CON0033.condition_b = CON0032
    CON0034.game_object = "NLO:CharacterController"
    CON0034.property_name = "jump"
    CON0034.compare_value = 2
    CON0034.operator = 4
    ACT0035.local = True
    ACT0035.condition = CON0037
    ACT0035.game_object = "NLO:CharacterController"
    ACT0035.force = mathutils.Vector((0.0, 0.0, -2000.0))
    CON0036.key_code = bge.events.FKEY
    CON0036.pulse = False
    CON0037.condition_a = CON0036
    CON0037.condition_b = CON0034
    CON0038.game_object = "NLO:CharacterController"
    CON0038.property_name = "jump"
    CON0038.compare_value = 1
    CON0038.operator = 0
    CON0039.condition_a = CON0038
    CON0039.condition_b = CON0133
    ACT0040.condition = CON0041
    ACT0040.game_object = "NLO:SonicBall"
    ACT0040.visible = False
    ACT0040.recursive = False
    CON0041.condition_a = CON0015
    CON0041.condition_b = CON0012
    CON0042.game_object = "NLO:CharacterController"
    CON0042.property_name = "isStomping"
    CON0042.compare_value = False
    CON0042.operator = 0
    CON0043.game_object = "NLO:CharacterController"
    CON0043.property_name = "isJumping"
    CON0043.compare_value = True
    CON0043.operator = 0
    ACT0044.condition = CON0011
    ACT0044.game_object = "NLO:chr_Sonic_HD.002"
    ACT0044.visible = False
    ACT0044.recursive = False
    ACT0045.condition = CON0041
    ACT0045.game_object = "NLO:chr_Sonic_HD.002"
    ACT0045.visible = True
    ACT0045.recursive = False
    CON0046.game_object = "NLO:CharacterController"
    CON0046.property_name = "isBoosting"
    CON0046.compare_value = True
    CON0046.operator = 0
    PAR0047.input_x = 0.0
    PAR0047.input_y = 1.0
    PAR0047.input_z = 0.0
    PAR0048.game_object = "NLO:CharacterController"
    PAR0048.property_name = "Speed"
    ACT0049.condition = CON0052
    ACT0049.game_object = "NLO:CharacterController"
    ACT0049.property_name = "rotSpeed"
    ACT0049.property_value = 2.0
    ACT0050.condition = CON0051
    ACT0050.game_object = "NLO:CharacterController"
    ACT0050.property_name = "rotSpeed"
    ACT0050.property_value = 4.0
    CON0051.condition_a = CON0062
    CON0051.condition_b = CON0063
    CON0052.condition_a = CON0064
    CON0052.condition_b = CON0065
    ACT0053.condition = CON0054
    ACT0053.game_object = "NLO:CharacterController"
    ACT0053.property_name = "rotSpeed"
    ACT0053.property_value = 3.0
    CON0054.condition_a = CON0068
    CON0054.condition_b = CON0069
    ACT0055.condition = CON0070
    ACT0055.game_object = "NLO:CharacterController"
    ACT0055.property_name = "rotSpeed"
    ACT0055.property_value = 1.0
    CON0056.condition_a = CON0060
    CON0056.condition_b = CON0061
    ACT0057.condition = CON0058
    ACT0057.game_object = "NLO:CharacterController"
    ACT0057.property_name = "rotSpeed"
    ACT0057.property_value = 5.0
    CON0058.condition_a = CON0066
    CON0058.condition_b = CON0067
    ACT0059.condition = CON0056
    ACT0059.game_object = "NLO:CharacterController"
    ACT0059.property_name = "rotSpeed"
    ACT0059.property_value = 3.0
    CON0060.game_object = "NLO:CharacterController"
    CON0060.property_name = "Speed"
    CON0060.compare_value = 0.10000000149011612
    CON0060.operator = 5
    CON0061.game_object = "NLO:CharacterController"
    CON0061.property_name = "Speed"
    CON0061.compare_value = 0.0
    CON0061.operator = 2
    CON0062.game_object = "NLO:CharacterController"
    CON0062.property_name = "Speed"
    CON0062.compare_value = 0.3199999928474426
    CON0062.operator = 5
    CON0063.game_object = "NLO:CharacterController"
    CON0063.property_name = "Speed"
    CON0063.compare_value = 0.1599999964237213
    CON0063.operator = 2
    CON0064.game_object = "NLO:CharacterController"
    CON0064.property_name = "Speed"
    CON0064.compare_value = 0.6399999856948853
    CON0064.operator = 5
    CON0065.game_object = "NLO:CharacterController"
    CON0065.property_name = "Speed"
    CON0065.compare_value = 0.47999998927116394
    CON0065.operator = 2
    CON0066.game_object = "NLO:CharacterController"
    CON0066.property_name = "Speed"
    CON0066.compare_value = 0.1599999964237213
    CON0066.operator = 5
    CON0067.game_object = "NLO:CharacterController"
    CON0067.property_name = "Speed"
    CON0067.compare_value = 0.10000000149011612
    CON0067.operator = 2
    CON0068.game_object = "NLO:CharacterController"
    CON0068.property_name = "Speed"
    CON0068.compare_value = 0.47999998927116394
    CON0068.operator = 5
    CON0069.game_object = "NLO:CharacterController"
    CON0069.property_name = "Speed"
    CON0069.compare_value = 0.3199999928474426
    CON0069.operator = 2
    CON0070.game_object = "NLO:CharacterController"
    CON0070.property_name = "Speed"
    CON0070.compare_value = 0.6399999856948853
    CON0070.operator = 2
    PAR0071.game_object = "NLO:SD"
    PAR0071.attribute_name = "worldPosition"
    PAR0072.game_object = "NLO:W"
    PAR0072.attribute_name = "worldPosition"
    PAR0073.game_object = "NLO:AS"
    PAR0073.attribute_name = "worldPosition"
    PAR0074.game_object = "NLO:DW"
    PAR0074.attribute_name = "worldPosition"
    PAR0075.game_object = "NLO:WA"
    PAR0075.attribute_name = "worldPosition"
    PAR0076.game_object = "NLO:CharacterController"
    PAR0076.property_name = "rotSpeed"
    PAR0077.game_object = "NLO:D"
    PAR0077.attribute_name = "worldPosition"
    PAR0078.game_object = "NLO:A"
    PAR0078.attribute_name = "worldPosition"
    PAR0079.game_object = "NLO:S"
    PAR0079.attribute_name = "worldPosition"
    ACT0080.condition = CON0097
    ACT0080.moving_object = "NLO:CharacterController"
    ACT0080.target_point = PAR0072
    ACT0080.speed = PAR0076
    ACT0080.rot_axis = 2
    ACT0080.front_axis = 1
    ACT0081.condition = CON0098
    ACT0081.moving_object = "NLO:CharacterController"
    ACT0081.target_point = PAR0079
    ACT0081.speed = PAR0076
    ACT0081.rot_axis = 2
    ACT0081.front_axis = 1
    ACT0082.condition = CON0095
    ACT0082.moving_object = "NLO:CharacterController"
    ACT0082.target_point = PAR0078
    ACT0082.speed = PAR0076
    ACT0082.rot_axis = 2
    ACT0082.front_axis = 1
    ACT0083.condition = CON0088
    ACT0083.moving_object = "NLO:CharacterController"
    ACT0083.target_point = PAR0077
    ACT0083.speed = PAR0076
    ACT0083.rot_axis = 2
    ACT0083.front_axis = 1
    ACT0084.condition = CON0142
    ACT0084.moving_object = "NLO:CharacterController"
    ACT0084.target_point = PAR0075
    ACT0084.speed = PAR0076
    ACT0084.rot_axis = 2
    ACT0084.front_axis = 1
    ACT0085.condition = CON0143
    ACT0085.moving_object = "NLO:CharacterController"
    ACT0085.target_point = PAR0074
    ACT0085.speed = PAR0076
    ACT0085.rot_axis = 2
    ACT0085.front_axis = 1
    ACT0086.condition = CON0144
    ACT0086.moving_object = "NLO:CharacterController"
    ACT0086.target_point = PAR0071
    ACT0086.speed = PAR0076
    ACT0086.rot_axis = 2
    ACT0086.front_axis = 1
    ACT0087.condition = CON0145
    ACT0087.moving_object = "NLO:CharacterController"
    ACT0087.target_point = PAR0073
    ACT0087.speed = PAR0076
    ACT0087.rot_axis = 2
    ACT0087.front_axis = 1
    CON0088.key_code = bge.events.DKEY
    CON0088.pulse = True
    CON0089.game_object = "NLO:CharacterController"
    CON0089.property_name = "Speed"
    CON0089.compare_value = 0.029999999329447746
    CON0089.operator = 2
    ACT0090.local = True
    ACT0090.condition = CON0089
    ACT0090.game_object = "NLO:CharacterController"
    ACT0090.movement = PAR0091
    PAR0091.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0091.operand_a = PAR0093.OUTV
    PAR0091.operand_b = PAR0092
    PAR0092.game_object = "NLO:CharacterController"
    PAR0092.property_name = "Speed"
    PAR0093.input_x = 0.0
    PAR0093.input_y = CON0096
    PAR0093.input_z = 0.0
    CON0094.ca = CON0097
    CON0094.cb = CON0098
    CON0094.cc = CON0095
    CON0094.cd = CON0088
    CON0094.ce = None
    CON0094.cf = None
    CON0095.key_code = bge.events.AKEY
    CON0095.pulse = True
    CON0096.game_object = "NLO:CharacterController"
    CON0096.property_name = "Speed"
    CON0096.compare_value = 0.029999999329447746
    CON0096.operator = 2
    CON0097.key_code = bge.events.WKEY
    CON0097.pulse = True
    CON0098.key_code = bge.events.SKEY
    CON0098.pulse = True
    CON0099.game_object = "NLO:CharacterController"
    CON0099.property_name = "isBoosting"
    CON0099.compare_value = False
    CON0099.operator = 0
    CON0100.condition_a = CON0094
    CON0100.condition_b = CON0099
    ACT0101.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("SUB")
    ACT0101.condition = ACT0102
    ACT0101.game_object = "NLO:CharacterController"
    ACT0101.property_name = "Speed"
    ACT0101.property_value = 0.009999999776482582
    ACT0102.condition = CON0104
    ACT0102.delay = 0.019999999552965164
    ACT0103.condition = CON0100
    ACT0103.delay = 0.019999999552965164
    CON0104.game_object = "NLO:CharacterController"
    CON0104.property_name = "Speed"
    CON0104.compare_value = 0.029999999329447746
    CON0104.operator = 2
    ACT0105.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("ADD")
    ACT0105.condition = ACT0103
    ACT0105.game_object = "NLO:CharacterController"
    ACT0105.property_name = "Speed"
    ACT0105.property_value = 0.029999999329447746
    ACT0106.condition = CON0107
    ACT0106.game_object = "NLO:CharacterController"
    ACT0106.property_name = "Speed"
    ACT0106.property_value = 0.029999999329447746
    CON0107.game_object = "NLO:CharacterController"
    CON0107.property_name = "Speed"
    CON0107.compare_value = 0.0
    CON0107.operator = 3
    CON0108.condition_a = CON0111
    CON0108.condition_b = CON0112
    ACT0109.condition = CON0108
    ACT0109.game_object = "NLO:CharacterController"
    ACT0109.property_name = "Speed"
    ACT0109.property_value = PAR0110
    PAR0110.game_object = "NLO:CharacterController"
    PAR0110.property_name = "max"
    CON0111.game_object = "NLO:CharacterController"
    CON0111.property_name = "Speed"
    CON0111.compare_value = PAR0110
    CON0111.operator = 2
    CON0112.game_object = "NLO:CharacterController"
    CON0112.property_name = "isBoosting"
    CON0112.compare_value = False
    CON0112.operator = 0
    ACT0113.condition = CON0115
    ACT0113.game_object = "NLO:CharacterController"
    ACT0113.property_name = "isStomping"
    ACT0113.property_value = True
    ACT0114.condition = CON0033
    ACT0114.game_object = "NLO:CharacterController"
    ACT0114.property_name = "isStomping"
    ACT0114.property_value = False
    CON0115.condition_a = CON0036
    CON0115.condition_b = CON0017
    ACT0116.condition = CON0115
    ACT0116.game_object = "NLO:CharacterController"
    ACT0116.property_name = "isFalling"
    ACT0116.property_value = False
    PAR0117.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0117.operand_a = PAR0047.OUTV
    PAR0117.operand_b = PAR0048
    ACT0118.condition = CON0046
    ACT0118.game_object = "NLO:CharacterController"
    ACT0118.property_name = "Speed"
    ACT0118.property_value = 1.5
    ACT0119.condition = ACT0124
    ACT0119.game_object = "NLO:CharacterController"
    ACT0119.property_name = "idle"
    ACT0119.property_value = 0.0
    CON0120.game_object = "NLO:CharacterController"
    CON0120.property_name = "Speed"
    CON0120.compare_value = 0.029999999329447746
    CON0120.operator = 2
    CON0121.game_object = "NLO:CharacterController"
    CON0121.property_name = "isFalling"
    CON0121.compare_value = True
    CON0121.operator = 2
    CON0122.game_object = "NLO:CharacterController"
    CON0122.property_name = "isJumping"
    CON0122.compare_value = True
    CON0122.operator = 2
    CON0123.ca = CON0120
    CON0123.cb = CON0122
    CON0123.cc = CON0121
    CON0123.cd = CON0017
    CON0123.ce = None
    CON0123.cf = None
    ACT0124.condition = CON0123
    ACT0124.delay = 0.0
    ACT0125.condition = CON0126
    ACT0125.origin = PAR0127
    ACT0125.destination = PAR0128
    ACT0125.local = False
    ACT0125.property_name = ""
    ACT0125.xray = False
    ACT0125.custom_dist = False
    ACT0125.distance = 0.0
    ACT0125.visualize = False
    PAR0127.game_object = "NLO:CharacterController"
    PAR0127.attribute_name = "worldPosition"
    PAR0128.game_object = "NLO:RayRotate"
    PAR0128.attribute_name = "worldPosition"
    CON0129.condition = ACT0125
    ACT0130.local = True
    ACT0130.condition = ACT0125
    ACT0130.game_object = "NLO:CharacterController"
    ACT0130.vector = ACT0125.NORMAL
    ACT0130.axis = 2
    ACT0130.factor = 1.0
    ACT0131.condition = CON0129
    ACT0131.xyz = {'x': True, 'y': True, 'z': False}
    ACT0131.game_object = "NLO:CharacterController"
    ACT0131.attribute_value = mathutils.Vector((0.0, 0.0, 0.0))
    ACT0131.value_type = 'worldOrientation'
    ACT0132.local = True
    ACT0132.condition = CON0039
    ACT0132.game_object = "NLO:CharacterController"
    ACT0132.force = mathutils.Vector((0.0, 0.0, 1500.0))
    CON0133.key_code = bge.events.SPACEKEY
    CON0133.pulse = False
    ACT0134.local = True
    ACT0134.condition = CON0135
    ACT0134.game_object = "NLO:CharacterController"
    ACT0134.force = mathutils.Vector((0.0, 1500.0, 0.0))
    CON0135.ca = CON0133
    CON0135.cb = CON0136
    CON0135.cc = CON0137
    CON0135.cd = True
    CON0135.ce = True
    CON0135.cf = True
    CON0136.game_object = "NLO:CharacterController"
    CON0136.property_name = "jump"
    CON0136.compare_value = 2
    CON0136.operator = 0
    CON0137.game_object = "NLO:CharacterController"
    CON0137.property_name = "isHommiable"
    CON0137.compare_value = False
    CON0137.operator = 0
    CON0138.ca = CON0142
    CON0138.cb = CON0143
    CON0138.cc = CON0145
    CON0138.cd = CON0144
    CON0138.ce = None
    CON0138.cf = None
    CON0139.condition = CON0146
    ACT0140.condition = CON0146
    ACT0140.game_object = "NLO:CharacterController"
    ACT0140.property_name = "max"
    ACT0140.property_value = 1.0
    ACT0141.condition = CON0139
    ACT0141.game_object = "NLO:CharacterController"
    ACT0141.property_name = "max"
    ACT0141.property_value = 1.0
    CON0142.condition_a = CON0097
    CON0142.condition_b = CON0095
    CON0143.condition_a = CON0097
    CON0143.condition_b = CON0088
    CON0144.condition_a = CON0098
    CON0144.condition_b = CON0088
    CON0145.condition_a = CON0098
    CON0145.condition_b = CON0095
    CON0146.condition_a = CON0138
    CON0146.condition_b = CON0147
    CON0147.game_object = "NLO:CharacterController"
    CON0147.property_name = "isBoosting"
    CON0147.compare_value = False
    CON0147.operator = 0
    PAR0148.game_object = "NLO:springSensor"
    PAR0148.attribute_name = "worldPosition"
    ACT0149.condition = CON0150
    ACT0149.game_object = "NLO:CharacterController"
    ACT0149.property_name = "Speed"
    ACT0149.property_value = 0.0
    CON0150.game_object = "NLO:CharacterController"
    CON0150.property_name = "homming"
    CON0150.compare_value = True
    CON0150.operator = 0
    ACT0151.condition = ACT0154
    ACT0151.game_object = "NLO:CharacterController"
    ACT0151.property_name = "homming"
    ACT0151.property_value = False
    CON0152.game_object = "NLO:CharacterController"
    CON0152.property_name = "homming"
    CON0152.compare_value = True
    CON0152.operator = 0
    ACT0153.condition = CON0152
    ACT0153.game_object = "NLO:CharacterController"
    ACT0153.activate = True
    ACT0153.ghost = False
    ACT0154.condition = CON0150
    ACT0154.moving_object = "NLO:CharacterController"
    ACT0154.destination_point = PAR0148
    ACT0154.dynamic = False
    ACT0154.speed = 60.0
    ACT0154.distance = 0.5
    ACT0155.condition = CON0150
    ACT0155.moving_object = "NLO:CharacterController"
    ACT0155.target_point = PAR0148
    ACT0155.speed = 0.0
    ACT0155.rot_axis = 0
    ACT0155.front_axis = 4
    PAR0156.game_object = "NLO:CharacterController"
    PAR0156.attribute_name = "worldPosition"
    CON0157.condition = CON0170
    ACT0158.condition = CON0170
    ACT0158.game_object = "NLO:CharacterController"
    ACT0158.property_name = "isHommiable"
    ACT0158.property_value = True
    ACT0159.condition = CON0157
    ACT0159.game_object = "NLO:CharacterController"
    ACT0159.property_name = "isHommiable"
    ACT0159.property_value = False
    CON0160.ca = CON0166
    CON0160.cb = CON0162
    CON0160.cc = CON0161
    CON0160.cd = True
    CON0160.ce = True
    CON0160.cf = True
    CON0161.key_code = bge.events.SPACEKEY
    CON0161.pulse = False
    CON0162.game_object = "NLO:CharacterController"
    CON0162.property_name = "isHommiable"
    CON0162.compare_value = True
    CON0162.operator = 0
    CON0163.condition_a = CON0167
    CON0163.condition_b = CON0168
    ACT0164.condition = CON0160
    ACT0164.game_object = "NLO:CharacterController"
    ACT0164.property_name = "homming"
    ACT0164.property_value = True
    ACT0165.condition = CON0163
    ACT0165.game_object = "NLO:CharacterController"
    ACT0165.property_name = "homming"
    ACT0165.property_value = False
    CON0166.game_object = "NLO:CharacterController"
    CON0166.property_name = "isJumping"
    CON0166.compare_value = True
    CON0166.operator = 0
    CON0167.game_object = "NLO:CharacterController"
    CON0167.property_name = "homming"
    CON0167.compare_value = True
    CON0167.operator = 0
    CON0168.game_object = "NLO:springSensor"
    CON0168.use_mat = False
    CON0168.prop = "player"
    CON0168.material = None
    CON0168.pulse = False
    CON0169.game_object = "NLO:springSensor"
    CON0169.use_mat = False
    CON0169.prop = "player"
    CON0169.material = None
    CON0169.pulse = False
    CON0170.operator = 5
    CON0170.param_a = PAR0156
    CON0170.param_b = PAR0171
    CON0170.dist = 25.0
    CON0170.hyst = None
    PAR0171.game_object = "NLO:springSensor"
    PAR0171.attribute_name = "worldPosition"
    network.add_cell(CON0000)
    network.add_cell(CON0002)
    network.add_cell(CON0005)
    network.add_cell(CON0008)
    network.add_cell(ACT0010)
    network.add_cell(CON0012)
    network.add_cell(CON0015)
    network.add_cell(CON0018)
    network.add_cell(ACT0023)
    network.add_cell(CON0025)
    network.add_cell(CON0028)
    network.add_cell(ACT0031)
    network.add_cell(CON0034)
    network.add_cell(CON0036)
    network.add_cell(CON0038)
    network.add_cell(CON0041)
    network.add_cell(CON0043)
    network.add_cell(ACT0045)
    network.add_cell(PAR0047)
    network.add_cell(CON0060)
    network.add_cell(CON0062)
    network.add_cell(CON0064)
    network.add_cell(CON0066)
    network.add_cell(CON0068)
    network.add_cell(CON0070)
    network.add_cell(PAR0072)
    network.add_cell(PAR0074)
    network.add_cell(PAR0076)
    network.add_cell(PAR0078)
    network.add_cell(CON0088)
    network.add_cell(PAR0092)
    network.add_cell(CON0095)
    network.add_cell(CON0097)
    network.add_cell(CON0099)
    network.add_cell(CON0104)
    network.add_cell(CON0107)
    network.add_cell(PAR0110)
    network.add_cell(CON0112)
    network.add_cell(CON0120)
    network.add_cell(CON0122)
    network.add_cell(CON0126)
    network.add_cell(PAR0128)
    network.add_cell(CON0133)
    network.add_cell(CON0136)
    network.add_cell(CON0142)
    network.add_cell(CON0147)
    network.add_cell(CON0150)
    network.add_cell(CON0152)
    network.add_cell(PAR0156)
    network.add_cell(CON0161)
    network.add_cell(CON0166)
    network.add_cell(CON0168)
    network.add_cell(PAR0171)
    network.add_cell(CON0001)
    network.add_cell(CON0004)
    network.add_cell(ACT0009)
    network.add_cell(ACT0016)
    network.add_cell(CON0019)
    network.add_cell(CON0026)
    network.add_cell(ACT0029)
    network.add_cell(CON0032)
    network.add_cell(CON0037)
    network.add_cell(ACT0040)
    network.add_cell(CON0046)
    network.add_cell(ACT0055)
    network.add_cell(CON0061)
    network.add_cell(CON0065)
    network.add_cell(CON0069)
    network.add_cell(PAR0073)
    network.add_cell(PAR0077)
    network.add_cell(ACT0080)
    network.add_cell(ACT0082)
    network.add_cell(CON0089)
    network.add_cell(CON0096)
    network.add_cell(ACT0102)
    network.add_cell(ACT0106)
    network.add_cell(CON0111)
    network.add_cell(ACT0118)
    network.add_cell(CON0121)
    network.add_cell(PAR0127)
    network.add_cell(CON0137)
    network.add_cell(CON0143)
    network.add_cell(PAR0148)
    network.add_cell(ACT0153)
    network.add_cell(ACT0155)
    network.add_cell(CON0162)
    network.add_cell(CON0167)
    network.add_cell(CON0170)
    network.add_cell(CON0006)
    network.add_cell(CON0017)
    network.add_cell(CON0022)
    network.add_cell(ACT0027)
    network.add_cell(CON0033)
    network.add_cell(CON0039)
    network.add_cell(PAR0048)
    network.add_cell(CON0052)
    network.add_cell(CON0054)
    network.add_cell(CON0063)
    network.add_cell(PAR0071)
    network.add_cell(PAR0079)
    network.add_cell(ACT0083)
    network.add_cell(ACT0085)
    network.add_cell(PAR0093)
    network.add_cell(CON0098)
    network.add_cell(ACT0101)
    network.add_cell(CON0108)
    network.add_cell(ACT0114)
    network.add_cell(PAR0117)
    network.add_cell(CON0123)
    network.add_cell(ACT0125)
    network.add_cell(ACT0130)
    network.add_cell(ACT0132)
    network.add_cell(CON0135)
    network.add_cell(CON0144)
    network.add_cell(ACT0149)
    network.add_cell(ACT0154)
    network.add_cell(ACT0158)
    network.add_cell(CON0160)
    network.add_cell(ACT0164)
    network.add_cell(CON0169)
    network.add_cell(CON0003)
    network.add_cell(ACT0024)
    network.add_cell(ACT0035)
    network.add_cell(ACT0049)
    network.add_cell(CON0051)
    network.add_cell(CON0056)
    network.add_cell(ACT0059)
    network.add_cell(PAR0075)
    network.add_cell(ACT0084)
    network.add_cell(PAR0091)
    network.add_cell(ACT0109)
    network.add_cell(CON0115)
    network.add_cell(ACT0124)
    network.add_cell(ACT0134)
    network.add_cell(CON0145)
    network.add_cell(ACT0151)
    network.add_cell(CON0163)
    network.add_cell(ACT0007)
    network.add_cell(ACT0030)
    network.add_cell(ACT0050)
    network.add_cell(CON0067)
    network.add_cell(ACT0086)
    network.add_cell(ACT0090)
    network.add_cell(ACT0113)
    network.add_cell(ACT0119)
    network.add_cell(CON0138)
    network.add_cell(CON0146)
    network.add_cell(ACT0165)
    network.add_cell(CON0042)
    network.add_cell(ACT0053)
    network.add_cell(CON0058)
    network.add_cell(ACT0087)
    network.add_cell(ACT0116)
    network.add_cell(CON0139)
    network.add_cell(ACT0141)
    network.add_cell(CON0011)
    network.add_cell(ACT0014)
    network.add_cell(ACT0044)
    network.add_cell(ACT0081)
    network.add_cell(CON0129)
    network.add_cell(ACT0140)
    network.add_cell(ACT0013)
    network.add_cell(ACT0057)
    network.add_cell(ACT0131)
    network.add_cell(CON0020)
    network.add_cell(CON0094)
    network.add_cell(CON0157)
    network.add_cell(ACT0021)
    network.add_cell(ACT0159)
    network.add_cell(CON0100)
    network.add_cell(ACT0103)
    network.add_cell(ACT0105)
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
