# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionAlignAxisToVector()
    CON0001 = nodes.ConditionNot()
    ACT0002 = nodes.ActionSetObjectAttribute()
    CON0003 = nodes.ConditionOnUpdate()
    PAR0004 = nodes.ParameterObjectAttribute()
    PAR0005 = nodes.ParameterObjectAttribute()
    ACT0006 = nodes.ActionRayPick()
    ACT0000.local = True
    ACT0000.condition = ACT0006
    ACT0000.game_object = "NLO:U_O"
    ACT0000.vector = ACT0006.NORMAL
    ACT0000.axis = 2
    ACT0000.factor = 1.0
    CON0001.condition = ACT0006
    ACT0002.condition = CON0001
    ACT0002.xyz = {'x': True, 'y': True, 'z': False}
    ACT0002.game_object = "NLO:CharacterController"
    ACT0002.attribute_value = mathutils.Vector((0.0, 0.0, 0.0))
    ACT0002.value_type = 'localOrientation'
    PAR0004.game_object = "NLO:CharacterController"
    PAR0004.attribute_name = "worldPosition"
    PAR0005.game_object = "NLO:RayRotate"
    PAR0005.attribute_name = "worldPosition"
    ACT0006.condition = CON0003
    ACT0006.origin = PAR0004
    ACT0006.destination = PAR0005
    ACT0006.local = False
    ACT0006.property_name = "adapt"
    ACT0006.xray = False
    ACT0006.custom_dist = False
    ACT0006.distance = 0.0
    ACT0006.visualize = False
    network.add_cell(CON0003)
    network.add_cell(PAR0005)
    network.add_cell(PAR0004)
    network.add_cell(ACT0006)
    network.add_cell(ACT0000)
    network.add_cell(CON0001)
    network.add_cell(ACT0002)
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
