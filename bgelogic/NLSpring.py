# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionSetCharacterVelocity()
    ACT0001 = nodes.ActionApplyForce()
    CON0002 = nodes.ConditionCollision()
    ACT0000.local = True
    ACT0000.condition = CON0002
    ACT0000.game_object = "NLO:CharacterController"
    ACT0000.vel = mathutils.Vector((0.0, 0.0, 0.0))
    ACT0000.time = 0.0
    ACT0001.local = False
    ACT0001.condition = CON0002
    ACT0001.game_object = "NLO:CharacterController"
    ACT0001.force = mathutils.Vector((0.0, 0.0, 4000.0))
    CON0002.game_object = "NLO:springSensor"
    CON0002.use_mat = False
    CON0002.prop = "player"
    CON0002.material = None
    CON0002.pulse = False
    network.add_cell(CON0002)
    network.add_cell(ACT0000)
    network.add_cell(ACT0001)
    owner["IGNLTree_Spring"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__Spring')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_Spring")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
