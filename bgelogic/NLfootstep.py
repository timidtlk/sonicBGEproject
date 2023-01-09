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
    ACT0011 = nodes.ActionSetGameObjectGameProperty()
    CON0012 = nodes.ObjectPropertyOperator()
    ACT0013 = nodes.ActionTimeFilter()
    CON0014 = nodes.ConditionOrList()
    ACT0015 = nodes.ActionSetGameObjectGameProperty()
    PAR0016 = nodes.ParameterObjectProperty()
    ACT0017 = nodes.ActionSetGameObjectGameProperty()
    ACT0018 = nodes.ActionSetGameObjectGameProperty()
    CON0019 = nodes.ConditionAnd()
    CON0020 = nodes.ConditionAnd()
    CON0021 = nodes.ConditionAnd()
    CON0022 = nodes.ConditionAnd()
    CON0023 = nodes.ConditionAnd()
    ACT0024 = nodes.ActionStart3DSoundAdv()
    ACT0025 = nodes.ActionStart3DSoundAdv()
    ACT0026 = nodes.ActionStart3DSoundAdv()
    ACT0027 = nodes.ActionStart3DSoundAdv()
    ACT0028 = nodes.ActionStart3DSoundAdv()
    ACT0029 = nodes.ActionSetGameObjectGameProperty()
    CON0030 = nodes.ObjectPropertyOperator()
    CON0031 = nodes.ObjectPropertyOperator()
    CON0032 = nodes.ObjectPropertyOperator()
    CON0033 = nodes.ObjectPropertyOperator()
    CON0034 = nodes.ObjectPropertyOperator()
    CON0035 = nodes.ObjectPropertyOperator()
    CON0036 = nodes.ConditionAnd()
    CON0037 = nodes.ConditionAnd()
    CON0038 = nodes.ConditionAnd()
    CON0039 = nodes.ConditionAnd()
    CON0040 = nodes.ConditionAnd()
    ACT0041 = nodes.ActionStart3DSoundAdv()
    ACT0042 = nodes.ActionStart3DSoundAdv()
    ACT0043 = nodes.ActionStart3DSoundAdv()
    ACT0044 = nodes.ActionStart3DSoundAdv()
    ACT0045 = nodes.ActionStart3DSoundAdv()
    CON0046 = nodes.ConditionAnd()
    CON0047 = nodes.ConditionAnd()
    CON0048 = nodes.ConditionAnd()
    CON0049 = nodes.ConditionAnd()
    CON0050 = nodes.ConditionAnd()
    CON0051 = nodes.ObjectPropertyOperator()
    CON0052 = nodes.ObjectPropertyOperator()
    CON0053 = nodes.ObjectPropertyOperator()
    CON0054 = nodes.ObjectPropertyOperator()
    CON0055 = nodes.ObjectPropertyOperator()
    CON0056 = nodes.ConditionAnd()
    CON0057 = nodes.ConditionAnd()
    CON0058 = nodes.ConditionAnd()
    CON0059 = nodes.ConditionAnd()
    CON0060 = nodes.ObjectPropertyOperator()
    CON0061 = nodes.ConditionAnd()
    CON0062 = nodes.ObjectPropertyOperator()
    CON0063 = nodes.ObjectPropertyOperator()
    CON0064 = nodes.ObjectPropertyOperator()
    CON0065 = nodes.ObjectPropertyOperator()
    CON0066 = nodes.ConditionAnd()
    CON0067 = nodes.ConditionAnd()
    CON0068 = nodes.ConditionAnd()
    CON0069 = nodes.ConditionAnd()
    CON0070 = nodes.ConditionAnd()
    CON0071 = nodes.ConditionAnd()
    CON0072 = nodes.ConditionAnd()
    CON0073 = nodes.ConditionAnd()
    CON0074 = nodes.ConditionAnd()
    CON0075 = nodes.ConditionAnd()
    ACT0076 = nodes.ActionStart3DSoundAdv()
    ACT0077 = nodes.ActionStart3DSoundAdv()
    ACT0078 = nodes.ActionStart3DSoundAdv()
    ACT0079 = nodes.ActionStart3DSoundAdv()
    ACT0080 = nodes.ActionStart3DSoundAdv()
    CON0081 = nodes.ObjectPropertyOperator()
    CON0082 = nodes.ObjectPropertyOperator()
    CON0083 = nodes.ObjectPropertyOperator()
    CON0084 = nodes.ObjectPropertyOperator()
    CON0085 = nodes.ObjectPropertyOperator()
    CON0086 = nodes.ObjectPropertyOperator()
    CON0087 = nodes.ConditionAnd()
    CON0088 = nodes.ConditionAnd()
    CON0089 = nodes.ConditionAnd()
    CON0090 = nodes.ConditionAnd()
    CON0091 = nodes.ConditionAnd()
    CON0092 = nodes.ObjectPropertyOperator()
    CON0093 = nodes.ConditionCollision()
    ACT0094 = nodes.ActionTimeFilter()
    CON0095 = nodes.ObjectPropertyOperator()
    CON0096 = nodes.ConditionAnd()
    CON0097 = nodes.ConditionAnd()
    CON0098 = nodes.ConditionAnd()
    CON0099 = nodes.ConditionAnd()
    CON0100 = nodes.ConditionAnd()
    ACT0101 = nodes.ActionStart3DSoundAdv()
    ACT0102 = nodes.ActionStart3DSoundAdv()
    ACT0103 = nodes.ActionStart3DSoundAdv()
    ACT0104 = nodes.ActionStart3DSoundAdv()
    ACT0105 = nodes.ActionStart3DSoundAdv()
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
    CON0003.condition_a = CON0093
    CON0003.condition_b = CON0012
    CON0004.condition_a = CON0093
    CON0004.condition_b = CON0000
    CON0005.condition_a = CON0093
    CON0005.condition_b = CON0001
    CON0006.condition_a = CON0093
    CON0006.condition_b = CON0002
    ACT0007.condition = ACT0013
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
    PAR0010.game_object = CON0093.TARGET
    PAR0010.property_name = "type"
    ACT0011.condition = CON0093
    ACT0011.game_object = "NLO:U_O"
    ACT0011.property_name = "step_ground"
    ACT0011.property_value = PAR0010
    CON0012.game_object = "NLO:U_O"
    CON0012.property_name = "animation"
    CON0012.compare_value = "walk"
    CON0012.operator = 0
    ACT0013.condition = CON0008
    ACT0013.delay = PAR0016
    CON0014.ca = CON0003
    CON0014.cb = CON0004
    CON0014.cc = CON0005
    CON0014.cd = CON0006
    CON0014.ce = None
    CON0014.cf = None
    ACT0015.condition = CON0003
    ACT0015.game_object = "NLO:U_O"
    ACT0015.property_name = "footstep_time"
    ACT0015.property_value = 0.30000001192092896
    PAR0016.game_object = "NLO:U_O"
    PAR0016.property_name = "footstep_time"
    ACT0017.condition = CON0004
    ACT0017.game_object = "NLO:U_O"
    ACT0017.property_name = "footstep_time"
    ACT0017.property_value = 0.20000000298023224
    ACT0018.condition = CON0005
    ACT0018.game_object = "NLO:U_O"
    ACT0018.property_name = "footstep_time"
    ACT0018.property_value = 0.10000000149011612
    CON0019.condition_a = ACT0094
    CON0019.condition_b = CON0039
    CON0020.condition_a = ACT0094
    CON0020.condition_b = CON0040
    CON0021.condition_a = ACT0094
    CON0021.condition_b = CON0038
    CON0022.condition_a = ACT0094
    CON0022.condition_b = CON0036
    CON0023.condition_a = ACT0094
    CON0023.condition_b = CON0037
    ACT0024.condition = CON0022
    ACT0024.speaker = "NLO:CharacterController"
    ACT0024.sound = "D:/Sonic BGE Project/sounds/footsteps/001_conc/00_sn_walk_conc_1.wav"
    ACT0024.occlusion = False
    ACT0024.transition = 0.10000000149011612
    ACT0024.cutoff = 0.10000000149011612
    ACT0024.device_custom = "default3D"
    ACT0024.loop_count = 0
    ACT0024.pitch = 1.0
    ACT0024.volume = 1.0
    ACT0024.attenuation = 1.0
    ACT0024.distance_ref = 1.0
    ACT0024.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0024.cone_outer_volume = 0.0
    ACT0025.condition = CON0023
    ACT0025.speaker = "NLO:CharacterController"
    ACT0025.sound = "D:/Sonic BGE Project/sounds/footsteps/001_conc/00_sn_walk_conc_2.wav"
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
    ACT0026.condition = CON0021
    ACT0026.speaker = "NLO:CharacterController"
    ACT0026.sound = "D:/Sonic BGE Project/sounds/footsteps/001_conc/00_sn_walk_conc_3.wav"
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
    ACT0027.condition = CON0019
    ACT0027.speaker = "NLO:CharacterController"
    ACT0027.sound = "D:/Sonic BGE Project/sounds/footsteps/001_conc/00_sn_walk_conc_4.wav"
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
    ACT0028.sound = "D:/Sonic BGE Project/sounds/footsteps/001_conc/00_sn_walk_conc_5.wav"
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
    ACT0029.condition = CON0006
    ACT0029.game_object = "NLO:U_O"
    ACT0029.property_name = "footstep_time"
    ACT0029.property_value = 0.07999999821186066
    CON0030.game_object = "NLO:U_O"
    CON0030.property_name = "number_footstep"
    CON0030.compare_value = 1
    CON0030.operator = 0
    CON0031.game_object = "NLO:U_O"
    CON0031.property_name = "number_footstep"
    CON0031.compare_value = 2
    CON0031.operator = 0
    CON0032.game_object = "NLO:U_O"
    CON0032.property_name = "number_footstep"
    CON0032.compare_value = 3
    CON0032.operator = 0
    CON0033.game_object = "NLO:U_O"
    CON0033.property_name = "number_footstep"
    CON0033.compare_value = 4
    CON0033.operator = 0
    CON0034.game_object = "NLO:U_O"
    CON0034.property_name = "number_footstep"
    CON0034.compare_value = 5
    CON0034.operator = 0
    CON0035.game_object = "NLO:U_O"
    CON0035.property_name = "step_ground"
    CON0035.compare_value = "concrete"
    CON0035.operator = 0
    CON0036.condition_a = CON0035
    CON0036.condition_b = CON0030
    CON0037.condition_a = CON0035
    CON0037.condition_b = CON0031
    CON0038.condition_a = CON0035
    CON0038.condition_b = CON0032
    CON0039.condition_a = CON0035
    CON0039.condition_b = CON0033
    CON0040.condition_a = CON0035
    CON0040.condition_b = CON0034
    ACT0041.condition = CON0047
    ACT0041.speaker = "NLO:CharacterController"
    ACT0041.sound = "D:/Sonic BGE Project/sounds/footsteps/004_wood/00_sn_walk_wood_5.wav"
    ACT0041.occlusion = False
    ACT0041.transition = 0.10000000149011612
    ACT0041.cutoff = 0.10000000149011612
    ACT0041.device_custom = "default3D"
    ACT0041.loop_count = 0
    ACT0041.pitch = 1.0
    ACT0041.volume = 1.0
    ACT0041.attenuation = 1.0
    ACT0041.distance_ref = 1.0
    ACT0041.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0041.cone_outer_volume = 0.0
    ACT0042.condition = CON0046
    ACT0042.speaker = "NLO:CharacterController"
    ACT0042.sound = "D:/Sonic BGE Project/sounds/footsteps/004_wood/00_sn_walk_wood_5.wav"
    ACT0042.occlusion = False
    ACT0042.transition = 0.10000000149011612
    ACT0042.cutoff = 0.10000000149011612
    ACT0042.device_custom = "default3D"
    ACT0042.loop_count = 0
    ACT0042.pitch = 1.0
    ACT0042.volume = 1.0
    ACT0042.attenuation = 1.0
    ACT0042.distance_ref = 1.0
    ACT0042.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0042.cone_outer_volume = 0.0
    ACT0043.condition = CON0048
    ACT0043.speaker = "NLO:CharacterController"
    ACT0043.sound = "D:/Sonic BGE Project/sounds/footsteps/004_wood/00_sn_walk_wood_3.wav"
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
    ACT0044.condition = CON0050
    ACT0044.speaker = "NLO:CharacterController"
    ACT0044.sound = "D:/Sonic BGE Project/sounds/footsteps/004_wood/00_sn_walk_wood_2.wav"
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
    ACT0045.condition = CON0061
    ACT0045.speaker = "NLO:CharacterController"
    ACT0045.sound = "D:/Sonic BGE Project/sounds/footsteps/004_wood/00_sn_walk_wood_1.wav"
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
    CON0046.condition_a = ACT0094
    CON0046.condition_b = CON0057
    CON0047.condition_a = ACT0094
    CON0047.condition_b = CON0058
    CON0048.condition_a = ACT0094
    CON0048.condition_b = CON0059
    CON0049.condition_a = CON0060
    CON0049.condition_b = CON0055
    CON0050.condition_a = ACT0094
    CON0050.condition_b = CON0056
    CON0051.game_object = "NLO:U_O"
    CON0051.property_name = "number_footstep"
    CON0051.compare_value = 2
    CON0051.operator = 0
    CON0052.game_object = "NLO:U_O"
    CON0052.property_name = "number_footstep"
    CON0052.compare_value = 3
    CON0052.operator = 0
    CON0053.game_object = "NLO:U_O"
    CON0053.property_name = "number_footstep"
    CON0053.compare_value = 4
    CON0053.operator = 0
    CON0054.game_object = "NLO:U_O"
    CON0054.property_name = "number_footstep"
    CON0054.compare_value = 5
    CON0054.operator = 0
    CON0055.game_object = "NLO:U_O"
    CON0055.property_name = "number_footstep"
    CON0055.compare_value = 1
    CON0055.operator = 0
    CON0056.condition_a = CON0060
    CON0056.condition_b = CON0051
    CON0057.condition_a = CON0060
    CON0057.condition_b = CON0053
    CON0058.condition_a = CON0060
    CON0058.condition_b = CON0054
    CON0059.condition_a = CON0060
    CON0059.condition_b = CON0052
    CON0060.game_object = "NLO:U_O"
    CON0060.property_name = "step_ground"
    CON0060.compare_value = "wood"
    CON0060.operator = 0
    CON0061.condition_a = ACT0094
    CON0061.condition_b = CON0049
    CON0062.game_object = "NLO:U_O"
    CON0062.property_name = "number_footstep"
    CON0062.compare_value = 2
    CON0062.operator = 0
    CON0063.game_object = "NLO:U_O"
    CON0063.property_name = "number_footstep"
    CON0063.compare_value = 3
    CON0063.operator = 0
    CON0064.game_object = "NLO:U_O"
    CON0064.property_name = "number_footstep"
    CON0064.compare_value = 4
    CON0064.operator = 0
    CON0065.game_object = "NLO:U_O"
    CON0065.property_name = "number_footstep"
    CON0065.compare_value = 5
    CON0065.operator = 0
    CON0066.condition_a = ACT0094
    CON0066.condition_b = CON0071
    CON0067.condition_a = ACT0094
    CON0067.condition_b = CON0072
    CON0068.condition_a = ACT0094
    CON0068.condition_b = CON0073
    CON0069.condition_a = ACT0094
    CON0069.condition_b = CON0074
    CON0070.condition_a = ACT0094
    CON0070.condition_b = CON0075
    CON0071.condition_a = CON0081
    CON0071.condition_b = CON0082
    CON0072.condition_a = CON0081
    CON0072.condition_b = CON0062
    CON0073.condition_a = CON0081
    CON0073.condition_b = CON0063
    CON0074.condition_a = CON0081
    CON0074.condition_b = CON0064
    CON0075.condition_a = CON0081
    CON0075.condition_b = CON0065
    ACT0076.condition = CON0066
    ACT0076.speaker = "NLO:CharacterController"
    ACT0076.sound = "D:/Sonic BGE Project/sounds/footsteps/002_metalpl/00_sn_walk_mtlp_1.wav"
    ACT0076.occlusion = False
    ACT0076.transition = 0.10000000149011612
    ACT0076.cutoff = 0.10000000149011612
    ACT0076.device_custom = "default3D"
    ACT0076.loop_count = 0
    ACT0076.pitch = 1.0
    ACT0076.volume = 1.0
    ACT0076.attenuation = 1.0
    ACT0076.distance_ref = 1.0
    ACT0076.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0076.cone_outer_volume = 0.0
    ACT0077.condition = CON0067
    ACT0077.speaker = "NLO:CharacterController"
    ACT0077.sound = "D:/Sonic BGE Project/sounds/footsteps/002_metalpl/00_sn_walk_mtlp_2.wav"
    ACT0077.occlusion = False
    ACT0077.transition = 0.10000000149011612
    ACT0077.cutoff = 0.10000000149011612
    ACT0077.device_custom = "default3D"
    ACT0077.loop_count = 0
    ACT0077.pitch = 1.0
    ACT0077.volume = 1.0
    ACT0077.attenuation = 1.0
    ACT0077.distance_ref = 1.0
    ACT0077.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0077.cone_outer_volume = 0.0
    ACT0078.condition = CON0068
    ACT0078.speaker = "NLO:CharacterController"
    ACT0078.sound = "D:/Sonic BGE Project/sounds/footsteps/002_metalpl/00_sn_walk_mtlp_3.wav"
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
    ACT0079.sound = "D:/Sonic BGE Project/sounds/footsteps/002_metalpl/00_sn_walk_mtlp_4.wav"
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
    ACT0080.sound = "D:/Sonic BGE Project/sounds/footsteps/002_metalpl/00_sn_walk_mtlp_5.wav"
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
    CON0081.game_object = "NLO:U_O"
    CON0081.property_name = "step_ground"
    CON0081.compare_value = "metal"
    CON0081.operator = 0
    CON0082.game_object = "NLO:U_O"
    CON0082.property_name = "number_footstep"
    CON0082.compare_value = 1
    CON0082.operator = 0
    CON0083.game_object = "NLO:U_O"
    CON0083.property_name = "number_footstep"
    CON0083.compare_value = 2
    CON0083.operator = 0
    CON0084.game_object = "NLO:U_O"
    CON0084.property_name = "number_footstep"
    CON0084.compare_value = 3
    CON0084.operator = 0
    CON0085.game_object = "NLO:U_O"
    CON0085.property_name = "number_footstep"
    CON0085.compare_value = 4
    CON0085.operator = 0
    CON0086.game_object = "NLO:U_O"
    CON0086.property_name = "number_footstep"
    CON0086.compare_value = 5
    CON0086.operator = 0
    CON0087.condition_a = ACT0094
    CON0087.condition_b = CON0096
    CON0088.condition_a = ACT0094
    CON0088.condition_b = CON0097
    CON0089.condition_a = ACT0094
    CON0089.condition_b = CON0098
    CON0090.condition_a = ACT0094
    CON0090.condition_b = CON0099
    CON0091.condition_a = ACT0094
    CON0091.condition_b = CON0100
    CON0092.game_object = "NLO:U_O"
    CON0092.property_name = "number_footstep"
    CON0092.compare_value = 1
    CON0092.operator = 0
    CON0093.game_object = "NLO:CharacterController"
    CON0093.use_mat = False
    CON0093.prop = "type"
    CON0093.material = None
    CON0093.pulse = True
    ACT0094.condition = CON0014
    ACT0094.delay = PAR0016
    CON0095.game_object = "NLO:U_O"
    CON0095.property_name = "step_ground"
    CON0095.compare_value = "water"
    CON0095.operator = 0
    CON0096.condition_a = CON0095
    CON0096.condition_b = CON0092
    CON0097.condition_a = CON0095
    CON0097.condition_b = CON0083
    CON0098.condition_a = CON0095
    CON0098.condition_b = CON0084
    CON0099.condition_a = CON0095
    CON0099.condition_b = CON0085
    CON0100.condition_a = CON0095
    CON0100.condition_b = CON0086
    ACT0101.condition = CON0087
    ACT0101.speaker = "NLO:CharacterController"
    ACT0101.sound = "D:/Sonic BGE Project/sounds/footsteps/007_water/00_sn_walk_watr_1.wav"
    ACT0101.occlusion = False
    ACT0101.transition = 0.10000000149011612
    ACT0101.cutoff = 0.10000000149011612
    ACT0101.device_custom = "default3D"
    ACT0101.loop_count = 0
    ACT0101.pitch = 1.0
    ACT0101.volume = 1.0
    ACT0101.attenuation = 1.0
    ACT0101.distance_ref = 1.0
    ACT0101.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0101.cone_outer_volume = 0.0
    ACT0102.condition = CON0088
    ACT0102.speaker = "NLO:CharacterController"
    ACT0102.sound = "D:/Sonic BGE Project/sounds/footsteps/007_water/00_sn_walk_watr_2.wav"
    ACT0102.occlusion = False
    ACT0102.transition = 0.10000000149011612
    ACT0102.cutoff = 0.10000000149011612
    ACT0102.device_custom = "default3D"
    ACT0102.loop_count = 0
    ACT0102.pitch = 1.0
    ACT0102.volume = 1.0
    ACT0102.attenuation = 1.0
    ACT0102.distance_ref = 1.0
    ACT0102.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0102.cone_outer_volume = 0.0
    ACT0103.condition = CON0089
    ACT0103.speaker = "NLO:CharacterController"
    ACT0103.sound = "D:/Sonic BGE Project/sounds/footsteps/007_water/00_sn_walk_watr_3.wav"
    ACT0103.occlusion = False
    ACT0103.transition = 0.10000000149011612
    ACT0103.cutoff = 0.10000000149011612
    ACT0103.device_custom = "default3D"
    ACT0103.loop_count = 0
    ACT0103.pitch = 1.0
    ACT0103.volume = 1.0
    ACT0103.attenuation = 1.0
    ACT0103.distance_ref = 1.0
    ACT0103.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0103.cone_outer_volume = 0.0
    ACT0104.condition = CON0090
    ACT0104.speaker = "NLO:CharacterController"
    ACT0104.sound = "D:/Sonic BGE Project/sounds/footsteps/007_water/00_sn_walk_watr_4.wav"
    ACT0104.occlusion = False
    ACT0104.transition = 0.10000000149011612
    ACT0104.cutoff = 0.10000000149011612
    ACT0104.device_custom = "default3D"
    ACT0104.loop_count = 0
    ACT0104.pitch = 1.0
    ACT0104.volume = 1.0
    ACT0104.attenuation = 1.0
    ACT0104.distance_ref = 1.0
    ACT0104.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0104.cone_outer_volume = 0.0
    ACT0105.condition = CON0091
    ACT0105.speaker = "NLO:CharacterController"
    ACT0105.sound = "D:/Sonic BGE Project/sounds/footsteps/007_water/00_sn_walk_watr_5.wav"
    ACT0105.occlusion = False
    ACT0105.transition = 0.10000000149011612
    ACT0105.cutoff = 0.10000000149011612
    ACT0105.device_custom = "default3D"
    ACT0105.loop_count = 0
    ACT0105.pitch = 1.0
    ACT0105.volume = 1.0
    ACT0105.attenuation = 1.0
    ACT0105.distance_ref = 1.0
    ACT0105.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0105.cone_outer_volume = 0.0
    network.add_cell(CON0000)
    network.add_cell(CON0002)
    network.add_cell(CON0008)
    network.add_cell(CON0012)
    network.add_cell(PAR0016)
    network.add_cell(CON0030)
    network.add_cell(CON0032)
    network.add_cell(CON0034)
    network.add_cell(CON0051)
    network.add_cell(CON0053)
    network.add_cell(CON0055)
    network.add_cell(CON0060)
    network.add_cell(CON0062)
    network.add_cell(CON0064)
    network.add_cell(CON0081)
    network.add_cell(CON0083)
    network.add_cell(CON0085)
    network.add_cell(CON0092)
    network.add_cell(CON0095)
    network.add_cell(CON0097)
    network.add_cell(CON0099)
    network.add_cell(CON0001)
    network.add_cell(ACT0013)
    network.add_cell(CON0031)
    network.add_cell(CON0035)
    network.add_cell(CON0037)
    network.add_cell(CON0040)
    network.add_cell(CON0049)
    network.add_cell(CON0052)
    network.add_cell(CON0056)
    network.add_cell(CON0059)
    network.add_cell(CON0063)
    network.add_cell(CON0072)
    network.add_cell(CON0074)
    network.add_cell(CON0082)
    network.add_cell(CON0086)
    network.add_cell(CON0093)
    network.add_cell(CON0096)
    network.add_cell(CON0100)
    network.add_cell(CON0003)
    network.add_cell(CON0005)
    network.add_cell(ACT0007)
    network.add_cell(PAR0010)
    network.add_cell(ACT0015)
    network.add_cell(ACT0018)
    network.add_cell(CON0033)
    network.add_cell(CON0038)
    network.add_cell(CON0054)
    network.add_cell(CON0058)
    network.add_cell(CON0065)
    network.add_cell(CON0071)
    network.add_cell(CON0075)
    network.add_cell(CON0084)
    network.add_cell(CON0098)
    network.add_cell(CON0004)
    network.add_cell(ACT0009)
    network.add_cell(ACT0017)
    network.add_cell(CON0036)
    network.add_cell(CON0057)
    network.add_cell(CON0073)
    network.add_cell(CON0006)
    network.add_cell(CON0014)
    network.add_cell(ACT0029)
    network.add_cell(ACT0094)
    network.add_cell(ACT0011)
    network.add_cell(CON0020)
    network.add_cell(CON0022)
    network.add_cell(ACT0024)
    network.add_cell(ACT0028)
    network.add_cell(CON0046)
    network.add_cell(CON0048)
    network.add_cell(CON0061)
    network.add_cell(CON0067)
    network.add_cell(CON0069)
    network.add_cell(ACT0077)
    network.add_cell(ACT0079)
    network.add_cell(CON0087)
    network.add_cell(CON0089)
    network.add_cell(CON0091)
    network.add_cell(ACT0103)
    network.add_cell(ACT0105)
    network.add_cell(CON0021)
    network.add_cell(ACT0026)
    network.add_cell(CON0039)
    network.add_cell(ACT0042)
    network.add_cell(ACT0045)
    network.add_cell(CON0050)
    network.add_cell(CON0068)
    network.add_cell(ACT0078)
    network.add_cell(CON0088)
    network.add_cell(ACT0101)
    network.add_cell(CON0019)
    network.add_cell(ACT0027)
    network.add_cell(ACT0043)
    network.add_cell(CON0047)
    network.add_cell(CON0070)
    network.add_cell(ACT0080)
    network.add_cell(ACT0102)
    network.add_cell(CON0023)
    network.add_cell(ACT0041)
    network.add_cell(CON0066)
    network.add_cell(CON0090)
    network.add_cell(ACT0025)
    network.add_cell(ACT0076)
    network.add_cell(ACT0044)
    network.add_cell(ACT0104)
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
