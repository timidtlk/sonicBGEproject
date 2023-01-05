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
    CON0003 = nodes.ObjectPropertyOperator()
    CON0004 = nodes.ObjectPropertyOperator()
    CON0005 = nodes.ConditionAndList()
    CON0006 = nodes.ObjectPropertyOperator()
    CON0007 = nodes.ObjectPropertyOperator()
    CON0008 = nodes.ObjectPropertyOperator()
    CON0009 = nodes.ConditionAndList()
    CON0010 = nodes.ObjectPropertyOperator()
    CON0011 = nodes.ObjectPropertyOperator()
    CON0012 = nodes.ConditionNot()
    CON0013 = nodes.ConditionAnd()
    CON0014 = nodes.ObjectPropertyOperator()
    CON0015 = nodes.ObjectPropertyOperator()
    CON0016 = nodes.ObjectPropertyOperator()
    ACT0017 = nodes.ActionPlayAction()
    CON0018 = nodes.ConditionAnd()
    CON0019 = nodes.ObjectPropertyOperator()
    CON0020 = nodes.ObjectPropertyOperator()
    CON0021 = nodes.ConditionAndList()
    CON0022 = nodes.ObjectPropertyOperator()
    CON0023 = nodes.ObjectPropertyOperator()
    CON0024 = nodes.ConditionAndList()
    CON0025 = nodes.ObjectPropertyOperator()
    CON0026 = nodes.ObjectPropertyOperator()
    CON0027 = nodes.ObjectPropertyOperator()
    CON0028 = nodes.ObjectPropertyOperator()
    CON0029 = nodes.ConditionAndList()
    CON0030 = nodes.ObjectPropertyOperator()
    CON0031 = nodes.ConditionOr()
    CON0032 = nodes.ObjectPropertyOperator()
    CON0033 = nodes.ObjectPropertyOperator()
    CON0034 = nodes.ObjectPropertyOperator()
    ACT0035 = nodes.ActionPlayAction()
    ACT0036 = nodes.ActionSetGameObjectGameProperty()
    ACT0037 = nodes.ActionPlayAction()
    ACT0038 = nodes.ActionSetGameObjectGameProperty()
    ACT0039 = nodes.ActionPlayAction()
    ACT0040 = nodes.ActionSetGameObjectGameProperty()
    CON0041 = nodes.ObjectPropertyOperator()
    CON0042 = nodes.ObjectPropertyOperator()
    CON0043 = nodes.ObjectPropertyOperator()
    ACT0044 = nodes.ActionPlayAction()
    CON0045 = nodes.ObjectPropertyOperator()
    CON0046 = nodes.ConditionAndList()
    ACT0047 = nodes.ActionSetGameObjectGameProperty()
    ACT0048 = nodes.ActionSetGameObjectGameProperty()
    ACT0049 = nodes.ActionPlayAction()
    ACT0050 = nodes.ActionSetGameObjectGameProperty()
    ACT0051 = nodes.ActionPlayAction()
    ACT0052 = nodes.ActionSetGameObjectGameProperty()
    ACT0053 = nodes.ActionSetGameObjectGameProperty()
    ACT0054 = nodes.ActionPlayAction()
    ACT0055 = nodes.ActionSetGameObjectGameProperty()
    ACT0056 = nodes.ActionSetGameObjectGameProperty()
    ACT0057 = nodes.ActionSetGameObjectGameProperty()
    ACT0058 = nodes.ActionPlayAction()
    ACT0000.local = True
    ACT0000.condition = CON0001
    ACT0000.game_object = "NLO:SonicBall"
    ACT0000.rotation = mathutils.Vector((0.5235987901687622, 0.0, 0.0))
    CON0002.game_object = "NLO:CharacterController"
    CON0002.property_name = "Speed"
    CON0002.compare_value = 0.30000001192092896
    CON0002.operator = 2
    CON0003.game_object = "NLO:CharacterController"
    CON0003.property_name = "Speed"
    CON0003.compare_value = 0.699999988079071
    CON0003.operator = 5
    CON0004.game_object = "NLO:CharacterController"
    CON0004.property_name = "isFalling"
    CON0004.compare_value = False
    CON0004.operator = 0
    CON0005.ca = CON0003
    CON0005.cb = CON0002
    CON0005.cc = CON0004
    CON0005.cd = CON0010
    CON0005.ce = CON0012
    CON0005.cf = True
    CON0006.game_object = "NLO:CharacterController"
    CON0006.property_name = "Speed"
    CON0006.compare_value = 0.699999988079071
    CON0006.operator = 2
    CON0007.game_object = "NLO:CharacterController"
    CON0007.property_name = "isFalling"
    CON0007.compare_value = False
    CON0007.operator = 0
    CON0008.game_object = "NLO:CharacterController"
    CON0008.property_name = "isStomping"
    CON0008.compare_value = False
    CON0008.operator = 0
    CON0009.ca = True
    CON0009.cb = CON0006
    CON0009.cc = CON0007
    CON0009.cd = CON0008
    CON0009.ce = CON0012
    CON0009.cf = True
    CON0010.game_object = "NLO:CharacterController"
    CON0010.property_name = "isStomping"
    CON0010.compare_value = False
    CON0010.operator = 0
    CON0011.game_object = "NLO:CharacterController"
    CON0011.property_name = "idle"
    CON0011.compare_value = 10.0
    CON0011.operator = 4
    CON0012.condition = CON0014
    CON0013.condition_a = CON0014
    CON0013.condition_b = CON0015
    CON0014.game_object = "NLO:CharacterController"
    CON0014.property_name = "isBoosting"
    CON0014.compare_value = True
    CON0014.operator = 0
    CON0015.game_object = "NLO:CharacterController"
    CON0015.property_name = "isFalling"
    CON0015.compare_value = False
    CON0015.operator = 0
    CON0016.game_object = "NLO:CharacterController"
    CON0016.property_name = "isFalling"
    CON0016.compare_value = True
    CON0016.operator = 0
    ACT0017.condition = CON0018
    ACT0017.game_object = "NLO:chr_Sonic_HD"
    ACT0017.action_name = "AirBoost"
    ACT0017.start_frame = 1.0
    ACT0017.end_frame = 9.0
    ACT0017.layer = 0
    ACT0017.priority = 40
    ACT0017.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0017.stop = True
    ACT0017.layer_weight = 1.0
    ACT0017.speed = 1.0
    ACT0017.blendin = 7.0
    ACT0017.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0018.condition_a = CON0019
    CON0018.condition_b = CON0020
    CON0019.game_object = "NLO:CharacterController"
    CON0019.property_name = "isFalling"
    CON0019.compare_value = True
    CON0019.operator = 0
    CON0020.game_object = "NLO:CharacterController"
    CON0020.property_name = "isBoosting"
    CON0020.compare_value = True
    CON0020.operator = 0
    CON0021.ca = CON0025
    CON0021.cb = CON0022
    CON0021.cc = True
    CON0021.cd = True
    CON0021.ce = True
    CON0021.cf = True
    CON0022.game_object = "NLO:CharacterController"
    CON0022.property_name = "isBoosting"
    CON0022.compare_value = False
    CON0022.operator = 0
    CON0023.game_object = "NLO:CharacterController"
    CON0023.property_name = "isBoosting"
    CON0023.compare_value = False
    CON0023.operator = 0
    CON0024.ca = CON0016
    CON0024.cb = CON0023
    CON0024.cc = CON0026
    CON0024.cd = True
    CON0024.ce = True
    CON0024.cf = True
    CON0025.game_object = "NLO:CharacterController"
    CON0025.property_name = "isStomping"
    CON0025.compare_value = True
    CON0025.operator = 0
    CON0026.game_object = "NLO:CharacterController"
    CON0026.property_name = "isStomping"
    CON0026.compare_value = False
    CON0026.operator = 0
    CON0027.game_object = "NLO:CharacterController"
    CON0027.property_name = "idle"
    CON0027.compare_value = 10.0
    CON0027.operator = 5
    CON0028.game_object = "NLO:CharacterController"
    CON0028.property_name = "idle"
    CON0028.compare_value = 16.0
    CON0028.operator = 2
    CON0029.ca = CON0030
    CON0029.cb = CON0027
    CON0029.cc = CON0012
    CON0029.cd = CON0034
    CON0029.ce = CON0033
    CON0029.cf = CON0032
    CON0030.game_object = "NLO:CharacterController"
    CON0030.property_name = "Speed"
    CON0030.compare_value = 0.029999999329447746
    CON0030.operator = 5
    CON0031.condition_a = CON0029
    CON0031.condition_b = CON0028
    CON0032.game_object = "NLO:CharacterController"
    CON0032.property_name = "isFalling"
    CON0032.compare_value = False
    CON0032.operator = 5
    CON0033.game_object = "NLO:CharacterController"
    CON0033.property_name = "isFalling"
    CON0033.compare_value = False
    CON0033.operator = 5
    CON0034.game_object = "NLO:CharacterController"
    CON0034.property_name = "isJumping"
    CON0034.compare_value = False
    CON0034.operator = 5
    ACT0035.condition = CON0031
    ACT0035.game_object = "NLO:U_O"
    ACT0035.action_name = "Idle"
    ACT0035.start_frame = 1.0
    ACT0035.end_frame = 68.0
    ACT0035.layer = 0
    ACT0035.priority = 90
    ACT0035.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0035.stop = False
    ACT0035.layer_weight = 1.0
    ACT0035.speed = 1.0
    ACT0035.blendin = 4.0
    ACT0035.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0036.condition = ACT0035.RUNNING
    ACT0036.game_object = "NLO:CharacterController"
    ACT0036.property_name = "animation"
    ACT0036.property_value = "idle"
    ACT0037.condition = CON0011
    ACT0037.game_object = "NLO:chr_Sonic_HD"
    ACT0037.action_name = "Idle00"
    ACT0037.start_frame = 1.0
    ACT0037.end_frame = 155.1600341796875
    ACT0037.layer = 0
    ACT0037.priority = 70
    ACT0037.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0037.stop = False
    ACT0037.layer_weight = 1.0
    ACT0037.speed = 1.0
    ACT0037.blendin = 4.0
    ACT0037.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0038.condition = ACT0037.RUNNING
    ACT0038.game_object = "NLO:CharacterController"
    ACT0038.property_name = "animation"
    ACT0038.property_value = "idle"
    ACT0039.condition = CON0005
    ACT0039.game_object = "NLO:U_O"
    ACT0039.action_name = "Jog"
    ACT0039.start_frame = 1.0
    ACT0039.end_frame = 34.0
    ACT0039.layer = 0
    ACT0039.priority = 8
    ACT0039.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0039.stop = False
    ACT0039.layer_weight = 1.0
    ACT0039.speed = 3.0
    ACT0039.blendin = 2.0
    ACT0039.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0040.condition = ACT0039.RUNNING
    ACT0040.game_object = "NLO:CharacterController"
    ACT0040.property_name = "animation"
    ACT0040.property_value = "jog"
    CON0041.game_object = "NLO:CharacterController"
    CON0041.property_name = "Speed"
    CON0041.compare_value = 0.30000001192092896
    CON0041.operator = 5
    CON0042.game_object = "NLO:CharacterController"
    CON0042.property_name = "Speed"
    CON0042.compare_value = 0.029999999329447746
    CON0042.operator = 2
    CON0043.game_object = "NLO:CharacterController"
    CON0043.property_name = "isFalling"
    CON0043.compare_value = False
    CON0043.operator = 0
    ACT0044.condition = CON0046
    ACT0044.game_object = "NLO:U_O"
    ACT0044.action_name = "Walk"
    ACT0044.start_frame = 1.0
    ACT0044.end_frame = 34.0
    ACT0044.layer = 0
    ACT0044.priority = 10
    ACT0044.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0044.stop = False
    ACT0044.layer_weight = 1.0
    ACT0044.speed = 2.0
    ACT0044.blendin = 4.0
    ACT0044.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0045.game_object = "NLO:CharacterController"
    CON0045.property_name = "isStomping"
    CON0045.compare_value = False
    CON0045.operator = 0
    CON0046.ca = CON0041
    CON0046.cb = CON0042
    CON0046.cc = CON0043
    CON0046.cd = CON0045
    CON0046.ce = CON0012
    CON0046.cf = True
    ACT0047.condition = ACT0044.RUNNING
    ACT0047.game_object = "NLO:CharacterController"
    ACT0047.property_name = "animation"
    ACT0047.property_value = "walk"
    ACT0048.condition = None
    ACT0048.game_object = "NLO:CharacterController"
    ACT0048.property_name = "animation"
    ACT0048.property_value = "walk"
    ACT0049.condition = CON0009
    ACT0049.game_object = "NLO:U_O"
    ACT0049.action_name = "Jet"
    ACT0049.start_frame = 1.0
    ACT0049.end_frame = 34.0
    ACT0049.layer = 0
    ACT0049.priority = 4
    ACT0049.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0049.stop = False
    ACT0049.layer_weight = 1.0
    ACT0049.speed = 4.0
    ACT0049.blendin = 2.0
    ACT0049.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0050.condition = ACT0049.RUNNING
    ACT0050.game_object = "NLO:CharacterController"
    ACT0050.property_name = "animation"
    ACT0050.property_value = "jet"
    ACT0051.condition = CON0013
    ACT0051.game_object = "NLO:chr_Sonic_HD"
    ACT0051.action_name = "Boost"
    ACT0051.start_frame = 1.0
    ACT0051.end_frame = 34.0
    ACT0051.layer = 1
    ACT0051.priority = 2
    ACT0051.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0051.stop = True
    ACT0051.layer_weight = 1.0
    ACT0051.speed = 4.0
    ACT0051.blendin = 4.0
    ACT0051.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0052.condition = ACT0051.RUNNING
    ACT0052.game_object = "NLO:CharacterController"
    ACT0052.property_name = "animation"
    ACT0052.property_value = "boost"
    ACT0053.condition = ACT0017.RUNNING
    ACT0053.game_object = "NLO:CharacterController"
    ACT0053.property_name = "animation"
    ACT0053.property_value = "null"
    ACT0054.condition = CON0021
    ACT0054.game_object = "NLO:chr_Sonic_HD"
    ACT0054.action_name = "Stomp"
    ACT0054.start_frame = 1.0
    ACT0054.end_frame = 6.0
    ACT0054.layer = 0
    ACT0054.priority = 39
    ACT0054.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0054.stop = False
    ACT0054.layer_weight = 1.0
    ACT0054.speed = 1.0
    ACT0054.blendin = 2.0
    ACT0054.blend_mode = bge.logic.KX_ACTION_BLEND_ADD
    ACT0055.condition = ACT0054.RUNNING
    ACT0055.game_object = "NLO:CharacterController"
    ACT0055.property_name = "animation"
    ACT0055.property_value = "null"
    ACT0056.condition = ACT0058.RUNNING
    ACT0056.game_object = "NLO:CharacterController"
    ACT0056.property_name = "animation"
    ACT0056.property_value = "null"
    ACT0057.condition = None
    ACT0057.game_object = "NLO:CharacterController"
    ACT0057.property_name = "animation"
    ACT0057.property_value = "null"
    ACT0058.condition = CON0024
    ACT0058.game_object = "NLO:chr_Sonic_HD"
    ACT0058.action_name = "JumpArc"
    ACT0058.start_frame = 1.0
    ACT0058.end_frame = 6.0
    ACT0058.layer = 0
    ACT0058.priority = 40
    ACT0058.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0058.stop = False
    ACT0058.layer_weight = 1.0
    ACT0058.speed = 1.0
    ACT0058.blendin = 7.0
    ACT0058.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    network.add_cell(CON0001)
    network.add_cell(CON0003)
    network.add_cell(CON0006)
    network.add_cell(CON0008)
    network.add_cell(CON0010)
    network.add_cell(CON0014)
    network.add_cell(CON0016)
    network.add_cell(CON0019)
    network.add_cell(CON0022)
    network.add_cell(CON0025)
    network.add_cell(CON0027)
    network.add_cell(CON0030)
    network.add_cell(CON0032)
    network.add_cell(CON0034)
    network.add_cell(CON0041)
    network.add_cell(CON0043)
    network.add_cell(CON0045)
    network.add_cell(ACT0048)
    network.add_cell(ACT0057)
    network.add_cell(ACT0000)
    network.add_cell(CON0004)
    network.add_cell(CON0007)
    network.add_cell(CON0011)
    network.add_cell(CON0015)
    network.add_cell(CON0020)
    network.add_cell(CON0023)
    network.add_cell(CON0026)
    network.add_cell(CON0033)
    network.add_cell(ACT0037)
    network.add_cell(CON0042)
    network.add_cell(CON0002)
    network.add_cell(CON0012)
    network.add_cell(CON0018)
    network.add_cell(CON0024)
    network.add_cell(CON0029)
    network.add_cell(ACT0038)
    network.add_cell(CON0046)
    network.add_cell(ACT0058)
    network.add_cell(CON0005)
    network.add_cell(CON0013)
    network.add_cell(CON0021)
    network.add_cell(ACT0039)
    network.add_cell(ACT0044)
    network.add_cell(ACT0051)
    network.add_cell(ACT0054)
    network.add_cell(ACT0056)
    network.add_cell(CON0009)
    network.add_cell(CON0028)
    network.add_cell(ACT0040)
    network.add_cell(ACT0049)
    network.add_cell(ACT0052)
    network.add_cell(ACT0055)
    network.add_cell(ACT0017)
    network.add_cell(ACT0047)
    network.add_cell(ACT0053)
    network.add_cell(CON0031)
    network.add_cell(ACT0050)
    network.add_cell(ACT0035)
    network.add_cell(ACT0036)
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
