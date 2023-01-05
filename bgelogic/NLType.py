# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionSetGameObjectGameProperty()
    CON0001 = nodes.ObjectPropertyOperator()
    CON0002 = nodes.ObjectPropertyOperator()
    ACT0003 = nodes.ActionSetGameObjectGameProperty()
    ACT0004 = nodes.ActionSetGameObjectGameProperty()
    ACT0005 = nodes.ActionSetGameObjectGameProperty()
    CON0006 = nodes.ObjectPropertyOperator()
    ACT0007 = nodes.ActionSetGameObjectGameProperty()
    ACT0008 = nodes.ActionSetGameObjectGameProperty()
    ACT0009 = nodes.ActionSetGameObjectGameProperty()
    CON0010 = nodes.ObjectPropertyOperator()
    ACT0011 = nodes.ActionSetGameObjectGameProperty()
    ACT0012 = nodes.ActionSetGameObjectGameProperty()
    ACT0013 = nodes.ActionSetGameObjectGameProperty()
    CON0014 = nodes.ObjectPropertyOperator()
    ACT0015 = nodes.ActionSetGameObjectGameProperty()
    ACT0016 = nodes.ActionSetGameObjectGameProperty()
    ACT0017 = nodes.ActionSetGameObjectGameProperty()
    ACT0018 = nodes.ActionSetGameObjectGameProperty()
    CON0019 = nodes.ObjectPropertyOperator()
    ACT0020 = nodes.ActionSetGameObjectGameProperty()
    ACT0021 = nodes.ActionSetGameObjectGameProperty()
    ACT0022 = nodes.ActionSetGameObjectGameProperty()
    CON0023 = nodes.ObjectPropertyOperator()
    ACT0024 = nodes.ActionSetGameObjectGameProperty()
    ACT0025 = nodes.ActionSetGameObjectGameProperty()
    CON0026 = nodes.ObjectPropertyOperator()
    ACT0027 = nodes.ActionSetGameObjectGameProperty()
    ACT0028 = nodes.ActionSetGameObjectGameProperty()
    ACT0029 = nodes.ActionSetGameObjectGameProperty()
    CON0030 = nodes.ObjectPropertyOperator()
    ACT0031 = nodes.ActionSetGameObjectGameProperty()
    ACT0032 = nodes.ActionSetGameObjectGameProperty()
    ACT0033 = nodes.ActionSetGameObjectGameProperty()
    PAR0034 = nodes.ParameterObjectProperty()
    ACT0035 = nodes.ActionSetResolution()
    ACT0036 = nodes.ActionSetGameObjectGameProperty()
    CON0037 = nodes.ConditionOnUpdate()
    ACT0038 = nodes.ActionSetGameObjectVisibility()
    CON0039 = nodes.ConditionOnUpdate()
    ACT0040 = nodes.ActionSetGameObjectVisibility()
    CON0041 = nodes.ConditionOnUpdate()
    ACT0042 = nodes.ActionSetGameObjectVisibility()
    ACT0043 = nodes.SetEeveeBloom()
    ACT0044 = nodes.SetEeveeAO()
    PAR0045 = nodes.ParameterObjectProperty()
    CON0046 = nodes.ObjectPropertyOperator()
    CON0047 = nodes.ObjectPropertyOperator()
    ACT0048 = nodes.ActionSetVSync()
    ACT0049 = nodes.ActionSetVSync()
    PAR0050 = nodes.ParameterObjectProperty()
    PAR0051 = nodes.ParameterObjectProperty()
    PAR0052 = nodes.ParameterObjectProperty()
    PAR0053 = nodes.ParameterObjectProperty()
    ACT0054 = nodes.ActionSetGameObjectVisibility()
    CON0055 = nodes.ConditionOnUpdate()
    CON0056 = nodes.GE_OnInit()
    ACT0057 = nodes.SetEeveeSSR()
    CON0058 = nodes.ConditionOnUpdate()
    PAR0059 = nodes.ParameterObjectProperty()
    CON0060 = nodes.ObjectPropertyOperator()
    CON0061 = nodes.ConditionOnUpdate()
    ACT0062 = nodes.ActionSetGameObjectVisibility()
    PAR0063 = nodes.ParameterObjectProperty()
    PAR0064 = nodes.ParameterObjectProperty()
    CON0065 = nodes.ConditionOnUpdate()
    ACT0066 = nodes.ActionSetGameObjectVisibility()
    PAR0067 = nodes.ParameterObjectProperty()
    CON0068 = nodes.ConditionOnUpdate()
    CON0069 = nodes.ObjectPropertyOperator()
    ACT0070 = nodes.GEShowFramerate()
    ACT0071 = nodes.ActionSetGameObjectVisibility()
    ACT0072 = nodes.ActionSaveVariable()
    ACT0073 = nodes.ActionSaveVariable()
    ACT0074 = nodes.ActionSaveVariable()
    ACT0075 = nodes.ActionSaveVariable()
    ACT0076 = nodes.ActionSaveVariable()
    CON0077 = nodes.ConditionAndList()
    ACT0078 = nodes.ActionSetGameObjectGameProperty()
    PAR0079 = nodes.ParameterObjectProperty()
    ACT0080 = nodes.ActionSetVSync()
    ACT0081 = nodes.ActionSetVSync()
    CON0082 = nodes.ObjectPropertyOperator()
    ACT0083 = nodes.ActionSaveVariable()
    CON0084 = nodes.ObjectPropertyOperator()
    ACT0085 = nodes.SetEeveeBloom()
    ACT0086 = nodes.SetEeveeAO()
    ACT0087 = nodes.ActionLoadVariable()
    ACT0088 = nodes.SetEeveeSSR()
    ACT0089 = nodes.ActionLoadVariable()
    ACT0090 = nodes.ActionLoadVariable()
    ACT0091 = nodes.ActionLoadVariable()
    ACT0092 = nodes.ActionSetGameObjectGameProperty()
    ACT0093 = nodes.ActionLoadVariable()
    ACT0094 = nodes.GEShowFramerate()
    ACT0000.condition = CON0001
    ACT0000.game_object = "NLO:Plane.009"
    ACT0000.property_name = "prop"
    ACT0000.property_value = 0
    CON0001.game_object = "NLO:Plane.009"
    CON0001.property_name = "prop"
    CON0001.compare_value = 8
    CON0001.operator = 4
    CON0002.game_object = "NLO:Plane.009"
    CON0002.property_name = "prop"
    CON0002.compare_value = 0.0
    CON0002.operator = 0
    ACT0003.condition = CON0002
    ACT0003.game_object = "NLO:Camera.001"
    ACT0003.property_name = "Width"
    ACT0003.property_value = 1920
    ACT0004.condition = CON0002
    ACT0004.game_object = "NLO:Camera.001"
    ACT0004.property_name = "Height"
    ACT0004.property_value = 1080
    ACT0005.condition = CON0002
    ACT0005.game_object = "NLO:Text.007"
    ACT0005.property_name = "Text"
    ACT0005.property_value = "1920x1080"
    CON0006.game_object = "NLO:Plane.009"
    CON0006.property_name = "prop"
    CON0006.compare_value = 3
    CON0006.operator = 0
    ACT0007.condition = CON0006
    ACT0007.game_object = "NLO:Camera.001"
    ACT0007.property_name = "Width"
    ACT0007.property_value = 1360
    ACT0008.condition = CON0006
    ACT0008.game_object = "NLO:Camera.001"
    ACT0008.property_name = "Height"
    ACT0008.property_value = 768
    ACT0009.condition = CON0006
    ACT0009.game_object = "NLO:Text.007"
    ACT0009.property_name = "Text"
    ACT0009.property_value = "1360x768"
    CON0010.game_object = "NLO:Plane.009"
    CON0010.property_name = "prop"
    CON0010.compare_value = 4
    CON0010.operator = 0
    ACT0011.condition = CON0010
    ACT0011.game_object = "NLO:Camera.001"
    ACT0011.property_name = "Width"
    ACT0011.property_value = 1280
    ACT0012.condition = CON0010
    ACT0012.game_object = "NLO:Camera.001"
    ACT0012.property_name = "Height"
    ACT0012.property_value = 720
    ACT0013.condition = CON0010
    ACT0013.game_object = "NLO:Text.007"
    ACT0013.property_name = "Text"
    ACT0013.property_value = "1280x720"
    CON0014.game_object = "NLO:Plane.009"
    CON0014.property_name = "prop"
    CON0014.compare_value = 5
    CON0014.operator = 0
    ACT0015.condition = CON0014
    ACT0015.game_object = "NLO:Camera.001"
    ACT0015.property_name = "Width"
    ACT0015.property_value = 1024
    ACT0016.condition = CON0014
    ACT0016.game_object = "NLO:Camera.001"
    ACT0016.property_name = "Height"
    ACT0016.property_value = 768
    ACT0017.condition = CON0014
    ACT0017.game_object = "NLO:Text.007"
    ACT0017.property_name = "Text"
    ACT0017.property_value = "1024x768"
    ACT0018.condition = CON0019
    ACT0018.game_object = "NLO:Text.007"
    ACT0018.property_name = "Text"
    ACT0018.property_value = "800x600"
    CON0019.game_object = "NLO:Plane.009"
    CON0019.property_name = "prop"
    CON0019.compare_value = 6
    CON0019.operator = 0
    ACT0020.condition = CON0019
    ACT0020.game_object = "NLO:Camera.001"
    ACT0020.property_name = "Width"
    ACT0020.property_value = 800
    ACT0021.condition = CON0019
    ACT0021.game_object = "NLO:Camera.001"
    ACT0021.property_name = "Height"
    ACT0021.property_value = 600
    ACT0022.condition = CON0023
    ACT0022.game_object = "NLO:Text.007"
    ACT0022.property_name = "Text"
    ACT0022.property_value = "640x480"
    CON0023.game_object = "NLO:Plane.009"
    CON0023.property_name = "prop"
    CON0023.compare_value = 7
    CON0023.operator = 0
    ACT0024.condition = CON0023
    ACT0024.game_object = "NLO:Camera.001"
    ACT0024.property_name = "Width"
    ACT0024.property_value = 640
    ACT0025.condition = CON0023
    ACT0025.game_object = "NLO:Camera.001"
    ACT0025.property_name = "Height"
    ACT0025.property_value = 480
    CON0026.game_object = "NLO:Plane.009"
    CON0026.property_name = "prop"
    CON0026.compare_value = 2
    CON0026.operator = 0
    ACT0027.condition = CON0026
    ACT0027.game_object = "NLO:Camera.001"
    ACT0027.property_name = "Width"
    ACT0027.property_value = 1366
    ACT0028.condition = CON0026
    ACT0028.game_object = "NLO:Camera.001"
    ACT0028.property_name = "Height"
    ACT0028.property_value = 768
    ACT0029.condition = CON0026
    ACT0029.game_object = "NLO:Text.007"
    ACT0029.property_name = "Text"
    ACT0029.property_value = "1366x768"
    CON0030.game_object = "NLO:Plane.009"
    CON0030.property_name = "prop"
    CON0030.compare_value = 1
    CON0030.operator = 0
    ACT0031.condition = CON0030
    ACT0031.game_object = "NLO:Camera.001"
    ACT0031.property_name = "Width"
    ACT0031.property_value = 1600
    ACT0032.condition = CON0030
    ACT0032.game_object = "NLO:Camera.001"
    ACT0032.property_name = "Height"
    ACT0032.property_value = 900
    ACT0033.condition = CON0030
    ACT0033.game_object = "NLO:Text.007"
    ACT0033.property_name = "Text"
    ACT0033.property_value = "1600x900"
    PAR0034.game_object = "NLO:Camera.001"
    PAR0034.property_name = "Height"
    ACT0035.condition = CON0069
    ACT0035.x_res = PAR0051
    ACT0035.y_res = PAR0034
    ACT0036.condition = ACT0035.OUT
    ACT0036.game_object = "NLO:Plane.010"
    ACT0036.property_name = "toggle"
    ACT0036.property_value = False
    ACT0038.condition = CON0037
    ACT0038.game_object = "NLO:toggleScr"
    ACT0038.visible = PAR0053
    ACT0038.recursive = False
    ACT0040.condition = CON0039
    ACT0040.game_object = "NLO:toggleAO"
    ACT0040.visible = PAR0063
    ACT0040.recursive = False
    ACT0042.condition = CON0041
    ACT0042.game_object = "NLO:toggleMB"
    ACT0042.visible = PAR0045
    ACT0042.recursive = False
    ACT0043.condition = CON0058
    ACT0043.value = PAR0050
    ACT0044.condition = CON0058
    ACT0044.value = PAR0063
    PAR0045.game_object = "NLO:mb"
    PAR0045.property_name = "mb"
    CON0046.game_object = "NLO:bosti"
    CON0046.property_name = "bostil"
    CON0046.compare_value = True
    CON0046.operator = 0
    CON0047.game_object = "NLO:bosti"
    CON0047.property_name = "bostil"
    CON0047.compare_value = False
    CON0047.operator = 0
    ACT0048.condition = CON0047
    ACT0048.vsync_mode = bge.render.VSYNC_OFF
    ACT0049.condition = CON0046
    ACT0049.vsync_mode = bge.render.VSYNC_ON
    PAR0050.game_object = "NLO:blo"
    PAR0050.property_name = "blo"
    PAR0051.game_object = "NLO:Camera.001"
    PAR0051.property_name = "Width"
    PAR0052.game_object = "NLO:Plane.009"
    PAR0052.property_name = "prop"
    PAR0053.game_object = "NLO:scr"
    PAR0053.property_name = "scr"
    ACT0054.condition = CON0055
    ACT0054.game_object = "NLO:toggleBloom"
    ACT0054.visible = PAR0050
    ACT0054.recursive = False
    ACT0057.condition = CON0058
    ACT0057.value = PAR0053
    PAR0059.game_object = "NLO:bosti"
    PAR0059.property_name = "bostil"
    CON0060.game_object = "NLO:Plane.002"
    CON0060.property_name = "write"
    CON0060.compare_value = True
    CON0060.operator = 0
    ACT0062.condition = CON0061
    ACT0062.game_object = "NLO:toggleBostil"
    ACT0062.visible = PAR0059
    ACT0062.recursive = False
    PAR0063.game_object = "NLO:ao"
    PAR0063.property_name = "ao"
    PAR0064.game_object = "NLO:ao.001"
    PAR0064.property_name = "fullscreen"
    ACT0066.condition = CON0065
    ACT0066.game_object = "NLO:toggleAO.001"
    ACT0066.visible = PAR0064
    ACT0066.recursive = False
    PAR0067.game_object = "NLO:bosti.001"
    PAR0067.property_name = "fps"
    CON0069.game_object = "NLO:Plane.010"
    CON0069.property_name = "toggle"
    CON0069.compare_value = True
    CON0069.operator = 0
    ACT0070.condition = ACT0071.OUT
    ACT0070.use_framerate = PAR0079
    ACT0071.condition = CON0068
    ACT0071.game_object = "NLO:toggleBostil.001"
    ACT0071.visible = PAR0067
    ACT0071.recursive = False
    ACT0072.path = '//saves'
    ACT0072.file_name = 'settings'
    ACT0072.condition = CON0060
    ACT0072.name = "ssr"
    ACT0072.val = PAR0053
    ACT0073.path = '//saves'
    ACT0073.file_name = 'settings'
    ACT0073.condition = CON0060
    ACT0073.name = "ambientOcclusion"
    ACT0073.val = PAR0063
    ACT0074.path = '//saves'
    ACT0074.file_name = 'settings'
    ACT0074.condition = CON0060
    ACT0074.name = "bloom"
    ACT0074.val = PAR0050
    ACT0075.path = '//saves'
    ACT0075.file_name = 'settings'
    ACT0075.condition = CON0060
    ACT0075.name = "vsync"
    ACT0075.val = PAR0059
    ACT0076.path = '//saves'
    ACT0076.file_name = 'settings'
    ACT0076.condition = CON0060
    ACT0076.name = "showfps"
    ACT0076.val = PAR0079
    CON0077.ca = ACT0072.OUT
    CON0077.cb = ACT0073.OUT
    CON0077.cc = ACT0074.OUT
    CON0077.cd = ACT0075.OUT
    CON0077.ce = ACT0076.OUT
    CON0077.cf = ACT0083.OUT
    ACT0078.condition = CON0077
    ACT0078.game_object = "NLO:Plane.002"
    ACT0078.property_name = "write"
    ACT0078.property_value = False
    PAR0079.game_object = "NLO:bosti.001"
    PAR0079.property_name = "fps"
    ACT0080.condition = CON0084
    ACT0080.vsync_mode = bge.render.VSYNC_OFF
    ACT0081.condition = CON0082
    ACT0081.vsync_mode = bge.render.VSYNC_ON
    CON0082.game_object = "NLO:Camera"
    CON0082.property_name = "vsync"
    CON0082.compare_value = True
    CON0082.operator = 0
    ACT0083.path = '//saves'
    ACT0083.file_name = 'settings'
    ACT0083.condition = CON0069
    ACT0083.name = "resolution"
    ACT0083.val = PAR0052
    CON0084.game_object = "NLO:Camera"
    CON0084.property_name = "vsync"
    CON0084.compare_value = False
    CON0084.operator = 0
    ACT0085.condition = ACT0091.OUT
    ACT0085.value = ACT0091.VAR
    ACT0086.condition = ACT0090.OUT
    ACT0086.value = ACT0090.VAR
    ACT0087.path = '//saves'
    ACT0087.file_name = 'settings'
    ACT0087.condition = CON0056
    ACT0087.name = "vsync"
    ACT0088.condition = ACT0089.OUT
    ACT0088.value = ACT0089.VAR
    ACT0089.path = '//saves'
    ACT0089.file_name = 'settings'
    ACT0089.condition = CON0056
    ACT0089.name = "ssr"
    ACT0090.path = '//saves'
    ACT0090.file_name = 'settings'
    ACT0090.condition = CON0056
    ACT0090.name = "ambientOcclusion"
    ACT0091.path = '//saves'
    ACT0091.file_name = 'settings'
    ACT0091.condition = CON0056
    ACT0091.name = "bloom"
    ACT0092.condition = ACT0087.OUT
    ACT0092.game_object = "NLO:Camera"
    ACT0092.property_name = "vsync"
    ACT0092.property_value = ACT0087.VAR
    ACT0093.path = '//saves'
    ACT0093.file_name = 'settings'
    ACT0093.condition = CON0056
    ACT0093.name = "fps"
    ACT0094.condition = ACT0093.OUT
    ACT0094.use_framerate = ACT0093.VAR
    network.add_cell(CON0001)
    network.add_cell(CON0006)
    network.add_cell(ACT0008)
    network.add_cell(CON0010)
    network.add_cell(ACT0012)
    network.add_cell(CON0014)
    network.add_cell(ACT0016)
    network.add_cell(CON0019)
    network.add_cell(ACT0021)
    network.add_cell(CON0023)
    network.add_cell(ACT0025)
    network.add_cell(CON0030)
    network.add_cell(ACT0032)
    network.add_cell(PAR0034)
    network.add_cell(CON0037)
    network.add_cell(CON0039)
    network.add_cell(CON0041)
    network.add_cell(PAR0045)
    network.add_cell(CON0047)
    network.add_cell(PAR0050)
    network.add_cell(PAR0052)
    network.add_cell(CON0055)
    network.add_cell(CON0058)
    network.add_cell(CON0060)
    network.add_cell(PAR0063)
    network.add_cell(CON0065)
    network.add_cell(PAR0067)
    network.add_cell(CON0069)
    network.add_cell(ACT0073)
    network.add_cell(PAR0079)
    network.add_cell(CON0082)
    network.add_cell(CON0084)
    network.add_cell(ACT0000)
    network.add_cell(ACT0007)
    network.add_cell(ACT0011)
    network.add_cell(ACT0015)
    network.add_cell(ACT0018)
    network.add_cell(ACT0022)
    network.add_cell(CON0026)
    network.add_cell(ACT0028)
    network.add_cell(ACT0031)
    network.add_cell(ACT0040)
    network.add_cell(ACT0043)
    network.add_cell(CON0046)
    network.add_cell(ACT0049)
    network.add_cell(PAR0053)
    network.add_cell(CON0056)
    network.add_cell(PAR0059)
    network.add_cell(PAR0064)
    network.add_cell(CON0068)
    network.add_cell(ACT0071)
    network.add_cell(ACT0074)
    network.add_cell(ACT0076)
    network.add_cell(ACT0080)
    network.add_cell(ACT0083)
    network.add_cell(ACT0087)
    network.add_cell(ACT0089)
    network.add_cell(ACT0091)
    network.add_cell(ACT0093)
    network.add_cell(CON0002)
    network.add_cell(ACT0004)
    network.add_cell(ACT0009)
    network.add_cell(ACT0017)
    network.add_cell(ACT0024)
    network.add_cell(ACT0029)
    network.add_cell(ACT0038)
    network.add_cell(ACT0044)
    network.add_cell(PAR0051)
    network.add_cell(ACT0057)
    network.add_cell(ACT0066)
    network.add_cell(ACT0072)
    network.add_cell(ACT0081)
    network.add_cell(ACT0088)
    network.add_cell(ACT0092)
    network.add_cell(ACT0003)
    network.add_cell(ACT0013)
    network.add_cell(ACT0027)
    network.add_cell(ACT0035)
    network.add_cell(ACT0042)
    network.add_cell(ACT0054)
    network.add_cell(ACT0070)
    network.add_cell(ACT0085)
    network.add_cell(ACT0090)
    network.add_cell(ACT0005)
    network.add_cell(ACT0033)
    network.add_cell(ACT0048)
    network.add_cell(ACT0075)
    network.add_cell(ACT0086)
    network.add_cell(ACT0020)
    network.add_cell(CON0061)
    network.add_cell(CON0077)
    network.add_cell(ACT0094)
    network.add_cell(ACT0036)
    network.add_cell(ACT0078)
    network.add_cell(ACT0062)
    owner["IGNLTree_Type"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__Type')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_Type")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
