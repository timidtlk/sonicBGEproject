# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    CON0000 = nodes.ConditionAnd()
    CON0001 = nodes.ConditionAnd()
    CON0002 = nodes.ConditionOrList()
    CON0003 = nodes.ConditionKeyPressed()
    CON0004 = nodes.ConditionKeyPressed()
    CON0005 = nodes.ConditionKeyPressed()
    CON0006 = nodes.ConditionKeyPressed()
    CON0007 = nodes.ConditionOnUpdate()
    PAR0008 = nodes.ParameterObjectProperty()
    ACT0009 = nodes.ActionSetGameObjectGameProperty()
    CON0010 = nodes.ConditionOnUpdate()
    ACT0011 = nodes.ActionSetGameObjectGameProperty()
    PAR0012 = nodes.ParameterObjectProperty()
    PAR0013 = nodes.ParameterObjectProperty()
    CON0014 = nodes.ObjectPropertyOperator()
    PAR0015 = nodes.ParameterObjectProperty()
    CON0016 = nodes.ObjectPropertyOperator()
    ACT0017 = nodes.ActionTimeFilter()
    ACT0018 = nodes.ActionTimeFilter()
    ACT0019 = nodes.ActionAddToGameObjectGameProperty()
    ACT0020 = nodes.ActionAddToGameObjectGameProperty()
    ACT0021 = nodes.ActionAddToGameObjectGameProperty()
    CON0000.condition_a = CON0006
    CON0000.condition_b = CON0003
    CON0001.condition_a = CON0004
    CON0001.condition_b = CON0005
    CON0002.ca = CON0004
    CON0002.cb = CON0005
    CON0002.cc = CON0006
    CON0002.cd = CON0003
    CON0002.ce = CON0001
    CON0002.cf = CON0000
    CON0003.key_code = bge.events.DKEY
    CON0003.pulse = False
    CON0004.key_code = bge.events.WKEY
    CON0004.pulse = False
    CON0005.key_code = bge.events.SKEY
    CON0005.pulse = False
    CON0006.key_code = bge.events.AKEY
    CON0006.pulse = False
    PAR0008.game_object = "NLO:U_O"
    PAR0008.property_name = "value_updown"
    ACT0009.condition = ACT0017
    ACT0009.game_object = "NLO:U_O"
    ACT0009.property_name = "old_ud"
    ACT0009.property_value = PAR0008
    ACT0011.condition = ACT0018
    ACT0011.game_object = "NLO:U_O"
    ACT0011.property_name = "old_lr"
    ACT0011.property_value = PAR0012
    PAR0012.game_object = "NLO:U_O"
    PAR0012.property_name = "value_leftright"
    PAR0013.game_object = "NLO:U_O"
    PAR0013.property_name = "old_ud"
    CON0014.game_object = "NLO:U_O"
    CON0014.property_name = "value_updown"
    CON0014.compare_value = PAR0013
    CON0014.operator = 1
    PAR0015.game_object = "NLO:U_O"
    PAR0015.property_name = "old_lr"
    CON0016.game_object = "NLO:U_O"
    CON0016.property_name = "value_leftright"
    CON0016.compare_value = PAR0015
    CON0016.operator = 1
    ACT0017.condition = CON0007
    ACT0017.delay = 0.009999999776482582
    ACT0018.condition = CON0010
    ACT0018.delay = 0.009999999776482582
    ACT0019.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("SUB")
    ACT0019.condition = CON0014
    ACT0019.game_object = "NLO:CharacterController"
    ACT0019.property_name = "Speed"
    ACT0019.property_value = 0.019999999552965164
    ACT0020.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("SUB")
    ACT0020.condition = CON0016
    ACT0020.game_object = "NLO:CharacterController"
    ACT0020.property_name = "Speed"
    ACT0020.property_value = 0.019999999552965164
    ACT0021.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("SUB")
    ACT0021.condition = CON0002
    ACT0021.game_object = "NLO:CharacterController"
    ACT0021.property_name = "Speed"
    ACT0021.property_value = 0.10000000149011612
    network.add_cell(CON0003)
    network.add_cell(CON0005)
    network.add_cell(CON0007)
    network.add_cell(CON0010)
    network.add_cell(PAR0012)
    network.add_cell(PAR0015)
    network.add_cell(ACT0017)
    network.add_cell(CON0004)
    network.add_cell(PAR0008)
    network.add_cell(PAR0013)
    network.add_cell(CON0016)
    network.add_cell(ACT0020)
    network.add_cell(CON0001)
    network.add_cell(CON0006)
    network.add_cell(CON0014)
    network.add_cell(ACT0019)
    network.add_cell(CON0000)
    network.add_cell(ACT0009)
    network.add_cell(ACT0018)
    network.add_cell(CON0002)
    network.add_cell(ACT0021)
    network.add_cell(ACT0011)
    owner["IGNLTree_decrement_on_rotate"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__decrement_on_rotate')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_decrement_on_rotate")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
