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
    PAR0004 = nodes.ParameterObjectAttribute()
    ACT0005 = nodes.ActionSetObjectAttribute()
    CON0006 = nodes.ConditionNot()
    CON0007 = nodes.ConditionOnUpdate()
    ACT0008 = nodes.ActionTimeFilter()
    PAR0009 = nodes.ParameterObjectAttribute()
    ACT0010 = nodes.ActionSetGameObjectGameProperty()
    ACT0011 = nodes.ActionApplyRotation()
    ACT0012 = nodes.ActionApplyRotation()
    PAR0013 = nodes.ConditionGamepadSticks()
    CON0014 = nodes.ObjectPropertyOperator()
    CON0015 = nodes.ObjectPropertyOperator()
    ACT0016 = nodes.ActionSetGameObjectGameProperty()
    CON0017 = nodes.ConditionOnUpdate()
    PAR0018 = nodes.ParameterObjectAttribute()
    PAR0019 = nodes.ParameterMatrixToVector()
    PAR0020 = nodes.ParameterVector3Split()
    PAR0021 = nodes.ParameterObjectAttribute()
    PAR0022 = nodes.ParameterMatrixToVector()
    CON0023 = nodes.ObjectPropertyOperator()
    PAR0024 = nodes.ParameterVector3Simple()
    PAR0025 = nodes.ParameterVector3Split()
    ACT0026 = nodes.ActionSetObjectAttribute()
    ACT0027 = nodes.ActionSetObjectAttribute()
    ACT0028 = nodes.ActionSetObjectAttribute()
    ACT0029 = nodes.ActionRayPick()
    CON0030 = nodes.ConditionOnUpdate()
    CON0031 = nodes.ConditionOnUpdate()
    CON0032 = nodes.ConditionOnUpdate()
    ACT0033 = nodes.ActionMouseLook()
    ACT0034 = nodes.GamepadLook()
    ACT0000.condition = CON0017
    ACT0000.xyz = {'x': True, 'y': True, 'z': True}
    ACT0000.game_object = "NLO:Camera"
    ACT0000.attribute_value = PAR0002
    ACT0000.value_type = 'worldOrientation'
    PAR0001.game_object = "NLO:cameraController"
    PAR0001.attribute_name = "worldPosition"
    PAR0002.game_object = "NLO:camPos"
    PAR0002.attribute_name = "worldOrientation"
    PAR0003.parama = PAR0001
    PAR0003.paramb = PAR0004
    PAR0004.game_object = "NLO:camPos"
    PAR0004.attribute_name = "worldPosition"
    ACT0005.condition = CON0006
    ACT0005.xyz = {'x': True, 'y': True, 'z': True}
    ACT0005.game_object = "NLO:Camera"
    ACT0005.attribute_value = PAR0004
    ACT0005.value_type = 'worldPosition'
    CON0006.condition = ACT0029
    ACT0008.condition = CON0007
    ACT0008.delay = 0.009999999776482582
    PAR0009.game_object = "NLO:CharacterController"
    PAR0009.attribute_name = "worldPosition"
    ACT0010.condition = CON0007
    ACT0010.game_object = "NLO:U_O"
    ACT0010.property_name = "right_axis"
    ACT0010.property_value = PAR0013.Y
    ACT0011.local = True
    ACT0011.condition = CON0014
    ACT0011.game_object = "NLO:Vertical"
    ACT0011.rotation = mathutils.Vector((-0.03490658476948738, 0.0, 0.0))
    ACT0012.local = True
    ACT0012.condition = CON0015
    ACT0012.game_object = "NLO:Vertical"
    ACT0012.rotation = mathutils.Vector((0.03490658476948738, 0.0, 0.0))
    PAR0013.inverted = False
    PAR0013.index = 0
    PAR0013.sensitivity = 1.0
    PAR0013.threshold = 0.5
    PAR0013.axis = 1
    CON0014.game_object = "NLO:U_O"
    CON0014.property_name = "right_axis"
    CON0014.compare_value = 0.10000000149011612
    CON0014.operator = 2
    CON0015.game_object = "NLO:U_O"
    CON0015.property_name = "right_axis"
    CON0015.compare_value = -0.10000000149011612
    CON0015.operator = 3
    ACT0016.condition = CON0017
    ACT0016.game_object = "NLO:U_O"
    ACT0016.property_name = "limit_x "
    ACT0016.property_value = PAR0020.OUTX
    PAR0018.game_object = "NLO:Vertical"
    PAR0018.attribute_name = "localOrientation"
    PAR0019.input_m = PAR0018
    PAR0020.input_v = PAR0019.OUT
    PAR0021.game_object = "NLO:Vertical"
    PAR0021.attribute_name = "localOrientation"
    PAR0022.input_m = PAR0021
    CON0023.game_object = "NLO:cameraController"
    CON0023.property_name = "limit_x "
    CON0023.compare_value = 1.3788100481033325
    CON0023.operator = 2
    PAR0024.input_x = 1.3788100481033325
    PAR0024.input_y = PAR0025.OUTY
    PAR0024.input_z = PAR0025.OUTZ
    PAR0025.input_v = PAR0022.OUT
    ACT0026.condition = ACT0008
    ACT0026.xyz = {'x': True, 'y': True, 'z': True}
    ACT0026.game_object = "NLO:cameraController"
    ACT0026.attribute_value = PAR0009
    ACT0026.value_type = 'worldPosition'
    ACT0027.condition = CON0023
    ACT0027.xyz = {'x': True, 'y': False, 'z': False}
    ACT0027.game_object = "NLO:Vertical"
    ACT0027.attribute_value = PAR0024.OUTV
    ACT0027.value_type = 'localOrientation'
    ACT0028.condition = ACT0029
    ACT0028.xyz = {'x': True, 'y': True, 'z': True}
    ACT0028.game_object = "NLO:Camera"
    ACT0028.attribute_value = ACT0029.POINT
    ACT0028.value_type = 'worldPosition'
    ACT0029.condition = CON0017
    ACT0029.origin = PAR0001
    ACT0029.destination = PAR0004
    ACT0029.local = False
    ACT0029.property_name = "obstacle"
    ACT0029.xray = False
    ACT0029.custom_dist = True
    ACT0029.distance = PAR0003
    ACT0029.visualize = False
    ACT0033.axis = 1
    ACT0033.condition = CON0031
    ACT0033.game_object_x = "NLO:cameraController"
    ACT0033.game_object_y = "NLO:Vertical"
    ACT0033.inverted = {'x': False, 'y': True}
    ACT0033.sensitivity = 0.8500000238418579
    ACT0033.use_cap_z = False
    ACT0033.cap_z = mathutils.Vector((0.0, 0.0))
    ACT0033.use_cap_y = True
    ACT0033.cap_y = mathutils.Vector((-1.378810167312622, 1.5533430576324463))
    ACT0033.smooth = 0.0
    ACT0034.condition = CON0032
    ACT0034.main_obj = "NLO:cameraController"
    ACT0034.head_obj = "NLO:Vertical"
    ACT0034.inverted = {'x': True, 'y': False}
    ACT0034.index = 0
    ACT0034.sensitivity = 0.05000000074505806
    ACT0034.exponent = 2.299999952316284
    ACT0034.use_cap_x = False
    ACT0034.cap_x = mathutils.Vector((0.0, 0.0))
    ACT0034.use_cap_y = True
    ACT0034.cap_y = mathutils.Vector((0.0, 0.0))
    ACT0034.threshold = 0.10000000149011612
    ACT0034.axis = 1
    network.add_cell(PAR0001)
    network.add_cell(PAR0004)
    network.add_cell(CON0007)
    network.add_cell(PAR0009)
    network.add_cell(PAR0013)
    network.add_cell(CON0015)
    network.add_cell(CON0017)
    network.add_cell(PAR0021)
    network.add_cell(CON0023)
    network.add_cell(CON0030)
    network.add_cell(CON0032)
    network.add_cell(ACT0034)
    network.add_cell(PAR0002)
    network.add_cell(ACT0008)
    network.add_cell(ACT0012)
    network.add_cell(PAR0018)
    network.add_cell(PAR0022)
    network.add_cell(PAR0025)
    network.add_cell(CON0031)
    network.add_cell(ACT0000)
    network.add_cell(ACT0010)
    network.add_cell(CON0014)
    network.add_cell(PAR0019)
    network.add_cell(PAR0024)
    network.add_cell(ACT0027)
    network.add_cell(ACT0033)
    network.add_cell(PAR0003)
    network.add_cell(ACT0011)
    network.add_cell(PAR0020)
    network.add_cell(ACT0029)
    network.add_cell(CON0006)
    network.add_cell(ACT0026)
    network.add_cell(ACT0005)
    network.add_cell(ACT0028)
    network.add_cell(ACT0016)
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
