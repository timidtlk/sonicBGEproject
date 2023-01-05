# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    CON0000 = nodes.ObjectPropertyOperator()
    CON0001 = nodes.ObjectPropertyOperator()
    CON0002 = nodes.ObjectPropertyOperator()
    CON0003 = nodes.ConditionAnd()
    CON0004 = nodes.ConditionAnd()
    CON0005 = nodes.ConditionAnd()
    CON0006 = nodes.ConditionAnd()
    ACT0007 = nodes.ActionRandomInt()
    CON0008 = nodes.ObjectPropertyOperator()
    ACT0009 = nodes.ActionSetGameObjectGameProperty()
    PAR0010 = nodes.ParameterObjectProperty()
    CON0011 = nodes.ConditionCollision()
    ACT0012 = nodes.ActionSetGameObjectGameProperty()
    CON0013 = nodes.ObjectPropertyOperator()
    ACT0014 = nodes.ActionTimeFilter()
    CON0015 = nodes.ConditionOrList()
    ACT0016 = nodes.ActionSetGameObjectGameProperty()
    PAR0017 = nodes.ParameterObjectProperty()
    ACT0018 = nodes.ActionSetGameObjectGameProperty()
    ACT0019 = nodes.ActionSetGameObjectGameProperty()
    CON0020 = nodes.ConditionAnd()
    CON0021 = nodes.ConditionAnd()
    CON0022 = nodes.ConditionAnd()
    CON0023 = nodes.ConditionAnd()
    CON0024 = nodes.ConditionAnd()
    ACT0025 = nodes.ActionStart3DSoundAdv()
    ACT0026 = nodes.ActionStart3DSoundAdv()
    ACT0027 = nodes.ActionStart3DSoundAdv()
    ACT0028 = nodes.ActionStart3DSoundAdv()
    ACT0029 = nodes.ActionStart3DSoundAdv()
    ACT0030 = nodes.ActionSetGameObjectGameProperty()
    CON0031 = nodes.ObjectPropertyOperator()
    CON0032 = nodes.ObjectPropertyOperator()
    CON0033 = nodes.ObjectPropertyOperator()
    CON0034 = nodes.ObjectPropertyOperator()
    CON0035 = nodes.ObjectPropertyOperator()
    CON0036 = nodes.ObjectPropertyOperator()
    CON0037 = nodes.ConditionAnd()
    CON0038 = nodes.ConditionAnd()
    CON0039 = nodes.ConditionAnd()
    CON0040 = nodes.ConditionAnd()
    CON0041 = nodes.ConditionAnd()
    ACT0042 = nodes.ActionTimeFilter()
    ACT0043 = nodes.ActionStart3DSoundAdv()
    ACT0044 = nodes.ActionStart3DSoundAdv()
    ACT0045 = nodes.ActionStart3DSoundAdv()
    ACT0046 = nodes.ActionStart3DSoundAdv()
    ACT0047 = nodes.ActionStart3DSoundAdv()
    CON0048 = nodes.ConditionAnd()
    CON0049 = nodes.ConditionAnd()
    CON0050 = nodes.ConditionAnd()
    CON0051 = nodes.ConditionAnd()
    CON0052 = nodes.ConditionAnd()
    CON0053 = nodes.ObjectPropertyOperator()
    CON0054 = nodes.ObjectPropertyOperator()
    CON0055 = nodes.ObjectPropertyOperator()
    CON0056 = nodes.ObjectPropertyOperator()
    CON0057 = nodes.ObjectPropertyOperator()
    CON0058 = nodes.ConditionAnd()
    CON0059 = nodes.ConditionAnd()
    CON0060 = nodes.ConditionAnd()
    CON0061 = nodes.ConditionAnd()
    CON0062 = nodes.ObjectPropertyOperator()
    CON0063 = nodes.ConditionAnd()
    CON0064 = nodes.ObjectPropertyOperator()
    CON0065 = nodes.ObjectPropertyOperator()
    CON0066 = nodes.ObjectPropertyOperator()
    CON0067 = nodes.ObjectPropertyOperator()
    CON0068 = nodes.ConditionAnd()
    CON0069 = nodes.ConditionAnd()
    CON0070 = nodes.ConditionAnd()
    CON0071 = nodes.ConditionAnd()
    CON0072 = nodes.ConditionAnd()
    CON0073 = nodes.ConditionAnd()
    CON0074 = nodes.ConditionAnd()
    CON0075 = nodes.ConditionAnd()
    CON0076 = nodes.ConditionAnd()
    CON0077 = nodes.ConditionAnd()
    ACT0078 = nodes.ActionStart3DSoundAdv()
    ACT0079 = nodes.ActionStart3DSoundAdv()
    ACT0080 = nodes.ActionStart3DSoundAdv()
    ACT0081 = nodes.ActionStart3DSoundAdv()
    ACT0082 = nodes.ActionStart3DSoundAdv()
    CON0083 = nodes.ObjectPropertyOperator()
    CON0084 = nodes.ObjectPropertyOperator()
    CON0000.game_object = "NLO:U_O"
    CON0000.property_name = "animation"
    CON0000.compare_value = "jog"
    CON0000.operator = 0
    CON0001.game_object = "NLO:U_O"
    CON0001.property_name = "animation"
    CON0001.compare_value = "jet"
    CON0001.operator = 0
    CON0002.game_object = "NLO:U_O"
    CON0002.property_name = "animation"
    CON0002.compare_value = "boost"
    CON0002.operator = 0
    CON0003.condition_a = CON0011
    CON0003.condition_b = CON0013
    CON0004.condition_a = CON0011
    CON0004.condition_b = CON0000
    CON0005.condition_a = CON0011
    CON0005.condition_b = CON0001
    CON0006.condition_a = CON0011
    CON0006.condition_b = CON0002
    ACT0007.condition = ACT0014
    ACT0007.max_value = 5
    ACT0007.min_value = 1
    CON0008.game_object = "NLO:CharacterController"
    CON0008.property_name = "animation"
    CON0008.compare_value = "idle"
    CON0008.operator = 1
    ACT0009.condition = ACT0007.DONE
    ACT0009.game_object = "NLO:U_O"
    ACT0009.property_name = "number_footstep"
    ACT0009.property_value = ACT0007.OUT_A
    PAR0010.game_object = CON0011.TARGET
    PAR0010.property_name = "type"
    CON0011.game_object = "NLO:CharacterController"
    CON0011.use_mat = False
    CON0011.prop = "type"
    CON0011.material = None
    CON0011.pulse = True
    ACT0012.condition = CON0011
    ACT0012.game_object = "NLO:U_O"
    ACT0012.property_name = "step_ground"
    ACT0012.property_value = PAR0010
    CON0013.game_object = "NLO:U_O"
    CON0013.property_name = "animation"
    CON0013.compare_value = "walk"
    CON0013.operator = 0
    ACT0014.condition = CON0008
    ACT0014.delay = PAR0017
    CON0015.ca = CON0003
    CON0015.cb = CON0004
    CON0015.cc = CON0005
    CON0015.cd = CON0006
    CON0015.ce = None
    CON0015.cf = None
    ACT0016.condition = CON0003
    ACT0016.game_object = "NLO:U_O"
    ACT0016.property_name = "footstep_time"
    ACT0016.property_value = 0.30000001192092896
    PAR0017.game_object = "NLO:U_O"
    PAR0017.property_name = "footstep_time"
    ACT0018.condition = CON0004
    ACT0018.game_object = "NLO:U_O"
    ACT0018.property_name = "footstep_time"
    ACT0018.property_value = 0.20000000298023224
    ACT0019.condition = CON0005
    ACT0019.game_object = "NLO:U_O"
    ACT0019.property_name = "footstep_time"
    ACT0019.property_value = 0.10000000149011612
    CON0020.condition_a = ACT0042
    CON0020.condition_b = CON0040
    CON0021.condition_a = ACT0042
    CON0021.condition_b = CON0041
    CON0022.condition_a = ACT0042
    CON0022.condition_b = CON0039
    CON0023.condition_a = ACT0042
    CON0023.condition_b = CON0037
    CON0024.condition_a = ACT0042
    CON0024.condition_b = CON0038
    ACT0025.condition = CON0023
    ACT0025.speaker = "NLO:CharacterController"
    ACT0025.sound = "D:/Sonic BGE Project/sounds/footsteps/001_conc/00_sn_walk_conc_1.wav"
    ACT0025.occlusion = False
    ACT0025.transition = 0.10000000149011612
    ACT0025.cutoff = 0.10000000149011612
    ACT0025.device_custom = "default3D"
    ACT0025.loop_count = 0
    ACT0025.pitch = 1.0
    ACT0025.volume = 1.0
    ACT0025.attenuation = 1.0
    ACT0025.distance_ref = 1.0
    ACT0025.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0025.cone_outer_volume = 0.0
    ACT0026.condition = CON0024
    ACT0026.speaker = "NLO:CharacterController"
    ACT0026.sound = "D:/Sonic BGE Project/sounds/footsteps/001_conc/00_sn_walk_conc_2.wav"
    ACT0026.occlusion = False
    ACT0026.transition = 0.10000000149011612
    ACT0026.cutoff = 0.10000000149011612
    ACT0026.device_custom = "default3D"
    ACT0026.loop_count = 0
    ACT0026.pitch = 1.0
    ACT0026.volume = 1.0
    ACT0026.attenuation = 1.0
    ACT0026.distance_ref = 1.0
    ACT0026.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0026.cone_outer_volume = 0.0
    ACT0027.condition = CON0022
    ACT0027.speaker = "NLO:CharacterController"
    ACT0027.sound = "D:/Sonic BGE Project/sounds/footsteps/001_conc/00_sn_walk_conc_3.wav"
    ACT0027.occlusion = False
    ACT0027.transition = 0.10000000149011612
    ACT0027.cutoff = 0.10000000149011612
    ACT0027.device_custom = "default3D"
    ACT0027.loop_count = 0
    ACT0027.pitch = 1.0
    ACT0027.volume = 1.0
    ACT0027.attenuation = 1.0
    ACT0027.distance_ref = 1.0
    ACT0027.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0027.cone_outer_volume = 0.0
    ACT0028.condition = CON0020
    ACT0028.speaker = "NLO:CharacterController"
    ACT0028.sound = "D:/Sonic BGE Project/sounds/footsteps/001_conc/00_sn_walk_conc_4.wav"
    ACT0028.occlusion = False
    ACT0028.transition = 0.10000000149011612
    ACT0028.cutoff = 0.10000000149011612
    ACT0028.device_custom = "default3D"
    ACT0028.loop_count = 0
    ACT0028.pitch = 1.0
    ACT0028.volume = 1.0
    ACT0028.attenuation = 1.0
    ACT0028.distance_ref = 1.0
    ACT0028.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0028.cone_outer_volume = 0.0
    ACT0029.condition = CON0021
    ACT0029.speaker = "NLO:CharacterController"
    ACT0029.sound = "D:/Sonic BGE Project/sounds/footsteps/001_conc/00_sn_walk_conc_5.wav"
    ACT0029.occlusion = False
    ACT0029.transition = 0.10000000149011612
    ACT0029.cutoff = 0.10000000149011612
    ACT0029.device_custom = "default3D"
    ACT0029.loop_count = 0
    ACT0029.pitch = 1.0
    ACT0029.volume = 1.0
    ACT0029.attenuation = 1.0
    ACT0029.distance_ref = 1.0
    ACT0029.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0029.cone_outer_volume = 0.0
    ACT0030.condition = CON0006
    ACT0030.game_object = "NLO:U_O"
    ACT0030.property_name = "footstep_time"
    ACT0030.property_value = 0.07999999821186066
    CON0031.game_object = "NLO:U_O"
    CON0031.property_name = "number_footstep"
    CON0031.compare_value = 1
    CON0031.operator = 0
    CON0032.game_object = "NLO:U_O"
    CON0032.property_name = "number_footstep"
    CON0032.compare_value = 2
    CON0032.operator = 0
    CON0033.game_object = "NLO:U_O"
    CON0033.property_name = "number_footstep"
    CON0033.compare_value = 3
    CON0033.operator = 0
    CON0034.game_object = "NLO:U_O"
    CON0034.property_name = "number_footstep"
    CON0034.compare_value = 4
    CON0034.operator = 0
    CON0035.game_object = "NLO:U_O"
    CON0035.property_name = "number_footstep"
    CON0035.compare_value = 5
    CON0035.operator = 0
    CON0036.game_object = "NLO:U_O"
    CON0036.property_name = "step_ground"
    CON0036.compare_value = "concrete"
    CON0036.operator = 0
    CON0037.condition_a = CON0036
    CON0037.condition_b = CON0031
    CON0038.condition_a = CON0036
    CON0038.condition_b = CON0032
    CON0039.condition_a = CON0036
    CON0039.condition_b = CON0033
    CON0040.condition_a = CON0036
    CON0040.condition_b = CON0034
    CON0041.condition_a = CON0036
    CON0041.condition_b = CON0035
    ACT0042.condition = CON0015
    ACT0042.delay = PAR0017
    ACT0043.condition = CON0049
    ACT0043.speaker = "NLO:CharacterController"
    ACT0043.sound = "D:/Sonic BGE Project/sounds/footsteps/004_wood/00_sn_walk_wood_5.wav"
    ACT0043.occlusion = False
    ACT0043.transition = 0.10000000149011612
    ACT0043.cutoff = 0.10000000149011612
    ACT0043.device_custom = "default3D"
    ACT0043.loop_count = 0
    ACT0043.pitch = 1.0
    ACT0043.volume = 1.0
    ACT0043.attenuation = 1.0
    ACT0043.distance_ref = 1.0
    ACT0043.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0043.cone_outer_volume = 0.0
    ACT0044.condition = CON0048
    ACT0044.speaker = "NLO:CharacterController"
    ACT0044.sound = "D:/Sonic BGE Project/sounds/footsteps/004_wood/00_sn_walk_wood_5.wav"
    ACT0044.occlusion = False
    ACT0044.transition = 0.10000000149011612
    ACT0044.cutoff = 0.10000000149011612
    ACT0044.device_custom = "default3D"
    ACT0044.loop_count = 0
    ACT0044.pitch = 1.0
    ACT0044.volume = 1.0
    ACT0044.attenuation = 1.0
    ACT0044.distance_ref = 1.0
    ACT0044.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0044.cone_outer_volume = 0.0
    ACT0045.condition = CON0050
    ACT0045.speaker = "NLO:CharacterController"
    ACT0045.sound = "D:/Sonic BGE Project/sounds/footsteps/004_wood/00_sn_walk_wood_3.wav"
    ACT0045.occlusion = False
    ACT0045.transition = 0.10000000149011612
    ACT0045.cutoff = 0.10000000149011612
    ACT0045.device_custom = "default3D"
    ACT0045.loop_count = 0
    ACT0045.pitch = 1.0
    ACT0045.volume = 1.0
    ACT0045.attenuation = 1.0
    ACT0045.distance_ref = 1.0
    ACT0045.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0045.cone_outer_volume = 0.0
    ACT0046.condition = CON0052
    ACT0046.speaker = "NLO:CharacterController"
    ACT0046.sound = "D:/Sonic BGE Project/sounds/footsteps/004_wood/00_sn_walk_wood_2.wav"
    ACT0046.occlusion = False
    ACT0046.transition = 0.10000000149011612
    ACT0046.cutoff = 0.10000000149011612
    ACT0046.device_custom = "default3D"
    ACT0046.loop_count = 0
    ACT0046.pitch = 1.0
    ACT0046.volume = 1.0
    ACT0046.attenuation = 1.0
    ACT0046.distance_ref = 1.0
    ACT0046.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0046.cone_outer_volume = 0.0
    ACT0047.condition = CON0063
    ACT0047.speaker = "NLO:CharacterController"
    ACT0047.sound = "D:/Sonic BGE Project/sounds/footsteps/004_wood/00_sn_walk_wood_1.wav"
    ACT0047.occlusion = False
    ACT0047.transition = 0.10000000149011612
    ACT0047.cutoff = 0.10000000149011612
    ACT0047.device_custom = "default3D"
    ACT0047.loop_count = 0
    ACT0047.pitch = 1.0
    ACT0047.volume = 1.0
    ACT0047.attenuation = 1.0
    ACT0047.distance_ref = 1.0
    ACT0047.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0047.cone_outer_volume = 0.0
    CON0048.condition_a = ACT0042
    CON0048.condition_b = CON0059
    CON0049.condition_a = ACT0042
    CON0049.condition_b = CON0060
    CON0050.condition_a = ACT0042
    CON0050.condition_b = CON0061
    CON0051.condition_a = CON0062
    CON0051.condition_b = CON0057
    CON0052.condition_a = ACT0042
    CON0052.condition_b = CON0058
    CON0053.game_object = "NLO:U_O"
    CON0053.property_name = "number_footstep"
    CON0053.compare_value = 2
    CON0053.operator = 0
    CON0054.game_object = "NLO:U_O"
    CON0054.property_name = "number_footstep"
    CON0054.compare_value = 3
    CON0054.operator = 0
    CON0055.game_object = "NLO:U_O"
    CON0055.property_name = "number_footstep"
    CON0055.compare_value = 4
    CON0055.operator = 0
    CON0056.game_object = "NLO:U_O"
    CON0056.property_name = "number_footstep"
    CON0056.compare_value = 5
    CON0056.operator = 0
    CON0057.game_object = "NLO:U_O"
    CON0057.property_name = "number_footstep"
    CON0057.compare_value = 1
    CON0057.operator = 0
    CON0058.condition_a = CON0062
    CON0058.condition_b = CON0053
    CON0059.condition_a = CON0062
    CON0059.condition_b = CON0055
    CON0060.condition_a = CON0062
    CON0060.condition_b = CON0056
    CON0061.condition_a = CON0062
    CON0061.condition_b = CON0054
    CON0062.game_object = "NLO:U_O"
    CON0062.property_name = "step_ground"
    CON0062.compare_value = "wood"
    CON0062.operator = 0
    CON0063.condition_a = ACT0042
    CON0063.condition_b = CON0051
    CON0064.game_object = "NLO:U_O"
    CON0064.property_name = "number_footstep"
    CON0064.compare_value = 2
    CON0064.operator = 0
    CON0065.game_object = "NLO:U_O"
    CON0065.property_name = "number_footstep"
    CON0065.compare_value = 3
    CON0065.operator = 0
    CON0066.game_object = "NLO:U_O"
    CON0066.property_name = "number_footstep"
    CON0066.compare_value = 4
    CON0066.operator = 0
    CON0067.game_object = "NLO:U_O"
    CON0067.property_name = "number_footstep"
    CON0067.compare_value = 5
    CON0067.operator = 0
    CON0068.condition_a = ACT0042
    CON0068.condition_b = CON0073
    CON0069.condition_a = ACT0042
    CON0069.condition_b = CON0074
    CON0070.condition_a = ACT0042
    CON0070.condition_b = CON0075
    CON0071.condition_a = ACT0042
    CON0071.condition_b = CON0076
    CON0072.condition_a = ACT0042
    CON0072.condition_b = CON0077
    CON0073.condition_a = CON0083
    CON0073.condition_b = CON0084
    CON0074.condition_a = CON0083
    CON0074.condition_b = CON0064
    CON0075.condition_a = CON0083
    CON0075.condition_b = CON0065
    CON0076.condition_a = CON0083
    CON0076.condition_b = CON0066
    CON0077.condition_a = CON0083
    CON0077.condition_b = CON0067
    ACT0078.condition = CON0068
    ACT0078.speaker = "NLO:CharacterController"
    ACT0078.sound = "D:/Sonic BGE Project/sounds/footsteps/002_metalpl/00_sn_walk_mtlp_1.wav"
    ACT0078.occlusion = False
    ACT0078.transition = 0.10000000149011612
    ACT0078.cutoff = 0.10000000149011612
    ACT0078.device_custom = "default3D"
    ACT0078.loop_count = 0
    ACT0078.pitch = 1.0
    ACT0078.volume = 1.0
    ACT0078.attenuation = 1.0
    ACT0078.distance_ref = 1.0
    ACT0078.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0078.cone_outer_volume = 0.0
    ACT0079.condition = CON0069
    ACT0079.speaker = "NLO:CharacterController"
    ACT0079.sound = "D:/Sonic BGE Project/sounds/footsteps/002_metalpl/00_sn_walk_mtlp_2.wav"
    ACT0079.occlusion = False
    ACT0079.transition = 0.10000000149011612
    ACT0079.cutoff = 0.10000000149011612
    ACT0079.device_custom = "default3D"
    ACT0079.loop_count = 0
    ACT0079.pitch = 1.0
    ACT0079.volume = 1.0
    ACT0079.attenuation = 1.0
    ACT0079.distance_ref = 1.0
    ACT0079.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0079.cone_outer_volume = 0.0
    ACT0080.condition = CON0070
    ACT0080.speaker = "NLO:CharacterController"
    ACT0080.sound = "D:/Sonic BGE Project/sounds/footsteps/002_metalpl/00_sn_walk_mtlp_3.wav"
    ACT0080.occlusion = False
    ACT0080.transition = 0.10000000149011612
    ACT0080.cutoff = 0.10000000149011612
    ACT0080.device_custom = "default3D"
    ACT0080.loop_count = 0
    ACT0080.pitch = 1.0
    ACT0080.volume = 1.0
    ACT0080.attenuation = 1.0
    ACT0080.distance_ref = 1.0
    ACT0080.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0080.cone_outer_volume = 0.0
    ACT0081.condition = CON0071
    ACT0081.speaker = "NLO:CharacterController"
    ACT0081.sound = "D:/Sonic BGE Project/sounds/footsteps/002_metalpl/00_sn_walk_mtlp_4.wav"
    ACT0081.occlusion = False
    ACT0081.transition = 0.10000000149011612
    ACT0081.cutoff = 0.10000000149011612
    ACT0081.device_custom = "default3D"
    ACT0081.loop_count = 0
    ACT0081.pitch = 1.0
    ACT0081.volume = 1.0
    ACT0081.attenuation = 1.0
    ACT0081.distance_ref = 1.0
    ACT0081.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0081.cone_outer_volume = 0.0
    ACT0082.condition = CON0072
    ACT0082.speaker = "NLO:CharacterController"
    ACT0082.sound = "D:/Sonic BGE Project/sounds/footsteps/002_metalpl/00_sn_walk_mtlp_5.wav"
    ACT0082.occlusion = False
    ACT0082.transition = 0.10000000149011612
    ACT0082.cutoff = 0.10000000149011612
    ACT0082.device_custom = "default3D"
    ACT0082.loop_count = 0
    ACT0082.pitch = 1.0
    ACT0082.volume = 1.0
    ACT0082.attenuation = 1.0
    ACT0082.distance_ref = 1.0
    ACT0082.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0082.cone_outer_volume = 0.0
    CON0083.game_object = "NLO:U_O"
    CON0083.property_name = "step_ground"
    CON0083.compare_value = "metal"
    CON0083.operator = 0
    CON0084.game_object = "NLO:U_O"
    CON0084.property_name = "number_footstep"
    CON0084.compare_value = 1
    CON0084.operator = 0
    network.add_cell(CON0000)
    network.add_cell(CON0002)
    network.add_cell(CON0008)
    network.add_cell(CON0011)
    network.add_cell(CON0013)
    network.add_cell(PAR0017)
    network.add_cell(CON0031)
    network.add_cell(CON0033)
    network.add_cell(CON0035)
    network.add_cell(CON0053)
    network.add_cell(CON0055)
    network.add_cell(CON0057)
    network.add_cell(CON0062)
    network.add_cell(CON0064)
    network.add_cell(CON0066)
    network.add_cell(CON0083)
    network.add_cell(CON0001)
    network.add_cell(CON0004)
    network.add_cell(CON0006)
    network.add_cell(PAR0010)
    network.add_cell(ACT0014)
    network.add_cell(ACT0018)
    network.add_cell(ACT0030)
    network.add_cell(CON0034)
    network.add_cell(CON0051)
    network.add_cell(CON0054)
    network.add_cell(CON0058)
    network.add_cell(CON0061)
    network.add_cell(CON0065)
    network.add_cell(CON0074)
    network.add_cell(CON0076)
    network.add_cell(CON0084)
    network.add_cell(CON0003)
    network.add_cell(ACT0007)
    network.add_cell(ACT0012)
    network.add_cell(ACT0016)
    network.add_cell(CON0032)
    network.add_cell(CON0056)
    network.add_cell(CON0060)
    network.add_cell(CON0067)
    network.add_cell(CON0073)
    network.add_cell(CON0077)
    network.add_cell(CON0005)
    network.add_cell(CON0015)
    network.add_cell(CON0036)
    network.add_cell(CON0038)
    network.add_cell(CON0040)
    network.add_cell(ACT0042)
    network.add_cell(CON0049)
    network.add_cell(CON0052)
    network.add_cell(CON0063)
    network.add_cell(CON0069)
    network.add_cell(CON0071)
    network.add_cell(CON0075)
    network.add_cell(ACT0079)
    network.add_cell(ACT0081)
    network.add_cell(ACT0009)
    network.add_cell(CON0020)
    network.add_cell(CON0024)
    network.add_cell(ACT0026)
    network.add_cell(ACT0028)
    network.add_cell(CON0037)
    network.add_cell(CON0041)
    network.add_cell(ACT0046)
    network.add_cell(CON0050)
    network.add_cell(CON0068)
    network.add_cell(CON0072)
    network.add_cell(ACT0082)
    network.add_cell(ACT0019)
    network.add_cell(CON0023)
    network.add_cell(CON0039)
    network.add_cell(ACT0045)
    network.add_cell(CON0059)
    network.add_cell(ACT0078)
    network.add_cell(CON0021)
    network.add_cell(ACT0025)
    network.add_cell(ACT0029)
    network.add_cell(ACT0047)
    network.add_cell(CON0070)
    network.add_cell(CON0022)
    network.add_cell(ACT0043)
    network.add_cell(CON0048)
    network.add_cell(ACT0027)
    network.add_cell(ACT0080)
    network.add_cell(ACT0044)
    owner["IGNLTree_footstep"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__footstep')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_footstep")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
