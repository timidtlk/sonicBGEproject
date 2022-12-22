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
    ACT0003 = nodes.ActionSetObjectAttribute()
    ACT0004 = nodes.ActionRayPick()
    PAR0005 = nodes.ParameterDistance()
    PAR0006 = nodes.ParameterObjectAttribute()
    PAR0007 = nodes.ParameterObjectAttribute()
    CON0008 = nodes.ConditionNot()
    CON0009 = nodes.ConditionOnUpdate()
    ACT0010 = nodes.ActionTimeFilter()
    CON0011 = nodes.ConditionOnUpdate()
    ACT0012 = nodes.ActionSetObjectAttribute()
    PAR0013 = nodes.ParameterObjectAttribute()
    ACT0014 = nodes.ActionMouseLook()
    CON0015 = nodes.ConditionOnUpdate()
    ACT0000.condition = CON0008
    ACT0000.xyz = {'x': True, 'y': True, 'z': True}
    ACT0000.game_object = "NLO:Camera.003"
    ACT0000.attribute_value = PAR0007
    ACT0000.value_type = 'worldPosition'
    ACT0001.condition = CON0009
    ACT0001.xyz = {'x': True, 'y': True, 'z': True}
    ACT0001.game_object = "NLO:Camera.003"
    ACT0001.attribute_value = PAR0002
    ACT0001.value_type = 'worldOrientation'
    PAR0002.game_object = "NLO:camPos.001"
    PAR0002.attribute_name = "worldOrientation"
    ACT0003.condition = ACT0004
    ACT0003.xyz = {'x': True, 'y': True, 'z': True}
    ACT0003.game_object = "NLO:Camera.003"
    ACT0003.attribute_value = ACT0004.POINT
    ACT0003.value_type = 'worldPosition'
    ACT0004.condition = CON0009
    ACT0004.origin = PAR0006
    ACT0004.destination = PAR0007
    ACT0004.local = False
    ACT0004.property_name = "obstacle"
    ACT0004.xray = False
    ACT0004.custom_dist = True
    ACT0004.distance = PAR0005
    ACT0004.visualize = True
    PAR0005.parama = PAR0006
    PAR0005.paramb = PAR0007
    PAR0006.game_object = "NLO:cameraController.001"
    PAR0006.attribute_name = "worldPosition"
    PAR0007.game_object = "NLO:camPos.001"
    PAR0007.attribute_name = "worldPosition"
    CON0008.condition = ACT0004
    ACT0010.condition = CON0011
    ACT0010.delay = 0.0
    ACT0012.condition = ACT0010
    ACT0012.xyz = {'x': True, 'y': True, 'z': True}
    ACT0012.game_object = "NLO:cameraController.001"
    ACT0012.attribute_value = PAR0013
    ACT0012.value_type = 'worldPosition'
    PAR0013.game_object = "NLO:CharacterController.001"
    PAR0013.attribute_name = "worldPosition"
    ACT0014.axis = 1
    ACT0014.condition = CON0015
    ACT0014.game_object_x = "NLO:cameraController.001"
    ACT0014.game_object_y = "NLO:Vertical.001"
    ACT0014.inverted = {'x': False, 'y': True}
    ACT0014.sensitivity = 1.0
    ACT0014.use_cap_z = False
    ACT0014.cap_z = mathutils.Vector((0.0, 0.0))
    ACT0014.use_cap_y = True
    ACT0014.cap_y = mathutils.Vector((-1.378810167312622, 1.5533430576324463))
    ACT0014.smooth = 0.0
    network.add_cell(PAR0002)
    network.add_cell(PAR0006)
    network.add_cell(CON0009)
    network.add_cell(CON0011)
    network.add_cell(PAR0013)
    network.add_cell(CON0015)
    network.add_cell(ACT0001)
    network.add_cell(PAR0007)
    network.add_cell(ACT0010)
    network.add_cell(ACT0014)
    network.add_cell(PAR0005)
    network.add_cell(ACT0012)
    network.add_cell(ACT0004)
    network.add_cell(ACT0003)
    network.add_cell(CON0008)
    network.add_cell(ACT0000)
    owner["IGNLTree_cameraPosition.001"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__cameraPosition.001')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_cameraPosition.001")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
