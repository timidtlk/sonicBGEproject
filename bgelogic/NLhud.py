# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionSetMaterialNodeValue()
    CON0001 = nodes.ConditionOnUpdate()
    PAR0002 = nodes.ParameterObjectProperty()
    PAR0003 = nodes.ParameterVector3Simple()
    ACT0004 = nodes.ActionSetMaterialNodeValue()
    ACT0005 = nodes.ActionAddToGameObjectGameProperty()
    CON0006 = nodes.ConditionOnUpdate()
    ACT0007 = nodes.ActionAddToGameObjectGameProperty()
    PAR0008 = nodes.ParameterVector3Simple()
    ACT0000.condition = CON0001
    ACT0000.mat_name = "cmn_metal_ms_dashbelt_dif"
    ACT0000.node_name = "Mapping"
    ACT0000.input_slot = 0
    ACT0000.value = PAR0003.OUTV
    PAR0002.game_object = "NLO:rdmobj01_rdmobj01.005"
    PAR0002.property_name = "Property"
    PAR0003.input_x = 0.0
    PAR0003.input_y = PAR0002
    PAR0003.input_z = 0.0
    ACT0004.condition = CON0006
    ACT0004.mat_name = "2"
    ACT0004.node_name = "Mapping"
    ACT0004.input_slot = 0
    ACT0004.value = PAR0008.OUTV
    ACT0005.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("ADD")
    ACT0005.condition = CON0001
    ACT0005.game_object = "NLO:rdmobj01_rdmobj01.005"
    ACT0005.property_name = "Property"
    ACT0005.property_value = 0.10000000149011612
    ACT0007.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("ADD")
    ACT0007.condition = CON0006
    ACT0007.game_object = "NLO:eff_mod_boost_1"
    ACT0007.property_name = "prop"
    ACT0007.property_value = 0.029999999329447746
    PAR0008.input_x = 0.0
    PAR0008.input_y = 0.0
    PAR0008.input_z = 0.0
    network.add_cell(CON0001)
    network.add_cell(ACT0005)
    network.add_cell(PAR0008)
    network.add_cell(PAR0002)
    network.add_cell(CON0006)
    network.add_cell(PAR0003)
    network.add_cell(ACT0007)
    network.add_cell(ACT0000)
    network.add_cell(ACT0004)
    owner["IGNLTree_hud"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__hud')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_hud")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
