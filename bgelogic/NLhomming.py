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
    CON0011 = nodes.ConditionAnd()
    ACT0012 = nodes.ActionSetGameObjectGameProperty()
    ACT0013 = nodes.ActionSetGameObjectGameProperty()
    CON0014 = nodes.ConditionOr()
    CON0015 = nodes.ObjectPropertyOperator()
    CON0016 = nodes.ConditionKeyPressed()
    CON0017 = nodes.ConditionGamepadButtons()
    CON0018 = nodes.ObjectPropertyOperator()
    CON0019 = nodes.ConditionDistanceCheck()
    ACT0020 = nodes.ActionRotateTo()
    ACT0021 = nodes.InitEmptyList()
    PAR0022 = nodes.ParameterObjectAttribute()
    PAR0023 = nodes.ParameterDistance()
    PAR0024 = nodes.ParameterObjectAttribute()
    CON0025 = nodes.ConditionCollision()
    CON0026 = nodes.ObjectPropertyOperator()
    CON0027 = nodes.ObjectPropertyOperator()
    PAR0000.game_object = "NLO:U_O"
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
    CON0007.condition = CON0019
    ACT0008.condition = CON0019
    ACT0008.game_object = "NLO:CharacterController"
    ACT0008.property_name = "isHommiable"
    ACT0008.property_value = True
    ACT0009.condition = CON0007
    ACT0009.game_object = "NLO:CharacterController"
    ACT0009.property_name = "isHommiable"
    ACT0009.property_value = False
    CON0010.ca = CON0027
    CON0010.cb = CON0015
    CON0010.cc = CON0014
    CON0010.cd = CON0026
    CON0010.ce = True
    CON0010.cf = True
    CON0011.condition_a = CON0018
    CON0011.condition_b = CON0025
    ACT0012.condition = CON0010
    ACT0012.game_object = "NLO:CharacterController"
    ACT0012.property_name = "homming"
    ACT0012.property_value = True
    ACT0013.condition = CON0011
    ACT0013.game_object = "NLO:CharacterController"
    ACT0013.property_name = "homming"
    ACT0013.property_value = False
    CON0014.condition_a = CON0016
    CON0014.condition_b = CON0017.BUTTON
    CON0015.game_object = "NLO:CharacterController"
    CON0015.property_name = "isHommiable"
    CON0015.compare_value = True
    CON0015.operator = 0
    CON0016.key_code = bge.events.SPACEKEY
    CON0016.pulse = False
    CON0017.index = 0
    CON0017.pulse = False
    CON0017.button = 0
    CON0018.game_object = "NLO:CharacterController"
    CON0018.property_name = "homming"
    CON0018.compare_value = True
    CON0018.operator = 0
    CON0019.operator = 5
    CON0019.param_a = PAR0022
    CON0019.param_b = PAR0024
    CON0019.dist = 25.0
    CON0019.hyst = 4.0
    ACT0020.condition = CON0002
    ACT0020.moving_object = "NLO:CharacterController"
    ACT0020.target_point = PAR0000
    ACT0020.speed = 0.0
    ACT0020.rot_axis = 0
    ACT0020.front_axis = 4
    ACT0021.condition = True
    ACT0021.length = 10
    PAR0022.game_object = "NLO:CharacterController"
    PAR0022.attribute_name = "worldPosition"
    PAR0023.parama = PAR0022
    PAR0023.paramb = PAR0024
    PAR0024.game_object = "NLO:U_O"
    PAR0024.attribute_name = "worldPosition"
    CON0025.game_object = "NLO:U_O"
    CON0025.use_mat = False
    CON0025.prop = "player"
    CON0025.material = None
    CON0025.pulse = False
    CON0026.game_object = "NLO:CharacterController"
    CON0026.property_name = "isJumping"
    CON0026.compare_value = True
    CON0026.operator = 0
    CON0027.game_object = "NLO:CharacterController"
    CON0027.property_name = "jump"
    CON0027.compare_value = 3
    CON0027.operator = 0
    network.add_cell(PAR0000)
    network.add_cell(CON0002)
    network.add_cell(CON0004)
    network.add_cell(ACT0006)
    network.add_cell(CON0015)
    network.add_cell(CON0017)
    network.add_cell(ACT0020)
    network.add_cell(PAR0022)
    network.add_cell(PAR0024)
    network.add_cell(CON0026)
    network.add_cell(ACT0001)
    network.add_cell(ACT0005)
    network.add_cell(CON0016)
    network.add_cell(CON0019)
    network.add_cell(PAR0023)
    network.add_cell(CON0027)
    network.add_cell(ACT0003)
    network.add_cell(ACT0008)
    network.add_cell(CON0014)
    network.add_cell(ACT0021)
    network.add_cell(CON0007)
    network.add_cell(CON0010)
    network.add_cell(ACT0012)
    network.add_cell(CON0018)
    network.add_cell(ACT0009)
    network.add_cell(CON0025)
    network.add_cell(CON0011)
    network.add_cell(ACT0013)
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
