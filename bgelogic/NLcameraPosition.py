# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionSetObjectAttribute()
    ACT0001 = nodes.ActionSetObjectAttribute()
    PAR0002 = nodes.ParameterObjectAttribute()
    CON0003 = nodes.ConditionNot()
    CON0004 = nodes.ConditionOnUpdate()
    CON0005 = nodes.ConditionOnUpdate()
    ACT0006 = nodes.ActionSetObjectAttribute()
    PAR0007 = nodes.ParameterObjectAttribute()
    CON0008 = nodes.ConditionOnUpdate()
    ACT0009 = nodes.ActionRayPick()
    ACT0010 = nodes.ActionTimeFilter()
    ACT0011 = nodes.ActionSetObjectAttribute()
    PAR0012 = nodes.ParameterObjectAttribute()
    PAR0013 = nodes.ParameterObjectAttribute()
    PAR0014 = nodes.ParameterDistance()
    ACT0015 = nodes.ActionMouseLook()
    ACT0000.condition = CON0004
    ACT0000.xyz = {'x': True, 'y': True, 'z': True}
    ACT0000.game_object = "NLO:Camera"
    ACT0000.attribute_value = PAR0013
    ACT0000.value_type = 'worldOrientation'
    ACT0001.condition = ACT0009
    ACT0001.xyz = {'x': True, 'y': True, 'z': True}
    ACT0001.game_object = "NLO:Camera"
    ACT0001.attribute_value = ACT0009.POINT
    ACT0001.value_type = 'worldPosition'
    PAR0002.game_object = "NLO:cameraController"
    PAR0002.attribute_name = "worldPosition"
    CON0003.condition = ACT0009
    ACT0006.condition = ACT0010
    ACT0006.xyz = {'x': True, 'y': True, 'z': True}
    ACT0006.game_object = "NLO:cameraController"
    ACT0006.attribute_value = PAR0007
    ACT0006.value_type = 'worldPosition'
    PAR0007.game_object = "NLO:CharacterController"
    PAR0007.attribute_name = "worldPosition"
    ACT0009.condition = CON0004
    ACT0009.origin = PAR0002
    ACT0009.destination = PAR0012
    ACT0009.local = False
    ACT0009.property_name = "obstacle"
    ACT0009.xray = False
    ACT0009.custom_dist = True
    ACT0009.distance = PAR0014
    ACT0009.visualize = False
    ACT0010.condition = CON0005
    ACT0010.delay = 0.0
    ACT0011.condition = CON0003
    ACT0011.xyz = {'x': True, 'y': True, 'z': True}
    ACT0011.game_object = "NLO:Camera"
    ACT0011.attribute_value = PAR0012
    ACT0011.value_type = 'worldPosition'
    PAR0012.game_object = "NLO:camPos"
    PAR0012.attribute_name = "worldPosition"
    PAR0013.game_object = "NLO:camPos"
    PAR0013.attribute_name = "worldOrientation"
    PAR0014.parama = PAR0002
    PAR0014.paramb = PAR0012
    ACT0015.axis = 1
    ACT0015.condition = CON0008
    ACT0015.game_object_x = "NLO:cameraController"
    ACT0015.game_object_y = "NLO:Vertical"
    ACT0015.inverted = {'x': False, 'y': True}
    ACT0015.sensitivity = 1.0
    ACT0015.use_cap_z = False
    ACT0015.cap_z = mathutils.Vector((0.0, 0.0))
    ACT0015.use_cap_y = True
    ACT0015.cap_y = mathutils.Vector((-1.378810167312622, 1.5533430576324463))
    ACT0015.smooth = 0.0
    network.add_cell(PAR0002)
    network.add_cell(CON0004)
    network.add_cell(PAR0007)
    network.add_cell(PAR0012)
    network.add_cell(PAR0014)
    network.add_cell(CON0005)
    network.add_cell(CON0008)
    network.add_cell(ACT0010)
    network.add_cell(PAR0013)
    network.add_cell(ACT0000)
    network.add_cell(ACT0006)
    network.add_cell(ACT0015)
    network.add_cell(ACT0009)
    network.add_cell(ACT0001)
    network.add_cell(CON0003)
    network.add_cell(ACT0011)
    owner["IGNLTree_cameraPosition"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__cameraPosition')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_cameraPosition")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
