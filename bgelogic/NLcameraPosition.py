# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionSetObjectAttribute()
    ACT0001 = nodes.ActionSetObjectAttribute()
    PAR0002 = nodes.ParameterObjectAttribute()
    PAR0003 = nodes.ParameterObjectAttribute()
    PAR0004 = nodes.ParameterDistance()
    CON0005 = nodes.ConditionOnUpdate()
    CON0006 = nodes.ConditionOnUpdate()
    ACT0007 = nodes.ActionMouseLook()
    ACT0008 = nodes.GamepadLook()
    PAR0009 = nodes.ParameterObjectAttribute()
    ACT0010 = nodes.ActionSetObjectAttribute()
    ACT0011 = nodes.ActionRayPick()
    CON0012 = nodes.ConditionNot()
    ACT0013 = nodes.ActionSetObjectAttribute()
    CON0014 = nodes.ConditionOnUpdate()
    ACT0015 = nodes.ActionTimeFilter()
    PAR0016 = nodes.ParameterObjectAttribute()
    ACT0017 = nodes.ActionSetGameObjectGameProperty()
    ACT0018 = nodes.ActionApplyRotation()
    ACT0019 = nodes.ActionApplyRotation()
    PAR0020 = nodes.ConditionGamepadSticks()
    CON0021 = nodes.ObjectPropertyOperator()
    CON0022 = nodes.ObjectPropertyOperator()
    ACT0023 = nodes.ActionSetGameObjectGameProperty()
    CON0024 = nodes.ConditionOnUpdate()
    PAR0025 = nodes.ParameterObjectAttribute()
    PAR0026 = nodes.ParameterMatrixToVector()
    PAR0027 = nodes.ParameterVector3Split()
    PAR0028 = nodes.ParameterObjectAttribute()
    PAR0029 = nodes.ParameterMatrixToVector()
    CON0030 = nodes.ObjectPropertyOperator()
    PAR0031 = nodes.ParameterVector3Simple()
    ACT0032 = nodes.ActionSetObjectAttribute()
    PAR0033 = nodes.ParameterVector3Split()
    ACT0000.condition = CON0024
    ACT0000.xyz = {'x': True, 'y': True, 'z': True}
    ACT0000.game_object = "NLO:Camera"
    ACT0000.attribute_value = PAR0003
    ACT0000.value_type = 'worldOrientation'
    ACT0001.condition = ACT0011
    ACT0001.xyz = {'x': True, 'y': True, 'z': True}
    ACT0001.game_object = "NLO:Camera"
    ACT0001.attribute_value = ACT0011.POINT
    ACT0001.value_type = 'worldPosition'
    PAR0002.game_object = "NLO:cameraController"
    PAR0002.attribute_name = "worldPosition"
    PAR0003.game_object = "NLO:camPos"
    PAR0003.attribute_name = "worldOrientation"
    PAR0004.parama = PAR0002
    PAR0004.paramb = PAR0009
    ACT0007.axis = 1
    ACT0007.condition = CON0005
    ACT0007.game_object_x = "NLO:cameraController"
    ACT0007.game_object_y = "NLO:Vertical"
    ACT0007.inverted = {'x': False, 'y': True}
    ACT0007.sensitivity = 0.8500000238418579
    ACT0007.use_cap_z = False
    ACT0007.cap_z = mathutils.Vector((0.0, 0.0))
    ACT0007.use_cap_y = True
    ACT0007.cap_y = mathutils.Vector((-1.378810167312622, 1.5533430576324463))
    ACT0007.smooth = 0.0
    ACT0008.condition = CON0006
    ACT0008.main_obj = "NLO:cameraController"
    ACT0008.head_obj = "NLO:Vertical"
    ACT0008.inverted = {'x': True, 'y': False}
    ACT0008.index = 0
    ACT0008.sensitivity = 0.05000000074505806
    ACT0008.exponent = 2.299999952316284
    ACT0008.use_cap_x = False
    ACT0008.cap_x = mathutils.Vector((0.0, 0.0))
    ACT0008.use_cap_y = True
    ACT0008.cap_y = mathutils.Vector((0.0, 0.0))
    ACT0008.threshold = 0.10000000149011612
    ACT0008.axis = 1
    PAR0009.game_object = "NLO:camPos"
    PAR0009.attribute_name = "worldPosition"
    ACT0010.condition = CON0012
    ACT0010.xyz = {'x': True, 'y': True, 'z': True}
    ACT0010.game_object = "NLO:Camera"
    ACT0010.attribute_value = PAR0009
    ACT0010.value_type = 'worldPosition'
    ACT0011.condition = CON0024
    ACT0011.origin = PAR0002
    ACT0011.destination = PAR0009
    ACT0011.local = False
    ACT0011.property_name = "obstacle"
    ACT0011.xray = False
    ACT0011.custom_dist = True
    ACT0011.distance = PAR0004
    ACT0011.visualize = False
    CON0012.condition = ACT0011
    ACT0013.condition = ACT0015
    ACT0013.xyz = {'x': True, 'y': True, 'z': True}
    ACT0013.game_object = "NLO:cameraController"
    ACT0013.attribute_value = PAR0016
    ACT0013.value_type = 'worldPosition'
    ACT0015.condition = CON0014
    ACT0015.delay = 0.009999999776482582
    PAR0016.game_object = "NLO:CharacterController"
    PAR0016.attribute_name = "worldPosition"
    ACT0017.condition = CON0014
    ACT0017.game_object = "NLO:U_O"
    ACT0017.property_name = "right_axis"
    ACT0017.property_value = PAR0020.Y
    ACT0018.local = True
    ACT0018.condition = CON0021
    ACT0018.game_object = "NLO:Vertical"
    ACT0018.rotation = mathutils.Vector((-0.03490658476948738, 0.0, 0.0))
    ACT0019.local = True
    ACT0019.condition = CON0022
    ACT0019.game_object = "NLO:Vertical"
    ACT0019.rotation = mathutils.Vector((0.03490658476948738, 0.0, 0.0))
    PAR0020.inverted = False
    PAR0020.index = 0
    PAR0020.sensitivity = 1.0
    PAR0020.threshold = 0.5
    PAR0020.axis = 1
    CON0021.game_object = "NLO:U_O"
    CON0021.property_name = "right_axis"
    CON0021.compare_value = 0.10000000149011612
    CON0021.operator = 2
    CON0022.game_object = "NLO:U_O"
    CON0022.property_name = "right_axis"
    CON0022.compare_value = -0.10000000149011612
    CON0022.operator = 3
    ACT0023.condition = CON0024
    ACT0023.game_object = "NLO:U_O"
    ACT0023.property_name = "limit_x "
    ACT0023.property_value = PAR0027.OUTX
    PAR0025.game_object = "NLO:Vertical"
    PAR0025.attribute_name = "localOrientation"
    PAR0026.input_m = PAR0025
    PAR0027.input_v = PAR0026.OUT
    PAR0028.game_object = "NLO:Vertical"
    PAR0028.attribute_name = "localOrientation"
    PAR0029.input_m = PAR0028
    CON0030.game_object = "NLO:cameraController"
    CON0030.property_name = "limit_x "
    CON0030.compare_value = 1.3788100481033325
    CON0030.operator = 2
    PAR0031.input_x = 1.3788100481033325
    PAR0031.input_y = PAR0033.OUTY
    PAR0031.input_z = PAR0033.OUTZ
    ACT0032.condition = CON0030
    ACT0032.xyz = {'x': True, 'y': False, 'z': False}
    ACT0032.game_object = "NLO:Vertical"
    ACT0032.attribute_value = PAR0031.OUTV
    ACT0032.value_type = 'localOrientation'
    PAR0033.input_v = PAR0029.OUT
    network.add_cell(PAR0002)
    network.add_cell(CON0005)
    network.add_cell(ACT0007)
    network.add_cell(PAR0009)
    network.add_cell(CON0014)
    network.add_cell(PAR0016)
    network.add_cell(PAR0020)
    network.add_cell(CON0022)
    network.add_cell(CON0024)
    network.add_cell(PAR0028)
    network.add_cell(CON0030)
    network.add_cell(PAR0003)
    network.add_cell(CON0006)
    network.add_cell(ACT0015)
    network.add_cell(ACT0019)
    network.add_cell(PAR0025)
    network.add_cell(PAR0029)
    network.add_cell(PAR0033)
    network.add_cell(ACT0000)
    network.add_cell(PAR0004)
    network.add_cell(ACT0011)
    network.add_cell(ACT0013)
    network.add_cell(CON0021)
    network.add_cell(PAR0026)
    network.add_cell(PAR0031)
    network.add_cell(ACT0001)
    network.add_cell(CON0012)
    network.add_cell(ACT0018)
    network.add_cell(PAR0027)
    network.add_cell(ACT0008)
    network.add_cell(ACT0017)
    network.add_cell(ACT0032)
    network.add_cell(ACT0010)
    network.add_cell(ACT0023)
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
