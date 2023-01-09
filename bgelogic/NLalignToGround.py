# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    CON0000 = nodes.ConditionOnUpdate()
    ACT0001 = nodes.ActionSetObjectAttribute()
    PAR0002 = nodes.ParameterObjectAttribute()
    PAR0003 = nodes.ParameterObjectAttribute()
    CON0004 = nodes.ConditionNot()
    ACT0005 = nodes.ActionAlignAxisToVector()
    ACT0006 = nodes.ActionRayPick()
    ACT0001.condition = CON0004
    ACT0001.xyz = {'x': True, 'y': True, 'z': False}
    ACT0001.game_object = "NLO:CharacterController"
    ACT0001.attribute_value = mathutils.Vector((0.0, 0.0, 0.0))
    ACT0001.value_type = 'localOrientation'
    PAR0002.game_object = "NLO:CharacterController"
    PAR0002.attribute_name = "worldPosition"
    PAR0003.game_object = "NLO:RayRotate"
    PAR0003.attribute_name = "worldPosition"
    CON0004.condition = ACT0006
    ACT0005.local = True
    ACT0005.condition = ACT0006
    ACT0005.game_object = "NLO:U_O"
    ACT0005.vector = ACT0006.NORMAL
    ACT0005.axis = 2
    ACT0005.factor = 1.0
    ACT0006.condition = CON0000
    ACT0006.origin = PAR0002
    ACT0006.destination = PAR0003
    ACT0006.local = False
    ACT0006.property_name = "adapt"
    ACT0006.xray = False
    ACT0006.custom_dist = False
    ACT0006.distance = 0.0
    ACT0006.visualize = False
    network.add_cell(CON0000)
    network.add_cell(PAR0002)
    network.add_cell(PAR0003)
    network.add_cell(ACT0006)
    network.add_cell(CON0004)
    network.add_cell(ACT0001)
    network.add_cell(ACT0005)
    owner["IGNLTree_alignToGround"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__alignToGround')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_alignToGround")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
