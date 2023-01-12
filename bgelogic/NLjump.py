# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionSetGameObjectGameProperty()
    CON0001 = nodes.ObjectPropertyOperator()
    CON0002 = nodes.ObjectPropertyOperator()
    CON0003 = nodes.ObjectPropertyOperator()
    CON0004 = nodes.ConditionOrList()
    ACT0005 = nodes.ActionTimeFilter()
    PAR0006 = nodes.ParameterObjectProperty()
    CON0007 = nodes.ObjectPropertyOperator()
    ACT0008 = nodes.ActionSetGameObjectGameProperty()
    CON0009 = nodes.ObjectPropertyOperator()
    ACT0010 = nodes.ActionSetGameObjectGameProperty()
    CON0011 = nodes.ConditionOnUpdate()
    PAR0012 = nodes.ParameterVector3Simple()
    ACT0013 = nodes.ActionSetObjectAttribute()
    CON0014 = nodes.ObjectPropertyOperator()
    CON0015 = nodes.ConditionAnd()
    CON0016 = nodes.ConditionKeyPressed()
    ACT0017 = nodes.ActionApplyForce()
    CON0018 = nodes.ConditionGamepadButtons()
    ACT0019 = nodes.ActionSetGameObjectVisibility()
    ACT0020 = nodes.ActionSetGameObjectVisibility()
    ACT0021 = nodes.ActionSetGameObjectVisibility()
    CON0022 = nodes.ObjectPropertyOperator()
    CON0023 = nodes.ObjectPropertyOperator()
    CON0024 = nodes.ConditionOrList()
    ACT0025 = nodes.ActionSetGameObjectVisibility()
    CON0026 = nodes.ConditionAndList()
    CON0027 = nodes.ObjectPropertyOperator()
    CON0028 = nodes.ObjectPropertyOperator()
    CON0029 = nodes.ConditionOr()
    CON0030 = nodes.ConditionAndList()
    CON0031 = nodes.ObjectPropertyOperator()
    ACT0032 = nodes.ActionApplyForce()
    ACT0033 = nodes.ActionStartSound()
    ACT0034 = nodes.ActionSetGameObjectGameProperty()
    ACT0035 = nodes.ActionSetGameObjectGameProperty()
    CON0036 = nodes.ObjectPropertyOperator()
    CON0037 = nodes.ObjectPropertyOperator()
    CON0038 = nodes.ObjectPropertyOperator()
    CON0039 = nodes.ConditionAnd()
    CON0040 = nodes.ConditionNot()
    CON0041 = nodes.ObjectPropertyOperator()
    CON0042 = nodes.ConditionAnd()
    ACT0043 = nodes.ActionSetGameObjectGameProperty()
    CON0044 = nodes.ConditionAndList()
    CON0045 = nodes.ConditionOr()
    CON0046 = nodes.ObjectPropertyOperator()
    ACT0047 = nodes.ActionSetGameObjectGameProperty()
    ACT0048 = nodes.ActionSetGameObjectGameProperty()
    ACT0049 = nodes.ActionApplyForce()
    ACT0050 = nodes.ActionSetGameObjectGameProperty()
    CON0051 = nodes.ConditionKeyPressed()
    CON0052 = nodes.ConditionGamepadButtons()
    ACT0053 = nodes.ActionApplyForce()
    CON0054 = nodes.ObjectPropertyOperator()
    CON0055 = nodes.ConditionAndList()
    ACT0056 = nodes.ActionSetGameObjectGameProperty()
    CON0057 = nodes.ObjectPropertyOperator()
    CON0058 = nodes.ObjectPropertyOperator()
    CON0059 = nodes.ObjectPropertyOperator()
    CON0060 = nodes.ObjectPropertyOperator()
    CON0061 = nodes.ObjectPropertyOperator()
    CON0062 = nodes.ConditionOrList()
    CON0063 = nodes.ObjectPropertyOperator()
    CON0064 = nodes.ObjectPropertyOperator()
    CON0065 = nodes.ObjectPropertyOperator()
    CON0066 = nodes.ObjectPropertyOperator()
    CON0067 = nodes.ObjectPropertyOperator()
    ACT0068 = nodes.ActionSetGameObjectGameProperty()
    CON0069 = nodes.ConditionAnd()
    ACT0070 = nodes.ActionStartSound()
    ACT0071 = nodes.ActionStartSound()
    PAR0072 = nodes.ParameterObjectAttribute()
    PAR0073 = nodes.ParameterObjectAttribute()
    CON0074 = nodes.ConditionNot()
    CON0075 = nodes.ConditionOr()
    CON0076 = nodes.ConditionAnd()
    CON0077 = nodes.ObjectPropertyOperator()
    CON0078 = nodes.ObjectPropertyOperator()
    CON0079 = nodes.ObjectPropertyOperator()
    ACT0080 = nodes.ActionAddToGameObjectGameProperty()
    ACT0081 = nodes.ActionSetGameObjectGameProperty()
    CON0082 = nodes.ObjectPropertyOperator()
    CON0083 = nodes.ConditionAnd()
    CON0084 = nodes.ConditionNot()
    ACT0085 = nodes.ActionSetGameObjectGameProperty()
    ACT0086 = nodes.ActionSetGameObjectGameProperty()
    CON0087 = nodes.ConditionOr()
    CON0088 = nodes.ObjectPropertyOperator()
    CON0089 = nodes.ObjectPropertyOperator()
    ACT0090 = nodes.ActionSetGameObjectGameProperty()
    CON0091 = nodes.ConditionAnd()
    ACT0092 = nodes.ActionSetGameObjectGameProperty()
    ACT0093 = nodes.ActionSetGameObjectGameProperty()
    CON0094 = nodes.ObjectPropertyOperator()
    CON0095 = nodes.ConditionCollision()
    CON0096 = nodes.ConditionCollision()
    CON0097 = nodes.ConditionAndList()
    ACT0098 = nodes.ActionRayPick()
    ACT0000.condition = ACT0005
    ACT0000.game_object = "NLO:CharacterController"
    ACT0000.property_name = "idle"
    ACT0000.property_value = 0.0
    CON0001.game_object = "NLO:CharacterController"
    CON0001.property_name = "Speed"
    CON0001.compare_value = 0.029999999329447746
    CON0001.operator = 2
    CON0002.game_object = "NLO:CharacterController"
    CON0002.property_name = "isFalling"
    CON0002.compare_value = True
    CON0002.operator = 2
    CON0003.game_object = "NLO:CharacterController"
    CON0003.property_name = "isJumping"
    CON0003.compare_value = True
    CON0003.operator = 2
    CON0004.ca = CON0001
    CON0004.cb = CON0003
    CON0004.cc = CON0002
    CON0004.cd = CON0084
    CON0004.ce = None
    CON0004.cf = None
    ACT0005.condition = CON0004
    ACT0005.delay = 0.0
    PAR0006.game_object = "NLO:U_O"
    PAR0006.property_name = "jump_force"
    CON0007.game_object = "NLO:U_O"
    CON0007.property_name = "isOnWaterP"
    CON0007.compare_value = True
    CON0007.operator = 0
    ACT0008.condition = CON0007
    ACT0008.game_object = "NLO:U_O"
    ACT0008.property_name = "jump_force"
    ACT0008.property_value = 500.0
    CON0009.game_object = "NLO:U_O"
    CON0009.property_name = "isOnWaterP"
    CON0009.compare_value = False
    CON0009.operator = 0
    ACT0010.condition = CON0009
    ACT0010.game_object = "NLO:U_O"
    ACT0010.property_name = "jump_force"
    ACT0010.property_value = 1000.0
    PAR0012.input_x = 0.0
    PAR0012.input_y = 0.0
    PAR0012.input_z = PAR0006
    ACT0013.condition = CON0044
    ACT0013.xyz = {'x': True, 'y': True, 'z': False}
    ACT0013.game_object = "NLO:CharacterController"
    ACT0013.attribute_value = mathutils.Vector((0.0, 0.0, 0.0))
    ACT0013.value_type = 'worldOrientation'
    CON0014.game_object = "NLO:CharacterController"
    CON0014.property_name = "jump"
    CON0014.compare_value = 1
    CON0014.operator = 0
    CON0015.condition_a = CON0014
    CON0015.condition_b = CON0029
    CON0016.key_code = bge.events.SPACEKEY
    CON0016.pulse = False
    ACT0017.local = True
    ACT0017.condition = CON0015
    ACT0017.game_object = "NLO:CharacterController"
    ACT0017.force = PAR0012.OUTV
    CON0018.index = 0
    CON0018.pulse = False
    CON0018.button = 0
    ACT0019.condition = CON0026
    ACT0019.game_object = "NLO:chr_Sonic_HD"
    ACT0019.visible = False
    ACT0019.recursive = True
    ACT0020.condition = CON0024
    ACT0020.game_object = "NLO:chr_Sonic_HD"
    ACT0020.visible = True
    ACT0020.recursive = True
    ACT0021.condition = CON0024
    ACT0021.game_object = "NLO:SonicBall"
    ACT0021.visible = False
    ACT0021.recursive = False
    CON0022.game_object = "NLO:CharacterController"
    CON0022.property_name = "isStomping"
    CON0022.compare_value = True
    CON0022.operator = 0
    CON0023.game_object = "NLO:CharacterController"
    CON0023.property_name = "isJumping"
    CON0023.compare_value = False
    CON0023.operator = 0
    CON0024.ca = CON0023
    CON0024.cb = CON0022
    CON0024.cc = CON0027
    CON0024.cd = None
    CON0024.ce = None
    CON0024.cf = None
    ACT0025.condition = CON0026
    ACT0025.game_object = "NLO:SonicBall"
    ACT0025.visible = True
    ACT0025.recursive = False
    CON0026.ca = CON0077
    CON0026.cb = CON0078
    CON0026.cc = CON0079
    CON0026.cd = True
    CON0026.ce = True
    CON0026.cf = True
    CON0027.game_object = "NLO:CharacterController"
    CON0027.property_name = "isSpringing"
    CON0027.compare_value = True
    CON0027.operator = 0
    CON0028.game_object = "NLO:CharacterController"
    CON0028.property_name = "isHommiable"
    CON0028.compare_value = False
    CON0028.operator = 0
    CON0029.condition_a = CON0016
    CON0029.condition_b = CON0018.BUTTON
    CON0030.ca = CON0029
    CON0030.cb = CON0031
    CON0030.cc = CON0028
    CON0030.cd = True
    CON0030.ce = True
    CON0030.cf = True
    CON0031.game_object = "NLO:CharacterController"
    CON0031.property_name = "jump"
    CON0031.compare_value = 2
    CON0031.operator = 0
    ACT0032.local = True
    ACT0032.condition = CON0030
    ACT0032.game_object = "NLO:CharacterController"
    ACT0032.force = mathutils.Vector((0.0, 1500.0, 0.0))
    ACT0033.condition = ACT0032.OUT
    ACT0033.sound = "D:/Sonic BGE Project/sounds/Player Sounds/Sonic the Hedgehog/30_sn_homing.wav"
    ACT0033.loop_count = 0
    ACT0033.pitch = 1.0
    ACT0033.volume = 0.05000000074505806
    ACT0034.condition = ACT0049.OUT
    ACT0034.game_object = "NLO:CharacterController"
    ACT0034.property_name = "isStomping"
    ACT0034.property_value = False
    ACT0035.condition = CON0042
    ACT0035.game_object = "NLO:CharacterController"
    ACT0035.property_name = "isStomping"
    ACT0035.property_value = False
    CON0036.game_object = "NLO:CharacterController"
    CON0036.property_name = "isStomping"
    CON0036.compare_value = True
    CON0036.operator = 4
    CON0037.game_object = "NLO:CharacterController"
    CON0037.property_name = "jump"
    CON0037.compare_value = 2
    CON0037.operator = 0
    CON0038.game_object = "NLO:CharacterController"
    CON0038.property_name = "isStomping"
    CON0038.compare_value = True
    CON0038.operator = 0
    CON0039.condition_a = CON0040
    CON0039.condition_b = CON0038
    CON0040.condition = CON0041
    CON0041.game_object = "NLO:CharacterController"
    CON0041.property_name = "object"
    CON0041.compare_value = 2.5
    CON0041.operator = 4
    CON0042.condition_a = CON0096
    CON0042.condition_b = CON0036
    ACT0043.condition = ACT0048.OUT
    ACT0043.game_object = "NLO:CharacterController"
    ACT0043.property_name = "jump"
    ACT0043.property_value = 4
    CON0044.ca = CON0045
    CON0044.cb = CON0075
    CON0044.cc = CON0041
    CON0044.cd = True
    CON0044.ce = True
    CON0044.cf = True
    CON0045.condition_a = CON0052.BUTTON
    CON0045.condition_b = CON0051
    CON0046.game_object = "NLO:CharacterController"
    CON0046.property_name = "jump"
    CON0046.compare_value = 3
    CON0046.operator = 0
    ACT0047.condition = CON0076
    ACT0047.game_object = "NLO:CharacterController"
    ACT0047.property_name = "isFalling"
    ACT0047.property_value = False
    ACT0048.condition = CON0076
    ACT0048.game_object = "NLO:CharacterController"
    ACT0048.property_name = "isStomping"
    ACT0048.property_value = True
    ACT0049.local = True
    ACT0049.condition = CON0039
    ACT0049.game_object = "NLO:CharacterController"
    ACT0049.force = mathutils.Vector((0.0, 0.0, 100.0))
    ACT0050.condition = ACT0053.OUT
    ACT0050.game_object = "NLO:CharacterController"
    ACT0050.property_name = "Speed"
    ACT0050.property_value = 0.0
    CON0051.key_code = bge.events.FKEY
    CON0051.pulse = False
    CON0052.index = 0
    CON0052.pulse = False
    CON0052.button = 1
    ACT0053.local = True
    ACT0053.condition = CON0044
    ACT0053.game_object = "NLO:CharacterController"
    ACT0053.force = mathutils.Vector((0.0, 0.0, -1000.0))
    CON0054.game_object = "NLO:CharacterController"
    CON0054.property_name = "jump"
    CON0054.compare_value = 1
    CON0054.operator = 0
    CON0055.ca = CON0060
    CON0055.cb = CON0061
    CON0055.cc = CON0045
    CON0055.cd = CON0059
    CON0055.ce = CON0058
    CON0055.cf = CON0057
    ACT0056.condition = CON0055
    ACT0056.game_object = "NLO:U_O"
    ACT0056.property_name = "isSliding"
    ACT0056.property_value = True
    CON0057.game_object = "NLO:U_O"
    CON0057.property_name = "isJumping"
    CON0057.compare_value = False
    CON0057.operator = 0
    CON0058.game_object = "NLO:U_O"
    CON0058.property_name = "isStomping"
    CON0058.compare_value = False
    CON0058.operator = 0
    CON0059.game_object = "NLO:U_O"
    CON0059.property_name = "isSpringing"
    CON0059.compare_value = False
    CON0059.operator = 0
    CON0060.game_object = "NLO:U_O"
    CON0060.property_name = "isFalling"
    CON0060.compare_value = False
    CON0060.operator = 0
    CON0061.game_object = "NLO:U_O"
    CON0061.property_name = "jump"
    CON0061.compare_value = 1
    CON0061.operator = 0
    CON0062.ca = CON0064
    CON0062.cb = CON0065
    CON0062.cc = CON0066
    CON0062.cd = CON0063
    CON0062.ce = CON0067
    CON0062.cf = None
    CON0063.game_object = "NLO:U_O"
    CON0063.property_name = "isFalling"
    CON0063.compare_value = True
    CON0063.operator = 0
    CON0064.game_object = "NLO:U_O"
    CON0064.property_name = "isJumping"
    CON0064.compare_value = True
    CON0064.operator = 0
    CON0065.game_object = "NLO:U_O"
    CON0065.property_name = "isStomping"
    CON0065.compare_value = True
    CON0065.operator = 0
    CON0066.game_object = "NLO:U_O"
    CON0066.property_name = "isSpringing"
    CON0066.compare_value = True
    CON0066.operator = 0
    CON0067.game_object = "NLO:U_O"
    CON0067.property_name = "jump"
    CON0067.compare_value = 1
    CON0067.operator = 1
    ACT0068.condition = CON0062
    ACT0068.game_object = "NLO:U_O"
    ACT0068.property_name = "isSliding"
    ACT0068.property_value = False
    CON0069.condition_a = CON0029
    CON0069.condition_b = CON0054
    ACT0070.condition = CON0069
    ACT0070.sound = "D:/Sonic BGE Project/sounds/Player Sounds/Sonic the Hedgehog/29_sn_spin.wav"
    ACT0070.loop_count = 0
    ACT0070.pitch = 1.0
    ACT0070.volume = 0.10000000149011612
    ACT0071.condition = CON0069
    ACT0071.sound = "D:/Sonic BGE Project/sounds/Player Sounds/Sonic the Hedgehog/28_sn_jump.wav"
    ACT0071.loop_count = 0
    ACT0071.pitch = 1.0
    ACT0071.volume = 0.10000000149011612
    PAR0072.game_object = "NLO:CharacterController"
    PAR0072.attribute_name = "worldPosition"
    PAR0073.game_object = "NLO:RayRotate"
    PAR0073.attribute_name = "worldPosition"
    CON0074.condition = ACT0098
    CON0075.condition_a = CON0037
    CON0075.condition_b = CON0046
    CON0076.condition_a = CON0045
    CON0076.condition_b = CON0084
    CON0077.game_object = "NLO:CharacterController"
    CON0077.property_name = "isStomping"
    CON0077.compare_value = False
    CON0077.operator = 0
    CON0078.game_object = "NLO:CharacterController"
    CON0078.property_name = "isJumping"
    CON0078.compare_value = True
    CON0078.operator = 0
    CON0079.game_object = "NLO:CharacterController"
    CON0079.property_name = "isSpringing"
    CON0079.compare_value = False
    CON0079.operator = 0
    ACT0080.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("ADD")
    ACT0080.condition = CON0029
    ACT0080.game_object = "NLO:CharacterController"
    ACT0080.property_name = "jump"
    ACT0080.property_value = 1.0
    ACT0081.condition = CON0029
    ACT0081.game_object = "NLO:CharacterController"
    ACT0081.property_name = "isJumping"
    ACT0081.property_value = True
    CON0082.game_object = "NLO:CharacterController"
    CON0082.property_name = "jump"
    CON0082.compare_value = 1
    CON0082.operator = 0
    CON0083.condition_a = CON0082
    CON0083.condition_b = CON0084
    CON0084.condition = CON0095
    ACT0085.condition = CON0083
    ACT0085.game_object = "NLO:CharacterController"
    ACT0085.property_name = "jump"
    ACT0085.property_value = 2
    ACT0086.condition = CON0087
    ACT0086.game_object = "NLO:CharacterController"
    ACT0086.property_name = "isFalling"
    ACT0086.property_value = False
    CON0087.condition_a = CON0095
    CON0087.condition_b = CON0089
    CON0088.game_object = "NLO:CharacterController"
    CON0088.property_name = "velocity"
    CON0088.compare_value = -0.10000000149011612
    CON0088.operator = 5
    CON0089.game_object = "NLO:CharacterController"
    CON0089.property_name = "isSpringing"
    CON0089.compare_value = True
    CON0089.operator = 0
    ACT0090.condition = CON0097
    ACT0090.game_object = "NLO:CharacterController"
    ACT0090.property_name = "isFalling"
    ACT0090.property_value = True
    CON0091.condition_a = CON0094
    CON0091.condition_b = CON0096
    ACT0092.condition = CON0095
    ACT0092.game_object = "NLO:CharacterController"
    ACT0092.property_name = "jump"
    ACT0092.property_value = 1
    ACT0093.condition = CON0091
    ACT0093.game_object = "NLO:CharacterController"
    ACT0093.property_name = "isJumping"
    ACT0093.property_value = False
    CON0094.game_object = "NLO:CharacterController"
    CON0094.property_name = "jump"
    CON0094.compare_value = 2
    CON0094.operator = 4
    CON0095.game_object = "NLO:groundSensor"
    CON0095.use_mat = False
    CON0095.prop = "obstacle"
    CON0095.material = None
    CON0095.pulse = True
    CON0096.game_object = "NLO:groundSensor"
    CON0096.use_mat = False
    CON0096.prop = "obstacle"
    CON0096.material = None
    CON0096.pulse = False
    CON0097.ca = CON0023
    CON0097.cb = CON0074
    CON0097.cc = True
    CON0097.cd = CON0088
    CON0097.ce = True
    CON0097.cf = True
    ACT0098.condition = CON0011
    ACT0098.origin = PAR0072
    ACT0098.destination = PAR0073
    ACT0098.local = False
    ACT0098.property_name = "obstacle"
    ACT0098.xray = False
    ACT0098.custom_dist = False
    ACT0098.distance = 0.0
    ACT0098.visualize = False
    network.add_cell(CON0001)
    network.add_cell(CON0003)
    network.add_cell(PAR0006)
    network.add_cell(CON0009)
    network.add_cell(CON0011)
    network.add_cell(CON0014)
    network.add_cell(CON0016)
    network.add_cell(CON0018)
    network.add_cell(CON0022)
    network.add_cell(CON0027)
    network.add_cell(CON0029)
    network.add_cell(CON0031)
    network.add_cell(CON0036)
    network.add_cell(CON0038)
    network.add_cell(CON0041)
    network.add_cell(CON0046)
    network.add_cell(CON0051)
    network.add_cell(CON0054)
    network.add_cell(CON0057)
    network.add_cell(CON0059)
    network.add_cell(CON0061)
    network.add_cell(CON0063)
    network.add_cell(CON0065)
    network.add_cell(CON0067)
    network.add_cell(CON0069)
    network.add_cell(ACT0071)
    network.add_cell(PAR0073)
    network.add_cell(CON0077)
    network.add_cell(CON0079)
    network.add_cell(ACT0081)
    network.add_cell(CON0088)
    network.add_cell(CON0094)
    network.add_cell(CON0096)
    network.add_cell(CON0002)
    network.add_cell(CON0007)
    network.add_cell(ACT0010)
    network.add_cell(CON0015)
    network.add_cell(CON0023)
    network.add_cell(CON0028)
    network.add_cell(CON0037)
    network.add_cell(CON0040)
    network.add_cell(CON0052)
    network.add_cell(CON0058)
    network.add_cell(CON0064)
    network.add_cell(ACT0070)
    network.add_cell(CON0075)
    network.add_cell(CON0078)
    network.add_cell(CON0082)
    network.add_cell(CON0089)
    network.add_cell(CON0091)
    network.add_cell(ACT0093)
    network.add_cell(ACT0008)
    network.add_cell(CON0024)
    network.add_cell(CON0026)
    network.add_cell(CON0039)
    network.add_cell(CON0045)
    network.add_cell(ACT0049)
    network.add_cell(CON0060)
    network.add_cell(CON0066)
    network.add_cell(PAR0072)
    network.add_cell(ACT0080)
    network.add_cell(CON0095)
    network.add_cell(ACT0098)
    network.add_cell(PAR0012)
    network.add_cell(ACT0017)
    network.add_cell(ACT0020)
    network.add_cell(ACT0025)
    network.add_cell(ACT0034)
    network.add_cell(CON0042)
    network.add_cell(CON0044)
    network.add_cell(ACT0053)
    network.add_cell(CON0062)
    network.add_cell(CON0074)
    network.add_cell(CON0084)
    network.add_cell(CON0087)
    network.add_cell(ACT0092)
    network.add_cell(CON0004)
    network.add_cell(ACT0013)
    network.add_cell(ACT0021)
    network.add_cell(ACT0035)
    network.add_cell(ACT0050)
    network.add_cell(ACT0068)
    network.add_cell(CON0083)
    network.add_cell(ACT0086)
    network.add_cell(CON0097)
    network.add_cell(ACT0005)
    network.add_cell(CON0030)
    network.add_cell(CON0055)
    network.add_cell(CON0076)
    network.add_cell(ACT0090)
    network.add_cell(ACT0000)
    network.add_cell(ACT0032)
    network.add_cell(ACT0047)
    network.add_cell(ACT0056)
    network.add_cell(ACT0019)
    network.add_cell(ACT0048)
    network.add_cell(ACT0033)
    network.add_cell(ACT0085)
    network.add_cell(ACT0043)
    owner["IGNLTree_jump"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__jump')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_jump")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
