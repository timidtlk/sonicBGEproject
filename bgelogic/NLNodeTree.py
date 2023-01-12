# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionAddToGameObjectGameProperty()
    ACT0001 = nodes.ActionSetMaterialNodeValue()
    PAR0002 = nodes.ParameterObjectProperty()
    CON0003 = nodes.ConditionOnUpdate()
    ACT0000.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("SUB")
    ACT0000.condition = CON0003
    ACT0000.game_object = "NLO:U_O"
    ACT0000.property_name = "alpha_homming"
    ACT0000.property_value = 0.019999999552965164
    ACT0001.condition = CON0003
    ACT0001.mat_name = "mat_homming_eff"
    ACT0001.node_name = "Principled BSDF"
    ACT0001.input_slot = 21
    ACT0001.value = PAR0002
    PAR0002.game_object = "NLO:U_O"
    PAR0002.property_name = "alpha_homming"
    network.add_cell(PAR0002)
    network.add_cell(CON0003)
    network.add_cell(ACT0000)
    network.add_cell(ACT0001)
    owner["IGNLTree_NodeTree"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__NodeTree')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_NodeTree")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
