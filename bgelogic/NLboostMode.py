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
    CON0008 = nodes.ObjectPropertyOperator()
    ACT0009 = nodes.ActionTimeFilter()
    PAR0010 = nodes.GESetOverlayCollection()
    ACT0011 = nodes.ActionSetGameObjectVisibility()
    CON0012 = nodes.ConditionNot()
    ACT0013 = nodes.ActionSetGameObjectVisibility()
    ACT0014 = nodes.ActionSetGameObjectVisibility()
    CON0015 = nodes.ObjectPropertyOperator()
    CON0016 = nodes.ConditionNot()
    ACT0017 = nodes.ActionSetGameObjectVisibility()
    CON0018 = nodes.ObjectPropertyOperator()
    ACT0019 = nodes.ActionSetGameObjectVisibility()
    CON0020 = nodes.ConditionNot()
    ACT0021 = nodes.ActionSetGameObjectVisibility()
    ACT0022 = nodes.ActionSetGameObjectVisibility()
    CON0023 = nodes.ObjectPropertyOperator()
    CON0024 = nodes.ConditionNot()
    ACT0025 = nodes.ActionSetGameObjectVisibility()
    CON0026 = nodes.ObjectPropertyOperator()
    ACT0027 = nodes.ActionSetGameObjectVisibility()
    CON0028 = nodes.ObjectPropertyOperator()
    CON0029 = nodes.ConditionNot()
    ACT0030 = nodes.ActionSetGameObjectVisibility()
    ACT0031 = nodes.ActionSetGameObjectVisibility()
    CON0032 = nodes.ConditionNot()
    ACT0033 = nodes.ActionSetGameObjectVisibility()
    ACT0034 = nodes.ActionSetGameObjectVisibility()
    CON0035 = nodes.ObjectPropertyOperator()
    CON0036 = nodes.ConditionNot()
    ACT0037 = nodes.ActionSetGameObjectVisibility()
    CON0038 = nodes.ObjectPropertyOperator()
    ACT0039 = nodes.ActionSetGameObjectVisibility()
    CON0040 = nodes.ConditionNot()
    ACT0041 = nodes.ActionSetGameObjectVisibility()
    ACT0042 = nodes.ActionSetGameObjectVisibility()
    CON0043 = nodes.ObjectPropertyOperator()
    CON0044 = nodes.ConditionNot()
    ACT0045 = nodes.ActionSetGameObjectVisibility()
    ACT0046 = nodes.ActionSetGameObjectVisibility()
    CON0047 = nodes.ObjectPropertyOperator()
    CON0048 = nodes.ConditionNot()
    ACT0049 = nodes.ActionSetGameObjectVisibility()
    CON0050 = nodes.ObjectPropertyOperator()
    ACT0051 = nodes.ActionSetGameObjectVisibility()
    CON0052 = nodes.ConditionNot()
    ACT0053 = nodes.ActionSetGameObjectVisibility()
    CON0054 = nodes.ObjectPropertyOperator()
    CON0055 = nodes.ConditionNot()
    ACT0056 = nodes.ActionSetGameObjectVisibility()
    CON0057 = nodes.ObjectPropertyOperator()
    ACT0058 = nodes.ActionSetGameObjectVisibility()
    CON0059 = nodes.ConditionNot()
    ACT0060 = nodes.ActionSetGameObjectVisibility()
    ACT0061 = nodes.ActionSetGameObjectVisibility()
    CON0062 = nodes.ObjectPropertyOperator()
    CON0063 = nodes.ConditionNot()
    ACT0064 = nodes.ActionSetGameObjectVisibility()
    CON0065 = nodes.ObjectPropertyOperator()
    ACT0066 = nodes.ActionSetGameObjectVisibility()
    CON0067 = nodes.ObjectPropertyOperator()
    CON0068 = nodes.ConditionNot()
    ACT0069 = nodes.ActionSetGameObjectVisibility()
    ACT0070 = nodes.ActionSetGameObjectVisibility()
    CON0071 = nodes.ConditionNot()
    ACT0072 = nodes.ActionSetGameObjectVisibility()
    ACT0073 = nodes.ActionSetGameObjectVisibility()
    CON0074 = nodes.ObjectPropertyOperator()
    CON0075 = nodes.ConditionNot()
    ACT0076 = nodes.ActionSetGameObjectVisibility()
    ACT0077 = nodes.ActionSetGameObjectVisibility()
    CON0078 = nodes.ConditionNot()
    ACT0079 = nodes.ActionSetGameObjectVisibility()
    ACT0080 = nodes.ActionSetGameObjectVisibility()
    CON0081 = nodes.ObjectPropertyOperator()
    CON0082 = nodes.ConditionNot()
    ACT0083 = nodes.ActionSetGameObjectVisibility()
    ACT0084 = nodes.ActionSetGameObjectVisibility()
    CON0085 = nodes.ObjectPropertyOperator()
    CON0086 = nodes.ConditionNot()
    ACT0087 = nodes.ActionSetGameObjectVisibility()
    CON0088 = nodes.ObjectPropertyOperator()
    ACT0089 = nodes.ActionSetGameObjectVisibility()
    CON0090 = nodes.ObjectPropertyOperator()
    CON0091 = nodes.GE_OnInit()
    CON0092 = nodes.ConditionKeyReleased()
    CON0093 = nodes.ConditionKeyPressed()
    CON0094 = nodes.ConditionOr()
    CON0095 = nodes.ConditionOr()
    CON0096 = nodes.ConditionGamepadButtonUp()
    CON0097 = nodes.ObjectPropertyOperator()
    ACT0098 = nodes.ActionSetGameObjectGameProperty()
    CON0099 = nodes.ConditionGamepadButtons()
    ACT0100 = nodes.ActionSetGameObjectVisibility()
    ACT0101 = nodes.ActionSetPhysics()
    ACT0102 = nodes.ActionSetPhysics()
    CON0103 = nodes.ObjectPropertyOperator()
    CON0104 = nodes.ConditionOr()
    CON0105 = nodes.ObjectPropertyOperator()
    CON0106 = nodes.ObjectPropertyOperator()
    CON0107 = nodes.ObjectPropertyOperator()
    CON0108 = nodes.ObjectPropertyOperator()
    CON0109 = nodes.ConditionOr()
    CON0110 = nodes.ConditionAndList()
    CON0111 = nodes.ConditionAnd()
    ACT0000.condition = CON0003
    ACT0000.game_object = "NLO:CharacterController"
    ACT0000.property_name = "isBoosting"
    ACT0000.property_value = True
    ACT0001.condition = CON0006
    ACT0001.game_object = "NLO:CharacterController"
    ACT0001.property_name = "isBoosting"
    ACT0001.property_value = False
    ACT0002.condition = CON0103
    ACT0002.game_object = "NLO:eff_mod_boost_1"
    ACT0002.visible = False
    ACT0002.recursive = False
    CON0003.ca = CON0094
    CON0003.cb = CON0004
    CON0003.cc = CON0007
    CON0003.cd = True
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
    CON0006.ca = CON0095
    CON0006.cb = CON0005
    CON0006.cc = CON0008
    CON0006.cd = None
    CON0006.ce = None
    CON0006.cf = None
    CON0007.game_object = "NLO:CharacterController"
    CON0007.property_name = "isJumping"
    CON0007.compare_value = False
    CON0007.operator = 0
    CON0008.game_object = "NLO:CharacterController"
    CON0008.property_name = "isJumping"
    CON0008.compare_value = True
    CON0008.operator = 0
    ACT0009.condition = CON0091
    ACT0009.delay = 0.0
    PAR0010.condition = ACT0009
    PAR0010.camera = "NLO:CameraHud"
    PAR0010.collection = "HUD"
    ACT0011.condition = CON0018
    ACT0011.game_object = "NLO:s1"
    ACT0011.visible = True
    ACT0011.recursive = False
    CON0012.condition = CON0018
    ACT0013.condition = CON0012
    ACT0013.game_object = "NLO:s1"
    ACT0013.visible = False
    ACT0013.recursive = False
    ACT0014.condition = CON0015
    ACT0014.game_object = "NLO:s2"
    ACT0014.visible = True
    ACT0014.recursive = False
    CON0015.game_object = "NLO:CharacterController"
    CON0015.property_name = "Speed"
    CON0015.compare_value = 0.10000000149011612
    CON0015.operator = 4
    CON0016.condition = CON0015
    ACT0017.condition = CON0016
    ACT0017.game_object = "NLO:s2"
    ACT0017.visible = False
    ACT0017.recursive = False
    CON0018.game_object = "NLO:CharacterController"
    CON0018.property_name = "Speed"
    CON0018.compare_value = 0.05000000074505806
    CON0018.operator = 4
    ACT0019.condition = CON0026
    ACT0019.game_object = "NLO:s3"
    ACT0019.visible = True
    ACT0019.recursive = False
    CON0020.condition = CON0026
    ACT0021.condition = CON0020
    ACT0021.game_object = "NLO:s3"
    ACT0021.visible = False
    ACT0021.recursive = False
    ACT0022.condition = CON0023
    ACT0022.game_object = "NLO:s4"
    ACT0022.visible = True
    ACT0022.recursive = False
    CON0023.game_object = "NLO:CharacterController"
    CON0023.property_name = "Speed"
    CON0023.compare_value = 0.20000000298023224
    CON0023.operator = 4
    CON0024.condition = CON0023
    ACT0025.condition = CON0024
    ACT0025.game_object = "NLO:s4"
    ACT0025.visible = False
    ACT0025.recursive = False
    CON0026.game_object = "NLO:CharacterController"
    CON0026.property_name = "Speed"
    CON0026.compare_value = 0.15000000596046448
    CON0026.operator = 4
    ACT0027.condition = CON0028
    ACT0027.game_object = "NLO:s5"
    ACT0027.visible = True
    ACT0027.recursive = False
    CON0028.game_object = "NLO:CharacterController"
    CON0028.property_name = "Speed"
    CON0028.compare_value = 0.25
    CON0028.operator = 4
    CON0029.condition = CON0028
    ACT0030.condition = CON0029
    ACT0030.game_object = "NLO:s5"
    ACT0030.visible = False
    ACT0030.recursive = False
    ACT0031.condition = CON0038
    ACT0031.game_object = "NLO:s6"
    ACT0031.visible = True
    ACT0031.recursive = False
    CON0032.condition = CON0038
    ACT0033.condition = CON0032
    ACT0033.game_object = "NLO:s6"
    ACT0033.visible = False
    ACT0033.recursive = False
    ACT0034.condition = CON0035
    ACT0034.game_object = "NLO:s7"
    ACT0034.visible = True
    ACT0034.recursive = False
    CON0035.game_object = "NLO:CharacterController"
    CON0035.property_name = "Speed"
    CON0035.compare_value = 0.3499999940395355
    CON0035.operator = 4
    CON0036.condition = CON0035
    ACT0037.condition = CON0036
    ACT0037.game_object = "NLO:s7"
    ACT0037.visible = False
    ACT0037.recursive = False
    CON0038.game_object = "NLO:CharacterController"
    CON0038.property_name = "Speed"
    CON0038.compare_value = 0.30000001192092896
    CON0038.operator = 4
    ACT0039.condition = CON0050
    ACT0039.game_object = "NLO:s8"
    ACT0039.visible = True
    ACT0039.recursive = False
    CON0040.condition = CON0050
    ACT0041.condition = CON0040
    ACT0041.game_object = "NLO:s8"
    ACT0041.visible = False
    ACT0041.recursive = False
    ACT0042.condition = CON0043
    ACT0042.game_object = "NLO:s9"
    ACT0042.visible = True
    ACT0042.recursive = False
    CON0043.game_object = "NLO:CharacterController"
    CON0043.property_name = "Speed"
    CON0043.compare_value = 0.44999998807907104
    CON0043.operator = 4
    CON0044.condition = CON0043
    ACT0045.condition = CON0044
    ACT0045.game_object = "NLO:s9"
    ACT0045.visible = False
    ACT0045.recursive = False
    ACT0046.condition = CON0047
    ACT0046.game_object = "NLO:s10"
    ACT0046.visible = True
    ACT0046.recursive = False
    CON0047.game_object = "NLO:CharacterController"
    CON0047.property_name = "Speed"
    CON0047.compare_value = 0.5
    CON0047.operator = 4
    CON0048.condition = CON0047
    ACT0049.condition = CON0048
    ACT0049.game_object = "NLO:s10"
    ACT0049.visible = False
    ACT0049.recursive = False
    CON0050.game_object = "NLO:CharacterController"
    CON0050.property_name = "Speed"
    CON0050.compare_value = 0.4000000059604645
    CON0050.operator = 4
    ACT0051.condition = CON0057
    ACT0051.game_object = "NLO:s11"
    ACT0051.visible = True
    ACT0051.recursive = False
    CON0052.condition = CON0057
    ACT0053.condition = CON0054
    ACT0053.game_object = "NLO:s12"
    ACT0053.visible = True
    ACT0053.recursive = False
    CON0054.game_object = "NLO:CharacterController"
    CON0054.property_name = "Speed"
    CON0054.compare_value = 0.6000000238418579
    CON0054.operator = 4
    CON0055.condition = CON0054
    ACT0056.condition = CON0055
    ACT0056.game_object = "NLO:s12"
    ACT0056.visible = False
    ACT0056.recursive = False
    CON0057.game_object = "NLO:CharacterController"
    CON0057.property_name = "Speed"
    CON0057.compare_value = 0.550000011920929
    CON0057.operator = 4
    ACT0058.condition = CON0065
    ACT0058.game_object = "NLO:s13"
    ACT0058.visible = True
    ACT0058.recursive = False
    CON0059.condition = CON0065
    ACT0060.condition = CON0059
    ACT0060.game_object = "NLO:s13"
    ACT0060.visible = False
    ACT0060.recursive = False
    ACT0061.condition = CON0062
    ACT0061.game_object = "NLO:s14"
    ACT0061.visible = True
    ACT0061.recursive = False
    CON0062.game_object = "NLO:CharacterController"
    CON0062.property_name = "Speed"
    CON0062.compare_value = 0.699999988079071
    CON0062.operator = 4
    CON0063.condition = CON0062
    ACT0064.condition = CON0063
    ACT0064.game_object = "NLO:s14"
    ACT0064.visible = False
    ACT0064.recursive = False
    CON0065.game_object = "NLO:CharacterController"
    CON0065.property_name = "Speed"
    CON0065.compare_value = 0.6499999761581421
    CON0065.operator = 4
    ACT0066.condition = CON0067
    ACT0066.game_object = "NLO:s15"
    ACT0066.visible = True
    ACT0066.recursive = False
    CON0067.game_object = "NLO:CharacterController"
    CON0067.property_name = "Speed"
    CON0067.compare_value = 0.75
    CON0067.operator = 4
    CON0068.condition = CON0067
    ACT0069.condition = CON0068
    ACT0069.game_object = "NLO:s15"
    ACT0069.visible = False
    ACT0069.recursive = False
    ACT0070.condition = CON0090
    ACT0070.game_object = "NLO:s16"
    ACT0070.visible = True
    ACT0070.recursive = False
    CON0071.condition = CON0090
    ACT0072.condition = CON0071
    ACT0072.game_object = "NLO:s16"
    ACT0072.visible = False
    ACT0072.recursive = False
    ACT0073.condition = CON0074
    ACT0073.game_object = "NLO:s17"
    ACT0073.visible = True
    ACT0073.recursive = False
    CON0074.game_object = "NLO:CharacterController"
    CON0074.property_name = "Speed"
    CON0074.compare_value = 0.8500000238418579
    CON0074.operator = 4
    CON0075.condition = CON0074
    ACT0076.condition = CON0075
    ACT0076.game_object = "NLO:s17"
    ACT0076.visible = False
    ACT0076.recursive = False
    ACT0077.condition = CON0088
    ACT0077.game_object = "NLO:s18"
    ACT0077.visible = True
    ACT0077.recursive = False
    CON0078.condition = CON0088
    ACT0079.condition = CON0078
    ACT0079.game_object = "NLO:s18"
    ACT0079.visible = False
    ACT0079.recursive = False
    ACT0080.condition = CON0081
    ACT0080.game_object = "NLO:s19"
    ACT0080.visible = True
    ACT0080.recursive = False
    CON0081.game_object = "NLO:CharacterController"
    CON0081.property_name = "Speed"
    CON0081.compare_value = 0.949999988079071
    CON0081.operator = 4
    CON0082.condition = CON0081
    ACT0083.condition = CON0082
    ACT0083.game_object = "NLO:s19"
    ACT0083.visible = False
    ACT0083.recursive = False
    ACT0084.condition = CON0085
    ACT0084.game_object = "NLO:s20"
    ACT0084.visible = True
    ACT0084.recursive = False
    CON0085.game_object = "NLO:CharacterController"
    CON0085.property_name = "Speed"
    CON0085.compare_value = 1.0
    CON0085.operator = 4
    CON0086.condition = CON0085
    ACT0087.condition = CON0086
    ACT0087.game_object = "NLO:s20"
    ACT0087.visible = False
    ACT0087.recursive = False
    CON0088.game_object = "NLO:CharacterController"
    CON0088.property_name = "Speed"
    CON0088.compare_value = 0.8999999761581421
    CON0088.operator = 4
    ACT0089.condition = CON0052
    ACT0089.game_object = "NLO:s11"
    ACT0089.visible = False
    ACT0089.recursive = False
    CON0090.game_object = "NLO:CharacterController"
    CON0090.property_name = "Speed"
    CON0090.compare_value = 0.800000011920929
    CON0090.operator = 4
    CON0092.key_code = bge.events.LEFTSHIFTKEY
    CON0092.pulse = True
    CON0093.key_code = bge.events.LEFTSHIFTKEY
    CON0093.pulse = True
    CON0094.condition_a = CON0099.BUTTON
    CON0094.condition_b = CON0093
    CON0095.condition_a = CON0096.BUTTON
    CON0095.condition_b = CON0092
    CON0096.index = 0
    CON0096.pulse = True
    CON0096.button = 2
    CON0097.game_object = "NLO:CharacterController"
    CON0097.property_name = "isBoosting"
    CON0097.compare_value = True
    CON0097.operator = 0
    ACT0098.condition = CON0097
    ACT0098.game_object = "NLO:CharacterController"
    ACT0098.property_name = "Speed"
    ACT0098.property_value = 1.5
    CON0099.index = 0
    CON0099.pulse = True
    CON0099.button = 2
    ACT0100.condition = CON0110
    ACT0100.game_object = "NLO:eff_mod_boost_1"
    ACT0100.visible = True
    ACT0100.recursive = False
    ACT0101.condition = CON0104
    ACT0101.game_object = "NLO:Water"
    ACT0101.activate = False
    ACT0101.free_const = False
    ACT0102.condition = CON0111
    ACT0102.game_object = "NLO:Water"
    ACT0102.activate = True
    ACT0102.free_const = False
    CON0103.game_object = "NLO:CharacterController"
    CON0103.property_name = "isBoosting"
    CON0103.compare_value = False
    CON0103.operator = 0
    CON0104.condition_a = CON0105
    CON0104.condition_b = CON0103
    CON0105.game_object = "NLO:CharacterController"
    CON0105.property_name = "Speed"
    CON0105.compare_value = 1.0
    CON0105.operator = 3
    CON0106.game_object = "NLO:CharacterController"
    CON0106.property_name = "Speed"
    CON0106.compare_value = 1.0
    CON0106.operator = 4
    CON0107.game_object = "NLO:CharacterController"
    CON0107.property_name = "isBoosting"
    CON0107.compare_value = True
    CON0107.operator = 0
    CON0108.game_object = "NLO:CharacterController"
    CON0108.property_name = "isOnWaterP"
    CON0108.compare_value = False
    CON0108.operator = 0
    CON0109.condition_a = CON0110
    CON0109.condition_b = CON0106
    CON0110.ca = CON0107
    CON0110.cb = CON0004
    CON0110.cc = CON0007
    CON0110.cd = True
    CON0110.ce = True
    CON0110.cf = True
    CON0111.condition_a = CON0109
    CON0111.condition_b = CON0108
    network.add_cell(CON0004)
    network.add_cell(CON0007)
    network.add_cell(CON0015)
    network.add_cell(CON0018)
    network.add_cell(CON0023)
    network.add_cell(CON0026)
    network.add_cell(CON0028)
    network.add_cell(CON0035)
    network.add_cell(CON0038)
    network.add_cell(CON0043)
    network.add_cell(CON0047)
    network.add_cell(CON0050)
    network.add_cell(CON0054)
    network.add_cell(CON0057)
    network.add_cell(CON0062)
    network.add_cell(CON0065)
    network.add_cell(CON0067)
    network.add_cell(CON0074)
    network.add_cell(CON0081)
    network.add_cell(CON0085)
    network.add_cell(CON0088)
    network.add_cell(CON0090)
    network.add_cell(CON0092)
    network.add_cell(CON0096)
    network.add_cell(CON0099)
    network.add_cell(CON0103)
    network.add_cell(CON0105)
    network.add_cell(CON0107)
    network.add_cell(CON0110)
    network.add_cell(ACT0002)
    network.add_cell(CON0005)
    network.add_cell(CON0008)
    network.add_cell(ACT0011)
    network.add_cell(ACT0014)
    network.add_cell(ACT0019)
    network.add_cell(ACT0022)
    network.add_cell(ACT0027)
    network.add_cell(ACT0031)
    network.add_cell(ACT0034)
    network.add_cell(ACT0039)
    network.add_cell(ACT0042)
    network.add_cell(ACT0046)
    network.add_cell(ACT0051)
    network.add_cell(ACT0053)
    network.add_cell(ACT0058)
    network.add_cell(ACT0061)
    network.add_cell(ACT0066)
    network.add_cell(ACT0070)
    network.add_cell(ACT0073)
    network.add_cell(ACT0077)
    network.add_cell(ACT0080)
    network.add_cell(ACT0084)
    network.add_cell(CON0091)
    network.add_cell(CON0095)
    network.add_cell(ACT0100)
    network.add_cell(CON0104)
    network.add_cell(CON0108)
    network.add_cell(CON0006)
    network.add_cell(CON0012)
    network.add_cell(CON0016)
    network.add_cell(CON0020)
    network.add_cell(CON0024)
    network.add_cell(CON0029)
    network.add_cell(CON0032)
    network.add_cell(CON0036)
    network.add_cell(CON0040)
    network.add_cell(CON0044)
    network.add_cell(CON0048)
    network.add_cell(CON0052)
    network.add_cell(CON0059)
    network.add_cell(CON0063)
    network.add_cell(CON0068)
    network.add_cell(CON0071)
    network.add_cell(CON0075)
    network.add_cell(CON0078)
    network.add_cell(CON0082)
    network.add_cell(CON0086)
    network.add_cell(ACT0089)
    network.add_cell(CON0097)
    network.add_cell(ACT0101)
    network.add_cell(CON0106)
    network.add_cell(ACT0001)
    network.add_cell(ACT0009)
    network.add_cell(ACT0013)
    network.add_cell(ACT0021)
    network.add_cell(ACT0030)
    network.add_cell(ACT0037)
    network.add_cell(ACT0045)
    network.add_cell(CON0055)
    network.add_cell(ACT0060)
    network.add_cell(ACT0069)
    network.add_cell(ACT0076)
    network.add_cell(ACT0083)
    network.add_cell(CON0093)
    network.add_cell(ACT0098)
    network.add_cell(CON0109)
    network.add_cell(PAR0010)
    network.add_cell(ACT0025)
    network.add_cell(ACT0041)
    network.add_cell(ACT0056)
    network.add_cell(ACT0072)
    network.add_cell(ACT0087)
    network.add_cell(CON0111)
    network.add_cell(ACT0017)
    network.add_cell(ACT0049)
    network.add_cell(ACT0079)
    network.add_cell(ACT0102)
    network.add_cell(ACT0033)
    network.add_cell(CON0094)
    network.add_cell(CON0003)
    network.add_cell(ACT0000)
    network.add_cell(ACT0064)
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
