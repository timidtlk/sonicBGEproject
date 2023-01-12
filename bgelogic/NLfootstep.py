# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    CON0000 = nodes.ObjectPropertyOperator()
    CON0001 = nodes.ObjectPropertyOperator()
    CON0002 = nodes.ConditionAnd()
    CON0003 = nodes.ConditionAnd()
    CON0004 = nodes.ConditionAnd()
    ACT0005 = nodes.ActionRandomInt()
    CON0006 = nodes.ObjectPropertyOperator()
    ACT0007 = nodes.ActionSetGameObjectGameProperty()
    ACT0008 = nodes.ActionTimeFilter()
    CON0009 = nodes.ConditionOrList()
    ACT0010 = nodes.ActionSetGameObjectGameProperty()
    PAR0011 = nodes.ParameterObjectProperty()
    ACT0012 = nodes.ActionSetGameObjectGameProperty()
    ACT0013 = nodes.ActionSetGameObjectGameProperty()
    CON0014 = nodes.ConditionAnd()
    CON0015 = nodes.ConditionAnd()
    CON0016 = nodes.ConditionAnd()
    CON0017 = nodes.ConditionAnd()
    CON0018 = nodes.ConditionAnd()
    ACT0019 = nodes.ActionStart3DSoundAdv()
    ACT0020 = nodes.ActionStart3DSoundAdv()
    ACT0021 = nodes.ActionStart3DSoundAdv()
    ACT0022 = nodes.ActionStart3DSoundAdv()
    ACT0023 = nodes.ActionStart3DSoundAdv()
    ACT0024 = nodes.ActionSetGameObjectGameProperty()
    CON0025 = nodes.ObjectPropertyOperator()
    CON0026 = nodes.ObjectPropertyOperator()
    CON0027 = nodes.ObjectPropertyOperator()
    CON0028 = nodes.ObjectPropertyOperator()
    CON0029 = nodes.ObjectPropertyOperator()
    CON0030 = nodes.ConditionAnd()
    CON0031 = nodes.ConditionAnd()
    CON0032 = nodes.ConditionAnd()
    CON0033 = nodes.ConditionAnd()
    CON0034 = nodes.ConditionAnd()
    ACT0035 = nodes.ActionStart3DSoundAdv()
    ACT0036 = nodes.ActionStart3DSoundAdv()
    ACT0037 = nodes.ActionStart3DSoundAdv()
    ACT0038 = nodes.ActionStart3DSoundAdv()
    ACT0039 = nodes.ActionStart3DSoundAdv()
    CON0040 = nodes.ConditionAnd()
    CON0041 = nodes.ConditionAnd()
    CON0042 = nodes.ConditionAnd()
    CON0043 = nodes.ConditionAnd()
    CON0044 = nodes.ConditionAnd()
    CON0045 = nodes.ObjectPropertyOperator()
    CON0046 = nodes.ObjectPropertyOperator()
    CON0047 = nodes.ObjectPropertyOperator()
    CON0048 = nodes.ObjectPropertyOperator()
    CON0049 = nodes.ObjectPropertyOperator()
    CON0050 = nodes.ConditionAnd()
    CON0051 = nodes.ConditionAnd()
    CON0052 = nodes.ConditionAnd()
    CON0053 = nodes.ConditionAnd()
    CON0054 = nodes.ObjectPropertyOperator()
    CON0055 = nodes.ConditionAnd()
    CON0056 = nodes.ObjectPropertyOperator()
    CON0057 = nodes.ObjectPropertyOperator()
    CON0058 = nodes.ObjectPropertyOperator()
    CON0059 = nodes.ObjectPropertyOperator()
    CON0060 = nodes.ConditionAnd()
    CON0061 = nodes.ConditionAnd()
    CON0062 = nodes.ConditionAnd()
    CON0063 = nodes.ConditionAnd()
    CON0064 = nodes.ConditionAnd()
    CON0065 = nodes.ConditionAnd()
    CON0066 = nodes.ConditionAnd()
    CON0067 = nodes.ConditionAnd()
    CON0068 = nodes.ConditionAnd()
    CON0069 = nodes.ConditionAnd()
    ACT0070 = nodes.ActionStart3DSoundAdv()
    ACT0071 = nodes.ActionStart3DSoundAdv()
    ACT0072 = nodes.ActionStart3DSoundAdv()
    ACT0073 = nodes.ActionStart3DSoundAdv()
    ACT0074 = nodes.ActionStart3DSoundAdv()
    CON0075 = nodes.ObjectPropertyOperator()
    CON0076 = nodes.ObjectPropertyOperator()
    CON0077 = nodes.ObjectPropertyOperator()
    CON0078 = nodes.ObjectPropertyOperator()
    CON0079 = nodes.ObjectPropertyOperator()
    CON0080 = nodes.ConditionAnd()
    CON0081 = nodes.ConditionAnd()
    CON0082 = nodes.ConditionAnd()
    CON0083 = nodes.ConditionAnd()
    CON0084 = nodes.ConditionAnd()
    CON0085 = nodes.ObjectPropertyOperator()
    ACT0086 = nodes.ActionTimeFilter()
    CON0087 = nodes.ObjectPropertyOperator()
    CON0088 = nodes.ConditionAnd()
    CON0089 = nodes.ConditionAnd()
    CON0090 = nodes.ConditionAnd()
    CON0091 = nodes.ConditionAnd()
    CON0092 = nodes.ConditionAnd()
    ACT0093 = nodes.ActionStart3DSoundAdv()
    ACT0094 = nodes.ActionStart3DSoundAdv()
    ACT0095 = nodes.ActionStart3DSoundAdv()
    ACT0096 = nodes.ActionStart3DSoundAdv()
    ACT0097 = nodes.ActionStart3DSoundAdv()
    CON0098 = nodes.ObjectPropertyOperator()
    CON0099 = nodes.ConditionAnd()
    CON0100 = nodes.ObjectPropertyOperator()
    PAR0101 = nodes.ParameterObjectAttribute()
    PAR0102 = nodes.ParameterObjectAttribute()
    CON0103 = nodes.ConditionOnUpdate()
    CON0104 = nodes.ConditionCollision()
    PAR0105 = nodes.ParameterObjectProperty()
    ACT0106 = nodes.ActionSetGameObjectGameProperty()
    CON0107 = nodes.ObjectPropertyOperator()
    CON0108 = nodes.ObjectPropertyOperator()
    ACT0109 = nodes.ActionStopSound()
    PAR0110 = nodes.ParameterObjectProperty()
    CON0111 = nodes.ObjectPropertyOperator()
    ACT0112 = nodes.ActionTimeFilter()
    CON0113 = nodes.ConditionValueTrigger()
    ACT0114 = nodes.ActionTimeFilter()
    ACT0115 = nodes.ActionStart3DSoundAdv()
    ACT0116 = nodes.ActionRayPick()
    CON0000.game_object = "NLO:U_O"
    CON0000.property_name = "animation"
    CON0000.compare_value = "jet"
    CON0000.operator = 0
    CON0001.game_object = "NLO:U_O"
    CON0001.property_name = "animation"
    CON0001.compare_value = "boost"
    CON0001.operator = 0
    CON0002.condition_a = ACT0116
    CON0002.condition_b = CON0108
    CON0003.condition_a = ACT0116
    CON0003.condition_b = CON0000
    CON0004.condition_a = ACT0116
    CON0004.condition_b = CON0001
    ACT0005.condition = ACT0008
    ACT0005.max_value = 5
    ACT0005.min_value = 1
    CON0006.game_object = "NLO:CharacterController"
    CON0006.property_name = "animation"
    CON0006.compare_value = "idle"
    CON0006.operator = 1
    ACT0007.condition = ACT0005.DONE
    ACT0007.game_object = "NLO:U_O"
    ACT0007.property_name = "number_footstep"
    ACT0007.property_value = ACT0005.OUT_A
    ACT0008.condition = CON0006
    ACT0008.delay = PAR0011
    CON0009.ca = CON0099
    CON0009.cb = CON0002
    CON0009.cc = CON0003
    CON0009.cd = CON0004
    CON0009.ce = None
    CON0009.cf = None
    ACT0010.condition = CON0099
    ACT0010.game_object = "NLO:U_O"
    ACT0010.property_name = "footstep_time"
    ACT0010.property_value = 0.30000001192092896
    PAR0011.game_object = "NLO:U_O"
    PAR0011.property_name = "footstep_time"
    ACT0012.condition = CON0002
    ACT0012.game_object = "NLO:U_O"
    ACT0012.property_name = "footstep_time"
    ACT0012.property_value = 0.20000000298023224
    ACT0013.condition = CON0003
    ACT0013.game_object = "NLO:U_O"
    ACT0013.property_name = "footstep_time"
    ACT0013.property_value = 0.10000000149011612
    CON0014.condition_a = ACT0086
    CON0014.condition_b = CON0033
    CON0015.condition_a = ACT0086
    CON0015.condition_b = CON0034
    CON0016.condition_a = ACT0086
    CON0016.condition_b = CON0032
    CON0017.condition_a = ACT0086
    CON0017.condition_b = CON0030
    CON0018.condition_a = ACT0086
    CON0018.condition_b = CON0031
    ACT0019.condition = CON0017
    ACT0019.speaker = "NLO:CharacterController"
    ACT0019.sound = "D:/Sonic BGE Project/sounds/footsteps/001_conc/00_sn_walk_conc_1.wav"
    ACT0019.occlusion = False
    ACT0019.transition = 0.10000000149011612
    ACT0019.cutoff = 0.10000000149011612
    ACT0019.device_custom = "default3D"
    ACT0019.loop_count = 0
    ACT0019.pitch = 1.0
    ACT0019.volume = 1.0
    ACT0019.attenuation = 1.0
    ACT0019.distance_ref = 1.0
    ACT0019.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0019.cone_outer_volume = 0.0
    ACT0020.condition = CON0018
    ACT0020.speaker = "NLO:CharacterController"
    ACT0020.sound = "D:/Sonic BGE Project/sounds/footsteps/001_conc/00_sn_walk_conc_2.wav"
    ACT0020.occlusion = False
    ACT0020.transition = 0.10000000149011612
    ACT0020.cutoff = 0.10000000149011612
    ACT0020.device_custom = "default3D"
    ACT0020.loop_count = 0
    ACT0020.pitch = 1.0
    ACT0020.volume = 1.0
    ACT0020.attenuation = 1.0
    ACT0020.distance_ref = 1.0
    ACT0020.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0020.cone_outer_volume = 0.0
    ACT0021.condition = CON0016
    ACT0021.speaker = "NLO:CharacterController"
    ACT0021.sound = "D:/Sonic BGE Project/sounds/footsteps/001_conc/00_sn_walk_conc_3.wav"
    ACT0021.occlusion = False
    ACT0021.transition = 0.10000000149011612
    ACT0021.cutoff = 0.10000000149011612
    ACT0021.device_custom = "default3D"
    ACT0021.loop_count = 0
    ACT0021.pitch = 1.0
    ACT0021.volume = 1.0
    ACT0021.attenuation = 1.0
    ACT0021.distance_ref = 1.0
    ACT0021.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0021.cone_outer_volume = 0.0
    ACT0022.condition = CON0014
    ACT0022.speaker = "NLO:CharacterController"
    ACT0022.sound = "D:/Sonic BGE Project/sounds/footsteps/001_conc/00_sn_walk_conc_4.wav"
    ACT0022.occlusion = False
    ACT0022.transition = 0.10000000149011612
    ACT0022.cutoff = 0.10000000149011612
    ACT0022.device_custom = "default3D"
    ACT0022.loop_count = 0
    ACT0022.pitch = 1.0
    ACT0022.volume = 1.0
    ACT0022.attenuation = 1.0
    ACT0022.distance_ref = 1.0
    ACT0022.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0022.cone_outer_volume = 0.0
    ACT0023.condition = CON0015
    ACT0023.speaker = "NLO:CharacterController"
    ACT0023.sound = "D:/Sonic BGE Project/sounds/footsteps/001_conc/00_sn_walk_conc_5.wav"
    ACT0023.occlusion = False
    ACT0023.transition = 0.10000000149011612
    ACT0023.cutoff = 0.10000000149011612
    ACT0023.device_custom = "default3D"
    ACT0023.loop_count = 0
    ACT0023.pitch = 1.0
    ACT0023.volume = 1.0
    ACT0023.attenuation = 1.0
    ACT0023.distance_ref = 1.0
    ACT0023.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0023.cone_outer_volume = 0.0
    ACT0024.condition = CON0004
    ACT0024.game_object = "NLO:U_O"
    ACT0024.property_name = "footstep_time"
    ACT0024.property_value = 0.07999999821186066
    CON0025.game_object = "NLO:U_O"
    CON0025.property_name = "number_footstep"
    CON0025.compare_value = 1
    CON0025.operator = 0
    CON0026.game_object = "NLO:U_O"
    CON0026.property_name = "number_footstep"
    CON0026.compare_value = 2
    CON0026.operator = 0
    CON0027.game_object = "NLO:U_O"
    CON0027.property_name = "number_footstep"
    CON0027.compare_value = 3
    CON0027.operator = 0
    CON0028.game_object = "NLO:U_O"
    CON0028.property_name = "number_footstep"
    CON0028.compare_value = 4
    CON0028.operator = 0
    CON0029.game_object = "NLO:U_O"
    CON0029.property_name = "number_footstep"
    CON0029.compare_value = 5
    CON0029.operator = 0
    CON0030.condition_a = CON0100
    CON0030.condition_b = CON0025
    CON0031.condition_a = CON0100
    CON0031.condition_b = CON0026
    CON0032.condition_a = CON0100
    CON0032.condition_b = CON0027
    CON0033.condition_a = CON0100
    CON0033.condition_b = CON0028
    CON0034.condition_a = CON0100
    CON0034.condition_b = CON0029
    ACT0035.condition = CON0041
    ACT0035.speaker = "NLO:CharacterController"
    ACT0035.sound = "D:/Sonic BGE Project/sounds/footsteps/004_wood/00_sn_walk_wood_5.wav"
    ACT0035.occlusion = False
    ACT0035.transition = 0.10000000149011612
    ACT0035.cutoff = 0.10000000149011612
    ACT0035.device_custom = "default3D"
    ACT0035.loop_count = 0
    ACT0035.pitch = 1.0
    ACT0035.volume = 1.0
    ACT0035.attenuation = 1.0
    ACT0035.distance_ref = 1.0
    ACT0035.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0035.cone_outer_volume = 0.0
    ACT0036.condition = CON0040
    ACT0036.speaker = "NLO:CharacterController"
    ACT0036.sound = "D:/Sonic BGE Project/sounds/footsteps/004_wood/00_sn_walk_wood_5.wav"
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
    ACT0037.condition = CON0042
    ACT0037.speaker = "NLO:CharacterController"
    ACT0037.sound = "D:/Sonic BGE Project/sounds/footsteps/004_wood/00_sn_walk_wood_3.wav"
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
    ACT0038.condition = CON0044
    ACT0038.speaker = "NLO:CharacterController"
    ACT0038.sound = "D:/Sonic BGE Project/sounds/footsteps/004_wood/00_sn_walk_wood_2.wav"
    ACT0038.occlusion = False
    ACT0038.transition = 0.10000000149011612
    ACT0038.cutoff = 0.10000000149011612
    ACT0038.device_custom = "default3D"
    ACT0038.loop_count = 0
    ACT0038.pitch = 1.0
    ACT0038.volume = 1.0
    ACT0038.attenuation = 1.0
    ACT0038.distance_ref = 1.0
    ACT0038.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0038.cone_outer_volume = 0.0
    ACT0039.condition = CON0055
    ACT0039.speaker = "NLO:CharacterController"
    ACT0039.sound = "D:/Sonic BGE Project/sounds/footsteps/004_wood/00_sn_walk_wood_1.wav"
    ACT0039.occlusion = False
    ACT0039.transition = 0.10000000149011612
    ACT0039.cutoff = 0.10000000149011612
    ACT0039.device_custom = "default3D"
    ACT0039.loop_count = 0
    ACT0039.pitch = 1.0
    ACT0039.volume = 1.0
    ACT0039.attenuation = 1.0
    ACT0039.distance_ref = 1.0
    ACT0039.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0039.cone_outer_volume = 0.0
    CON0040.condition_a = ACT0086
    CON0040.condition_b = CON0051
    CON0041.condition_a = ACT0086
    CON0041.condition_b = CON0052
    CON0042.condition_a = ACT0086
    CON0042.condition_b = CON0053
    CON0043.condition_a = CON0054
    CON0043.condition_b = CON0049
    CON0044.condition_a = ACT0086
    CON0044.condition_b = CON0050
    CON0045.game_object = "NLO:U_O"
    CON0045.property_name = "number_footstep"
    CON0045.compare_value = 2
    CON0045.operator = 0
    CON0046.game_object = "NLO:U_O"
    CON0046.property_name = "number_footstep"
    CON0046.compare_value = 3
    CON0046.operator = 0
    CON0047.game_object = "NLO:U_O"
    CON0047.property_name = "number_footstep"
    CON0047.compare_value = 4
    CON0047.operator = 0
    CON0048.game_object = "NLO:U_O"
    CON0048.property_name = "number_footstep"
    CON0048.compare_value = 5
    CON0048.operator = 0
    CON0049.game_object = "NLO:U_O"
    CON0049.property_name = "number_footstep"
    CON0049.compare_value = 1
    CON0049.operator = 0
    CON0050.condition_a = CON0054
    CON0050.condition_b = CON0045
    CON0051.condition_a = CON0054
    CON0051.condition_b = CON0047
    CON0052.condition_a = CON0054
    CON0052.condition_b = CON0048
    CON0053.condition_a = CON0054
    CON0053.condition_b = CON0046
    CON0054.game_object = "NLO:U_O"
    CON0054.property_name = "step_ground"
    CON0054.compare_value = "wood"
    CON0054.operator = 0
    CON0055.condition_a = ACT0086
    CON0055.condition_b = CON0043
    CON0056.game_object = "NLO:U_O"
    CON0056.property_name = "number_footstep"
    CON0056.compare_value = 2
    CON0056.operator = 0
    CON0057.game_object = "NLO:U_O"
    CON0057.property_name = "number_footstep"
    CON0057.compare_value = 3
    CON0057.operator = 0
    CON0058.game_object = "NLO:U_O"
    CON0058.property_name = "number_footstep"
    CON0058.compare_value = 4
    CON0058.operator = 0
    CON0059.game_object = "NLO:U_O"
    CON0059.property_name = "number_footstep"
    CON0059.compare_value = 5
    CON0059.operator = 0
    CON0060.condition_a = ACT0086
    CON0060.condition_b = CON0065
    CON0061.condition_a = ACT0086
    CON0061.condition_b = CON0066
    CON0062.condition_a = ACT0086
    CON0062.condition_b = CON0067
    CON0063.condition_a = ACT0086
    CON0063.condition_b = CON0068
    CON0064.condition_a = ACT0086
    CON0064.condition_b = CON0069
    CON0065.condition_a = CON0098
    CON0065.condition_b = CON0075
    CON0066.condition_a = CON0098
    CON0066.condition_b = CON0056
    CON0067.condition_a = CON0098
    CON0067.condition_b = CON0057
    CON0068.condition_a = CON0098
    CON0068.condition_b = CON0058
    CON0069.condition_a = CON0098
    CON0069.condition_b = CON0059
    ACT0070.condition = CON0060
    ACT0070.speaker = "NLO:CharacterController"
    ACT0070.sound = "D:/Sonic BGE Project/sounds/footsteps/002_metalpl/00_sn_walk_mtlp_1.wav"
    ACT0070.occlusion = False
    ACT0070.transition = 0.10000000149011612
    ACT0070.cutoff = 0.10000000149011612
    ACT0070.device_custom = "default3D"
    ACT0070.loop_count = 0
    ACT0070.pitch = 1.0
    ACT0070.volume = 1.0
    ACT0070.attenuation = 1.0
    ACT0070.distance_ref = 1.0
    ACT0070.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0070.cone_outer_volume = 0.0
    ACT0071.condition = CON0061
    ACT0071.speaker = "NLO:CharacterController"
    ACT0071.sound = "D:/Sonic BGE Project/sounds/footsteps/002_metalpl/00_sn_walk_mtlp_2.wav"
    ACT0071.occlusion = False
    ACT0071.transition = 0.10000000149011612
    ACT0071.cutoff = 0.10000000149011612
    ACT0071.device_custom = "default3D"
    ACT0071.loop_count = 0
    ACT0071.pitch = 1.0
    ACT0071.volume = 1.0
    ACT0071.attenuation = 1.0
    ACT0071.distance_ref = 1.0
    ACT0071.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0071.cone_outer_volume = 0.0
    ACT0072.condition = CON0062
    ACT0072.speaker = "NLO:CharacterController"
    ACT0072.sound = "D:/Sonic BGE Project/sounds/footsteps/002_metalpl/00_sn_walk_mtlp_3.wav"
    ACT0072.occlusion = False
    ACT0072.transition = 0.10000000149011612
    ACT0072.cutoff = 0.10000000149011612
    ACT0072.device_custom = "default3D"
    ACT0072.loop_count = 0
    ACT0072.pitch = 1.0
    ACT0072.volume = 1.0
    ACT0072.attenuation = 1.0
    ACT0072.distance_ref = 1.0
    ACT0072.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0072.cone_outer_volume = 0.0
    ACT0073.condition = CON0063
    ACT0073.speaker = "NLO:CharacterController"
    ACT0073.sound = "D:/Sonic BGE Project/sounds/footsteps/002_metalpl/00_sn_walk_mtlp_4.wav"
    ACT0073.occlusion = False
    ACT0073.transition = 0.10000000149011612
    ACT0073.cutoff = 0.10000000149011612
    ACT0073.device_custom = "default3D"
    ACT0073.loop_count = 0
    ACT0073.pitch = 1.0
    ACT0073.volume = 1.0
    ACT0073.attenuation = 1.0
    ACT0073.distance_ref = 1.0
    ACT0073.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0073.cone_outer_volume = 0.0
    ACT0074.condition = CON0064
    ACT0074.speaker = "NLO:CharacterController"
    ACT0074.sound = "D:/Sonic BGE Project/sounds/footsteps/002_metalpl/00_sn_walk_mtlp_5.wav"
    ACT0074.occlusion = False
    ACT0074.transition = 0.10000000149011612
    ACT0074.cutoff = 0.10000000149011612
    ACT0074.device_custom = "default3D"
    ACT0074.loop_count = 0
    ACT0074.pitch = 1.0
    ACT0074.volume = 1.0
    ACT0074.attenuation = 1.0
    ACT0074.distance_ref = 1.0
    ACT0074.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0074.cone_outer_volume = 0.0
    CON0075.game_object = "NLO:U_O"
    CON0075.property_name = "number_footstep"
    CON0075.compare_value = 1
    CON0075.operator = 0
    CON0076.game_object = "NLO:U_O"
    CON0076.property_name = "number_footstep"
    CON0076.compare_value = 2
    CON0076.operator = 0
    CON0077.game_object = "NLO:U_O"
    CON0077.property_name = "number_footstep"
    CON0077.compare_value = 3
    CON0077.operator = 0
    CON0078.game_object = "NLO:U_O"
    CON0078.property_name = "number_footstep"
    CON0078.compare_value = 4
    CON0078.operator = 0
    CON0079.game_object = "NLO:U_O"
    CON0079.property_name = "number_footstep"
    CON0079.compare_value = 5
    CON0079.operator = 0
    CON0080.condition_a = ACT0086
    CON0080.condition_b = CON0088
    CON0081.condition_a = ACT0086
    CON0081.condition_b = CON0089
    CON0082.condition_a = ACT0086
    CON0082.condition_b = CON0090
    CON0083.condition_a = ACT0086
    CON0083.condition_b = CON0091
    CON0084.condition_a = ACT0086
    CON0084.condition_b = CON0092
    CON0085.game_object = "NLO:U_O"
    CON0085.property_name = "number_footstep"
    CON0085.compare_value = 1
    CON0085.operator = 0
    ACT0086.condition = CON0009
    ACT0086.delay = PAR0011
    CON0087.game_object = "NLO:U_O"
    CON0087.property_name = "step_ground"
    CON0087.compare_value = "water"
    CON0087.operator = 0
    CON0088.condition_a = CON0087
    CON0088.condition_b = CON0085
    CON0089.condition_a = CON0087
    CON0089.condition_b = CON0076
    CON0090.condition_a = CON0087
    CON0090.condition_b = CON0077
    CON0091.condition_a = CON0087
    CON0091.condition_b = CON0078
    CON0092.condition_a = CON0087
    CON0092.condition_b = CON0079
    ACT0093.condition = CON0080
    ACT0093.speaker = "NLO:CharacterController"
    ACT0093.sound = "D:/Sonic BGE Project/sounds/footsteps/007_water/00_sn_walk_watr_1.wav"
    ACT0093.occlusion = False
    ACT0093.transition = 0.10000000149011612
    ACT0093.cutoff = 0.10000000149011612
    ACT0093.device_custom = "default3D"
    ACT0093.loop_count = 0
    ACT0093.pitch = 1.0
    ACT0093.volume = 1.0
    ACT0093.attenuation = 1.0
    ACT0093.distance_ref = 1.0
    ACT0093.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0093.cone_outer_volume = 0.0
    ACT0094.condition = CON0081
    ACT0094.speaker = "NLO:CharacterController"
    ACT0094.sound = "D:/Sonic BGE Project/sounds/footsteps/007_water/00_sn_walk_watr_2.wav"
    ACT0094.occlusion = False
    ACT0094.transition = 0.10000000149011612
    ACT0094.cutoff = 0.10000000149011612
    ACT0094.device_custom = "default3D"
    ACT0094.loop_count = 0
    ACT0094.pitch = 1.0
    ACT0094.volume = 1.0
    ACT0094.attenuation = 1.0
    ACT0094.distance_ref = 1.0
    ACT0094.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0094.cone_outer_volume = 0.0
    ACT0095.condition = CON0082
    ACT0095.speaker = "NLO:CharacterController"
    ACT0095.sound = "D:/Sonic BGE Project/sounds/footsteps/007_water/00_sn_walk_watr_3.wav"
    ACT0095.occlusion = False
    ACT0095.transition = 0.10000000149011612
    ACT0095.cutoff = 0.10000000149011612
    ACT0095.device_custom = "default3D"
    ACT0095.loop_count = 0
    ACT0095.pitch = 1.0
    ACT0095.volume = 1.0
    ACT0095.attenuation = 1.0
    ACT0095.distance_ref = 1.0
    ACT0095.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0095.cone_outer_volume = 0.0
    ACT0096.condition = CON0083
    ACT0096.speaker = "NLO:CharacterController"
    ACT0096.sound = "D:/Sonic BGE Project/sounds/footsteps/007_water/00_sn_walk_watr_4.wav"
    ACT0096.occlusion = False
    ACT0096.transition = 0.10000000149011612
    ACT0096.cutoff = 0.10000000149011612
    ACT0096.device_custom = "default3D"
    ACT0096.loop_count = 0
    ACT0096.pitch = 1.0
    ACT0096.volume = 1.0
    ACT0096.attenuation = 1.0
    ACT0096.distance_ref = 1.0
    ACT0096.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0096.cone_outer_volume = 0.0
    ACT0097.condition = CON0084
    ACT0097.speaker = "NLO:CharacterController"
    ACT0097.sound = "D:/Sonic BGE Project/sounds/footsteps/007_water/00_sn_walk_watr_5.wav"
    ACT0097.occlusion = False
    ACT0097.transition = 0.10000000149011612
    ACT0097.cutoff = 0.10000000149011612
    ACT0097.device_custom = "default3D"
    ACT0097.loop_count = 0
    ACT0097.pitch = 1.0
    ACT0097.volume = 1.0
    ACT0097.attenuation = 1.0
    ACT0097.distance_ref = 1.0
    ACT0097.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0097.cone_outer_volume = 0.0
    CON0098.game_object = "NLO:U_O"
    CON0098.property_name = "step_ground"
    CON0098.compare_value = "metal"
    CON0098.operator = 0
    CON0099.condition_a = ACT0116
    CON0099.condition_b = CON0107
    CON0100.game_object = "NLO:U_O"
    CON0100.property_name = "step_ground"
    CON0100.compare_value = "concrete"
    CON0100.operator = 0
    PAR0101.game_object = "NLO:RayRotate"
    PAR0101.attribute_name = "worldPosition"
    PAR0102.game_object = "NLO:CharacterController"
    PAR0102.attribute_name = "worldPosition"
    CON0104.game_object = "NLO:CharacterController"
    CON0104.use_mat = False
    CON0104.prop = "type"
    CON0104.material = None
    CON0104.pulse = True
    PAR0105.game_object = ACT0116.PICKED_OBJECT
    PAR0105.property_name = "type"
    ACT0106.condition = ACT0116
    ACT0106.game_object = "NLO:U_O"
    ACT0106.property_name = "step_ground"
    ACT0106.property_value = PAR0105
    CON0107.game_object = "NLO:U_O"
    CON0107.property_name = "animation"
    CON0107.compare_value = "walk"
    CON0107.operator = 0
    CON0108.game_object = "NLO:U_O"
    CON0108.property_name = "animation"
    CON0108.compare_value = "jog"
    CON0108.operator = 0
    ACT0109.condition = ACT0114
    ACT0109.sound = ACT0115.HANDLE
    PAR0110.game_object = "NLO:U_O"
    PAR0110.property_name = "isSliding"
    CON0111.game_object = "NLO:CharacterController"
    CON0111.property_name = "isSliding"
    CON0111.compare_value = True
    CON0111.operator = 0
    ACT0112.condition = CON0111
    ACT0112.delay = 1.2999999523162842
    CON0113.monitored_value = PAR0110
    CON0113.trigger_value = False
    ACT0114.condition = CON0113
    ACT0114.delay = 0.0
    ACT0115.condition = ACT0112
    ACT0115.speaker = "NLO:CharacterController"
    ACT0115.sound = "C:/Users/firef/OneDrive/Área de Trabalho/37_sn_sliding_lp.mp3"
    ACT0115.occlusion = False
    ACT0115.transition = 0.10000000149011612
    ACT0115.cutoff = 0.10000000149011612
    ACT0115.device_custom = "default3D"
    ACT0115.loop_count = 0
    ACT0115.pitch = 1.0
    ACT0115.volume = 1.0
    ACT0115.attenuation = 1.0
    ACT0115.distance_ref = 1.0
    ACT0115.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0115.cone_outer_volume = 0.0
    ACT0116.condition = CON0103
    ACT0116.origin = PAR0102
    ACT0116.destination = PAR0101
    ACT0116.local = False
    ACT0116.property_name = "type"
    ACT0116.xray = False
    ACT0116.custom_dist = False
    ACT0116.distance = 100.0
    ACT0116.visualize = False
    network.add_cell(CON0000)
    network.add_cell(CON0006)
    network.add_cell(PAR0011)
    network.add_cell(CON0025)
    network.add_cell(CON0027)
    network.add_cell(CON0029)
    network.add_cell(CON0045)
    network.add_cell(CON0047)
    network.add_cell(CON0049)
    network.add_cell(CON0054)
    network.add_cell(CON0056)
    network.add_cell(CON0058)
    network.add_cell(CON0075)
    network.add_cell(CON0077)
    network.add_cell(CON0079)
    network.add_cell(CON0085)
    network.add_cell(CON0087)
    network.add_cell(CON0090)
    network.add_cell(CON0092)
    network.add_cell(CON0098)
    network.add_cell(CON0100)
    network.add_cell(PAR0102)
    network.add_cell(CON0104)
    network.add_cell(CON0107)
    network.add_cell(PAR0110)
    network.add_cell(CON0113)
    network.add_cell(CON0001)
    network.add_cell(ACT0008)
    network.add_cell(CON0026)
    network.add_cell(CON0030)
    network.add_cell(CON0032)
    network.add_cell(CON0034)
    network.add_cell(CON0043)
    network.add_cell(CON0046)
    network.add_cell(CON0050)
    network.add_cell(CON0053)
    network.add_cell(CON0057)
    network.add_cell(CON0065)
    network.add_cell(CON0067)
    network.add_cell(CON0076)
    network.add_cell(CON0088)
    network.add_cell(PAR0101)
    network.add_cell(CON0108)
    network.add_cell(CON0111)
    network.add_cell(ACT0114)
    network.add_cell(ACT0005)
    network.add_cell(CON0028)
    network.add_cell(CON0033)
    network.add_cell(CON0048)
    network.add_cell(CON0052)
    network.add_cell(CON0059)
    network.add_cell(CON0066)
    network.add_cell(CON0069)
    network.add_cell(CON0078)
    network.add_cell(CON0089)
    network.add_cell(CON0103)
    network.add_cell(ACT0112)
    network.add_cell(ACT0116)
    network.add_cell(CON0002)
    network.add_cell(CON0004)
    network.add_cell(ACT0012)
    network.add_cell(ACT0024)
    network.add_cell(CON0051)
    network.add_cell(CON0068)
    network.add_cell(CON0091)
    network.add_cell(CON0099)
    network.add_cell(ACT0115)
    network.add_cell(CON0003)
    network.add_cell(CON0009)
    network.add_cell(ACT0013)
    network.add_cell(CON0031)
    network.add_cell(ACT0086)
    network.add_cell(PAR0105)
    network.add_cell(ACT0109)
    network.add_cell(ACT0007)
    network.add_cell(CON0014)
    network.add_cell(CON0016)
    network.add_cell(CON0018)
    network.add_cell(ACT0020)
    network.add_cell(ACT0022)
    network.add_cell(CON0040)
    network.add_cell(CON0042)
    network.add_cell(CON0055)
    network.add_cell(CON0061)
    network.add_cell(CON0063)
    network.add_cell(ACT0071)
    network.add_cell(ACT0073)
    network.add_cell(CON0080)
    network.add_cell(CON0082)
    network.add_cell(CON0084)
    network.add_cell(ACT0095)
    network.add_cell(ACT0097)
    network.add_cell(ACT0010)
    network.add_cell(CON0017)
    network.add_cell(ACT0021)
    network.add_cell(ACT0036)
    network.add_cell(ACT0039)
    network.add_cell(CON0044)
    network.add_cell(CON0062)
    network.add_cell(ACT0072)
    network.add_cell(CON0081)
    network.add_cell(ACT0093)
    network.add_cell(ACT0106)
    network.add_cell(CON0015)
    network.add_cell(ACT0023)
    network.add_cell(ACT0037)
    network.add_cell(CON0041)
    network.add_cell(CON0064)
    network.add_cell(ACT0074)
    network.add_cell(ACT0094)
    network.add_cell(ACT0019)
    network.add_cell(ACT0038)
    network.add_cell(CON0083)
    network.add_cell(ACT0035)
    network.add_cell(ACT0096)
    network.add_cell(CON0060)
    network.add_cell(ACT0070)
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
