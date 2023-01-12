# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionSetGameObjectGameProperty()
    ACT0001 = nodes.ActionSetGameObjectGameProperty()
    ACT0002 = nodes.ActionSetGameObjectVisibility()
    CON0003 = nodes.ConditionAndList()
    CON0004 = nodes.ObjectPropertyOperator()
    CON0005 = nodes.ObjectPropertyOperator()
    CON0006 = nodes.ConditionOrList()
    CON0007 = nodes.ObjectPropertyOperator()
    ACT0008 = nodes.ActionSetGameObjectVisibility()
    CON0009 = nodes.ConditionNot()
    ACT0010 = nodes.ActionSetGameObjectVisibility()
    ACT0011 = nodes.ActionSetGameObjectVisibility()
    CON0012 = nodes.ObjectPropertyOperator()
    CON0013 = nodes.ConditionNot()
    ACT0014 = nodes.ActionSetGameObjectVisibility()
    CON0015 = nodes.ObjectPropertyOperator()
    ACT0016 = nodes.ActionSetGameObjectVisibility()
    CON0017 = nodes.ConditionNot()
    ACT0018 = nodes.ActionSetGameObjectVisibility()
    ACT0019 = nodes.ActionSetGameObjectVisibility()
    CON0020 = nodes.ObjectPropertyOperator()
    CON0021 = nodes.ConditionNot()
    ACT0022 = nodes.ActionSetGameObjectVisibility()
    CON0023 = nodes.ObjectPropertyOperator()
    ACT0024 = nodes.ActionSetGameObjectVisibility()
    CON0025 = nodes.ObjectPropertyOperator()
    CON0026 = nodes.ConditionNot()
    ACT0027 = nodes.ActionSetGameObjectVisibility()
    ACT0028 = nodes.ActionSetGameObjectVisibility()
    CON0029 = nodes.ConditionNot()
    ACT0030 = nodes.ActionSetGameObjectVisibility()
    ACT0031 = nodes.ActionSetGameObjectVisibility()
    CON0032 = nodes.ObjectPropertyOperator()
    CON0033 = nodes.ConditionNot()
    ACT0034 = nodes.ActionSetGameObjectVisibility()
    CON0035 = nodes.ObjectPropertyOperator()
    ACT0036 = nodes.ActionSetGameObjectVisibility()
    CON0037 = nodes.ConditionNot()
    ACT0038 = nodes.ActionSetGameObjectVisibility()
    ACT0039 = nodes.ActionSetGameObjectVisibility()
    CON0040 = nodes.ObjectPropertyOperator()
    CON0041 = nodes.ConditionNot()
    ACT0042 = nodes.ActionSetGameObjectVisibility()
    ACT0043 = nodes.ActionSetGameObjectVisibility()
    CON0044 = nodes.ObjectPropertyOperator()
    CON0045 = nodes.ConditionNot()
    ACT0046 = nodes.ActionSetGameObjectVisibility()
    CON0047 = nodes.ObjectPropertyOperator()
    ACT0048 = nodes.ActionSetGameObjectVisibility()
    CON0049 = nodes.ConditionNot()
    ACT0050 = nodes.ActionSetGameObjectVisibility()
    CON0051 = nodes.ObjectPropertyOperator()
    CON0052 = nodes.ConditionNot()
    ACT0053 = nodes.ActionSetGameObjectVisibility()
    CON0054 = nodes.ObjectPropertyOperator()
    ACT0055 = nodes.ActionSetGameObjectVisibility()
    CON0056 = nodes.ConditionNot()
    ACT0057 = nodes.ActionSetGameObjectVisibility()
    ACT0058 = nodes.ActionSetGameObjectVisibility()
    CON0059 = nodes.ObjectPropertyOperator()
    CON0060 = nodes.ConditionNot()
    ACT0061 = nodes.ActionSetGameObjectVisibility()
    CON0062 = nodes.ObjectPropertyOperator()
    ACT0063 = nodes.ActionSetGameObjectVisibility()
    CON0064 = nodes.ObjectPropertyOperator()
    CON0065 = nodes.ConditionNot()
    ACT0066 = nodes.ActionSetGameObjectVisibility()
    ACT0067 = nodes.ActionSetGameObjectVisibility()
    CON0068 = nodes.ConditionNot()
    ACT0069 = nodes.ActionSetGameObjectVisibility()
    ACT0070 = nodes.ActionSetGameObjectVisibility()
    CON0071 = nodes.ObjectPropertyOperator()
    CON0072 = nodes.ConditionNot()
    ACT0073 = nodes.ActionSetGameObjectVisibility()
    ACT0074 = nodes.ActionSetGameObjectVisibility()
    CON0075 = nodes.ConditionNot()
    ACT0076 = nodes.ActionSetGameObjectVisibility()
    ACT0077 = nodes.ActionSetGameObjectVisibility()
    CON0078 = nodes.ObjectPropertyOperator()
    CON0079 = nodes.ConditionNot()
    ACT0080 = nodes.ActionSetGameObjectVisibility()
    ACT0081 = nodes.ActionSetGameObjectVisibility()
    CON0082 = nodes.ObjectPropertyOperator()
    CON0083 = nodes.ConditionNot()
    ACT0084 = nodes.ActionSetGameObjectVisibility()
    CON0085 = nodes.ObjectPropertyOperator()
    ACT0086 = nodes.ActionSetGameObjectVisibility()
    CON0087 = nodes.ObjectPropertyOperator()
    CON0088 = nodes.ConditionKeyReleased()
    CON0089 = nodes.ConditionKeyPressed()
    CON0090 = nodes.ConditionOr()
    CON0091 = nodes.ConditionOr()
    CON0092 = nodes.ConditionGamepadButtonUp()
    CON0093 = nodes.ObjectPropertyOperator()
    ACT0094 = nodes.ActionSetGameObjectGameProperty()
    CON0095 = nodes.ConditionGamepadButtons()
    ACT0096 = nodes.ActionSetGameObjectVisibility()
    ACT0097 = nodes.ActionSetPhysics()
    ACT0098 = nodes.ActionSetPhysics()
    CON0099 = nodes.ObjectPropertyOperator()
    CON0100 = nodes.ConditionOr()
    CON0101 = nodes.ObjectPropertyOperator()
    CON0102 = nodes.ObjectPropertyOperator()
    CON0103 = nodes.ObjectPropertyOperator()
    CON0104 = nodes.ObjectPropertyOperator()
    CON0105 = nodes.ConditionOr()
    CON0106 = nodes.ConditionAndList()
    CON0107 = nodes.ConditionAnd()
    CON0108 = nodes.ObjectPropertyOperator()
    CON0109 = nodes.ObjectPropertyOperator()
    CON0110 = nodes.GE_OnInit()
    ACT0111 = nodes.ActionTimeFilter()
    PAR0112 = nodes.GESetOverlayCollection()
    CON0113 = nodes.ObjectPropertyOperator()
    ACT0000.condition = CON0003
    ACT0000.game_object = "NLO:CharacterController"
    ACT0000.property_name = "isBoosting"
    ACT0000.property_value = True
    ACT0001.condition = CON0006
    ACT0001.game_object = "NLO:CharacterController"
    ACT0001.property_name = "isBoosting"
    ACT0001.property_value = False
    ACT0002.condition = CON0099
    ACT0002.game_object = "NLO:eff_mod_boost_1"
    ACT0002.visible = False
    ACT0002.recursive = False
    CON0003.ca = CON0090
    CON0003.cb = CON0004
    CON0003.cc = CON0109
    CON0003.cd = CON0113
    CON0003.ce = True
    CON0003.cf = True
    CON0004.game_object = "NLO:CharacterController"
    CON0004.property_name = "isStomping"
    CON0004.compare_value = False
    CON0004.operator = 0
    CON0005.game_object = "NLO:CharacterController"
    CON0005.property_name = "isStomping"
    CON0005.compare_value = True
    CON0005.operator = 0
    CON0006.ca = CON0091
    CON0006.cb = CON0005
    CON0006.cc = CON0007
    CON0006.cd = CON0108
    CON0006.ce = None
    CON0006.cf = None
    CON0007.game_object = "NLO:CharacterController"
    CON0007.property_name = "isJumping"
    CON0007.compare_value = True
    CON0007.operator = 0
    ACT0008.condition = CON0015
    ACT0008.game_object = "NLO:s1"
    ACT0008.visible = True
    ACT0008.recursive = False
    CON0009.condition = CON0015
    ACT0010.condition = CON0009
    ACT0010.game_object = "NLO:s1"
    ACT0010.visible = False
    ACT0010.recursive = False
    ACT0011.condition = CON0012
    ACT0011.game_object = "NLO:s2"
    ACT0011.visible = True
    ACT0011.recursive = False
    CON0012.game_object = "NLO:CharacterController"
    CON0012.property_name = "Speed"
    CON0012.compare_value = 0.10000000149011612
    CON0012.operator = 4
    CON0013.condition = CON0012
    ACT0014.condition = CON0013
    ACT0014.game_object = "NLO:s2"
    ACT0014.visible = False
    ACT0014.recursive = False
    CON0015.game_object = "NLO:CharacterController"
    CON0015.property_name = "Speed"
    CON0015.compare_value = 0.05000000074505806
    CON0015.operator = 4
    ACT0016.condition = CON0023
    ACT0016.game_object = "NLO:s3"
    ACT0016.visible = True
    ACT0016.recursive = False
    CON0017.condition = CON0023
    ACT0018.condition = CON0017
    ACT0018.game_object = "NLO:s3"
    ACT0018.visible = False
    ACT0018.recursive = False
    ACT0019.condition = CON0020
    ACT0019.game_object = "NLO:s4"
    ACT0019.visible = True
    ACT0019.recursive = False
    CON0020.game_object = "NLO:CharacterController"
    CON0020.property_name = "Speed"
    CON0020.compare_value = 0.20000000298023224
    CON0020.operator = 4
    CON0021.condition = CON0020
    ACT0022.condition = CON0021
    ACT0022.game_object = "NLO:s4"
    ACT0022.visible = False
    ACT0022.recursive = False
    CON0023.game_object = "NLO:CharacterController"
    CON0023.property_name = "Speed"
    CON0023.compare_value = 0.15000000596046448
    CON0023.operator = 4
    ACT0024.condition = CON0025
    ACT0024.game_object = "NLO:s5"
    ACT0024.visible = True
    ACT0024.recursive = False
    CON0025.game_object = "NLO:CharacterController"
    CON0025.property_name = "Speed"
    CON0025.compare_value = 0.25
    CON0025.operator = 4
    CON0026.condition = CON0025
    ACT0027.condition = CON0026
    ACT0027.game_object = "NLO:s5"
    ACT0027.visible = False
    ACT0027.recursive = False
    ACT0028.condition = CON0035
    ACT0028.game_object = "NLO:s6"
    ACT0028.visible = True
    ACT0028.recursive = False
    CON0029.condition = CON0035
    ACT0030.condition = CON0029
    ACT0030.game_object = "NLO:s6"
    ACT0030.visible = False
    ACT0030.recursive = False
    ACT0031.condition = CON0032
    ACT0031.game_object = "NLO:s7"
    ACT0031.visible = True
    ACT0031.recursive = False
    CON0032.game_object = "NLO:CharacterController"
    CON0032.property_name = "Speed"
    CON0032.compare_value = 0.3499999940395355
    CON0032.operator = 4
    CON0033.condition = CON0032
    ACT0034.condition = CON0033
    ACT0034.game_object = "NLO:s7"
    ACT0034.visible = False
    ACT0034.recursive = False
    CON0035.game_object = "NLO:CharacterController"
    CON0035.property_name = "Speed"
    CON0035.compare_value = 0.30000001192092896
    CON0035.operator = 4
    ACT0036.condition = CON0047
    ACT0036.game_object = "NLO:s8"
    ACT0036.visible = True
    ACT0036.recursive = False
    CON0037.condition = CON0047
    ACT0038.condition = CON0037
    ACT0038.game_object = "NLO:s8"
    ACT0038.visible = False
    ACT0038.recursive = False
    ACT0039.condition = CON0040
    ACT0039.game_object = "NLO:s9"
    ACT0039.visible = True
    ACT0039.recursive = False
    CON0040.game_object = "NLO:CharacterController"
    CON0040.property_name = "Speed"
    CON0040.compare_value = 0.44999998807907104
    CON0040.operator = 4
    CON0041.condition = CON0040
    ACT0042.condition = CON0041
    ACT0042.game_object = "NLO:s9"
    ACT0042.visible = False
    ACT0042.recursive = False
    ACT0043.condition = CON0044
    ACT0043.game_object = "NLO:s10"
    ACT0043.visible = True
    ACT0043.recursive = False
    CON0044.game_object = "NLO:CharacterController"
    CON0044.property_name = "Speed"
    CON0044.compare_value = 0.5
    CON0044.operator = 4
    CON0045.condition = CON0044
    ACT0046.condition = CON0045
    ACT0046.game_object = "NLO:s10"
    ACT0046.visible = False
    ACT0046.recursive = False
    CON0047.game_object = "NLO:CharacterController"
    CON0047.property_name = "Speed"
    CON0047.compare_value = 0.4000000059604645
    CON0047.operator = 4
    ACT0048.condition = CON0054
    ACT0048.game_object = "NLO:s11"
    ACT0048.visible = True
    ACT0048.recursive = False
    CON0049.condition = CON0054
    ACT0050.condition = CON0051
    ACT0050.game_object = "NLO:s12"
    ACT0050.visible = True
    ACT0050.recursive = False
    CON0051.game_object = "NLO:CharacterController"
    CON0051.property_name = "Speed"
    CON0051.compare_value = 0.6000000238418579
    CON0051.operator = 4
    CON0052.condition = CON0051
    ACT0053.condition = CON0052
    ACT0053.game_object = "NLO:s12"
    ACT0053.visible = False
    ACT0053.recursive = False
    CON0054.game_object = "NLO:CharacterController"
    CON0054.property_name = "Speed"
    CON0054.compare_value = 0.550000011920929
    CON0054.operator = 4
    ACT0055.condition = CON0062
    ACT0055.game_object = "NLO:s13"
    ACT0055.visible = True
    ACT0055.recursive = False
    CON0056.condition = CON0062
    ACT0057.condition = CON0056
    ACT0057.game_object = "NLO:s13"
    ACT0057.visible = False
    ACT0057.recursive = False
    ACT0058.condition = CON0059
    ACT0058.game_object = "NLO:s14"
    ACT0058.visible = True
    ACT0058.recursive = False
    CON0059.game_object = "NLO:CharacterController"
    CON0059.property_name = "Speed"
    CON0059.compare_value = 0.699999988079071
    CON0059.operator = 4
    CON0060.condition = CON0059
    ACT0061.condition = CON0060
    ACT0061.game_object = "NLO:s14"
    ACT0061.visible = False
    ACT0061.recursive = False
    CON0062.game_object = "NLO:CharacterController"
    CON0062.property_name = "Speed"
    CON0062.compare_value = 0.6499999761581421
    CON0062.operator = 4
    ACT0063.condition = CON0064
    ACT0063.game_object = "NLO:s15"
    ACT0063.visible = True
    ACT0063.recursive = False
    CON0064.game_object = "NLO:CharacterController"
    CON0064.property_name = "Speed"
    CON0064.compare_value = 0.75
    CON0064.operator = 4
    CON0065.condition = CON0064
    ACT0066.condition = CON0065
    ACT0066.game_object = "NLO:s15"
    ACT0066.visible = False
    ACT0066.recursive = False
    ACT0067.condition = CON0087
    ACT0067.game_object = "NLO:s16"
    ACT0067.visible = True
    ACT0067.recursive = False
    CON0068.condition = CON0087
    ACT0069.condition = CON0068
    ACT0069.game_object = "NLO:s16"
    ACT0069.visible = False
    ACT0069.recursive = False
    ACT0070.condition = CON0071
    ACT0070.game_object = "NLO:s17"
    ACT0070.visible = True
    ACT0070.recursive = False
    CON0071.game_object = "NLO:CharacterController"
    CON0071.property_name = "Speed"
    CON0071.compare_value = 0.8500000238418579
    CON0071.operator = 4
    CON0072.condition = CON0071
    ACT0073.condition = CON0072
    ACT0073.game_object = "NLO:s17"
    ACT0073.visible = False
    ACT0073.recursive = False
    ACT0074.condition = CON0085
    ACT0074.game_object = "NLO:s18"
    ACT0074.visible = True
    ACT0074.recursive = False
    CON0075.condition = CON0085
    ACT0076.condition = CON0075
    ACT0076.game_object = "NLO:s18"
    ACT0076.visible = False
    ACT0076.recursive = False
    ACT0077.condition = CON0078
    ACT0077.game_object = "NLO:s19"
    ACT0077.visible = True
    ACT0077.recursive = False
    CON0078.game_object = "NLO:CharacterController"
    CON0078.property_name = "Speed"
    CON0078.compare_value = 0.949999988079071
    CON0078.operator = 4
    CON0079.condition = CON0078
    ACT0080.condition = CON0079
    ACT0080.game_object = "NLO:s19"
    ACT0080.visible = False
    ACT0080.recursive = False
    ACT0081.condition = CON0082
    ACT0081.game_object = "NLO:s20"
    ACT0081.visible = True
    ACT0081.recursive = False
    CON0082.game_object = "NLO:CharacterController"
    CON0082.property_name = "Speed"
    CON0082.compare_value = 1.0
    CON0082.operator = 4
    CON0083.condition = CON0082
    ACT0084.condition = CON0083
    ACT0084.game_object = "NLO:s20"
    ACT0084.visible = False
    ACT0084.recursive = False
    CON0085.game_object = "NLO:CharacterController"
    CON0085.property_name = "Speed"
    CON0085.compare_value = 0.8999999761581421
    CON0085.operator = 4
    ACT0086.condition = CON0049
    ACT0086.game_object = "NLO:s11"
    ACT0086.visible = False
    ACT0086.recursive = False
    CON0087.game_object = "NLO:CharacterController"
    CON0087.property_name = "Speed"
    CON0087.compare_value = 0.800000011920929
    CON0087.operator = 4
    CON0088.key_code = bge.events.LEFTSHIFTKEY
    CON0088.pulse = True
    CON0089.key_code = bge.events.LEFTSHIFTKEY
    CON0089.pulse = True
    CON0090.condition_a = CON0095.BUTTON
    CON0090.condition_b = CON0089
    CON0091.condition_a = CON0092.BUTTON
    CON0091.condition_b = CON0088
    CON0092.index = 0
    CON0092.pulse = True
    CON0092.button = 2
    CON0093.game_object = "NLO:CharacterController"
    CON0093.property_name = "isBoosting"
    CON0093.compare_value = True
    CON0093.operator = 0
    ACT0094.condition = CON0093
    ACT0094.game_object = "NLO:CharacterController"
    ACT0094.property_name = "Speed"
    ACT0094.property_value = 1.5
    CON0095.index = 0
    CON0095.pulse = True
    CON0095.button = 2
    ACT0096.condition = CON0106
    ACT0096.game_object = "NLO:eff_mod_boost_1"
    ACT0096.visible = True
    ACT0096.recursive = False
    ACT0097.condition = CON0100
    ACT0097.game_object = "NLO:Water"
    ACT0097.activate = False
    ACT0097.free_const = False
    ACT0098.condition = CON0107
    ACT0098.game_object = "NLO:Water"
    ACT0098.activate = True
    ACT0098.free_const = False
    CON0099.game_object = "NLO:CharacterController"
    CON0099.property_name = "isBoosting"
    CON0099.compare_value = False
    CON0099.operator = 0
    CON0100.condition_a = CON0101
    CON0100.condition_b = CON0099
    CON0101.game_object = "NLO:CharacterController"
    CON0101.property_name = "Speed"
    CON0101.compare_value = 1.0
    CON0101.operator = 3
    CON0102.game_object = "NLO:CharacterController"
    CON0102.property_name = "Speed"
    CON0102.compare_value = 1.0
    CON0102.operator = 4
    CON0103.game_object = "NLO:CharacterController"
    CON0103.property_name = "isBoosting"
    CON0103.compare_value = True
    CON0103.operator = 0
    CON0104.game_object = "NLO:CharacterController"
    CON0104.property_name = "isOnWaterP"
    CON0104.compare_value = False
    CON0104.operator = 0
    CON0105.condition_a = CON0106
    CON0105.condition_b = CON0102
    CON0106.ca = CON0103
    CON0106.cb = CON0004
    CON0106.cc = CON0109
    CON0106.cd = True
    CON0106.ce = True
    CON0106.cf = True
    CON0107.condition_a = CON0105
    CON0107.condition_b = CON0104
    CON0108.game_object = "NLO:U_O"
    CON0108.property_name = "isSliding"
    CON0108.compare_value = True
    CON0108.operator = 0
    CON0109.game_object = "NLO:CharacterController"
    CON0109.property_name = "isJumping"
    CON0109.compare_value = False
    CON0109.operator = 0
    ACT0111.condition = CON0110
    ACT0111.delay = 0.0
    PAR0112.condition = ACT0111
    PAR0112.camera = "NLO:CameraHud"
    PAR0112.collection = "HUD"
    CON0113.game_object = "NLO:CharacterController"
    CON0113.property_name = "isSliding"
    CON0113.compare_value = False
    CON0113.operator = 0
    network.add_cell(CON0004)
    network.add_cell(CON0007)
    network.add_cell(CON0012)
    network.add_cell(CON0015)
    network.add_cell(CON0020)
    network.add_cell(CON0023)
    network.add_cell(CON0025)
    network.add_cell(CON0032)
    network.add_cell(CON0035)
    network.add_cell(CON0040)
    network.add_cell(CON0044)
    network.add_cell(CON0047)
    network.add_cell(CON0051)
    network.add_cell(CON0054)
    network.add_cell(CON0059)
    network.add_cell(CON0062)
    network.add_cell(CON0064)
    network.add_cell(CON0071)
    network.add_cell(CON0078)
    network.add_cell(CON0082)
    network.add_cell(CON0085)
    network.add_cell(CON0087)
    network.add_cell(CON0089)
    network.add_cell(CON0092)
    network.add_cell(CON0095)
    network.add_cell(CON0099)
    network.add_cell(CON0101)
    network.add_cell(CON0103)
    network.add_cell(CON0108)
    network.add_cell(CON0110)
    network.add_cell(CON0113)
    network.add_cell(ACT0002)
    network.add_cell(CON0005)
    network.add_cell(ACT0008)
    network.add_cell(ACT0011)
    network.add_cell(ACT0016)
    network.add_cell(ACT0019)
    network.add_cell(ACT0024)
    network.add_cell(ACT0028)
    network.add_cell(ACT0031)
    network.add_cell(ACT0036)
    network.add_cell(ACT0039)
    network.add_cell(ACT0043)
    network.add_cell(ACT0048)
    network.add_cell(ACT0050)
    network.add_cell(ACT0055)
    network.add_cell(ACT0058)
    network.add_cell(ACT0063)
    network.add_cell(ACT0067)
    network.add_cell(ACT0070)
    network.add_cell(ACT0074)
    network.add_cell(ACT0077)
    network.add_cell(ACT0081)
    network.add_cell(CON0088)
    network.add_cell(CON0091)
    network.add_cell(CON0100)
    network.add_cell(CON0104)
    network.add_cell(CON0109)
    network.add_cell(CON0006)
    network.add_cell(CON0013)
    network.add_cell(CON0017)
    network.add_cell(CON0021)
    network.add_cell(CON0026)
    network.add_cell(CON0029)
    network.add_cell(CON0033)
    network.add_cell(CON0037)
    network.add_cell(CON0041)
    network.add_cell(CON0045)
    network.add_cell(CON0049)
    network.add_cell(CON0056)
    network.add_cell(CON0060)
    network.add_cell(CON0065)
    network.add_cell(CON0068)
    network.add_cell(CON0072)
    network.add_cell(CON0075)
    network.add_cell(CON0079)
    network.add_cell(CON0083)
    network.add_cell(ACT0086)
    network.add_cell(CON0093)
    network.add_cell(ACT0097)
    network.add_cell(CON0102)
    network.add_cell(CON0106)
    network.add_cell(ACT0111)
    network.add_cell(ACT0001)
    network.add_cell(CON0009)
    network.add_cell(ACT0014)
    network.add_cell(ACT0022)
    network.add_cell(ACT0030)
    network.add_cell(ACT0038)
    network.add_cell(ACT0046)
    network.add_cell(ACT0057)
    network.add_cell(ACT0066)
    network.add_cell(ACT0073)
    network.add_cell(ACT0080)
    network.add_cell(CON0090)
    network.add_cell(ACT0096)
    network.add_cell(CON0105)
    network.add_cell(PAR0112)
    network.add_cell(CON0003)
    network.add_cell(ACT0018)
    network.add_cell(ACT0034)
    network.add_cell(CON0052)
    network.add_cell(ACT0061)
    network.add_cell(ACT0076)
    network.add_cell(ACT0094)
    network.add_cell(CON0107)
    network.add_cell(ACT0000)
    network.add_cell(ACT0027)
    network.add_cell(ACT0053)
    network.add_cell(ACT0084)
    network.add_cell(ACT0010)
    network.add_cell(ACT0069)
    network.add_cell(ACT0042)
    network.add_cell(ACT0098)
    owner["IGNLTree_boostMode"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__boostMode')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_boostMode")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
