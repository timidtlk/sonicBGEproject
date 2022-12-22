# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    PAR0000 = nodes.ParameterObjectAttribute()
    ACT0001 = nodes.ActionSetObjectAttribute()
    ACT0002 = nodes.ActionSetObjectAttribute()
    ACT0003 = nodes.ActionSetGameObjectGameProperty()
    ACT0004 = nodes.ActionApplyForce()
    CON0005 = nodes.ConditionCollision()
    PAR0000.game_object = "NLO:grounDashSensor"
    PAR0000.attribute_name = "worldOrientation"
    ACT0001.condition = CON0005
    ACT0001.xyz = {'x': True, 'y': True, 'z': True}
    ACT0001.game_object = "NLO:cameraController"
    ACT0001.attribute_value = PAR0000
    ACT0001.value_type = 'worldOrientation'
    ACT0002.condition = CON0005
    ACT0002.xyz = {'x': True, 'y': True, 'z': True}
    ACT0002.game_object = "NLO:CharacterController"
    ACT0002.attribute_value = PAR0000
    ACT0002.value_type = 'worldOrientation'
    ACT0003.condition = CON0005
    ACT0003.game_object = "NLO:CharacterController"
    ACT0003.property_name = "Speed"
    ACT0003.property_value = 1.0299999713897705
    ACT0004.local = True
    ACT0004.condition = CON0005
    ACT0004.game_object = "NLO:CharacterController"
    ACT0004.force = mathutils.Vector((0.0, 500.0, 0.0))
    CON0005.game_object = "NLO:grounDashSensor"
    CON0005.use_mat = False
    CON0005.prop = "player"
    CON0005.material = None
    CON0005.pulse = True
    network.add_cell(PAR0000)
    network.add_cell(CON0005)
    network.add_cell(ACT0001)
    network.add_cell(ACT0003)
    network.add_cell(ACT0002)
    network.add_cell(ACT0004)
    owner["IGNLTree_GroundDashP"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__GroundDashP')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_GroundDashP")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
