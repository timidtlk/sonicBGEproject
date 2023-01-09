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
    ACT0023 = nodes.ActionSetGravity()
    CON0024 = nodes.ObjectPropertyOperator()
    CON0025 = nodes.ObjectPropertyOperator()
    ACT0026 = nodes.ActionSetGameObjectGameProperty()
    ACT0027 = nodes.ActionSetGameObjectGameProperty()
    CON0028 = nodes.ConditionNot()
    CON0029 = nodes.ObjectPropertyOperator()
    ACT0030 = nodes.ActionSetGameObjectGameProperty()
    CON0031 = nodes.ConditionNot()
    CON0032 = nodes.ObjectPropertyOperator()
    ACT0033 = nodes.ActionSetGameObjectGameProperty()
    PAR0034 = nodes.ParameterObjectProperty()
    CON0035 = nodes.ConditionValueTrigger()
    CON0036 = nodes.ConditionValueTrigger()
    ACT0037 = nodes.ActionStart3DSoundAdv()
    CON0038 = nodes.ConditionValueTrigger()
    ACT0039 = nodes.ActionStart3DSoundAdv()
    ACT0040 = nodes.ActionStart3DSoundAdv()
    ACT0041 = nodes.ActionStart3DSoundAdv()
    ACT0042 = nodes.ActionSetMaterialNodeValue()
    CON0043 = nodes.ConditionValueTrigger()
    PAR0044 = nodes.ParameterObjectProperty()
    ACT0045 = nodes.ActionAddToGameObjectGameProperty()
    CON0046 = nodes.ObjectPropertyOperator()
    PAR0047 = nodes.ParameterObjectProperty()
    ACT0048 = nodes.ActionSetGameObjectVisibility()
    CON0049 = nodes.ObjectPropertyOperator()
    ACT0050 = nodes.ActionApplyLocation()
    ACT0051 = nodes.ActionSetGameObjectGameProperty()
    ACT0052 = nodes.ActionApplyLocation()
    ACT0053 = nodes.ActionSetGameObjectVisibility()
    ACT0054 = nodes.ActionSetGameObjectGameProperty()
    ACT0055 = nodes.ActionSetGameObjectGameProperty()
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
    CON0018.condition_b = CON0029
    CON0019.game_object = "NLO:U_O"
    CON0019.property_name = "isOnWater"
    CON0019.compare_value = False
    CON0019.operator = 0
    CON0020.game_object = "NLO:U_O"
    CON0020.property_name = "isOnWater"
    CON0020.compare_value = True
    CON0020.operator = 0
    ACT0021.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("DIV")
    ACT0021.condition = CON0025
    ACT0021.game_object = "NLO:CharacterController"
    ACT0021.property_name = "Speed"
    ACT0021.property_value = 1.0299999713897705
    ACT0022.condition = CON0024
    ACT0022.gravity = mathutils.Vector((0.0, 0.0, -50.0))
    ACT0023.condition = CON0025
    ACT0023.gravity = mathutils.Vector((0.0, 0.0, -30.0))
    CON0024.game_object = "NLO:CharacterController"
    CON0024.property_name = "isOnWaterP"
    CON0024.compare_value = False
    CON0024.operator = 0
    CON0025.game_object = "NLO:CharacterController"
    CON0025.property_name = "isOnWaterP"
    CON0025.compare_value = True
    CON0025.operator = 0
    ACT0026.condition = CON0028
    ACT0026.game_object = "NLO:U_O"
    ACT0026.property_name = "isOnWater"
    ACT0026.property_value = False
    ACT0027.condition = CON0018
    ACT0027.game_object = "NLO:U_O"
    ACT0027.property_name = "isOnWater"
    ACT0027.property_value = True
    CON0028.condition = CON0018
    CON0029.game_object = "NLO:CharacterController"
    CON0029.property_name = "object"
    CON0029.compare_value = -2.0
    CON0029.operator = 5
    ACT0030.condition = CON0031
    ACT0030.game_object = "NLO:CharacterController"
    ACT0030.property_name = "isOnWaterP"
    ACT0030.property_value = False
    CON0031.condition = CON0032
    CON0032.game_object = "NLO:CharacterController"
    CON0032.property_name = "object"
    CON0032.compare_value = -2.0
    CON0032.operator = 5
    ACT0033.condition = CON0032
    ACT0033.game_object = "NLO:CharacterController"
    ACT0033.property_name = "isOnWaterP"
    ACT0033.property_value = True
    PAR0034.game_object = "NLO:CharacterController"
    PAR0034.property_name = "isOnWaterP"
    CON0035.monitored_value = PAR0034
    CON0035.trigger_value = True
    CON0036.monitored_value = PAR0034
    CON0036.trigger_value = False
    ACT0037.condition = CON0035
    ACT0037.speaker = "NLO:CharacterController"
    ACT0037.sound = "C:/Users/firef/OneDrive/Área de Trabalho/water_dive.ogg"
    ACT0037.occlusion = False
    ACT0037.transition = 0.10000000149011612
    ACT0037.cutoff = 0.10000000149011612
    ACT0037.device_custom = "default3D"
    ACT0037.loop_count = 0
    ACT0037.pitch = 1.0
    ACT0037.volume = 1.0
    ACT0037.attenuation = 1.0
    ACT0037.distance_ref = 1.0
    ACT0037.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0037.cone_outer_volume = 0.0
    CON0038.monitored_value = PAR0044
    CON0038.trigger_value = True
    ACT0039.condition = CON0036
    ACT0039.speaker = "NLO:CharacterController"
    ACT0039.sound = "C:/Users/firef/OneDrive/Área de Trabalho/coming_out_water.mp3"
    ACT0039.occlusion = False
    ACT0039.transition = 0.10000000149011612
    ACT0039.cutoff = 0.10000000149011612
    ACT0039.device_custom = "default3D"
    ACT0039.loop_count = 0
    ACT0039.pitch = 1.0
    ACT0039.volume = 0.5
    ACT0039.attenuation = 1.0
    ACT0039.distance_ref = 1.0
    ACT0039.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0039.cone_outer_volume = 0.0
    ACT0040.condition = CON0043
    ACT0040.speaker = "NLO:CharacterController"
    ACT0040.sound = "C:/Users/firef/OneDrive/Área de Trabalho/coming_out_water.mp3"
    ACT0040.occlusion = False
    ACT0040.transition = 0.10000000149011612
    ACT0040.cutoff = 0.10000000149011612
    ACT0040.device_custom = "default3D"
    ACT0040.loop_count = 0
    ACT0040.pitch = 1.0
    ACT0040.volume = 0.20000000298023224
    ACT0040.attenuation = 1.0
    ACT0040.distance_ref = 1.0
    ACT0040.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0040.cone_outer_volume = 0.0
    ACT0041.condition = CON0038
    ACT0041.speaker = "NLO:CharacterController"
    ACT0041.sound = "C:/Users/firef/OneDrive/Área de Trabalho/water_dive.ogg"
    ACT0041.occlusion = False
    ACT0041.transition = 0.10000000149011612
    ACT0041.cutoff = 0.10000000149011612
    ACT0041.device_custom = "default3D"
    ACT0041.loop_count = 0
    ACT0041.pitch = 1.0
    ACT0041.volume = 0.5
    ACT0041.attenuation = 1.0
    ACT0041.distance_ref = 1.0
    ACT0041.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0041.cone_outer_volume = 0.0
    ACT0042.condition = CON0049
    ACT0042.mat_name = "droplets"
    ACT0042.node_name = "Principled BSDF"
    ACT0042.input_slot = 21
    ACT0042.value = PAR0047
    CON0043.monitored_value = PAR0044
    CON0043.trigger_value = False
    PAR0044.game_object = "NLO:U_O"
    PAR0044.property_name = "isOnWater"
    ACT0045.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("SUB")
    ACT0045.condition = CON0049
    ACT0045.game_object = "NLO:droplets"
    ACT0045.property_name = "coco"
    ACT0045.property_value = 0.016699999570846558
    CON0046.game_object = "NLO:droplets"
    CON0046.property_name = "coco"
    CON0046.compare_value = 0.0
    CON0046.operator = 5
    PAR0047.game_object = "NLO:droplets"
    PAR0047.property_name = "coco"
    ACT0048.condition = CON0046
    ACT0048.game_object = "NLO:droplets"
    ACT0048.visible = False
    ACT0048.recursive = False
    CON0049.game_object = "NLO:droplets"
    CON0049.property_name = "droplets"
    CON0049.compare_value = True
    CON0049.operator = 0
    ACT0050.local = True
    ACT0050.condition = CON0049
    ACT0050.game_object = "NLO:droplets"
    ACT0050.movement = mathutils.Vector((0.0, 0.0015999999595806003, 0.0))
    ACT0051.condition = ACT0048.OUT
    ACT0051.game_object = "NLO:droplets"
    ACT0051.property_name = "coco"
    ACT0051.property_value = 1.0
    ACT0052.local = True
    ACT0052.condition = ACT0048.OUT
    ACT0052.game_object = "NLO:droplets"
    ACT0052.movement = mathutils.Vector((0.0, -0.09600000083446503, 0.0))
    ACT0053.condition = CON0043
    ACT0053.game_object = "NLO:droplets"
    ACT0053.visible = True
    ACT0053.recursive = False
    ACT0054.condition = ACT0053.OUT
    ACT0054.game_object = "NLO:droplets"
    ACT0054.property_name = "droplets"
    ACT0054.property_value = True
    ACT0055.condition = ACT0048.OUT
    ACT0055.game_object = "NLO:droplets"
    ACT0055.property_name = "droplets"
    ACT0055.property_value = False
    network.add_cell(PAR0006)
    network.add_cell(CON0008)
    network.add_cell(PAR0012)
    network.add_cell(PAR0015)
    network.add_cell(CON0017)
    network.add_cell(CON0019)
    network.add_cell(CON0024)
    network.add_cell(CON0029)
    network.add_cell(CON0032)
    network.add_cell(PAR0034)
    network.add_cell(CON0036)
    network.add_cell(ACT0039)
    network.add_cell(PAR0044)
    network.add_cell(CON0046)
    network.add_cell(ACT0048)
    network.add_cell(ACT0051)
    network.add_cell(ACT0055)
    network.add_cell(ACT0000)
    network.add_cell(CON0003)
    network.add_cell(ACT0005)
    network.add_cell(CON0009)
    network.add_cell(PAR0011)
    network.add_cell(PAR0014)
    network.add_cell(CON0018)
    network.add_cell(ACT0022)
    network.add_cell(CON0025)
    network.add_cell(ACT0027)
    network.add_cell(CON0031)
    network.add_cell(CON0035)
    network.add_cell(CON0038)
    network.add_cell(ACT0041)
    network.add_cell(CON0043)
    network.add_cell(PAR0047)
    network.add_cell(ACT0052)
    network.add_cell(CON0004)
    network.add_cell(ACT0010)
    network.add_cell(CON0020)
    network.add_cell(ACT0023)
    network.add_cell(CON0028)
    network.add_cell(ACT0033)
    network.add_cell(ACT0040)
    network.add_cell(CON0049)
    network.add_cell(ACT0053)
    network.add_cell(ACT0001)
    network.add_cell(ACT0007)
    network.add_cell(ACT0021)
    network.add_cell(ACT0030)
    network.add_cell(ACT0042)
    network.add_cell(ACT0050)
    network.add_cell(ACT0002)
    network.add_cell(ACT0026)
    network.add_cell(ACT0045)
    network.add_cell(CON0013)
    network.add_cell(ACT0037)
    network.add_cell(ACT0016)
    network.add_cell(ACT0054)
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
