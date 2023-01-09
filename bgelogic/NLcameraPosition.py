# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionSetObjectAttribute()
    PAR0001 = nodes.ParameterObjectAttribute()
    PAR0002 = nodes.ParameterObjectAttribute()
    PAR0003 = nodes.ParameterDistance()
    CON0004 = nodes.ConditionOnUpdate()
    CON0005 = nodes.ConditionOnUpdate()
    ACT0006 = nodes.ActionMouseLook()
    ACT0007 = nodes.GamepadLook()
    PAR0008 = nodes.ParameterObjectAttribute()
    ACT0009 = nodes.ActionSetObjectAttribute()
    CON0010 = nodes.ConditionNot()
    CON0011 = nodes.ConditionOnUpdate()
    ACT0012 = nodes.ActionTimeFilter()
    PAR0013 = nodes.ParameterObjectAttribute()
    ACT0014 = nodes.ActionSetGameObjectGameProperty()
    ACT0015 = nodes.ActionApplyRotation()
    ACT0016 = nodes.ActionApplyRotation()
    PAR0017 = nodes.ConditionGamepadSticks()
    CON0018 = nodes.ObjectPropertyOperator()
    CON0019 = nodes.ObjectPropertyOperator()
    ACT0020 = nodes.ActionSetGameObjectGameProperty()
    CON0021 = nodes.ConditionOnUpdate()
    PAR0022 = nodes.ParameterObjectAttribute()
    PAR0023 = nodes.ParameterMatrixToVector()
    PAR0024 = nodes.ParameterVector3Split()
    PAR0025 = nodes.ParameterObjectAttribute()
    PAR0026 = nodes.ParameterMatrixToVector()
    CON0027 = nodes.ObjectPropertyOperator()
    PAR0028 = nodes.ParameterVector3Simple()
    PAR0029 = nodes.ParameterVector3Split()
    ACT0030 = nodes.ActionSetObjectAttribute()
    ACT0031 = nodes.ActionSetObjectAttribute()
    ACT0032 = nodes.ActionSetObjectAttribute()
    ACT0033 = nodes.ActionRayPick()
    ACT0000.condition = CON0021
    ACT0000.xyz = {'x': True, 'y': True, 'z': True}
    ACT0000.game_object = "NLO:Camera"
    ACT0000.attribute_value = PAR0002
    ACT0000.value_type = 'worldOrientation'
    PAR0001.game_object = "NLO:cameraController"
    PAR0001.attribute_name = "worldPosition"
    PAR0002.game_object = "NLO:camPos"
    PAR0002.attribute_name = "worldOrientation"
    PAR0003.parama = PAR0001
    PAR0003.paramb = PAR0008
    ACT0006.axis = 1
    ACT0006.condition = CON0004
    ACT0006.game_object_x = "NLO:cameraController"
    ACT0006.game_object_y = "NLO:Vertical"
    ACT0006.inverted = {'x': False, 'y': True}
    ACT0006.sensitivity = 0.8500000238418579
    ACT0006.use_cap_z = False
    ACT0006.cap_z = mathutils.Vector((0.0, 0.0))
    ACT0006.use_cap_y = True
    ACT0006.cap_y = mathutils.Vector((-1.378810167312622, 1.5533430576324463))
    ACT0006.smooth = 0.0
    ACT0007.condition = CON0005
    ACT0007.main_obj = "NLO:cameraController"
    ACT0007.head_obj = "NLO:Vertical"
    ACT0007.inverted = {'x': True, 'y': False}
    ACT0007.index = 0
    ACT0007.sensitivity = 0.05000000074505806
    ACT0007.exponent = 2.299999952316284
    ACT0007.use_cap_x = False
    ACT0007.cap_x = mathutils.Vector((0.0, 0.0))
    ACT0007.use_cap_y = True
    ACT0007.cap_y = mathutils.Vector((0.0, 0.0))
    ACT0007.threshold = 0.10000000149011612
    ACT0007.axis = 1
    PAR0008.game_object = "NLO:camPos"
    PAR0008.attribute_name = "worldPosition"
    ACT0009.condition = CON0010
    ACT0009.xyz = {'x': True, 'y': True, 'z': True}
    ACT0009.game_object = "NLO:Camera"
    ACT0009.attribute_value = PAR0008
    ACT0009.value_type = 'worldPosition'
    CON0010.condition = ACT0033
    ACT0012.condition = CON0011
    ACT0012.delay = 0.009999999776482582
    PAR0013.game_object = "NLO:CharacterController"
    PAR0013.attribute_name = "worldPosition"
    ACT0014.condition = CON0011
    ACT0014.game_object = "NLO:U_O"
    ACT0014.property_name = "right_axis"
    ACT0014.property_value = PAR0017.Y
    ACT0015.local = True
    ACT0015.condition = CON0018
    ACT0015.game_object = "NLO:Vertical"
    ACT0015.rotation = mathutils.Vector((-0.03490658476948738, 0.0, 0.0))
    ACT0016.local = True
    ACT0016.condition = CON0019
    ACT0016.game_object = "NLO:Vertical"
    ACT0016.rotation = mathutils.Vector((0.03490658476948738, 0.0, 0.0))
    PAR0017.inverted = False
    PAR0017.index = 0
    PAR0017.sensitivity = 1.0
    PAR0017.threshold = 0.5
    PAR0017.axis = 1
    CON0018.game_object = "NLO:U_O"
    CON0018.property_name = "right_axis"
    CON0018.compare_value = 0.10000000149011612
    CON0018.operator = 2
    CON0019.game_object = "NLO:U_O"
    CON0019.property_name = "right_axis"
    CON0019.compare_value = -0.10000000149011612
    CON0019.operator = 3
    ACT0020.condition = CON0021
    ACT0020.game_object = "NLO:U_O"
    ACT0020.property_name = "limit_x "
    ACT0020.property_value = PAR0024.OUTX
    PAR0022.game_object = "NLO:Vertical"
    PAR0022.attribute_name = "localOrientation"
    PAR0023.input_m = PAR0022
    PAR0024.input_v = PAR0023.OUT
    PAR0025.game_object = "NLO:Vertical"
    PAR0025.attribute_name = "localOrientation"
    PAR0026.input_m = PAR0025
    CON0027.game_object = "NLO:cameraController"
    CON0027.property_name = "limit_x "
    CON0027.compare_value = 1.3788100481033325
    CON0027.operator = 2
    PAR0028.input_x = 1.3788100481033325
    PAR0028.input_y = PAR0029.OUTY
    PAR0028.input_z = PAR0029.OUTZ
    PAR0029.input_v = PAR0026.OUT
    ACT0030.condition = ACT0012
    ACT0030.xyz = {'x': True, 'y': True, 'z': True}
    ACT0030.game_object = "NLO:cameraController"
    ACT0030.attribute_value = PAR0013
    ACT0030.value_type = 'worldPosition'
    ACT0031.condition = CON0027
    ACT0031.xyz = {'x': True, 'y': False, 'z': False}
    ACT0031.game_object = "NLO:Vertical"
    ACT0031.attribute_value = PAR0028.OUTV
    ACT0031.value_type = 'localOrientation'
    ACT0032.condition = ACT0033
    ACT0032.xyz = {'x': True, 'y': True, 'z': True}
    ACT0032.game_object = "NLO:Camera"
    ACT0032.attribute_value = ACT0033.POINT
    ACT0032.value_type = 'worldPosition'
    ACT0033.condition = CON0021
    ACT0033.origin = PAR0001
    ACT0033.destination = PAR0008
    ACT0033.local = False
    ACT0033.property_name = "obstacle"
    ACT0033.xray = False
    ACT0033.custom_dist = True
    ACT0033.distance = PAR0003
    ACT0033.visualize = False
    network.add_cell(PAR0001)
    network.add_cell(CON0004)
    network.add_cell(ACT0006)
    network.add_cell(PAR0008)
    network.add_cell(CON0011)
    network.add_cell(PAR0013)
    network.add_cell(PAR0017)
    network.add_cell(CON0019)
    network.add_cell(CON0021)
    network.add_cell(PAR0025)
    network.add_cell(CON0027)
    network.add_cell(PAR0002)
    network.add_cell(CON0005)
    network.add_cell(ACT0012)
    network.add_cell(ACT0016)
    network.add_cell(PAR0022)
    network.add_cell(PAR0026)
    network.add_cell(PAR0029)
    network.add_cell(ACT0000)
    network.add_cell(ACT0007)
    network.add_cell(ACT0014)
    network.add_cell(CON0018)
    network.add_cell(PAR0023)
    network.add_cell(PAR0028)
    network.add_cell(ACT0031)
    network.add_cell(PAR0003)
    network.add_cell(ACT0015)
    network.add_cell(PAR0024)
    network.add_cell(ACT0033)
    network.add_cell(CON0010)
    network.add_cell(ACT0030)
    network.add_cell(ACT0009)
    network.add_cell(ACT0032)
    network.add_cell(ACT0020)
    owner["IGNLTree_cameraPosition"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__cameraPosition')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_cameraPosition")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
