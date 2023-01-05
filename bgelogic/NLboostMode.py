# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionSetGameObjectGameProperty()
    ACT0001 = nodes.ActionSetGameObjectGameProperty()
    CON0002 = nodes.ObjectPropertyOperator()
    ACT0003 = nodes.ActionSetGameObjectVisibility()
    CON0004 = nodes.ConditionAndList()
    ACT0005 = nodes.ActionSetGameObjectVisibility()
    CON0006 = nodes.ConditionAndList()
    CON0007 = nodes.ObjectPropertyOperator()
    CON0008 = nodes.ObjectPropertyOperator()
    CON0009 = nodes.ObjectPropertyOperator()
    CON0010 = nodes.ConditionOrList()
    CON0011 = nodes.ObjectPropertyOperator()
    CON0012 = nodes.ObjectPropertyOperator()
    ACT0013 = nodes.ActionTimeFilter()
    PAR0014 = nodes.GESetOverlayCollection()
    ACT0015 = nodes.ActionSetGameObjectVisibility()
    CON0016 = nodes.ConditionNot()
    ACT0017 = nodes.ActionSetGameObjectVisibility()
    ACT0018 = nodes.ActionSetGameObjectVisibility()
    CON0019 = nodes.ObjectPropertyOperator()
    CON0020 = nodes.ConditionNot()
    ACT0021 = nodes.ActionSetGameObjectVisibility()
    CON0022 = nodes.ObjectPropertyOperator()
    ACT0023 = nodes.ActionSetGameObjectVisibility()
    CON0024 = nodes.ConditionNot()
    ACT0025 = nodes.ActionSetGameObjectVisibility()
    ACT0026 = nodes.ActionSetGameObjectVisibility()
    CON0027 = nodes.ObjectPropertyOperator()
    CON0028 = nodes.ConditionNot()
    ACT0029 = nodes.ActionSetGameObjectVisibility()
    CON0030 = nodes.ObjectPropertyOperator()
    ACT0031 = nodes.ActionSetGameObjectVisibility()
    CON0032 = nodes.ObjectPropertyOperator()
    CON0033 = nodes.ConditionNot()
    ACT0034 = nodes.ActionSetGameObjectVisibility()
    ACT0035 = nodes.ActionSetGameObjectVisibility()
    CON0036 = nodes.ConditionNot()
    ACT0037 = nodes.ActionSetGameObjectVisibility()
    ACT0038 = nodes.ActionSetGameObjectVisibility()
    CON0039 = nodes.ObjectPropertyOperator()
    CON0040 = nodes.ConditionNot()
    ACT0041 = nodes.ActionSetGameObjectVisibility()
    CON0042 = nodes.ObjectPropertyOperator()
    ACT0043 = nodes.ActionSetGameObjectVisibility()
    CON0044 = nodes.ConditionNot()
    ACT0045 = nodes.ActionSetGameObjectVisibility()
    ACT0046 = nodes.ActionSetGameObjectVisibility()
    CON0047 = nodes.ObjectPropertyOperator()
    CON0048 = nodes.ConditionNot()
    ACT0049 = nodes.ActionSetGameObjectVisibility()
    ACT0050 = nodes.ActionSetGameObjectVisibility()
    CON0051 = nodes.ObjectPropertyOperator()
    CON0052 = nodes.ConditionNot()
    ACT0053 = nodes.ActionSetGameObjectVisibility()
    CON0054 = nodes.ObjectPropertyOperator()
    ACT0055 = nodes.ActionSetGameObjectVisibility()
    CON0056 = nodes.ConditionNot()
    ACT0057 = nodes.ActionSetGameObjectVisibility()
    CON0058 = nodes.ObjectPropertyOperator()
    CON0059 = nodes.ConditionNot()
    ACT0060 = nodes.ActionSetGameObjectVisibility()
    CON0061 = nodes.ObjectPropertyOperator()
    ACT0062 = nodes.ActionSetGameObjectVisibility()
    CON0063 = nodes.ConditionNot()
    ACT0064 = nodes.ActionSetGameObjectVisibility()
    ACT0065 = nodes.ActionSetGameObjectVisibility()
    CON0066 = nodes.ObjectPropertyOperator()
    CON0067 = nodes.ConditionNot()
    ACT0068 = nodes.ActionSetGameObjectVisibility()
    CON0069 = nodes.ObjectPropertyOperator()
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
    CON0082 = nodes.ConditionNot()
    ACT0083 = nodes.ActionSetGameObjectVisibility()
    ACT0084 = nodes.ActionSetGameObjectVisibility()
    CON0085 = nodes.ObjectPropertyOperator()
    CON0086 = nodes.ConditionNot()
    ACT0087 = nodes.ActionSetGameObjectVisibility()
    ACT0088 = nodes.ActionSetGameObjectVisibility()
    CON0089 = nodes.ObjectPropertyOperator()
    CON0090 = nodes.ConditionNot()
    ACT0091 = nodes.ActionSetGameObjectVisibility()
    CON0092 = nodes.ObjectPropertyOperator()
    ACT0093 = nodes.ActionSetGameObjectVisibility()
    CON0094 = nodes.ObjectPropertyOperator()
    CON0095 = nodes.GE_OnInit()
    CON0096 = nodes.ConditionKeyReleased()
    CON0097 = nodes.ConditionKeyPressed()
    CON0098 = nodes.ConditionOr()
    CON0099 = nodes.ConditionOr()
    CON0100 = nodes.ConditionGamepadButtonUp()
    CON0101 = nodes.ConditionGamepadButtons()
    CON0102 = nodes.ObjectPropertyOperator()
    ACT0103 = nodes.ActionSetGameObjectGameProperty()
    ACT0000.condition = CON0006
    ACT0000.game_object = "NLO:CharacterController"
    ACT0000.property_name = "isBoosting"
    ACT0000.property_value = True
    ACT0001.condition = CON0010
    ACT0001.game_object = "NLO:CharacterController"
    ACT0001.property_name = "isBoosting"
    ACT0001.property_value = False
    CON0002.game_object = "NLO:CharacterController"
    CON0002.property_name = "isBoosting"
    CON0002.compare_value = False
    CON0002.operator = 0
    ACT0003.condition = CON0004
    ACT0003.game_object = "NLO:eff_mod_boost_1"
    ACT0003.visible = True
    ACT0003.recursive = False
    CON0004.ca = CON0007
    CON0004.cb = CON0008
    CON0004.cc = CON0011
    CON0004.cd = True
    CON0004.ce = True
    CON0004.cf = True
    ACT0005.condition = CON0002
    ACT0005.game_object = "NLO:eff_mod_boost_1"
    ACT0005.visible = False
    ACT0005.recursive = False
    CON0006.ca = CON0098
    CON0006.cb = CON0008
    CON0006.cc = CON0011
    CON0006.cd = True
    CON0006.ce = True
    CON0006.cf = True
    CON0007.game_object = "NLO:CharacterController"
    CON0007.property_name = "isBoosting"
    CON0007.compare_value = True
    CON0007.operator = 0
    CON0008.game_object = "NLO:CharacterController"
    CON0008.property_name = "isStomping"
    CON0008.compare_value = False
    CON0008.operator = 0
    CON0009.game_object = "NLO:CharacterController"
    CON0009.property_name = "isStomping"
    CON0009.compare_value = True
    CON0009.operator = 0
    CON0010.ca = CON0099
    CON0010.cb = CON0009
    CON0010.cc = CON0012
    CON0010.cd = None
    CON0010.ce = None
    CON0010.cf = None
    CON0011.game_object = "NLO:CharacterController"
    CON0011.property_name = "isJumping"
    CON0011.compare_value = False
    CON0011.operator = 0
    CON0012.game_object = "NLO:CharacterController"
    CON0012.property_name = "isJumping"
    CON0012.compare_value = True
    CON0012.operator = 0
    ACT0013.condition = CON0095
    ACT0013.delay = 0.0
    PAR0014.condition = ACT0013
    PAR0014.camera = "NLO:CameraHud"
    PAR0014.collection = "HUD"
    ACT0015.condition = CON0022
    ACT0015.game_object = "NLO:s1"
    ACT0015.visible = True
    ACT0015.recursive = False
    CON0016.condition = CON0022
    ACT0017.condition = CON0016
    ACT0017.game_object = "NLO:s1"
    ACT0017.visible = False
    ACT0017.recursive = False
    ACT0018.condition = CON0019
    ACT0018.game_object = "NLO:s2"
    ACT0018.visible = True
    ACT0018.recursive = False
    CON0019.game_object = "NLO:CharacterController"
    CON0019.property_name = "Speed"
    CON0019.compare_value = 0.10000000149011612
    CON0019.operator = 4
    CON0020.condition = CON0019
    ACT0021.condition = CON0020
    ACT0021.game_object = "NLO:s2"
    ACT0021.visible = False
    ACT0021.recursive = False
    CON0022.game_object = "NLO:CharacterController"
    CON0022.property_name = "Speed"
    CON0022.compare_value = 0.05000000074505806
    CON0022.operator = 4
    ACT0023.condition = CON0030
    ACT0023.game_object = "NLO:s3"
    ACT0023.visible = True
    ACT0023.recursive = False
    CON0024.condition = CON0030
    ACT0025.condition = CON0024
    ACT0025.game_object = "NLO:s3"
    ACT0025.visible = False
    ACT0025.recursive = False
    ACT0026.condition = CON0027
    ACT0026.game_object = "NLO:s4"
    ACT0026.visible = True
    ACT0026.recursive = False
    CON0027.game_object = "NLO:CharacterController"
    CON0027.property_name = "Speed"
    CON0027.compare_value = 0.20000000298023224
    CON0027.operator = 4
    CON0028.condition = CON0027
    ACT0029.condition = CON0028
    ACT0029.game_object = "NLO:s4"
    ACT0029.visible = False
    ACT0029.recursive = False
    CON0030.game_object = "NLO:CharacterController"
    CON0030.property_name = "Speed"
    CON0030.compare_value = 0.15000000596046448
    CON0030.operator = 4
    ACT0031.condition = CON0032
    ACT0031.game_object = "NLO:s5"
    ACT0031.visible = True
    ACT0031.recursive = False
    CON0032.game_object = "NLO:CharacterController"
    CON0032.property_name = "Speed"
    CON0032.compare_value = 0.25
    CON0032.operator = 4
    CON0033.condition = CON0032
    ACT0034.condition = CON0033
    ACT0034.game_object = "NLO:s5"
    ACT0034.visible = False
    ACT0034.recursive = False
    ACT0035.condition = CON0042
    ACT0035.game_object = "NLO:s6"
    ACT0035.visible = True
    ACT0035.recursive = False
    CON0036.condition = CON0042
    ACT0037.condition = CON0036
    ACT0037.game_object = "NLO:s6"
    ACT0037.visible = False
    ACT0037.recursive = False
    ACT0038.condition = CON0039
    ACT0038.game_object = "NLO:s7"
    ACT0038.visible = True
    ACT0038.recursive = False
    CON0039.game_object = "NLO:CharacterController"
    CON0039.property_name = "Speed"
    CON0039.compare_value = 0.3499999940395355
    CON0039.operator = 4
    CON0040.condition = CON0039
    ACT0041.condition = CON0040
    ACT0041.game_object = "NLO:s7"
    ACT0041.visible = False
    ACT0041.recursive = False
    CON0042.game_object = "NLO:CharacterController"
    CON0042.property_name = "Speed"
    CON0042.compare_value = 0.30000001192092896
    CON0042.operator = 4
    ACT0043.condition = CON0054
    ACT0043.game_object = "NLO:s8"
    ACT0043.visible = True
    ACT0043.recursive = False
    CON0044.condition = CON0054
    ACT0045.condition = CON0044
    ACT0045.game_object = "NLO:s8"
    ACT0045.visible = False
    ACT0045.recursive = False
    ACT0046.condition = CON0047
    ACT0046.game_object = "NLO:s9"
    ACT0046.visible = True
    ACT0046.recursive = False
    CON0047.game_object = "NLO:CharacterController"
    CON0047.property_name = "Speed"
    CON0047.compare_value = 0.44999998807907104
    CON0047.operator = 4
    CON0048.condition = CON0047
    ACT0049.condition = CON0048
    ACT0049.game_object = "NLO:s9"
    ACT0049.visible = False
    ACT0049.recursive = False
    ACT0050.condition = CON0051
    ACT0050.game_object = "NLO:s10"
    ACT0050.visible = True
    ACT0050.recursive = False
    CON0051.game_object = "NLO:CharacterController"
    CON0051.property_name = "Speed"
    CON0051.compare_value = 0.5
    CON0051.operator = 4
    CON0052.condition = CON0051
    ACT0053.condition = CON0052
    ACT0053.game_object = "NLO:s10"
    ACT0053.visible = False
    ACT0053.recursive = False
    CON0054.game_object = "NLO:CharacterController"
    CON0054.property_name = "Speed"
    CON0054.compare_value = 0.4000000059604645
    CON0054.operator = 4
    ACT0055.condition = CON0061
    ACT0055.game_object = "NLO:s11"
    ACT0055.visible = True
    ACT0055.recursive = False
    CON0056.condition = CON0061
    ACT0057.condition = CON0058
    ACT0057.game_object = "NLO:s12"
    ACT0057.visible = True
    ACT0057.recursive = False
    CON0058.game_object = "NLO:CharacterController"
    CON0058.property_name = "Speed"
    CON0058.compare_value = 0.6000000238418579
    CON0058.operator = 4
    CON0059.condition = CON0058
    ACT0060.condition = CON0059
    ACT0060.game_object = "NLO:s12"
    ACT0060.visible = False
    ACT0060.recursive = False
    CON0061.game_object = "NLO:CharacterController"
    CON0061.property_name = "Speed"
    CON0061.compare_value = 0.550000011920929
    CON0061.operator = 4
    ACT0062.condition = CON0069
    ACT0062.game_object = "NLO:s13"
    ACT0062.visible = True
    ACT0062.recursive = False
    CON0063.condition = CON0069
    ACT0064.condition = CON0063
    ACT0064.game_object = "NLO:s13"
    ACT0064.visible = False
    ACT0064.recursive = False
    ACT0065.condition = CON0066
    ACT0065.game_object = "NLO:s14"
    ACT0065.visible = True
    ACT0065.recursive = False
    CON0066.game_object = "NLO:CharacterController"
    CON0066.property_name = "Speed"
    CON0066.compare_value = 0.699999988079071
    CON0066.operator = 4
    CON0067.condition = CON0066
    ACT0068.condition = CON0067
    ACT0068.game_object = "NLO:s14"
    ACT0068.visible = False
    ACT0068.recursive = False
    CON0069.game_object = "NLO:CharacterController"
    CON0069.property_name = "Speed"
    CON0069.compare_value = 0.6499999761581421
    CON0069.operator = 4
    ACT0070.condition = CON0071
    ACT0070.game_object = "NLO:s15"
    ACT0070.visible = True
    ACT0070.recursive = False
    CON0071.game_object = "NLO:CharacterController"
    CON0071.property_name = "Speed"
    CON0071.compare_value = 0.75
    CON0071.operator = 4
    CON0072.condition = CON0071
    ACT0073.condition = CON0072
    ACT0073.game_object = "NLO:s15"
    ACT0073.visible = False
    ACT0073.recursive = False
    ACT0074.condition = CON0094
    ACT0074.game_object = "NLO:s16"
    ACT0074.visible = True
    ACT0074.recursive = False
    CON0075.condition = CON0094
    ACT0076.condition = CON0075
    ACT0076.game_object = "NLO:s16"
    ACT0076.visible = False
    ACT0076.recursive = False
    ACT0077.condition = CON0078
    ACT0077.game_object = "NLO:s17"
    ACT0077.visible = True
    ACT0077.recursive = False
    CON0078.game_object = "NLO:CharacterController"
    CON0078.property_name = "Speed"
    CON0078.compare_value = 0.8500000238418579
    CON0078.operator = 4
    CON0079.condition = CON0078
    ACT0080.condition = CON0079
    ACT0080.game_object = "NLO:s17"
    ACT0080.visible = False
    ACT0080.recursive = False
    ACT0081.condition = CON0092
    ACT0081.game_object = "NLO:s18"
    ACT0081.visible = True
    ACT0081.recursive = False
    CON0082.condition = CON0092
    ACT0083.condition = CON0082
    ACT0083.game_object = "NLO:s18"
    ACT0083.visible = False
    ACT0083.recursive = False
    ACT0084.condition = CON0085
    ACT0084.game_object = "NLO:s19"
    ACT0084.visible = True
    ACT0084.recursive = False
    CON0085.game_object = "NLO:CharacterController"
    CON0085.property_name = "Speed"
    CON0085.compare_value = 0.949999988079071
    CON0085.operator = 4
    CON0086.condition = CON0085
    ACT0087.condition = CON0086
    ACT0087.game_object = "NLO:s19"
    ACT0087.visible = False
    ACT0087.recursive = False
    ACT0088.condition = CON0089
    ACT0088.game_object = "NLO:s20"
    ACT0088.visible = True
    ACT0088.recursive = False
    CON0089.game_object = "NLO:CharacterController"
    CON0089.property_name = "Speed"
    CON0089.compare_value = 1.0
    CON0089.operator = 4
    CON0090.condition = CON0089
    ACT0091.condition = CON0090
    ACT0091.game_object = "NLO:s20"
    ACT0091.visible = False
    ACT0091.recursive = False
    CON0092.game_object = "NLO:CharacterController"
    CON0092.property_name = "Speed"
    CON0092.compare_value = 0.8999999761581421
    CON0092.operator = 4
    ACT0093.condition = CON0056
    ACT0093.game_object = "NLO:s11"
    ACT0093.visible = False
    ACT0093.recursive = False
    CON0094.game_object = "NLO:CharacterController"
    CON0094.property_name = "Speed"
    CON0094.compare_value = 0.800000011920929
    CON0094.operator = 4
    CON0096.key_code = bge.events.LEFTSHIFTKEY
    CON0096.pulse = True
    CON0097.key_code = bge.events.LEFTSHIFTKEY
    CON0097.pulse = True
    CON0098.condition_a = CON0101.BUTTON
    CON0098.condition_b = CON0097
    CON0099.condition_a = CON0100.BUTTON
    CON0099.condition_b = CON0096
    CON0100.index = 0
    CON0100.pulse = True
    CON0100.button = 2
    CON0101.index = 0
    CON0101.pulse = True
    CON0101.button = 2
    CON0102.game_object = "NLO:CharacterController"
    CON0102.property_name = "isBoosting"
    CON0102.compare_value = True
    CON0102.operator = 0
    ACT0103.condition = CON0102
    ACT0103.game_object = "NLO:CharacterController"
    ACT0103.property_name = "Speed"
    ACT0103.property_value = 1.5
    network.add_cell(CON0002)
    network.add_cell(ACT0005)
    network.add_cell(CON0007)
    network.add_cell(CON0009)
    network.add_cell(CON0011)
    network.add_cell(CON0019)
    network.add_cell(CON0022)
    network.add_cell(CON0027)
    network.add_cell(CON0030)
    network.add_cell(CON0032)
    network.add_cell(CON0039)
    network.add_cell(CON0042)
    network.add_cell(CON0047)
    network.add_cell(CON0051)
    network.add_cell(CON0054)
    network.add_cell(CON0058)
    network.add_cell(CON0061)
    network.add_cell(CON0066)
    network.add_cell(CON0069)
    network.add_cell(CON0071)
    network.add_cell(CON0078)
    network.add_cell(CON0085)
    network.add_cell(CON0089)
    network.add_cell(CON0092)
    network.add_cell(CON0094)
    network.add_cell(CON0096)
    network.add_cell(CON0100)
    network.add_cell(CON0102)
    network.add_cell(CON0008)
    network.add_cell(CON0012)
    network.add_cell(ACT0015)
    network.add_cell(ACT0018)
    network.add_cell(ACT0023)
    network.add_cell(ACT0026)
    network.add_cell(ACT0031)
    network.add_cell(ACT0035)
    network.add_cell(ACT0038)
    network.add_cell(ACT0043)
    network.add_cell(ACT0046)
    network.add_cell(ACT0050)
    network.add_cell(ACT0055)
    network.add_cell(ACT0057)
    network.add_cell(ACT0062)
    network.add_cell(ACT0065)
    network.add_cell(ACT0070)
    network.add_cell(ACT0074)
    network.add_cell(ACT0077)
    network.add_cell(ACT0081)
    network.add_cell(ACT0084)
    network.add_cell(ACT0088)
    network.add_cell(CON0095)
    network.add_cell(CON0099)
    network.add_cell(ACT0103)
    network.add_cell(CON0004)
    network.add_cell(CON0010)
    network.add_cell(CON0016)
    network.add_cell(CON0020)
    network.add_cell(CON0024)
    network.add_cell(CON0028)
    network.add_cell(CON0033)
    network.add_cell(CON0036)
    network.add_cell(CON0040)
    network.add_cell(CON0044)
    network.add_cell(CON0048)
    network.add_cell(CON0052)
    network.add_cell(CON0056)
    network.add_cell(CON0063)
    network.add_cell(CON0067)
    network.add_cell(CON0072)
    network.add_cell(CON0075)
    network.add_cell(CON0079)
    network.add_cell(CON0082)
    network.add_cell(CON0086)
    network.add_cell(CON0090)
    network.add_cell(ACT0093)
    network.add_cell(CON0101)
    network.add_cell(ACT0001)
    network.add_cell(ACT0013)
    network.add_cell(ACT0017)
    network.add_cell(ACT0025)
    network.add_cell(ACT0034)
    network.add_cell(ACT0041)
    network.add_cell(ACT0049)
    network.add_cell(CON0059)
    network.add_cell(ACT0064)
    network.add_cell(ACT0073)
    network.add_cell(ACT0080)
    network.add_cell(ACT0087)
    network.add_cell(CON0097)
    network.add_cell(ACT0003)
    network.add_cell(PAR0014)
    network.add_cell(ACT0029)
    network.add_cell(ACT0045)
    network.add_cell(ACT0060)
    network.add_cell(ACT0076)
    network.add_cell(ACT0091)
    network.add_cell(ACT0021)
    network.add_cell(ACT0053)
    network.add_cell(ACT0083)
    network.add_cell(ACT0037)
    network.add_cell(CON0098)
    network.add_cell(CON0006)
    network.add_cell(ACT0000)
    network.add_cell(ACT0068)
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
