# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionPlayAction()
    ACT0001 = nodes.ActionApplyRotation()
    CON0002 = nodes.ConditionOnUpdate()
    CON0003 = nodes.ObjectPropertyOperator()
    CON0004 = nodes.ObjectPropertyOperator()
    CON0005 = nodes.ObjectPropertyOperator()
    CON0006 = nodes.ConditionAndList()
    ACT0007 = nodes.ActionPlayAction()
    CON0008 = nodes.ObjectPropertyOperator()
    CON0009 = nodes.ObjectPropertyOperator()
    CON0010 = nodes.ObjectPropertyOperator()
    CON0011 = nodes.ConditionAndList()
    CON0012 = nodes.ObjectPropertyOperator()
    CON0013 = nodes.ObjectPropertyOperator()
    CON0014 = nodes.ObjectPropertyOperator()
    ACT0015 = nodes.ActionPlayAction()
    CON0016 = nodes.ObjectPropertyOperator()
    CON0017 = nodes.ConditionAndList()
    ACT0018 = nodes.ActionPlayAction()
    CON0019 = nodes.ObjectPropertyOperator()
    CON0020 = nodes.ObjectPropertyOperator()
    ACT0021 = nodes.ActionPlayAction()
    CON0022 = nodes.ConditionNot()
    CON0023 = nodes.ConditionAnd()
    CON0024 = nodes.ObjectPropertyOperator()
    CON0025 = nodes.ObjectPropertyOperator()
    CON0026 = nodes.ObjectPropertyOperator()
    ACT0027 = nodes.ActionPlayAction()
    ACT0028 = nodes.ActionPlayAction()
    CON0029 = nodes.ConditionAnd()
    CON0030 = nodes.ObjectPropertyOperator()
    CON0031 = nodes.ObjectPropertyOperator()
    ACT0032 = nodes.ActionPlayAction()
    CON0033 = nodes.ConditionAndList()
    CON0034 = nodes.ObjectPropertyOperator()
    CON0035 = nodes.ObjectPropertyOperator()
    CON0036 = nodes.ConditionAndList()
    CON0037 = nodes.ObjectPropertyOperator()
    CON0038 = nodes.ObjectPropertyOperator()
    ACT0039 = nodes.ActionPlayAction()
    CON0040 = nodes.ObjectPropertyOperator()
    CON0041 = nodes.ObjectPropertyOperator()
    CON0042 = nodes.ConditionAndList()
    CON0043 = nodes.ObjectPropertyOperator()
    CON0044 = nodes.ConditionOr()
    CON0045 = nodes.ObjectPropertyOperator()
    CON0046 = nodes.ObjectPropertyOperator()
    CON0047 = nodes.ObjectPropertyOperator()
    ACT0000.condition = CON0020
    ACT0000.game_object = "NLO:chr_Sonic_HD"
    ACT0000.action_name = "Idle00"
    ACT0000.start_frame = 1.0
    ACT0000.end_frame = 155.1600341796875
    ACT0000.layer = 0
    ACT0000.priority = 70
    ACT0000.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0000.stop = False
    ACT0000.layer_weight = 1.0
    ACT0000.speed = 1.0
    ACT0000.blendin = 4.0
    ACT0000.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0001.local = True
    ACT0001.condition = CON0002
    ACT0001.game_object = "NLO:SonicBall"
    ACT0001.rotation = mathutils.Vector((0.5235987901687622, 0.0, 0.0))
    CON0003.game_object = "NLO:CharacterController"
    CON0003.property_name = "Speed"
    CON0003.compare_value = 0.30000001192092896
    CON0003.operator = 2
    CON0004.game_object = "NLO:CharacterController"
    CON0004.property_name = "Speed"
    CON0004.compare_value = 0.699999988079071
    CON0004.operator = 5
    CON0005.game_object = "NLO:CharacterController"
    CON0005.property_name = "isFalling"
    CON0005.compare_value = False
    CON0005.operator = 0
    CON0006.ca = CON0004
    CON0006.cb = CON0003
    CON0006.cc = CON0005
    CON0006.cd = CON0019
    CON0006.ce = CON0022
    CON0006.cf = True
    ACT0007.condition = CON0011
    ACT0007.game_object = "NLO:U_O"
    ACT0007.action_name = "Jet"
    ACT0007.start_frame = 1.0
    ACT0007.end_frame = 34.0
    ACT0007.layer = 0
    ACT0007.priority = 4
    ACT0007.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0007.stop = False
    ACT0007.layer_weight = 1.0
    ACT0007.speed = 4.0
    ACT0007.blendin = 2.0
    ACT0007.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0008.game_object = "NLO:CharacterController"
    CON0008.property_name = "Speed"
    CON0008.compare_value = 0.699999988079071
    CON0008.operator = 2
    CON0009.game_object = "NLO:CharacterController"
    CON0009.property_name = "isFalling"
    CON0009.compare_value = False
    CON0009.operator = 0
    CON0010.game_object = "NLO:CharacterController"
    CON0010.property_name = "isStomping"
    CON0010.compare_value = False
    CON0010.operator = 0
    CON0011.ca = True
    CON0011.cb = CON0008
    CON0011.cc = CON0009
    CON0011.cd = CON0010
    CON0011.ce = CON0022
    CON0011.cf = True
    CON0012.game_object = "NLO:CharacterController"
    CON0012.property_name = "Speed"
    CON0012.compare_value = 0.30000001192092896
    CON0012.operator = 5
    CON0013.game_object = "NLO:CharacterController"
    CON0013.property_name = "Speed"
    CON0013.compare_value = 0.029999999329447746
    CON0013.operator = 2
    CON0014.game_object = "NLO:CharacterController"
    CON0014.property_name = "isFalling"
    CON0014.compare_value = False
    CON0014.operator = 0
    ACT0015.condition = CON0017
    ACT0015.game_object = "NLO:U_O"
    ACT0015.action_name = "Walk"
    ACT0015.start_frame = 1.0
    ACT0015.end_frame = 34.0
    ACT0015.layer = 0
    ACT0015.priority = 10
    ACT0015.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0015.stop = False
    ACT0015.layer_weight = 1.0
    ACT0015.speed = 2.0
    ACT0015.blendin = 4.0
    ACT0015.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0016.game_object = "NLO:CharacterController"
    CON0016.property_name = "isStomping"
    CON0016.compare_value = False
    CON0016.operator = 0
    CON0017.ca = CON0012
    CON0017.cb = CON0013
    CON0017.cc = CON0014
    CON0017.cd = CON0016
    CON0017.ce = CON0022
    CON0017.cf = True
    ACT0018.condition = CON0006
    ACT0018.game_object = "NLO:U_O"
    ACT0018.action_name = "Jog"
    ACT0018.start_frame = 1.0
    ACT0018.end_frame = 34.0
    ACT0018.layer = 0
    ACT0018.priority = 8
    ACT0018.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0018.stop = False
    ACT0018.layer_weight = 1.0
    ACT0018.speed = 3.0
    ACT0018.blendin = 2.0
    ACT0018.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0019.game_object = "NLO:CharacterController"
    CON0019.property_name = "isStomping"
    CON0019.compare_value = False
    CON0019.operator = 0
    CON0020.game_object = "NLO:CharacterController"
    CON0020.property_name = "idle"
    CON0020.compare_value = 10.0
    CON0020.operator = 4
    ACT0021.condition = CON0023
    ACT0021.game_object = "NLO:chr_Sonic_HD"
    ACT0021.action_name = "Boost"
    ACT0021.start_frame = 1.0
    ACT0021.end_frame = 34.0
    ACT0021.layer = 1
    ACT0021.priority = 2
    ACT0021.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0021.stop = True
    ACT0021.layer_weight = 1.0
    ACT0021.speed = 4.0
    ACT0021.blendin = 4.0
    ACT0021.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0022.condition = CON0024
    CON0023.condition_a = CON0024
    CON0023.condition_b = CON0025
    CON0024.game_object = "NLO:CharacterController"
    CON0024.property_name = "isBoosting"
    CON0024.compare_value = True
    CON0024.operator = 0
    CON0025.game_object = "NLO:CharacterController"
    CON0025.property_name = "isFalling"
    CON0025.compare_value = False
    CON0025.operator = 0
    CON0026.game_object = "NLO:CharacterController"
    CON0026.property_name = "isFalling"
    CON0026.compare_value = True
    CON0026.operator = 0
    ACT0027.condition = CON0036
    ACT0027.game_object = "NLO:chr_Sonic_HD"
    ACT0027.action_name = "JumpArc"
    ACT0027.start_frame = 1.0
    ACT0027.end_frame = 6.0
    ACT0027.layer = 0
    ACT0027.priority = 40
    ACT0027.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0027.stop = False
    ACT0027.layer_weight = 1.0
    ACT0027.speed = 1.0
    ACT0027.blendin = 7.0
    ACT0027.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0028.condition = CON0029
    ACT0028.game_object = "NLO:chr_Sonic_HD"
    ACT0028.action_name = "AirBoost"
    ACT0028.start_frame = 1.0
    ACT0028.end_frame = 9.0
    ACT0028.layer = 0
    ACT0028.priority = 40
    ACT0028.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0028.stop = True
    ACT0028.layer_weight = 1.0
    ACT0028.speed = 1.0
    ACT0028.blendin = 7.0
    ACT0028.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0029.condition_a = CON0030
    CON0029.condition_b = CON0031
    CON0030.game_object = "NLO:CharacterController"
    CON0030.property_name = "isFalling"
    CON0030.compare_value = True
    CON0030.operator = 0
    CON0031.game_object = "NLO:CharacterController"
    CON0031.property_name = "isBoosting"
    CON0031.compare_value = True
    CON0031.operator = 0
    ACT0032.condition = CON0033
    ACT0032.game_object = "NLO:chr_Sonic_HD"
    ACT0032.action_name = "Stomp"
    ACT0032.start_frame = 1.0
    ACT0032.end_frame = 6.0
    ACT0032.layer = 0
    ACT0032.priority = 39
    ACT0032.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0032.stop = False
    ACT0032.layer_weight = 1.0
    ACT0032.speed = 1.0
    ACT0032.blendin = 2.0
    ACT0032.blend_mode = bge.logic.KX_ACTION_BLEND_ADD
    CON0033.ca = CON0037
    CON0033.cb = CON0034
    CON0033.cc = True
    CON0033.cd = True
    CON0033.ce = True
    CON0033.cf = True
    CON0034.game_object = "NLO:CharacterController"
    CON0034.property_name = "isBoosting"
    CON0034.compare_value = False
    CON0034.operator = 0
    CON0035.game_object = "NLO:CharacterController"
    CON0035.property_name = "isBoosting"
    CON0035.compare_value = False
    CON0035.operator = 0
    CON0036.ca = CON0026
    CON0036.cb = CON0035
    CON0036.cc = CON0038
    CON0036.cd = True
    CON0036.ce = True
    CON0036.cf = True
    CON0037.game_object = "NLO:CharacterController"
    CON0037.property_name = "isStomping"
    CON0037.compare_value = True
    CON0037.operator = 0
    CON0038.game_object = "NLO:CharacterController"
    CON0038.property_name = "isStomping"
    CON0038.compare_value = False
    CON0038.operator = 0
    ACT0039.condition = CON0044
    ACT0039.game_object = "NLO:U_O"
    ACT0039.action_name = "Idle"
    ACT0039.start_frame = 1.0
    ACT0039.end_frame = 68.0
    ACT0039.layer = 0
    ACT0039.priority = 90
    ACT0039.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0039.stop = False
    ACT0039.layer_weight = 1.0
    ACT0039.speed = 1.0
    ACT0039.blendin = 4.0
    ACT0039.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0040.game_object = "NLO:CharacterController"
    CON0040.property_name = "idle"
    CON0040.compare_value = 10.0
    CON0040.operator = 5
    CON0041.game_object = "NLO:CharacterController"
    CON0041.property_name = "idle"
    CON0041.compare_value = 16.0
    CON0041.operator = 2
    CON0042.ca = CON0043
    CON0042.cb = CON0040
    CON0042.cc = CON0022
    CON0042.cd = CON0047
    CON0042.ce = CON0046
    CON0042.cf = CON0045
    CON0043.game_object = "NLO:CharacterController"
    CON0043.property_name = "Speed"
    CON0043.compare_value = 0.029999999329447746
    CON0043.operator = 5
    CON0044.condition_a = CON0042
    CON0044.condition_b = CON0041
    CON0045.game_object = "NLO:CharacterController"
    CON0045.property_name = "isFalling"
    CON0045.compare_value = False
    CON0045.operator = 5
    CON0046.game_object = "NLO:CharacterController"
    CON0046.property_name = "isFalling"
    CON0046.compare_value = False
    CON0046.operator = 5
    CON0047.game_object = "NLO:CharacterController"
    CON0047.property_name = "isJumping"
    CON0047.compare_value = False
    CON0047.operator = 5
    network.add_cell(CON0002)
    network.add_cell(CON0004)
    network.add_cell(CON0008)
    network.add_cell(CON0010)
    network.add_cell(CON0012)
    network.add_cell(CON0014)
    network.add_cell(CON0016)
    network.add_cell(CON0019)
    network.add_cell(CON0024)
    network.add_cell(CON0026)
    network.add_cell(CON0030)
    network.add_cell(CON0034)
    network.add_cell(CON0037)
    network.add_cell(CON0040)
    network.add_cell(CON0043)
    network.add_cell(CON0045)
    network.add_cell(CON0047)
    network.add_cell(ACT0001)
    network.add_cell(CON0005)
    network.add_cell(CON0009)
    network.add_cell(CON0013)
    network.add_cell(CON0020)
    network.add_cell(CON0022)
    network.add_cell(CON0025)
    network.add_cell(CON0031)
    network.add_cell(CON0033)
    network.add_cell(CON0038)
    network.add_cell(CON0041)
    network.add_cell(CON0046)
    network.add_cell(ACT0000)
    network.add_cell(CON0011)
    network.add_cell(CON0017)
    network.add_cell(CON0023)
    network.add_cell(CON0029)
    network.add_cell(CON0035)
    network.add_cell(CON0042)
    network.add_cell(CON0003)
    network.add_cell(ACT0007)
    network.add_cell(ACT0021)
    network.add_cell(ACT0028)
    network.add_cell(CON0036)
    network.add_cell(CON0044)
    network.add_cell(CON0006)
    network.add_cell(ACT0018)
    network.add_cell(ACT0032)
    network.add_cell(ACT0015)
    network.add_cell(ACT0039)
    network.add_cell(ACT0027)
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
