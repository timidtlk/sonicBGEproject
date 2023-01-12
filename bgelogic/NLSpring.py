# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionSetGameObjectGameProperty()
    ACT0001 = nodes.ActionApplyForce()
    PAR0002 = nodes.ParameterObjectAttribute()
    PAR0003 = nodes.ParameterArithmeticOp()
    PAR0004 = nodes.ParameterObjectProperty()
    PAR0005 = nodes.ParameterVector3Split()
    ACT0006 = nodes.ActionSetGameObjectGameProperty()
    ACT0007 = nodes.ActionTimeFilter()
    CON0008 = nodes.ConditionOnUpdate()
    ACT0009 = nodes.ActionSetGameObjectGameProperty()
    CON0010 = nodes.ConditionAndList()
    ACT0011 = nodes.ActionSetGameObjectGameProperty()
    CON0012 = nodes.ObjectPropertyOperator()
    CON0013 = nodes.ConditionCollision()
    PAR0014 = nodes.ParameterVector3Simple()
    PAR0015 = nodes.ParameterObjectProperty()
    PAR0016 = nodes.ParameterObjectProperty()
    PAR0017 = nodes.ParameterObjectProperty()
    CON0018 = nodes.ObjectPropertyOperator()
    CON0019 = nodes.ObjectPropertyOperator()
    ACT0020 = nodes.ActionSetGameObjectGameProperty()
    ACT0021 = nodes.ActionSetGameObjectGameProperty()
    ACT0022 = nodes.ActionSetGameObjectGameProperty()
    ACT0023 = nodes.ActionSetObjectAttribute()
    ACT0024 = nodes.ActionStartSound()
    ACT0000.condition = CON0013
    ACT0000.game_object = "NLO:CharacterController"
    ACT0000.property_name = "time_springing"
    ACT0000.property_value = 0.0
    ACT0001.local = False
    ACT0001.condition = CON0013
    ACT0001.game_object = "NLO:CharacterController"
    ACT0001.force = PAR0014.OUTV
    PAR0002.game_object = "NLO:CharacterController"
    PAR0002.attribute_name = "worldPosition"
    PAR0003.operator = nodes.ParameterArithmeticOp.op_by_code("SUB")
    PAR0003.operand_a = PAR0005.OUTZ
    PAR0003.operand_b = PAR0004
    PAR0004.game_object = "NLO:CharacterController"
    PAR0004.property_name = "temp_velocity"
    PAR0005.input_v = PAR0002
    ACT0006.condition = ACT0007
    ACT0006.game_object = "NLO:CharacterController"
    ACT0006.property_name = "temp_velocity"
    ACT0006.property_value = PAR0005.OUTZ
    ACT0007.condition = CON0008
    ACT0007.delay = 0.5
    ACT0009.condition = CON0008
    ACT0009.game_object = "NLO:CharacterController"
    ACT0009.property_name = "velocity"
    ACT0009.property_value = PAR0003
    CON0010.ca = CON0018
    CON0010.cb = CON0012
    CON0010.cc = CON0019
    CON0010.cd = True
    CON0010.ce = True
    CON0010.cf = True
    ACT0011.condition = CON0010
    ACT0011.game_object = "NLO:CharacterController"
    ACT0011.property_name = "isSpringing"
    ACT0011.property_value = False
    CON0012.game_object = "NLO:CharacterController"
    CON0012.property_name = "isSpringing"
    CON0012.compare_value = True
    CON0012.operator = 0
    CON0013.game_object = "NLO:U_O"
    CON0013.use_mat = False
    CON0013.prop = "player"
    CON0013.material = None
    CON0013.pulse = False
    PAR0014.input_x = PAR0015
    PAR0014.input_y = PAR0016
    PAR0014.input_z = PAR0017
    PAR0015.game_object = "NLO:U_O"
    PAR0015.property_name = "x_loc"
    PAR0016.game_object = "NLO:U_O"
    PAR0016.property_name = "y_loc"
    PAR0017.game_object = "NLO:U_O"
    PAR0017.property_name = "z_loc"
    CON0018.game_object = "NLO:CharacterController"
    CON0018.property_name = "velocity"
    CON0018.compare_value = -0.10000000149011612
    CON0018.operator = 5
    CON0019.game_object = "NLO:CharacterController"
    CON0019.property_name = "time_springing"
    CON0019.compare_value = 0.5
    CON0019.operator = 4
    ACT0020.condition = CON0013
    ACT0020.game_object = "NLO:CharacterController"
    ACT0020.property_name = "isSpringing"
    ACT0020.property_value = True
    ACT0021.condition = CON0013
    ACT0021.game_object = "NLO:CharacterController"
    ACT0021.property_name = "isStomping"
    ACT0021.property_value = False
    ACT0022.condition = CON0013
    ACT0022.game_object = "NLO:CharacterController"
    ACT0022.property_name = "Speed"
    ACT0022.property_value = 0.0
    ACT0023.condition = CON0013
    ACT0023.xyz = {'x': True, 'y': True, 'z': True}
    ACT0023.game_object = "NLO:CharacterController"
    ACT0023.attribute_value = mathutils.Vector((0.0, 0.0, 0.0))
    ACT0023.value_type = 'localLinearVelocity'
    ACT0024.condition = CON0013
    ACT0024.sound = "D:/Sonic BGE Project/sounds/Object Sounds/Day Stages/00_common/0007_objsn_spring.wav"
    ACT0024.loop_count = 0
    ACT0024.pitch = 1.0
    ACT0024.volume = 0.05000000074505806
    network.add_cell(PAR0002)
    network.add_cell(PAR0004)
    network.add_cell(CON0008)
    network.add_cell(CON0012)
    network.add_cell(PAR0015)
    network.add_cell(PAR0017)
    network.add_cell(CON0019)
    network.add_cell(PAR0005)
    network.add_cell(ACT0007)
    network.add_cell(CON0013)
    network.add_cell(PAR0016)
    network.add_cell(ACT0020)
    network.add_cell(ACT0022)
    network.add_cell(ACT0024)
    network.add_cell(ACT0000)
    network.add_cell(PAR0003)
    network.add_cell(ACT0009)
    network.add_cell(PAR0014)
    network.add_cell(ACT0021)
    network.add_cell(ACT0001)
    network.add_cell(CON0018)
    network.add_cell(ACT0006)
    network.add_cell(ACT0023)
    network.add_cell(CON0010)
    network.add_cell(ACT0011)
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
