# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionApplyForce()
    CON0001 = nodes.ConditionCollision()
    ACT0000.local = True
    ACT0000.condition = CON0001
    ACT0000.game_object = "NLO:CharacterController"
    ACT0000.force = mathutils.Vector((0.0, 0.0, 4000.0))
    CON0001.game_object = "NLO:springSensor"
    CON0001.use_mat = False
    CON0001.prop = "player"
    CON0001.material = None
    CON0001.pulse = False
    network.add_cell(CON0001)
    network.add_cell(ACT0000)
    owner["IGNLTree_objects"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__objects')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_objects")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
