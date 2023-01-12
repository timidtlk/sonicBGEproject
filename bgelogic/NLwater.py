# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionSetGameObjectVisibility()
    ACT0001 = nodes.ActionSetGameObjectVisibility()
    ACT0002 = nodes.ActionStopSound()
    CON0003 = nodes.ConditionValueTrigger()
    CON0004 = nodes.ConditionValueTrigger()
    ACT0005 = nodes.ActionStartSound()
    PAR0006 = nodes.ParameterObjectProperty()
    ACT0007 = nodes.ActionToggleGameObjectGameProperty()
    CON0008 = nodes.ConditionKeyPressed()
    CON0009 = nodes.ConditionOnUpdate()
    ACT0010 = nodes.ActionSetGameObjectGameProperty()
    PAR0011 = nodes.ParameterVector3Split()
    PAR0012 = nodes.ParameterObjectAttribute()
    CON0013 = nodes.ConditionOnUpdate()
    PAR0014 = nodes.ParameterVector3Split()
    PAR0015 = nodes.ParameterObjectAttribute()
    ACT0016 = nodes.ActionSetGameObjectGameProperty()
    CON0017 = nodes.ObjectPropertyOperator()
    CON0018 = nodes.ConditionAnd()
    CON0019 = nodes.ObjectPropertyOperator()
    CON0020 = nodes.ObjectPropertyOperator()
    ACT0021 = nodes.ActionAddToGameObjectGameProperty()
    ACT0022 = nodes.ActionSetGravity()
    CON0023 = nodes.ObjectPropertyOperator()
    CON0024 = nodes.ObjectPropertyOperator()
    ACT0025 = nodes.ActionSetGameObjectGameProperty()
    ACT0026 = nodes.ActionSetGameObjectGameProperty()
    CON0027 = nodes.ConditionNot()
    CON0028 = nodes.ObjectPropertyOperator()
    ACT0029 = nodes.ActionSetGameObjectGameProperty()
    CON0030 = nodes.ConditionNot()
    CON0031 = nodes.ObjectPropertyOperator()
    ACT0032 = nodes.ActionSetGameObjectGameProperty()
    PAR0033 = nodes.ParameterObjectProperty()
    CON0034 = nodes.ConditionValueTrigger()
    CON0035 = nodes.ConditionValueTrigger()
    ACT0036 = nodes.ActionStart3DSoundAdv()
    CON0037 = nodes.ConditionValueTrigger()
    ACT0038 = nodes.ActionStart3DSoundAdv()
    ACT0039 = nodes.ActionStart3DSoundAdv()
    ACT0040 = nodes.ActionStart3DSoundAdv()
    CON0041 = nodes.ConditionValueTrigger()
    PAR0042 = nodes.ParameterObjectProperty()
    CON0043 = nodes.ObjectPropertyOperator()
    ACT0044 = nodes.ActionSetGameObjectGameProperty()
    ACT0045 = nodes.ActionSetGameObjectGameProperty()
    ACT0046 = nodes.ActionSetGravity()
    ACT0000.condition = CON0019
    ACT0000.game_object = "NLO:water_filter"
    ACT0000.visible = False
    ACT0000.recursive = False
    ACT0001.condition = CON0020
    ACT0001.game_object = "NLO:water_filter"
    ACT0001.visible = True
    ACT0001.recursive = False
    ACT0002.condition = CON0004
    ACT0002.sound = ACT0005.HANDLE
    CON0003.monitored_value = PAR0006
    CON0003.trigger_value = True
    CON0004.monitored_value = PAR0006
    CON0004.trigger_value = False
    ACT0005.condition = CON0003
    ACT0005.sound = "C:/Users/firef/Downloads/Under Water Sound FX.mp3"
    ACT0005.loop_count = -1
    ACT0005.pitch = 1.0
    ACT0005.volume = 1.0
    PAR0006.game_object = "NLO:U_O"
    PAR0006.property_name = "isOnWater"
    ACT0007.condition = CON0008
    ACT0007.game_object = "NLO:U_O"
    ACT0007.property_name = "isOnWater"
    CON0008.key_code = bge.events.OKEY
    CON0008.pulse = False
    ACT0010.condition = CON0009
    ACT0010.game_object = "NLO:U_O"
    ACT0010.property_name = "camera"
    ACT0010.property_value = PAR0011.OUTZ
    PAR0011.input_v = PAR0012
    PAR0012.game_object = "NLO:camPos"
    PAR0012.attribute_name = "worldPosition"
    PAR0014.input_v = PAR0015
    PAR0015.game_object = "NLO:CharacterController"
    PAR0015.attribute_name = "worldPosition"
    ACT0016.condition = CON0013
    ACT0016.game_object = "NLO:CharacterController"
    ACT0016.property_name = "object"
    ACT0016.property_value = PAR0014.OUTZ
    CON0017.game_object = "NLO:U_O"
    CON0017.property_name = "camera"
    CON0017.compare_value = -1.0
    CON0017.operator = 5
    CON0018.condition_a = CON0017
    CON0018.condition_b = CON0028
    CON0019.game_object = "NLO:U_O"
    CON0019.property_name = "isOnWater"
    CON0019.compare_value = False
    CON0019.operator = 0
    CON0020.game_object = "NLO:U_O"
    CON0020.property_name = "isOnWater"
    CON0020.compare_value = True
    CON0020.operator = 0
    ACT0021.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("DIV")
    ACT0021.condition = CON0024
    ACT0021.game_object = "NLO:CharacterController"
    ACT0021.property_name = "Speed"
    ACT0021.property_value = 1.0299999713897705
    ACT0022.condition = CON0024
    ACT0022.gravity = mathutils.Vector((0.0, 0.0, -25.0))
    CON0023.game_object = "NLO:CharacterController"
    CON0023.property_name = "isOnWaterP"
    CON0023.compare_value = False
    CON0023.operator = 0
    CON0024.game_object = "NLO:CharacterController"
    CON0024.property_name = "isOnWaterP"
    CON0024.compare_value = True
    CON0024.operator = 0
    ACT0025.condition = CON0027
    ACT0025.game_object = "NLO:U_O"
    ACT0025.property_name = "isOnWater"
    ACT0025.property_value = False
    ACT0026.condition = CON0018
    ACT0026.game_object = "NLO:U_O"
    ACT0026.property_name = "isOnWater"
    ACT0026.property_value = True
    CON0027.condition = CON0018
    CON0028.game_object = "NLO:CharacterController"
    CON0028.property_name = "object"
    CON0028.compare_value = -2.0
    CON0028.operator = 5
    ACT0029.condition = CON0030
    ACT0029.game_object = "NLO:CharacterController"
    ACT0029.property_name = "isOnWaterP"
    ACT0029.property_value = False
    CON0030.condition = CON0031
    CON0031.game_object = "NLO:CharacterController"
    CON0031.property_name = "object"
    CON0031.compare_value = -2.0
    CON0031.operator = 5
    ACT0032.condition = CON0031
    ACT0032.game_object = "NLO:CharacterController"
    ACT0032.property_name = "isOnWaterP"
    ACT0032.property_value = True
    PAR0033.game_object = "NLO:CharacterController"
    PAR0033.property_name = "isOnWaterP"
    CON0034.monitored_value = PAR0033
    CON0034.trigger_value = True
    CON0035.monitored_value = PAR0033
    CON0035.trigger_value = False
    ACT0036.condition = CON0034
    ACT0036.speaker = "NLO:CharacterController"
    ACT0036.sound = "C:/Users/firef/OneDrive/Área de Trabalho/water_dive.ogg"
    ACT0036.occlusion = False
    ACT0036.transition = 0.10000000149011612
    ACT0036.cutoff = 0.10000000149011612
    ACT0036.device_custom = "default3D"
    ACT0036.loop_count = 0
    ACT0036.pitch = 1.0
    ACT0036.volume = 1.0
    ACT0036.attenuation = 1.0
    ACT0036.distance_ref = 1.0
    ACT0036.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0036.cone_outer_volume = 0.0
    CON0037.monitored_value = PAR0042
    CON0037.trigger_value = True
    ACT0038.condition = CON0035
    ACT0038.speaker = "NLO:CharacterController"
    ACT0038.sound = "C:/Users/firef/OneDrive/Área de Trabalho/coming_out_water.mp3"
    ACT0038.occlusion = False
    ACT0038.transition = 0.10000000149011612
    ACT0038.cutoff = 0.10000000149011612
    ACT0038.device_custom = "default3D"
    ACT0038.loop_count = 0
    ACT0038.pitch = 1.0
    ACT0038.volume = 0.5
    ACT0038.attenuation = 1.0
    ACT0038.distance_ref = 1.0
    ACT0038.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0038.cone_outer_volume = 0.0
    ACT0039.condition = CON0041
    ACT0039.speaker = "NLO:CharacterController"
    ACT0039.sound = "C:/Users/firef/OneDrive/Área de Trabalho/coming_out_water.mp3"
    ACT0039.occlusion = False
    ACT0039.transition = 0.10000000149011612
    ACT0039.cutoff = 0.10000000149011612
    ACT0039.device_custom = "default3D"
    ACT0039.loop_count = 0
    ACT0039.pitch = 1.0
    ACT0039.volume = 0.20000000298023224
    ACT0039.attenuation = 1.0
    ACT0039.distance_ref = 1.0
    ACT0039.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0039.cone_outer_volume = 0.0
    ACT0040.condition = CON0037
    ACT0040.speaker = "NLO:CharacterController"
    ACT0040.sound = "C:/Users/firef/OneDrive/Área de Trabalho/water_dive.ogg"
    ACT0040.occlusion = False
    ACT0040.transition = 0.10000000149011612
    ACT0040.cutoff = 0.10000000149011612
    ACT0040.device_custom = "default3D"
    ACT0040.loop_count = 0
    ACT0040.pitch = 1.0
    ACT0040.volume = 0.5
    ACT0040.attenuation = 1.0
    ACT0040.distance_ref = 1.0
    ACT0040.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0040.cone_outer_volume = 0.0
    CON0041.monitored_value = PAR0042
    CON0041.trigger_value = False
    PAR0042.game_object = "NLO:U_O"
    PAR0042.property_name = "isOnWater"
    CON0043.game_object = "NLO:U_O"
    CON0043.property_name = "isOnWater"
    CON0043.compare_value = True
    CON0043.operator = 0
    ACT0044.condition = CON0043
    ACT0044.game_object = "NLO:U_O"
    ACT0044.property_name = "resettimer"
    ACT0044.property_value = -5.0
    ACT0045.condition = CON0041
    ACT0045.game_object = "NLO:U_O"
    ACT0045.property_name = "resettimer"
    ACT0045.property_value = 0.10000000149011612
    ACT0046.condition = CON0023
    ACT0046.gravity = mathutils.Vector((0.0, 0.0, -40.0))
    network.add_cell(PAR0006)
    network.add_cell(CON0008)
    network.add_cell(PAR0012)
    network.add_cell(PAR0015)
    network.add_cell(CON0017)
    network.add_cell(CON0019)
    network.add_cell(CON0023)
    network.add_cell(CON0028)
    network.add_cell(CON0031)
    network.add_cell(PAR0033)
    network.add_cell(CON0035)
    network.add_cell(ACT0038)
    network.add_cell(PAR0042)
    network.add_cell(ACT0046)
    network.add_cell(ACT0000)
    network.add_cell(CON0003)
    network.add_cell(ACT0005)
    network.add_cell(CON0009)
    network.add_cell(PAR0011)
    network.add_cell(PAR0014)
    network.add_cell(CON0018)
    network.add_cell(CON0024)
    network.add_cell(ACT0026)
    network.add_cell(CON0030)
    network.add_cell(CON0034)
    network.add_cell(CON0037)
    network.add_cell(ACT0040)
    network.add_cell(CON0043)
    network.add_cell(CON0004)
    network.add_cell(ACT0010)
    network.add_cell(CON0020)
    network.add_cell(ACT0022)
    network.add_cell(CON0027)
    network.add_cell(ACT0032)
    network.add_cell(CON0041)
    network.add_cell(ACT0045)
    network.add_cell(ACT0001)
    network.add_cell(ACT0007)
    network.add_cell(ACT0021)
    network.add_cell(ACT0029)
    network.add_cell(ACT0039)
    network.add_cell(ACT0002)
    network.add_cell(ACT0025)
    network.add_cell(ACT0044)
    network.add_cell(CON0013)
    network.add_cell(ACT0036)
    network.add_cell(ACT0016)
    owner["IGNLTree_water"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__water')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_water")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
