# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionSetGameObjectGameProperty()
    ACT0001 = nodes.ActionSetGameObjectGameProperty()
    CON0002 = nodes.ConditionOnUpdate()
    PAR0003 = nodes.ParameterObjectProperty()
    ACT0000.condition = CON0002
    ACT0000.game_object = "NLO:ringsOutside"
    ACT0000.property_name = "Text"
    ACT0000.property_value = PAR0003
    ACT0001.condition = CON0002
    ACT0001.game_object = "NLO:ringsInside"
    ACT0001.property_name = "Text"
    ACT0001.property_value = PAR0003
    PAR0003.game_object = "NLO:CharacterController"
    PAR0003.property_name = "ringsQtd"
    network.add_cell(CON0002)
    network.add_cell(PAR0003)
    network.add_cell(ACT0000)
    network.add_cell(ACT0001)
    owner["IGNLTree_ringCount"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__ringCount')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_ringCount")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
