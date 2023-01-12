# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    PAR0000 = nodes.ParameterObjectAttribute()
    ACT0001 = nodes.ActionSetGameObjectGameProperty()
    CON0002 = nodes.ObjectPropertyOperator()
    ACT0003 = nodes.ActionSetGameObjectGameProperty()
    CON0004 = nodes.ObjectPropertyOperator()
    ACT0005 = nodes.ActionSetDynamics()
    ACT0006 = nodes.ActionMoveTo()
    CON0007 = nodes.ConditionNot()
    ACT0008 = nodes.ActionSetGameObjectGameProperty()
    ACT0009 = nodes.ActionSetGameObjectGameProperty()
    CON0010 = nodes.ConditionAndList()
    CON0011 = nodes.ConditionOr()
    CON0012 = nodes.ConditionKeyPressed()
    CON0013 = nodes.ConditionGamepadButtons()
    ACT0014 = nodes.ActionRotateTo()
    ACT0015 = nodes.ParameterPythonModuleFunction()
    CON0016 = nodes.GE_OnInit()
    CON0017 = nodes.ConditionOnUpdate()
    ACT0018 = nodes.ActionSetGameObjectVisibility()
    ACT0019 = nodes.ActionSetGameObjectVisibility()
    CON0020 = nodes.ConditionDistanceCheck()
    CON0021 = nodes.ObjectPropertyOperator()
    CON0022 = nodes.ObjectPropertyOperator()
    CON0023 = nodes.ObjectPropertyOperator()
    ACT0024 = nodes.ActionSetGameObjectGameProperty()
    PAR0025 = nodes.ParameterObjectAttribute()
    CON0026 = nodes.ConditionDistanceCheck()
    PAR0027 = nodes.ParameterObjectAttribute()
    PAR0028 = nodes.ParameterObjectAttribute()
    PAR0029 = nodes.GetObjectDataName()
    ACT0030 = nodes.ParameterPythonModuleFunction()
    PAR0031 = nodes.ParameterObjectProperty()
    CON0032 = nodes.ConditionValueTrigger()
    ACT0033 = nodes.ActionStartSound()
    CON0034 = nodes.ObjectPropertyOperator()
    CON0035 = nodes.ConditionAnd()
    CON0036 = nodes.ConditionOr()
    CON0037 = nodes.ConditionCollision()
    ACT0038 = nodes.ActionSetGameObjectGameProperty()
    ACT0039 = nodes.ActionSetGameObjectGameProperty()
    PAR0040 = nodes.ParameterObjectProperty()
    PAR0041 = nodes.ParameterObjectProperty()
    ACT0042 = nodes.ActionStartSound()
    ACT0043 = nodes.ActionSetGameObjectGameProperty()
    CON0044 = nodes.ConditionValueTrigger()
    ACT0045 = nodes.ActionSetGameObjectGameProperty()
    PAR0000.game_object = "NLO:aim"
    PAR0000.attribute_name = "worldPosition"
    ACT0001.condition = CON0002
    ACT0001.game_object = "NLO:CharacterController"
    ACT0001.property_name = "Speed"
    ACT0001.property_value = 0.0
    CON0002.game_object = "NLO:CharacterController"
    CON0002.property_name = "homming"
    CON0002.compare_value = True
    CON0002.operator = 0
    ACT0003.condition = ACT0006
    ACT0003.game_object = "NLO:CharacterController"
    ACT0003.property_name = "homming"
    ACT0003.property_value = False
    CON0004.game_object = "NLO:CharacterController"
    CON0004.property_name = "homming"
    CON0004.compare_value = True
    CON0004.operator = 0
    ACT0005.condition = CON0004
    ACT0005.game_object = "NLO:CharacterController"
    ACT0005.activate = True
    ACT0005.ghost = False
    ACT0006.condition = CON0002
    ACT0006.moving_object = "NLO:CharacterController"
    ACT0006.destination_point = PAR0000
    ACT0006.dynamic = False
    ACT0006.speed = 60.0
    ACT0006.distance = 0.0
    CON0007.condition = CON0020
    ACT0008.condition = CON0020
    ACT0008.game_object = "NLO:CharacterController"
    ACT0008.property_name = "isHommiable"
    ACT0008.property_value = True
    ACT0009.condition = CON0007
    ACT0009.game_object = "NLO:CharacterController"
    ACT0009.property_name = "isHommiable"
    ACT0009.property_value = False
    CON0010.ca = CON0022
    CON0010.cb = CON0023
    CON0010.cc = CON0011
    CON0010.cd = CON0021
    CON0010.ce = True
    CON0010.cf = True
    CON0011.condition_a = CON0012
    CON0011.condition_b = CON0013.BUTTON
    CON0012.key_code = bge.events.SPACEKEY
    CON0012.pulse = False
    CON0013.index = 0
    CON0013.pulse = False
    CON0013.button = 0
    ACT0014.condition = CON0002
    ACT0014.moving_object = "NLO:CharacterController"
    ACT0014.target_point = PAR0000
    ACT0014.speed = 0.0
    ACT0014.rot_axis = 0
    ACT0014.front_axis = 4
    ACT0015.condition = CON0016
    ACT0015.module_name = "distanceChecker"
    ACT0015.module_func = "obj_loader"
    ACT0015.arg = nodes.Invalid()
    ACT0018.condition = CON0020
    ACT0018.game_object = "NLO:aim"
    ACT0018.visible = True
    ACT0018.recursive = False
    ACT0019.condition = CON0007
    ACT0019.game_object = "NLO:aim"
    ACT0019.visible = False
    ACT0019.recursive = False
    CON0020.operator = 5
    CON0020.param_a = PAR0025
    CON0020.param_b = PAR0027
    CON0020.dist = 25.0
    CON0020.hyst = 4.0
    CON0021.game_object = "NLO:CharacterController"
    CON0021.property_name = "isJumping"
    CON0021.compare_value = True
    CON0021.operator = 0
    CON0022.game_object = "NLO:CharacterController"
    CON0022.property_name = "jump"
    CON0022.compare_value = 3
    CON0022.operator = 0
    CON0023.game_object = "NLO:CharacterController"
    CON0023.property_name = "isHommiable"
    CON0023.compare_value = True
    CON0023.operator = 0
    ACT0024.condition = CON0010
    ACT0024.game_object = "NLO:CharacterController"
    ACT0024.property_name = "homming"
    ACT0024.property_value = True
    PAR0025.game_object = "NLO:CharacterController"
    PAR0025.attribute_name = "worldPosition"
    CON0026.operator = 5
    CON0026.param_a = PAR0025
    CON0026.param_b = PAR0028
    CON0026.dist = 1.0
    CON0026.hyst = None
    PAR0027.game_object = "NLO:aim"
    PAR0027.attribute_name = "worldPosition"
    PAR0028.game_object = "NLO:U_O"
    PAR0028.attribute_name = "worldPosition"
    PAR0029.game_object = ACT0030.VAL
    ACT0030.condition = CON0017
    ACT0030.module_name = "distanceChecker"
    ACT0030.module_func = "update"
    ACT0030.arg = PAR0040
    PAR0031.game_object = "NLO:CharacterController"
    PAR0031.property_name = "homming"
    CON0032.monitored_value = PAR0031
    CON0032.trigger_value = True
    ACT0033.condition = CON0032
    ACT0033.sound = "D:/Sonic BGE Project/sounds/Player Sounds/Sonic the Hedgehog/30_sn_homing.wav"
    ACT0033.loop_count = 0
    ACT0033.pitch = 1.0
    ACT0033.volume = 0.05000000074505806
    CON0034.game_object = "NLO:CharacterController"
    CON0034.property_name = "homming"
    CON0034.compare_value = True
    CON0034.operator = 0
    CON0035.condition_a = CON0034
    CON0035.condition_b = CON0026
    CON0036.condition_a = CON0035
    CON0036.condition_b = CON0037
    CON0037.game_object = "NLO:CharacterController"
    CON0037.use_mat = False
    CON0037.prop = "spring"
    CON0037.material = None
    CON0037.pulse = False
    ACT0038.condition = CON0036
    ACT0038.game_object = "NLO:CharacterController"
    ACT0038.property_name = "homming"
    ACT0038.property_value = False
    ACT0039.condition = ACT0038.OUT
    ACT0039.game_object = "NLO:CharacterController"
    ACT0039.property_name = "jump"
    ACT0039.property_value = 1
    PAR0040.game_object = "NLO:CharacterController"
    PAR0040.property_name = "homming"
    PAR0041.game_object = "NLO:aim"
    PAR0041.property_name = "executeSound"
    ACT0042.condition = CON0044
    ACT0042.sound = "D:/Sonic BGE Project/sounds/Object Sounds/Common/99_obj_lockon.wav"
    ACT0042.loop_count = 0
    ACT0042.pitch = 1.0
    ACT0042.volume = 0.20000000298023224
    ACT0043.condition = ACT0030.OUT
    ACT0043.game_object = "NLO:CharacterController"
    ACT0043.property_name = "homming_object"
    ACT0043.property_value = PAR0029
    CON0044.monitored_value = PAR0041
    CON0044.trigger_value = True
    ACT0045.condition = ACT0042.ON_FINISH
    ACT0045.game_object = "NLO:aim"
    ACT0045.property_name = "executeSound"
    ACT0045.property_value = False
    network.add_cell(PAR0000)
    network.add_cell(CON0002)
    network.add_cell(CON0004)
    network.add_cell(ACT0006)
    network.add_cell(CON0012)
    network.add_cell(ACT0014)
    network.add_cell(CON0016)
    network.add_cell(CON0021)
    network.add_cell(CON0023)
    network.add_cell(PAR0025)
    network.add_cell(PAR0027)
    network.add_cell(PAR0031)
    network.add_cell(CON0034)
    network.add_cell(CON0037)
    network.add_cell(PAR0040)
    network.add_cell(ACT0001)
    network.add_cell(ACT0005)
    network.add_cell(CON0013)
    network.add_cell(CON0017)
    network.add_cell(CON0020)
    network.add_cell(PAR0028)
    network.add_cell(ACT0030)
    network.add_cell(PAR0041)
    network.add_cell(CON0044)
    network.add_cell(ACT0003)
    network.add_cell(ACT0008)
    network.add_cell(CON0011)
    network.add_cell(ACT0018)
    network.add_cell(CON0022)
    network.add_cell(CON0026)
    network.add_cell(CON0032)
    network.add_cell(CON0035)
    network.add_cell(ACT0042)
    network.add_cell(ACT0045)
    network.add_cell(CON0007)
    network.add_cell(CON0010)
    network.add_cell(ACT0019)
    network.add_cell(PAR0029)
    network.add_cell(CON0036)
    network.add_cell(ACT0043)
    network.add_cell(ACT0009)
    network.add_cell(ACT0024)
    network.add_cell(ACT0038)
    network.add_cell(ACT0015)
    network.add_cell(ACT0039)
    network.add_cell(ACT0033)
    owner["IGNLTree_homming"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__homming')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_homming")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
