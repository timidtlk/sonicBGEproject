# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionPlayAction()
    CON0001 = nodes.ObjectPropertyOperator()
    ACT0002 = nodes.ActionApplyRotation()
    CON0003 = nodes.ConditionOnUpdate()
    CON0004 = nodes.ObjectPropertyOperator()
    ACT0005 = nodes.ActionPlayAction()
    CON0006 = nodes.ObjectPropertyOperator()
    CON0007 = nodes.ConditionAnd()
    CON0008 = nodes.ConditionNot()
    CON0009 = nodes.ConditionCollision()
    ACT0010 = nodes.ActionPlayAction()
    ACT0011 = nodes.ActionPlayAction()
    CON0012 = nodes.ObjectPropertyOperator()
    CON0013 = nodes.ObjectPropertyOperator()
    CON0014 = nodes.ObjectPropertyOperator()
    CON0015 = nodes.ConditionAndList()
    ACT0016 = nodes.ActionPlayAction()
    CON0017 = nodes.ObjectPropertyOperator()
    CON0018 = nodes.ObjectPropertyOperator()
    CON0019 = nodes.ObjectPropertyOperator()
    CON0020 = nodes.ObjectPropertyOperator()
    CON0021 = nodes.ConditionAndList()
    CON0022 = nodes.ObjectPropertyOperator()
    CON0023 = nodes.ObjectPropertyOperator()
    CON0024 = nodes.ObjectPropertyOperator()
    ACT0025 = nodes.ActionPlayAction()
    CON0026 = nodes.ObjectPropertyOperator()
    CON0027 = nodes.ConditionAndList()
    ACT0028 = nodes.ActionPlayAction()
    ACT0029 = nodes.ActionPlayAction()
    CON0030 = nodes.ObjectPropertyOperator()
    CON0031 = nodes.ObjectPropertyOperator()
    CON0032 = nodes.ObjectPropertyOperator()
    CON0033 = nodes.ConditionAndList()
    CON0034 = nodes.ConditionOr()
    CON0035 = nodes.ObjectPropertyOperator()
    ACT0000.condition = CON0001
    ACT0000.game_object = "NLO:chr_Sonic_HD.002"
    ACT0000.action_name = "Idle00.001"
    ACT0000.start_frame = 1.0
    ACT0000.end_frame = 155.0
    ACT0000.layer = 0
    ACT0000.priority = 70
    ACT0000.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0000.stop = False
    ACT0000.layer_weight = 1.0
    ACT0000.speed = 1.0
    ACT0000.blendin = 4.0
    ACT0000.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0001.game_object = "NLO:CharacterController.001"
    CON0001.property_name = "idle"
    CON0001.compare_value = 10.0
    CON0001.operator = 4
    ACT0002.local = True
    ACT0002.condition = CON0003
    ACT0002.game_object = "NLO:SonicBall.001"
    ACT0002.rotation = mathutils.Vector((0.5235987901687622, 0.0, 0.0))
    CON0004.game_object = "NLO:CharacterController.001"
    CON0004.property_name = "isFalling"
    CON0004.compare_value = True
    CON0004.operator = 0
    ACT0005.condition = CON0004
    ACT0005.game_object = "NLO:chr_Sonic_HD.002"
    ACT0005.action_name = "JumpArc.001"
    ACT0005.start_frame = 1.0
    ACT0005.end_frame = 6.0
    ACT0005.layer = 0
    ACT0005.priority = 40
    ACT0005.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0005.stop = False
    ACT0005.layer_weight = 1.0
    ACT0005.speed = 1.0
    ACT0005.blendin = 5.0
    ACT0005.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0006.game_object = "NLO:CharacterController.001"
    CON0006.property_name = "isStomping"
    CON0006.compare_value = True
    CON0006.operator = 0
    CON0007.condition_a = CON0006
    CON0007.condition_b = CON0008
    CON0008.condition = CON0009
    CON0009.game_object = "NLO:groundSensor.001"
    CON0009.use_mat = False
    CON0009.prop = "obstacle"
    CON0009.material = None
    CON0009.pulse = False
    ACT0010.condition = CON0009
    ACT0010.game_object = "NLO:chr_Sonic_HD.002"
    ACT0010.action_name = "LandingIdle.001"
    ACT0010.start_frame = 1.0
    ACT0010.end_frame = 24.0
    ACT0010.layer = 0
    ACT0010.priority = 5
    ACT0010.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0010.stop = True
    ACT0010.layer_weight = 1.0
    ACT0010.speed = 1.0
    ACT0010.blendin = 4.0
    ACT0010.blend_mode = bge.logic.KX_ACTION_BLEND_ADD
    ACT0011.condition = CON0007
    ACT0011.game_object = "NLO:chr_Sonic_HD.002"
    ACT0011.action_name = "Stomp.001"
    ACT0011.start_frame = 1.0
    ACT0011.end_frame = 6.0
    ACT0011.layer = 0
    ACT0011.priority = 2
    ACT0011.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0011.stop = True
    ACT0011.layer_weight = 1.0
    ACT0011.speed = 1.0
    ACT0011.blendin = 0.0
    ACT0011.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0012.game_object = "NLO:CharacterController.001"
    CON0012.property_name = "Speed"
    CON0012.compare_value = 0.30000001192092896
    CON0012.operator = 2
    CON0013.game_object = "NLO:CharacterController.001"
    CON0013.property_name = "Speed"
    CON0013.compare_value = 0.699999988079071
    CON0013.operator = 5
    CON0014.game_object = "NLO:CharacterController.001"
    CON0014.property_name = "isFalling"
    CON0014.compare_value = False
    CON0014.operator = 0
    CON0015.ca = CON0013
    CON0015.cb = CON0012
    CON0015.cc = CON0014
    CON0015.cd = CON0035
    CON0015.ce = True
    CON0015.cf = True
    ACT0016.condition = CON0021
    ACT0016.game_object = "NLO:U_O"
    ACT0016.action_name = "Jet.001"
    ACT0016.start_frame = 1.0
    ACT0016.end_frame = 34.0
    ACT0016.layer = 0
    ACT0016.priority = 4
    ACT0016.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0016.stop = False
    ACT0016.layer_weight = 1.0
    ACT0016.speed = 4.0
    ACT0016.blendin = 2.0
    ACT0016.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0017.game_object = "NLO:CharacterController.001"
    CON0017.property_name = "Speed"
    CON0017.compare_value = 0.800000011920929
    CON0017.operator = 5
    CON0018.game_object = "NLO:CharacterController.001"
    CON0018.property_name = "Speed"
    CON0018.compare_value = 0.699999988079071
    CON0018.operator = 2
    CON0019.game_object = "NLO:CharacterController.001"
    CON0019.property_name = "isFalling"
    CON0019.compare_value = False
    CON0019.operator = 0
    CON0020.game_object = "NLO:CharacterController.001"
    CON0020.property_name = "isStomping"
    CON0020.compare_value = False
    CON0020.operator = 0
    CON0021.ca = CON0017
    CON0021.cb = CON0018
    CON0021.cc = CON0019
    CON0021.cd = CON0020
    CON0021.ce = True
    CON0021.cf = True
    CON0022.game_object = "NLO:CharacterController.001"
    CON0022.property_name = "Speed"
    CON0022.compare_value = 0.30000001192092896
    CON0022.operator = 5
    CON0023.game_object = "NLO:CharacterController.001"
    CON0023.property_name = "Speed"
    CON0023.compare_value = 0.029999999329447746
    CON0023.operator = 2
    CON0024.game_object = "NLO:CharacterController.001"
    CON0024.property_name = "isFalling"
    CON0024.compare_value = False
    CON0024.operator = 0
    ACT0025.condition = CON0027
    ACT0025.game_object = "NLO:U_O"
    ACT0025.action_name = "Walk.001"
    ACT0025.start_frame = 1.0
    ACT0025.end_frame = 34.0
    ACT0025.layer = 0
    ACT0025.priority = 10
    ACT0025.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0025.stop = False
    ACT0025.layer_weight = 1.0
    ACT0025.speed = 2.0
    ACT0025.blendin = 4.0
    ACT0025.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0026.game_object = "NLO:CharacterController.001"
    CON0026.property_name = "isStomping"
    CON0026.compare_value = False
    CON0026.operator = 0
    CON0027.ca = CON0022
    CON0027.cb = CON0023
    CON0027.cc = CON0024
    CON0027.cd = CON0026
    CON0027.ce = True
    CON0027.cf = True
    ACT0028.condition = CON0015
    ACT0028.game_object = "NLO:U_O"
    ACT0028.action_name = "Jog.001"
    ACT0028.start_frame = 1.0
    ACT0028.end_frame = 34.0
    ACT0028.layer = 0
    ACT0028.priority = 8
    ACT0028.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0028.stop = False
    ACT0028.layer_weight = 1.0
    ACT0028.speed = 3.0
    ACT0028.blendin = 2.0
    ACT0028.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0029.condition = CON0034
    ACT0029.game_object = "NLO:U_O"
    ACT0029.action_name = "Idle.001"
    ACT0029.start_frame = 1.0
    ACT0029.end_frame = 68.0
    ACT0029.layer = 0
    ACT0029.priority = 99
    ACT0029.play_mode = bge.logic.KX_ACTION_MODE_LOOP + 3
    ACT0029.stop = False
    ACT0029.layer_weight = 1.0
    ACT0029.speed = 1.0
    ACT0029.blendin = 4.0
    ACT0029.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0030.game_object = "NLO:CharacterController.001"
    CON0030.property_name = "Speed"
    CON0030.compare_value = 0.0
    CON0030.operator = 5
    CON0031.game_object = "NLO:CharacterController.001"
    CON0031.property_name = "idle"
    CON0031.compare_value = 10.0
    CON0031.operator = 5
    CON0032.game_object = "NLO:CharacterController.001"
    CON0032.property_name = "idle"
    CON0032.compare_value = 16.0
    CON0032.operator = 2
    CON0033.ca = CON0030
    CON0033.cb = CON0031
    CON0033.cc = True
    CON0033.cd = True
    CON0033.ce = True
    CON0033.cf = True
    CON0034.condition_a = CON0033
    CON0034.condition_b = CON0032
    CON0035.game_object = "NLO:CharacterController.001"
    CON0035.property_name = "isStomping"
    CON0035.compare_value = False
    CON0035.operator = 0
    network.add_cell(CON0001)
    network.add_cell(CON0003)
    network.add_cell(CON0006)
    network.add_cell(CON0009)
    network.add_cell(CON0012)
    network.add_cell(CON0014)
    network.add_cell(CON0017)
    network.add_cell(CON0019)
    network.add_cell(CON0022)
    network.add_cell(CON0024)
    network.add_cell(CON0026)
    network.add_cell(CON0030)
    network.add_cell(CON0032)
    network.add_cell(CON0035)
    network.add_cell(ACT0000)
    network.add_cell(CON0004)
    network.add_cell(CON0008)
    network.add_cell(CON0013)
    network.add_cell(CON0018)
    network.add_cell(CON0023)
    network.add_cell(CON0027)
    network.add_cell(CON0031)
    network.add_cell(ACT0002)
    network.add_cell(CON0007)
    network.add_cell(ACT0011)
    network.add_cell(CON0020)
    network.add_cell(ACT0025)
    network.add_cell(CON0033)
    network.add_cell(ACT0005)
    network.add_cell(CON0015)
    network.add_cell(CON0021)
    network.add_cell(CON0034)
    network.add_cell(ACT0010)
    network.add_cell(ACT0028)
    network.add_cell(ACT0016)
    network.add_cell(ACT0029)
    owner["IGNLTree_playerAnim.001"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__playerAnim.001')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_playerAnim.001")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
