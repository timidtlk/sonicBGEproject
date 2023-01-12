# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    PAR0000 = nodes.ParameterObjectAttribute()
    ACT0001 = nodes.ActionSetGameObjectGameProperty()
    ACT0002 = nodes.ActionApplyForce()
    CON0003 = nodes.ConditionCollision()
    ACT0004 = nodes.ActionSetObjectAttribute()
    ACT0005 = nodes.ActionStartSound()
    ACT0006 = nodes.ActionSetObjectAttribute()
    PAR0000.game_object = "NLO:U_O"
    PAR0000.attribute_name = "worldOrientation"
    ACT0001.condition = CON0003
    ACT0001.game_object = "NLO:CharacterController"
    ACT0001.property_name = "Speed"
    ACT0001.property_value = 1.0299999713897705
    ACT0002.local = True
    ACT0002.condition = CON0003
    ACT0002.game_object = "NLO:CharacterController"
    ACT0002.force = mathutils.Vector((0.0, 800.0, 0.0))
    CON0003.game_object = "NLO:grounDashSensor"
    CON0003.use_mat = False
    CON0003.prop = "player"
    CON0003.material = None
    CON0003.pulse = True
    ACT0004.condition = CON0003
    ACT0004.xyz = {'x': True, 'y': True, 'z': True}
    ACT0004.game_object = "NLO:CharacterController"
    ACT0004.attribute_value = PAR0000
    ACT0004.value_type = 'worldOrientation'
    ACT0005.condition = None
    ACT0005.sound = "None"
    ACT0005.loop_count = 0
    ACT0005.pitch = 1.0
    ACT0005.volume = 1.0
    ACT0006.condition = CON0003
    ACT0006.xyz = {'x': True, 'y': True, 'z': True}
    ACT0006.game_object = "NLO:cameraController"
    ACT0006.attribute_value = PAR0000
    ACT0006.value_type = 'worldOrientation'
    network.add_cell(PAR0000)
    network.add_cell(CON0003)
    network.add_cell(ACT0005)
    network.add_cell(ACT0001)
    network.add_cell(ACT0004)
    network.add_cell(ACT0002)
    network.add_cell(ACT0006)
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
