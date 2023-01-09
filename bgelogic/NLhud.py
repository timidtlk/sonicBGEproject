# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionSetMaterialNodeValue()
    CON0001 = nodes.ConditionOnUpdate()
    ACT0002 = nodes.ActionAddToGameObjectGameProperty()
    PAR0003 = nodes.ParameterVector3Simple()
    ACT0004 = nodes.ActionSetMaterialNodeValue()
    CON0005 = nodes.ConditionOnUpdate()
    PAR0006 = nodes.ParameterObjectProperty()
    PAR0007 = nodes.ParameterVector3Simple()
    ACT0008 = nodes.ActionAddToGameObjectGameProperty()
    PAR0009 = nodes.ParameterObjectProperty()
    PAR0010 = nodes.ParameterVector3Simple()
    ACT0011 = nodes.ActionSetMaterialNodeValue()
    ACT0012 = nodes.ActionSetMaterialNodeValue()
    CON0013 = nodes.ConditionOnUpdate()
    ACT0014 = nodes.ActionAddToGameObjectGameProperty()
    ACT0000.condition = CON0001
    ACT0000.mat_name = "2"
    ACT0000.node_name = "Mapping"
    ACT0000.input_slot = 0
    ACT0000.value = PAR0003.OUTV
    ACT0002.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("ADD")
    ACT0002.condition = CON0001
    ACT0002.game_object = "NLO:eff_mod_boost_1"
    ACT0002.property_name = "prop"
    ACT0002.property_value = 0.029999999329447746
    PAR0003.input_x = 0.0
    PAR0003.input_y = 0.0
    PAR0003.input_z = 0.0
    ACT0004.condition = CON0005
    ACT0004.mat_name = "cmn_metal_ms_dashbelt_dif"
    ACT0004.node_name = "Mapping"
    ACT0004.input_slot = 0
    ACT0004.value = PAR0007.OUTV
    PAR0006.game_object = "NLO:rdmobj01_rdmobj01.005"
    PAR0006.property_name = "Property"
    PAR0007.input_x = 0.0
    PAR0007.input_y = PAR0006
    PAR0007.input_z = 0.0
    ACT0008.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("ADD")
    ACT0008.condition = CON0005
    ACT0008.game_object = "NLO:rdmobj01_rdmobj01.005"
    ACT0008.property_name = "Property"
    ACT0008.property_value = 0.10000000149011612
    PAR0009.game_object = "NLO:Water"
    PAR0009.property_name = "water_map"
    PAR0010.input_x = 0.0
    PAR0010.input_y = PAR0009
    PAR0010.input_z = 0.0
    ACT0011.condition = CON0013
    ACT0011.mat_name = "Water"
    ACT0011.node_name = "Mapping"
    ACT0011.input_slot = 1
    ACT0011.value = PAR0010.OUTV
    ACT0012.condition = CON0013
    ACT0012.mat_name = "Water"
    ACT0012.node_name = "Mapping.001"
    ACT0012.input_slot = 1
    ACT0012.value = PAR0010.OUTV
    ACT0014.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("ADD")
    ACT0014.condition = CON0013
    ACT0014.game_object = "NLO:Water"
    ACT0014.property_name = "water_map"
    ACT0014.property_value = 0.0010000000474974513
    network.add_cell(CON0001)
    network.add_cell(PAR0003)
    network.add_cell(CON0005)
    network.add_cell(ACT0008)
    network.add_cell(CON0013)
    network.add_cell(ACT0000)
    network.add_cell(PAR0006)
    network.add_cell(PAR0009)
    network.add_cell(ACT0014)
    network.add_cell(ACT0002)
    network.add_cell(PAR0007)
    network.add_cell(ACT0004)
    network.add_cell(PAR0010)
    network.add_cell(ACT0012)
    network.add_cell(ACT0011)
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
