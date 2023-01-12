# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionApplyRotation()
    CON0001 = nodes.ConditionOnUpdate()
    CON0002 = nodes.ObjectPropertyOperator()
    CON0003 = nodes.ConditionAndList()
    CON0004 = nodes.ObjectPropertyOperator()
    CON0005 = nodes.ObjectPropertyOperator()
    ACT0006 = nodes.ActionSetGameObjectGameProperty()
    ACT0007 = nodes.ActionSetGameObjectGameProperty()
    ACT0008 = nodes.ActionSetGameObjectGameProperty()
    ACT0009 = nodes.ActionSetGameObjectGameProperty()
    ACT0010 = nodes.ActionSetGameObjectGameProperty()
    ACT0011 = nodes.ActionSetGameObjectGameProperty()
    ACT0012 = nodes.ActionPlayAction()
    ACT0013 = nodes.ActionSetGameObjectGameProperty()
    ACT0014 = nodes.ActionSetGameObjectGameProperty()
    ACT0015 = nodes.ActionPlayAction()
    CON0016 = nodes.ConditionAnd()
    CON0017 = nodes.ObjectPropertyOperator()
    CON0018 = nodes.ObjectPropertyOperator()
    ACT0019 = nodes.ActionPlayAction()
    ACT0020 = nodes.ActionSetGameObjectGameProperty()
    ACT0021 = nodes.ActionSetGameObjectGameProperty()
    CON0022 = nodes.ConditionAndList()
    CON0023 = nodes.ObjectPropertyOperator()
    CON0024 = nodes.ObjectPropertyOperator()
    CON0025 = nodes.ObjectPropertyOperator()
    CON0026 = nodes.ObjectPropertyOperator()
    ACT0027 = nodes.ActionPlayAction()
    CON0028 = nodes.ObjectPropertyOperator()
    CON0029 = nodes.ConditionNot()
    CON0030 = nodes.ObjectPropertyOperator()
    CON0031 = nodes.ConditionAndList()
    ACT0032 = nodes.ActionPlayAction()
    CON0033 = nodes.ObjectPropertyOperator()
    CON0034 = nodes.ObjectPropertyOperator()
    CON0035 = nodes.ObjectPropertyOperator()
    CON0036 = nodes.ObjectPropertyOperator()
    CON0037 = nodes.ObjectPropertyOperator()
    CON0038 = nodes.ConditionAndList()
    ACT0039 = nodes.ActionPlayAction()
    CON0040 = nodes.ConditionAnd()
    CON0041 = nodes.ObjectPropertyOperator()
    CON0042 = nodes.ObjectPropertyOperator()
    CON0043 = nodes.ObjectPropertyOperator()
    CON0044 = nodes.ObjectPropertyOperator()
    CON0045 = nodes.ConditionAndList()
    ACT0046 = nodes.ActionPlayAction()
    CON0047 = nodes.ConditionAnd()
    CON0048 = nodes.ObjectPropertyOperator()
    ACT0049 = nodes.ActionPlayAction()
    CON0050 = nodes.ConditionAndList()
    CON0051 = nodes.ObjectPropertyOperator()
    CON0052 = nodes.ConditionAnd()
    ACT0053 = nodes.ActionPlayAction()
    CON0054 = nodes.ObjectPropertyOperator()
    CON0055 = nodes.ObjectPropertyOperator()
    CON0056 = nodes.ObjectPropertyOperator()
    CON0057 = nodes.ObjectPropertyOperator()
    CON0058 = nodes.ConditionAnd()
    CON0059 = nodes.ObjectPropertyOperator()
    ACT0060 = nodes.ActionPlayAction()
    CON0061 = nodes.ConditionAndList()
    CON0062 = nodes.ConditionNot()
    CON0063 = nodes.ObjectPropertyOperator()
    CON0064 = nodes.ConditionAnd()
    ACT0065 = nodes.ActionPlayAction()
    CON0066 = nodes.ObjectPropertyOperator()
    CON0067 = nodes.ObjectPropertyOperator()
    CON0068 = nodes.ObjectPropertyOperator()
    CON0069 = nodes.ObjectPropertyOperator()
    CON0070 = nodes.ConditionOr()
    CON0071 = nodes.ObjectPropertyOperator()
    CON0072 = nodes.ConditionAndList()
    CON0073 = nodes.ConditionAndList()
    CON0074 = nodes.ObjectPropertyOperator()
    CON0075 = nodes.ObjectPropertyOperator()
    CON0076 = nodes.ObjectPropertyOperator()
    ACT0077 = nodes.ActionSetGameObjectGameProperty()
    ACT0078 = nodes.ActionSetGameObjectGameProperty()
    ACT0000.local = True
    ACT0000.condition = CON0001
    ACT0000.game_object = "NLO:SonicBall"
    ACT0000.rotation = mathutils.Vector((0.5235987901687622, 0.0, 0.0))
    CON0002.game_object = "NLO:CharacterController"
    CON0002.property_name = "isBoosting"
    CON0002.compare_value = True
    CON0002.operator = 0
    CON0003.ca = CON0005
    CON0003.cb = CON0004
    CON0003.cc = CON0062
    CON0003.cd = True
    CON0003.ce = True
    CON0003.cf = True
    CON0004.game_object = "NLO:CharacterController"
    CON0004.property_name = "isBoosting"
    CON0004.compare_value = False
    CON0004.operator = 0
    CON0005.game_object = "NLO:CharacterController"
    CON0005.property_name = "isStomping"
    CON0005.compare_value = True
    CON0005.operator = 0
    ACT0006.condition = ACT0065.RUNNING
    ACT0006.game_object = "NLO:CharacterController"
    ACT0006.property_name = "animation"
    ACT0006.property_value = "idle"
    ACT0007.condition = ACT0032.RUNNING
    ACT0007.game_object = "NLO:CharacterController"
    ACT0007.property_name = "animation"
    ACT0007.property_value = "idle"
    ACT0008.condition = ACT0046.RUNNING
    ACT0008.game_object = "NLO:CharacterController"
    ACT0008.property_name = "animation"
    ACT0008.property_value = "jog"
    ACT0009.condition = ACT0039.RUNNING
    ACT0009.game_object = "NLO:CharacterController"
    ACT0009.property_name = "animation"
    ACT0009.property_value = "walk"
    ACT0010.condition = None
    ACT0010.game_object = "NLO:CharacterController"
    ACT0010.property_name = "animation"
    ACT0010.property_value = "walk"
    ACT0011.condition = ACT0060.RUNNING
    ACT0011.game_object = "NLO:CharacterController"
    ACT0011.property_name = "animation"
    ACT0011.property_value = "jet"
    ACT0012.condition = CON0050
    ACT0012.game_object = "NLO:chr_Sonic_HD"
    ACT0012.action_name = "Boost"
    ACT0012.start_frame = 1.0
    ACT0012.end_frame = 34.0
    ACT0012.layer = 1
    ACT0012.priority = 2
    ACT0012.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0012.stop = True
    ACT0012.layer_weight = 1.0
    ACT0012.speed = 4.0
    ACT0012.blendin = 4.0
    ACT0012.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0013.condition = ACT0012.RUNNING
    ACT0013.game_object = "NLO:CharacterController"
    ACT0013.property_name = "animation"
    ACT0013.property_value = "boost"
    ACT0014.condition = ACT0049.RUNNING
    ACT0014.game_object = "NLO:CharacterController"
    ACT0014.property_name = "animation"
    ACT0014.property_value = "null"
    ACT0015.condition = CON0003
    ACT0015.game_object = "NLO:chr_Sonic_HD"
    ACT0015.action_name = "Stomp"
    ACT0015.start_frame = 1.0
    ACT0015.end_frame = 6.0
    ACT0015.layer = 0
    ACT0015.priority = 39
    ACT0015.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0015.stop = False
    ACT0015.layer_weight = 1.0
    ACT0015.speed = 1.0
    ACT0015.blendin = 2.0
    ACT0015.blend_mode = bge.logic.KX_ACTION_BLEND_ADD
    CON0016.condition_a = CON0048
    CON0016.condition_b = CON0002
    CON0017.game_object = "NLO:CharacterController"
    CON0017.property_name = "isStomping"
    CON0017.compare_value = False
    CON0017.operator = 0
    CON0018.game_object = "NLO:CharacterController"
    CON0018.property_name = "isBoosting"
    CON0018.compare_value = False
    CON0018.operator = 0
    ACT0019.condition = CON0031
    ACT0019.game_object = "NLO:chr_Sonic_HD"
    ACT0019.action_name = "JumpArc"
    ACT0019.start_frame = 1.0
    ACT0019.end_frame = 6.0
    ACT0019.layer = 0
    ACT0019.priority = 40
    ACT0019.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0019.stop = False
    ACT0019.layer_weight = 1.0
    ACT0019.speed = 1.0
    ACT0019.blendin = 7.0
    ACT0019.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0020.condition = ACT0019.RUNNING
    ACT0020.game_object = "NLO:CharacterController"
    ACT0020.property_name = "animation"
    ACT0020.property_value = "null"
    ACT0021.condition = ACT0027.RUNNING
    ACT0021.game_object = "NLO:CharacterController"
    ACT0021.property_name = "animation"
    ACT0021.property_value = "null"
    CON0022.ca = CON0030
    CON0022.cb = CON0024
    CON0022.cc = CON0023
    CON0022.cd = CON0025
    CON0022.ce = True
    CON0022.cf = True
    CON0023.game_object = "NLO:CharacterController"
    CON0023.property_name = "isBoosting"
    CON0023.compare_value = False
    CON0023.operator = 0
    CON0024.game_object = "NLO:CharacterController"
    CON0024.property_name = "isFalling"
    CON0024.compare_value = False
    CON0024.operator = 0
    CON0025.game_object = "NLO:CharacterController"
    CON0025.property_name = "isStomping"
    CON0025.compare_value = False
    CON0025.operator = 0
    CON0026.game_object = "NLO:CharacterController"
    CON0026.property_name = "isFalling"
    CON0026.compare_value = True
    CON0026.operator = 0
    ACT0027.condition = CON0022
    ACT0027.game_object = "NLO:chr_Sonic_HD"
    ACT0027.action_name = "SpringJump"
    ACT0027.start_frame = 1.0
    ACT0027.end_frame = 9.25
    ACT0027.layer = 0
    ACT0027.priority = 13
    ACT0027.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0027.stop = False
    ACT0027.layer_weight = 1.0
    ACT0027.speed = 1.0
    ACT0027.blendin = 7.0
    ACT0027.blend_mode = bge.logic.KX_ACTION_BLEND_ADD
    CON0028.game_object = "NLO:CharacterController"
    CON0028.property_name = "isSpringing"
    CON0028.compare_value = False
    CON0028.operator = 0
    CON0029.condition = CON0055
    CON0030.game_object = "NLO:CharacterController"
    CON0030.property_name = "isSpringing"
    CON0030.compare_value = True
    CON0030.operator = 0
    CON0031.ca = CON0026
    CON0031.cb = CON0018
    CON0031.cc = CON0017
    CON0031.cd = CON0028
    CON0031.ce = CON0062
    CON0031.cf = True
    ACT0032.condition = CON0052
    ACT0032.game_object = "NLO:chr_Sonic_HD"
    ACT0032.action_name = "Idle00"
    ACT0032.start_frame = 1.0
    ACT0032.end_frame = 155.1600341796875
    ACT0032.layer = 0
    ACT0032.priority = 70
    ACT0032.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0032.stop = False
    ACT0032.layer_weight = 1.0
    ACT0032.speed = 1.0
    ACT0032.blendin = 4.0
    ACT0032.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0033.game_object = "NLO:CharacterController"
    CON0033.property_name = "idle"
    CON0033.compare_value = 10.0
    CON0033.operator = 4
    CON0034.game_object = "NLO:CharacterController"
    CON0034.property_name = "Speed"
    CON0034.compare_value = 0.30000001192092896
    CON0034.operator = 5
    CON0035.game_object = "NLO:CharacterController"
    CON0035.property_name = "Speed"
    CON0035.compare_value = 0.029999999329447746
    CON0035.operator = 2
    CON0036.game_object = "NLO:CharacterController"
    CON0036.property_name = "isFalling"
    CON0036.compare_value = False
    CON0036.operator = 0
    CON0037.game_object = "NLO:CharacterController"
    CON0037.property_name = "isStomping"
    CON0037.compare_value = False
    CON0037.operator = 0
    CON0038.ca = CON0034
    CON0038.cb = CON0035
    CON0038.cc = CON0036
    CON0038.cd = CON0037
    CON0038.ce = CON0029
    CON0038.cf = CON0062
    ACT0039.condition = CON0040
    ACT0039.game_object = "NLO:U_O"
    ACT0039.action_name = "Walk"
    ACT0039.start_frame = 1.0
    ACT0039.end_frame = 34.0
    ACT0039.layer = 0
    ACT0039.priority = 10
    ACT0039.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0039.stop = False
    ACT0039.layer_weight = 1.0
    ACT0039.speed = 2.0
    ACT0039.blendin = 4.0
    ACT0039.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0040.condition_a = CON0038
    CON0040.condition_b = CON0076
    CON0041.game_object = "NLO:CharacterController"
    CON0041.property_name = "Speed"
    CON0041.compare_value = 0.30000001192092896
    CON0041.operator = 2
    CON0042.game_object = "NLO:CharacterController"
    CON0042.property_name = "Speed"
    CON0042.compare_value = 0.699999988079071
    CON0042.operator = 5
    CON0043.game_object = "NLO:CharacterController"
    CON0043.property_name = "isStomping"
    CON0043.compare_value = False
    CON0043.operator = 0
    CON0044.game_object = "NLO:CharacterController"
    CON0044.property_name = "isFalling"
    CON0044.compare_value = False
    CON0044.operator = 0
    CON0045.ca = CON0042
    CON0045.cb = CON0041
    CON0045.cc = CON0044
    CON0045.cd = CON0043
    CON0045.ce = CON0029
    CON0045.cf = CON0028
    ACT0046.condition = CON0047
    ACT0046.game_object = "NLO:U_O"
    ACT0046.action_name = "Jog"
    ACT0046.start_frame = 1.0
    ACT0046.end_frame = 34.0
    ACT0046.layer = 0
    ACT0046.priority = 8
    ACT0046.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0046.stop = False
    ACT0046.layer_weight = 1.0
    ACT0046.speed = 3.0
    ACT0046.blendin = 2.0
    ACT0046.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0047.condition_a = CON0045
    CON0047.condition_b = CON0076
    CON0048.game_object = "NLO:CharacterController"
    CON0048.property_name = "isFalling"
    CON0048.compare_value = True
    CON0048.operator = 0
    ACT0049.condition = CON0016
    ACT0049.game_object = "NLO:chr_Sonic_HD"
    ACT0049.action_name = "AirBoost"
    ACT0049.start_frame = 1.0
    ACT0049.end_frame = 9.0
    ACT0049.layer = 0
    ACT0049.priority = 40
    ACT0049.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0049.stop = True
    ACT0049.layer_weight = 1.0
    ACT0049.speed = 1.0
    ACT0049.blendin = 7.0
    ACT0049.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0050.ca = CON0055
    CON0050.cb = CON0051
    CON0050.cc = CON0054
    CON0050.cd = True
    CON0050.ce = True
    CON0050.cf = True
    CON0051.game_object = "NLO:CharacterController"
    CON0051.property_name = "isFalling"
    CON0051.compare_value = False
    CON0051.operator = 0
    CON0052.condition_a = CON0033
    CON0052.condition_b = CON0076
    ACT0053.condition = CON0058
    ACT0053.game_object = "NLO:chr_Sonic_HD"
    ACT0053.action_name = "Sliding"
    ACT0053.start_frame = 1.0
    ACT0053.end_frame = 6.050000190734863
    ACT0053.layer = 0
    ACT0053.priority = 69
    ACT0053.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0053.stop = False
    ACT0053.layer_weight = 1.0
    ACT0053.speed = 0.5
    ACT0053.blendin = 5.0
    ACT0053.blend_mode = bge.logic.KX_ACTION_BLEND_ADD
    CON0054.game_object = "NLO:CharacterController"
    CON0054.property_name = "isSliding"
    CON0054.compare_value = False
    CON0054.operator = 0
    CON0055.game_object = "NLO:CharacterController"
    CON0055.property_name = "isBoosting"
    CON0055.compare_value = True
    CON0055.operator = 0
    CON0056.game_object = "NLO:CharacterController"
    CON0056.property_name = "isSliding"
    CON0056.compare_value = True
    CON0056.operator = 0
    CON0057.game_object = "NLO:CharacterController"
    CON0057.property_name = "isBoosting"
    CON0057.compare_value = False
    CON0057.operator = 0
    CON0058.condition_a = CON0056
    CON0058.condition_b = CON0057
    CON0059.game_object = "NLO:CharacterController"
    CON0059.property_name = "isFalling"
    CON0059.compare_value = False
    CON0059.operator = 0
    ACT0060.condition = CON0073
    ACT0060.game_object = "NLO:U_O"
    ACT0060.action_name = "Jet"
    ACT0060.start_frame = 1.0
    ACT0060.end_frame = 34.0
    ACT0060.layer = 0
    ACT0060.priority = 4
    ACT0060.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0060.stop = False
    ACT0060.layer_weight = 1.0
    ACT0060.speed = 4.0
    ACT0060.blendin = 2.0
    ACT0060.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0061.ca = True
    CON0061.cb = CON0063
    CON0061.cc = CON0059
    CON0061.cd = CON0075
    CON0061.ce = CON0029
    CON0061.cf = CON0062
    CON0062.condition = CON0030
    CON0063.game_object = "NLO:CharacterController"
    CON0063.property_name = "Speed"
    CON0063.compare_value = 0.699999988079071
    CON0063.operator = 2
    CON0064.condition_a = CON0070
    CON0064.condition_b = CON0076
    ACT0065.condition = CON0064
    ACT0065.game_object = "NLO:U_O"
    ACT0065.action_name = "Idle"
    ACT0065.start_frame = 1.0
    ACT0065.end_frame = 68.0
    ACT0065.layer = 0
    ACT0065.priority = 90
    ACT0065.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0065.stop = False
    ACT0065.layer_weight = 1.0
    ACT0065.speed = 1.0
    ACT0065.blendin = 4.0
    ACT0065.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0066.game_object = "NLO:CharacterController"
    CON0066.property_name = "idle"
    CON0066.compare_value = 16.0
    CON0066.operator = 2
    CON0067.game_object = "NLO:CharacterController"
    CON0067.property_name = "idle"
    CON0067.compare_value = 10.0
    CON0067.operator = 5
    CON0068.game_object = "NLO:CharacterController"
    CON0068.property_name = "isFalling"
    CON0068.compare_value = False
    CON0068.operator = 5
    CON0069.game_object = "NLO:CharacterController"
    CON0069.property_name = "isJumping"
    CON0069.compare_value = False
    CON0069.operator = 5
    CON0070.condition_a = CON0072
    CON0070.condition_b = CON0066
    CON0071.game_object = "NLO:CharacterController"
    CON0071.property_name = "Speed"
    CON0071.compare_value = 0.029999999329447746
    CON0071.operator = 5
    CON0072.ca = CON0071
    CON0072.cb = CON0067
    CON0072.cc = CON0029
    CON0072.cd = CON0069
    CON0072.ce = CON0068
    CON0072.cf = CON0062
    CON0073.ca = CON0061
    CON0073.cb = CON0062
    CON0073.cc = CON0074
    CON0073.cd = CON0076
    CON0073.ce = True
    CON0073.cf = True
    CON0074.game_object = "NLO:CharacterController"
    CON0074.property_name = "isBoosting"
    CON0074.compare_value = False
    CON0074.operator = 0
    CON0075.game_object = "NLO:CharacterController"
    CON0075.property_name = "isStomping"
    CON0075.compare_value = False
    CON0075.operator = 0
    CON0076.game_object = "NLO:CharacterController"
    CON0076.property_name = "isSliding"
    CON0076.compare_value = False
    CON0076.operator = 0
    ACT0077.condition = ACT0015.RUNNING
    ACT0077.game_object = "NLO:CharacterController"
    ACT0077.property_name = "animation"
    ACT0077.property_value = "null"
    ACT0078.condition = ACT0053.RUNNING
    ACT0078.game_object = "NLO:CharacterController"
    ACT0078.property_name = "animation"
    ACT0078.property_value = "sliding"
    network.add_cell(CON0001)
    network.add_cell(CON0004)
    network.add_cell(ACT0010)
    network.add_cell(CON0017)
    network.add_cell(CON0023)
    network.add_cell(CON0025)
    network.add_cell(CON0028)
    network.add_cell(CON0030)
    network.add_cell(CON0033)
    network.add_cell(CON0035)
    network.add_cell(CON0037)
    network.add_cell(CON0041)
    network.add_cell(CON0043)
    network.add_cell(CON0048)
    network.add_cell(CON0051)
    network.add_cell(CON0054)
    network.add_cell(CON0056)
    network.add_cell(CON0059)
    network.add_cell(CON0062)
    network.add_cell(CON0066)
    network.add_cell(CON0068)
    network.add_cell(CON0071)
    network.add_cell(CON0074)
    network.add_cell(CON0076)
    network.add_cell(ACT0000)
    network.add_cell(CON0005)
    network.add_cell(CON0018)
    network.add_cell(CON0024)
    network.add_cell(CON0034)
    network.add_cell(CON0042)
    network.add_cell(CON0052)
    network.add_cell(CON0055)
    network.add_cell(CON0063)
    network.add_cell(CON0067)
    network.add_cell(CON0075)
    network.add_cell(CON0002)
    network.add_cell(CON0016)
    network.add_cell(CON0022)
    network.add_cell(ACT0027)
    network.add_cell(ACT0032)
    network.add_cell(CON0044)
    network.add_cell(ACT0049)
    network.add_cell(CON0057)
    network.add_cell(CON0069)
    network.add_cell(CON0003)
    network.add_cell(ACT0007)
    network.add_cell(ACT0014)
    network.add_cell(ACT0021)
    network.add_cell(CON0029)
    network.add_cell(CON0036)
    network.add_cell(CON0045)
    network.add_cell(CON0047)
    network.add_cell(CON0058)
    network.add_cell(CON0061)
    network.add_cell(CON0072)
    network.add_cell(ACT0015)
    network.add_cell(CON0026)
    network.add_cell(CON0038)
    network.add_cell(CON0040)
    network.add_cell(CON0050)
    network.add_cell(CON0070)
    network.add_cell(ACT0077)
    network.add_cell(ACT0012)
    network.add_cell(CON0031)
    network.add_cell(ACT0046)
    network.add_cell(CON0064)
    network.add_cell(CON0073)
    network.add_cell(ACT0008)
    network.add_cell(ACT0013)
    network.add_cell(ACT0039)
    network.add_cell(ACT0060)
    network.add_cell(ACT0009)
    network.add_cell(ACT0019)
    network.add_cell(ACT0053)
    network.add_cell(ACT0078)
    network.add_cell(ACT0011)
    network.add_cell(ACT0065)
    network.add_cell(ACT0006)
    network.add_cell(ACT0020)
    owner["IGNLTree_playerAnim"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__playerAnim')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_playerAnim")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
