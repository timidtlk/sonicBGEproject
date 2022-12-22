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
    CON0007 = nodes.ConditionKeyPressed()
    CON0008 = nodes.ObjectPropertyOperator()
    CON0009 = nodes.ObjectPropertyOperator()
    CON0010 = nodes.ObjectPropertyOperator()
    CON0011 = nodes.ConditionOrList()
    CON0012 = nodes.ConditionKeyReleased()
    CON0013 = nodes.ObjectPropertyOperator()
    CON0014 = nodes.ObjectPropertyOperator()
    ACT0015 = nodes.ActionTimeFilter()
    PAR0016 = nodes.GESetOverlayCollection()
    ACT0017 = nodes.ActionSetGameObjectVisibility()
    CON0018 = nodes.ConditionNot()
    ACT0019 = nodes.ActionSetGameObjectVisibility()
    ACT0020 = nodes.ActionSetGameObjectVisibility()
    CON0021 = nodes.ObjectPropertyOperator()
    CON0022 = nodes.ConditionNot()
    ACT0023 = nodes.ActionSetGameObjectVisibility()
    CON0024 = nodes.ObjectPropertyOperator()
    ACT0025 = nodes.ActionSetGameObjectVisibility()
    CON0026 = nodes.ConditionNot()
    ACT0027 = nodes.ActionSetGameObjectVisibility()
    ACT0028 = nodes.ActionSetGameObjectVisibility()
    CON0029 = nodes.ObjectPropertyOperator()
    CON0030 = nodes.ConditionNot()
    ACT0031 = nodes.ActionSetGameObjectVisibility()
    CON0032 = nodes.ObjectPropertyOperator()
    ACT0033 = nodes.ActionSetGameObjectVisibility()
    CON0034 = nodes.ObjectPropertyOperator()
    CON0035 = nodes.ConditionNot()
    ACT0036 = nodes.ActionSetGameObjectVisibility()
    ACT0037 = nodes.ActionSetGameObjectVisibility()
    CON0038 = nodes.ConditionNot()
    ACT0039 = nodes.ActionSetGameObjectVisibility()
    ACT0040 = nodes.ActionSetGameObjectVisibility()
    CON0041 = nodes.ObjectPropertyOperator()
    CON0042 = nodes.ConditionNot()
    ACT0043 = nodes.ActionSetGameObjectVisibility()
    CON0044 = nodes.ObjectPropertyOperator()
    ACT0045 = nodes.ActionSetGameObjectVisibility()
    CON0046 = nodes.ConditionNot()
    ACT0047 = nodes.ActionSetGameObjectVisibility()
    ACT0048 = nodes.ActionSetGameObjectVisibility()
    CON0049 = nodes.ObjectPropertyOperator()
    CON0050 = nodes.ConditionNot()
    ACT0051 = nodes.ActionSetGameObjectVisibility()
    ACT0052 = nodes.ActionSetGameObjectVisibility()
    CON0053 = nodes.ObjectPropertyOperator()
    CON0054 = nodes.ConditionNot()
    ACT0055 = nodes.ActionSetGameObjectVisibility()
    CON0056 = nodes.ObjectPropertyOperator()
    ACT0057 = nodes.ActionSetGameObjectVisibility()
    CON0058 = nodes.ConditionNot()
    ACT0059 = nodes.ActionSetGameObjectVisibility()
    CON0060 = nodes.ObjectPropertyOperator()
    CON0061 = nodes.ConditionNot()
    ACT0062 = nodes.ActionSetGameObjectVisibility()
    CON0063 = nodes.ObjectPropertyOperator()
    ACT0064 = nodes.ActionSetGameObjectVisibility()
    CON0065 = nodes.ConditionNot()
    ACT0066 = nodes.ActionSetGameObjectVisibility()
    ACT0067 = nodes.ActionSetGameObjectVisibility()
    CON0068 = nodes.ObjectPropertyOperator()
    CON0069 = nodes.ConditionNot()
    ACT0070 = nodes.ActionSetGameObjectVisibility()
    CON0071 = nodes.ObjectPropertyOperator()
    ACT0072 = nodes.ActionSetGameObjectVisibility()
    CON0073 = nodes.ObjectPropertyOperator()
    CON0074 = nodes.ConditionNot()
    ACT0075 = nodes.ActionSetGameObjectVisibility()
    ACT0076 = nodes.ActionSetGameObjectVisibility()
    CON0077 = nodes.ConditionNot()
    ACT0078 = nodes.ActionSetGameObjectVisibility()
    ACT0079 = nodes.ActionSetGameObjectVisibility()
    CON0080 = nodes.ObjectPropertyOperator()
    CON0081 = nodes.ConditionNot()
    ACT0082 = nodes.ActionSetGameObjectVisibility()
    ACT0083 = nodes.ActionSetGameObjectVisibility()
    CON0084 = nodes.ConditionNot()
    ACT0085 = nodes.ActionSetGameObjectVisibility()
    ACT0086 = nodes.ActionSetGameObjectVisibility()
    CON0087 = nodes.ObjectPropertyOperator()
    CON0088 = nodes.ConditionNot()
    ACT0089 = nodes.ActionSetGameObjectVisibility()
    ACT0090 = nodes.ActionSetGameObjectVisibility()
    CON0091 = nodes.ObjectPropertyOperator()
    CON0092 = nodes.ConditionNot()
    ACT0093 = nodes.ActionSetGameObjectVisibility()
    CON0094 = nodes.ObjectPropertyOperator()
    ACT0095 = nodes.ActionSetGameObjectVisibility()
    CON0096 = nodes.ObjectPropertyOperator()
    CON0097 = nodes.GE_OnInit()
    ACT0000.condition = CON0006
    ACT0000.game_object = "NLO:CharacterController"
    ACT0000.property_name = "isBoosting"
    ACT0000.property_value = True
    ACT0001.condition = CON0011
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
    CON0004.ca = CON0008
    CON0004.cb = CON0009
    CON0004.cc = CON0013
    CON0004.cd = True
    CON0004.ce = True
    CON0004.cf = True
    ACT0005.condition = CON0002
    ACT0005.game_object = "NLO:eff_mod_boost_1"
    ACT0005.visible = False
    ACT0005.recursive = False
    CON0006.ca = CON0007
    CON0006.cb = CON0009
    CON0006.cc = CON0013
    CON0006.cd = True
    CON0006.ce = True
    CON0006.cf = True
    CON0007.key_code = bge.events.LEFTSHIFTKEY
    CON0007.pulse = True
    CON0008.game_object = "NLO:CharacterController"
    CON0008.property_name = "isBoosting"
    CON0008.compare_value = True
    CON0008.operator = 0
    CON0009.game_object = "NLO:CharacterController"
    CON0009.property_name = "isStomping"
    CON0009.compare_value = False
    CON0009.operator = 0
    CON0010.game_object = "NLO:CharacterController"
    CON0010.property_name = "isStomping"
    CON0010.compare_value = True
    CON0010.operator = 0
    CON0011.ca = CON0012
    CON0011.cb = CON0010
    CON0011.cc = CON0014
    CON0011.cd = None
    CON0011.ce = None
    CON0011.cf = None
    CON0012.key_code = bge.events.LEFTSHIFTKEY
    CON0012.pulse = True
    CON0013.game_object = "NLO:CharacterController"
    CON0013.property_name = "isJumping"
    CON0013.compare_value = False
    CON0013.operator = 0
    CON0014.game_object = "NLO:CharacterController"
    CON0014.property_name = "isJumping"
    CON0014.compare_value = True
    CON0014.operator = 0
    ACT0015.condition = CON0097
    ACT0015.delay = 0.0
    PAR0016.condition = ACT0015
    PAR0016.camera = "NLO:CameraHud"
    PAR0016.collection = "HUD"
    ACT0017.condition = CON0024
    ACT0017.game_object = "NLO:s1"
    ACT0017.visible = True
    ACT0017.recursive = False
    CON0018.condition = CON0024
    ACT0019.condition = CON0018
    ACT0019.game_object = "NLO:s1"
    ACT0019.visible = False
    ACT0019.recursive = False
    ACT0020.condition = CON0021
    ACT0020.game_object = "NLO:s2"
    ACT0020.visible = True
    ACT0020.recursive = False
    CON0021.game_object = "NLO:CharacterController"
    CON0021.property_name = "Speed"
    CON0021.compare_value = 0.10000000149011612
    CON0021.operator = 4
    CON0022.condition = CON0021
    ACT0023.condition = CON0022
    ACT0023.game_object = "NLO:s2"
    ACT0023.visible = False
    ACT0023.recursive = False
    CON0024.game_object = "NLO:CharacterController"
    CON0024.property_name = "Speed"
    CON0024.compare_value = 0.05000000074505806
    CON0024.operator = 4
    ACT0025.condition = CON0032
    ACT0025.game_object = "NLO:s3"
    ACT0025.visible = True
    ACT0025.recursive = False
    CON0026.condition = CON0032
    ACT0027.condition = CON0026
    ACT0027.game_object = "NLO:s3"
    ACT0027.visible = False
    ACT0027.recursive = False
    ACT0028.condition = CON0029
    ACT0028.game_object = "NLO:s4"
    ACT0028.visible = True
    ACT0028.recursive = False
    CON0029.game_object = "NLO:CharacterController"
    CON0029.property_name = "Speed"
    CON0029.compare_value = 0.20000000298023224
    CON0029.operator = 4
    CON0030.condition = CON0029
    ACT0031.condition = CON0030
    ACT0031.game_object = "NLO:s4"
    ACT0031.visible = False
    ACT0031.recursive = False
    CON0032.game_object = "NLO:CharacterController"
    CON0032.property_name = "Speed"
    CON0032.compare_value = 0.15000000596046448
    CON0032.operator = 4
    ACT0033.condition = CON0034
    ACT0033.game_object = "NLO:s5"
    ACT0033.visible = True
    ACT0033.recursive = False
    CON0034.game_object = "NLO:CharacterController"
    CON0034.property_name = "Speed"
    CON0034.compare_value = 0.25
    CON0034.operator = 4
    CON0035.condition = CON0034
    ACT0036.condition = CON0035
    ACT0036.game_object = "NLO:s5"
    ACT0036.visible = False
    ACT0036.recursive = False
    ACT0037.condition = CON0044
    ACT0037.game_object = "NLO:s6"
    ACT0037.visible = True
    ACT0037.recursive = False
    CON0038.condition = CON0044
    ACT0039.condition = CON0038
    ACT0039.game_object = "NLO:s6"
    ACT0039.visible = False
    ACT0039.recursive = False
    ACT0040.condition = CON0041
    ACT0040.game_object = "NLO:s7"
    ACT0040.visible = True
    ACT0040.recursive = False
    CON0041.game_object = "NLO:CharacterController"
    CON0041.property_name = "Speed"
    CON0041.compare_value = 0.3499999940395355
    CON0041.operator = 4
    CON0042.condition = CON0041
    ACT0043.condition = CON0042
    ACT0043.game_object = "NLO:s7"
    ACT0043.visible = False
    ACT0043.recursive = False
    CON0044.game_object = "NLO:CharacterController"
    CON0044.property_name = "Speed"
    CON0044.compare_value = 0.30000001192092896
    CON0044.operator = 4
    ACT0045.condition = CON0056
    ACT0045.game_object = "NLO:s8"
    ACT0045.visible = True
    ACT0045.recursive = False
    CON0046.condition = CON0056
    ACT0047.condition = CON0046
    ACT0047.game_object = "NLO:s8"
    ACT0047.visible = False
    ACT0047.recursive = False
    ACT0048.condition = CON0049
    ACT0048.game_object = "NLO:s9"
    ACT0048.visible = True
    ACT0048.recursive = False
    CON0049.game_object = "NLO:CharacterController"
    CON0049.property_name = "Speed"
    CON0049.compare_value = 0.44999998807907104
    CON0049.operator = 4
    CON0050.condition = CON0049
    ACT0051.condition = CON0050
    ACT0051.game_object = "NLO:s9"
    ACT0051.visible = False
    ACT0051.recursive = False
    ACT0052.condition = CON0053
    ACT0052.game_object = "NLO:s10"
    ACT0052.visible = True
    ACT0052.recursive = False
    CON0053.game_object = "NLO:CharacterController"
    CON0053.property_name = "Speed"
    CON0053.compare_value = 0.5
    CON0053.operator = 4
    CON0054.condition = CON0053
    ACT0055.condition = CON0054
    ACT0055.game_object = "NLO:s10"
    ACT0055.visible = False
    ACT0055.recursive = False
    CON0056.game_object = "NLO:CharacterController"
    CON0056.property_name = "Speed"
    CON0056.compare_value = 0.4000000059604645
    CON0056.operator = 4
    ACT0057.condition = CON0063
    ACT0057.game_object = "NLO:s11"
    ACT0057.visible = True
    ACT0057.recursive = False
    CON0058.condition = CON0063
    ACT0059.condition = CON0060
    ACT0059.game_object = "NLO:s12"
    ACT0059.visible = True
    ACT0059.recursive = False
    CON0060.game_object = "NLO:CharacterController"
    CON0060.property_name = "Speed"
    CON0060.compare_value = 0.6000000238418579
    CON0060.operator = 4
    CON0061.condition = CON0060
    ACT0062.condition = CON0061
    ACT0062.game_object = "NLO:s12"
    ACT0062.visible = False
    ACT0062.recursive = False
    CON0063.game_object = "NLO:CharacterController"
    CON0063.property_name = "Speed"
    CON0063.compare_value = 0.550000011920929
    CON0063.operator = 4
    ACT0064.condition = CON0071
    ACT0064.game_object = "NLO:s13"
    ACT0064.visible = True
    ACT0064.recursive = False
    CON0065.condition = CON0071
    ACT0066.condition = CON0065
    ACT0066.game_object = "NLO:s13"
    ACT0066.visible = False
    ACT0066.recursive = False
    ACT0067.condition = CON0068
    ACT0067.game_object = "NLO:s14"
    ACT0067.visible = True
    ACT0067.recursive = False
    CON0068.game_object = "NLO:CharacterController"
    CON0068.property_name = "Speed"
    CON0068.compare_value = 0.699999988079071
    CON0068.operator = 4
    CON0069.condition = CON0068
    ACT0070.condition = CON0069
    ACT0070.game_object = "NLO:s14"
    ACT0070.visible = False
    ACT0070.recursive = False
    CON0071.game_object = "NLO:CharacterController"
    CON0071.property_name = "Speed"
    CON0071.compare_value = 0.6499999761581421
    CON0071.operator = 4
    ACT0072.condition = CON0073
    ACT0072.game_object = "NLO:s15"
    ACT0072.visible = True
    ACT0072.recursive = False
    CON0073.game_object = "NLO:CharacterController"
    CON0073.property_name = "Speed"
    CON0073.compare_value = 0.75
    CON0073.operator = 4
    CON0074.condition = CON0073
    ACT0075.condition = CON0074
    ACT0075.game_object = "NLO:s15"
    ACT0075.visible = False
    ACT0075.recursive = False
    ACT0076.condition = CON0096
    ACT0076.game_object = "NLO:s16"
    ACT0076.visible = True
    ACT0076.recursive = False
    CON0077.condition = CON0096
    ACT0078.condition = CON0077
    ACT0078.game_object = "NLO:s16"
    ACT0078.visible = False
    ACT0078.recursive = False
    ACT0079.condition = CON0080
    ACT0079.game_object = "NLO:s17"
    ACT0079.visible = True
    ACT0079.recursive = False
    CON0080.game_object = "NLO:CharacterController"
    CON0080.property_name = "Speed"
    CON0080.compare_value = 0.8500000238418579
    CON0080.operator = 4
    CON0081.condition = CON0080
    ACT0082.condition = CON0081
    ACT0082.game_object = "NLO:s17"
    ACT0082.visible = False
    ACT0082.recursive = False
    ACT0083.condition = CON0094
    ACT0083.game_object = "NLO:s18"
    ACT0083.visible = True
    ACT0083.recursive = False
    CON0084.condition = CON0094
    ACT0085.condition = CON0084
    ACT0085.game_object = "NLO:s18"
    ACT0085.visible = False
    ACT0085.recursive = False
    ACT0086.condition = CON0087
    ACT0086.game_object = "NLO:s19"
    ACT0086.visible = True
    ACT0086.recursive = False
    CON0087.game_object = "NLO:CharacterController"
    CON0087.property_name = "Speed"
    CON0087.compare_value = 0.949999988079071
    CON0087.operator = 4
    CON0088.condition = CON0087
    ACT0089.condition = CON0088
    ACT0089.game_object = "NLO:s19"
    ACT0089.visible = False
    ACT0089.recursive = False
    ACT0090.condition = CON0091
    ACT0090.game_object = "NLO:s20"
    ACT0090.visible = True
    ACT0090.recursive = False
    CON0091.game_object = "NLO:CharacterController"
    CON0091.property_name = "Speed"
    CON0091.compare_value = 1.0
    CON0091.operator = 4
    CON0092.condition = CON0091
    ACT0093.condition = CON0092
    ACT0093.game_object = "NLO:s20"
    ACT0093.visible = False
    ACT0093.recursive = False
    CON0094.game_object = "NLO:CharacterController"
    CON0094.property_name = "Speed"
    CON0094.compare_value = 0.8999999761581421
    CON0094.operator = 4
    ACT0095.condition = CON0058
    ACT0095.game_object = "NLO:s11"
    ACT0095.visible = False
    ACT0095.recursive = False
    CON0096.game_object = "NLO:CharacterController"
    CON0096.property_name = "Speed"
    CON0096.compare_value = 0.800000011920929
    CON0096.operator = 4
    network.add_cell(CON0002)
    network.add_cell(ACT0005)
    network.add_cell(CON0007)
    network.add_cell(CON0009)
    network.add_cell(CON0012)
    network.add_cell(CON0014)
    network.add_cell(CON0021)
    network.add_cell(CON0024)
    network.add_cell(CON0029)
    network.add_cell(CON0032)
    network.add_cell(CON0034)
    network.add_cell(CON0041)
    network.add_cell(CON0044)
    network.add_cell(CON0049)
    network.add_cell(CON0053)
    network.add_cell(CON0056)
    network.add_cell(CON0060)
    network.add_cell(CON0063)
    network.add_cell(CON0068)
    network.add_cell(CON0071)
    network.add_cell(CON0073)
    network.add_cell(CON0080)
    network.add_cell(CON0087)
    network.add_cell(CON0091)
    network.add_cell(CON0094)
    network.add_cell(CON0096)
    network.add_cell(CON0008)
    network.add_cell(CON0013)
    network.add_cell(ACT0017)
    network.add_cell(ACT0020)
    network.add_cell(ACT0025)
    network.add_cell(ACT0028)
    network.add_cell(ACT0033)
    network.add_cell(ACT0037)
    network.add_cell(ACT0040)
    network.add_cell(ACT0045)
    network.add_cell(ACT0048)
    network.add_cell(ACT0052)
    network.add_cell(ACT0057)
    network.add_cell(ACT0059)
    network.add_cell(ACT0064)
    network.add_cell(ACT0067)
    network.add_cell(ACT0072)
    network.add_cell(ACT0076)
    network.add_cell(ACT0079)
    network.add_cell(ACT0083)
    network.add_cell(ACT0086)
    network.add_cell(ACT0090)
    network.add_cell(CON0097)
    network.add_cell(CON0004)
    network.add_cell(CON0010)
    network.add_cell(ACT0015)
    network.add_cell(CON0018)
    network.add_cell(CON0022)
    network.add_cell(CON0026)
    network.add_cell(CON0030)
    network.add_cell(CON0035)
    network.add_cell(CON0038)
    network.add_cell(CON0042)
    network.add_cell(CON0046)
    network.add_cell(CON0050)
    network.add_cell(CON0054)
    network.add_cell(CON0058)
    network.add_cell(CON0065)
    network.add_cell(CON0069)
    network.add_cell(CON0074)
    network.add_cell(CON0077)
    network.add_cell(CON0081)
    network.add_cell(CON0084)
    network.add_cell(CON0088)
    network.add_cell(CON0092)
    network.add_cell(ACT0095)
    network.add_cell(ACT0003)
    network.add_cell(CON0011)
    network.add_cell(ACT0019)
    network.add_cell(ACT0027)
    network.add_cell(ACT0036)
    network.add_cell(ACT0043)
    network.add_cell(ACT0051)
    network.add_cell(CON0061)
    network.add_cell(ACT0066)
    network.add_cell(ACT0075)
    network.add_cell(ACT0082)
    network.add_cell(ACT0089)
    network.add_cell(ACT0001)
    network.add_cell(PAR0016)
    network.add_cell(ACT0031)
    network.add_cell(ACT0047)
    network.add_cell(ACT0062)
    network.add_cell(ACT0078)
    network.add_cell(ACT0093)
    network.add_cell(CON0006)
    network.add_cell(ACT0039)
    network.add_cell(ACT0070)
    network.add_cell(ACT0000)
    network.add_cell(ACT0055)
    network.add_cell(ACT0023)
    network.add_cell(ACT0085)
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
