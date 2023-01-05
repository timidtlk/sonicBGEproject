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
    ACT0007 = nodes.ActionRotateTo()
    PAR0008 = nodes.ParameterObjectAttribute()
    CON0009 = nodes.ConditionNot()
    ACT0010 = nodes.ActionSetGameObjectGameProperty()
    ACT0011 = nodes.ActionSetGameObjectGameProperty()
    CON0012 = nodes.ConditionAndList()
    CON0013 = nodes.ConditionAnd()
    ACT0014 = nodes.ActionSetGameObjectGameProperty()
    ACT0015 = nodes.ActionSetGameObjectGameProperty()
    PAR0016 = nodes.ParameterObjectAttribute()
    CON0017 = nodes.ConditionOr()
    CON0018 = nodes.ConditionCollision()
    CON0019 = nodes.ObjectPropertyOperator()
    CON0020 = nodes.ConditionKeyPressed()
    CON0021 = nodes.ConditionGamepadButtons()
    CON0022 = nodes.ObjectPropertyOperator()
    CON0023 = nodes.ConditionDistanceCheck()
    CON0024 = nodes.ObjectPropertyOperator()
    CON0025 = nodes.ObjectPropertyOperator()
    PAR0000.game_object = "NLO:springSensor"
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
    ACT0007.condition = CON0002
    ACT0007.moving_object = "NLO:CharacterController"
    ACT0007.target_point = PAR0000
    ACT0007.speed = 0.0
    ACT0007.rot_axis = 0
    ACT0007.front_axis = 4
    PAR0008.game_object = "NLO:CharacterController"
    PAR0008.attribute_name = "worldPosition"
    CON0009.condition = CON0023
    ACT0010.condition = CON0023
    ACT0010.game_object = "NLO:CharacterController"
    ACT0010.property_name = "isHommiable"
    ACT0010.property_value = True
    ACT0011.condition = CON0009
    ACT0011.game_object = "NLO:CharacterController"
    ACT0011.property_name = "isHommiable"
    ACT0011.property_value = False
    CON0012.ca = CON0024
    CON0012.cb = CON0019
    CON0012.cc = CON0017
    CON0012.cd = CON0025
    CON0012.ce = True
    CON0012.cf = True
    CON0013.condition_a = CON0022
    CON0013.condition_b = CON0018
    ACT0014.condition = CON0012
    ACT0014.game_object = "NLO:CharacterController"
    ACT0014.property_name = "homming"
    ACT0014.property_value = True
    ACT0015.condition = CON0013
    ACT0015.game_object = "NLO:CharacterController"
    ACT0015.property_name = "homming"
    ACT0015.property_value = False
    PAR0016.game_object = "NLO:springSensor"
    PAR0016.attribute_name = "worldPosition"
    CON0017.condition_a = CON0020
    CON0017.condition_b = CON0021.BUTTON
    CON0018.game_object = "NLO:springSensor"
    CON0018.use_mat = False
    CON0018.prop = "player"
    CON0018.material = None
    CON0018.pulse = False
    CON0019.game_object = "NLO:CharacterController"
    CON0019.property_name = "isHommiable"
    CON0019.compare_value = True
    CON0019.operator = 0
    CON0020.key_code = bge.events.SPACEKEY
    CON0020.pulse = False
    CON0021.index = 0
    CON0021.pulse = False
    CON0021.button = 0
    CON0022.game_object = "NLO:CharacterController"
    CON0022.property_name = "homming"
    CON0022.compare_value = True
    CON0022.operator = 0
    CON0023.operator = 5
    CON0023.param_a = PAR0008
    CON0023.param_b = PAR0016
    CON0023.dist = 25.0
    CON0023.hyst = None
    CON0024.game_object = "NLO:CharacterController"
    CON0024.property_name = "jump"
    CON0024.compare_value = 3
    CON0024.operator = 0
    CON0025.game_object = "NLO:CharacterController"
    CON0025.property_name = "isJumping"
    CON0025.compare_value = True
    CON0025.operator = 0
    network.add_cell(PAR0000)
    network.add_cell(CON0002)
    network.add_cell(CON0004)
    network.add_cell(ACT0006)
    network.add_cell(PAR0008)
    network.add_cell(PAR0016)
    network.add_cell(CON0018)
    network.add_cell(CON0020)
    network.add_cell(CON0022)
    network.add_cell(CON0024)
    network.add_cell(ACT0001)
    network.add_cell(ACT0005)
    network.add_cell(CON0013)
    network.add_cell(ACT0015)
    network.add_cell(CON0019)
    network.add_cell(CON0023)
    network.add_cell(ACT0003)
    network.add_cell(CON0009)
    network.add_cell(ACT0011)
    network.add_cell(CON0021)
    network.add_cell(ACT0007)
    network.add_cell(CON0017)
    network.add_cell(ACT0010)
    network.add_cell(CON0025)
    network.add_cell(CON0012)
    network.add_cell(ACT0014)
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
