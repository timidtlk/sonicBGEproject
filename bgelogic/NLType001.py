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
    PAR0035 = nodes.ParameterObjectProperty()
    CON0036 = nodes.ObjectPropertyOperator()
    ACT0037 = nodes.ActionSetResolution()
    ACT0038 = nodes.ActionSetGameObjectGameProperty()
    CON0039 = nodes.ConditionOnUpdate()
    ACT0040 = nodes.ActionSetGameObjectVisibility()
    CON0041 = nodes.ConditionOnUpdate()
    ACT0042 = nodes.ActionSetGameObjectVisibility()
    CON0043 = nodes.ConditionOnUpdate()
    PAR0044 = nodes.ParameterObjectProperty()
    ACT0045 = nodes.ActionSetGameObjectVisibility()
    CON0046 = nodes.ConditionOnUpdate()
    PAR0047 = nodes.ParameterObjectProperty()
    ACT0048 = nodes.ActionSetGameObjectVisibility()
    CON0049 = nodes.ConditionOnUpdate()
    PAR0050 = nodes.ParameterObjectProperty()
    ACT0051 = nodes.ActionSetGameObjectVisibility()
    ACT0052 = nodes.SetEeveeVolumetrics()
    ACT0053 = nodes.SetEeveeBloom()
    ACT0054 = nodes.SetEeveeAO()
    PAR0055 = nodes.ParameterObjectProperty()
    PAR0056 = nodes.ParameterObjectProperty()
    CON0057 = nodes.ConditionOnUpdate()
    ACT0058 = nodes.ActionSetVSync()
    ACT0059 = nodes.ActionSetVSync()
    CON0060 = nodes.ObjectPropertyOperator()
    CON0061 = nodes.ObjectPropertyOperator()
    ACT0000.condition = CON0001
    ACT0000.game_object = "NLO:Plane.005"
    ACT0000.property_name = "prop"
    ACT0000.property_value = 0
    CON0001.game_object = "NLO:Plane.005"
    CON0001.property_name = "prop"
    CON0001.compare_value = 8
    CON0001.operator = 4
    CON0002.game_object = "NLO:Plane.005"
    CON0002.property_name = "prop"
    CON0002.compare_value = 0.0
    CON0002.operator = 0
    ACT0003.condition = CON0002
    ACT0003.game_object = "NLO:Camera.002"
    ACT0003.property_name = "Width"
    ACT0003.property_value = 1920
    ACT0004.condition = CON0002
    ACT0004.game_object = "NLO:Camera.002"
    ACT0004.property_name = "Height"
    ACT0004.property_value = 1080
    ACT0005.condition = CON0002
    ACT0005.game_object = "NLO:Text.019"
    ACT0005.property_name = "Text"
    ACT0005.property_value = "1920x1080"
    CON0006.game_object = "NLO:Plane.005"
    CON0006.property_name = "prop"
    CON0006.compare_value = 3
    CON0006.operator = 0
    ACT0007.condition = CON0006
    ACT0007.game_object = "NLO:Camera.002"
    ACT0007.property_name = "Width"
    ACT0007.property_value = 1360
    ACT0008.condition = CON0006
    ACT0008.game_object = "NLO:Camera.002"
    ACT0008.property_name = "Height"
    ACT0008.property_value = 768
    ACT0009.condition = CON0006
    ACT0009.game_object = "NLO:Text.019"
    ACT0009.property_name = "Text"
    ACT0009.property_value = "1360x768"
    CON0010.game_object = "NLO:Plane.005"
    CON0010.property_name = "prop"
    CON0010.compare_value = 4
    CON0010.operator = 0
    ACT0011.condition = CON0010
    ACT0011.game_object = "NLO:Camera.002"
    ACT0011.property_name = "Width"
    ACT0011.property_value = 1280
    ACT0012.condition = CON0010
    ACT0012.game_object = "NLO:Camera.002"
    ACT0012.property_name = "Height"
    ACT0012.property_value = 720
    ACT0013.condition = CON0010
    ACT0013.game_object = "NLO:Text.019"
    ACT0013.property_name = "Text"
    ACT0013.property_value = "1280x720"
    CON0014.game_object = "NLO:Plane.005"
    CON0014.property_name = "prop"
    CON0014.compare_value = 5
    CON0014.operator = 0
    ACT0015.condition = CON0014
    ACT0015.game_object = "NLO:Camera.002"
    ACT0015.property_name = "Width"
    ACT0015.property_value = 1024
    ACT0016.condition = CON0014
    ACT0016.game_object = "NLO:Camera.002"
    ACT0016.property_name = "Height"
    ACT0016.property_value = 768
    ACT0017.condition = CON0014
    ACT0017.game_object = "NLO:Text.019"
    ACT0017.property_name = "Text"
    ACT0017.property_value = "1024x768"
    ACT0018.condition = CON0019
    ACT0018.game_object = "NLO:Text.019"
    ACT0018.property_name = "Text"
    ACT0018.property_value = "800x600"
    CON0019.game_object = "NLO:Plane.005"
    CON0019.property_name = "prop"
    CON0019.compare_value = 6
    CON0019.operator = 0
    ACT0020.condition = CON0019
    ACT0020.game_object = "NLO:Camera.002"
    ACT0020.property_name = "Width"
    ACT0020.property_value = 800
    ACT0021.condition = CON0019
    ACT0021.game_object = "NLO:Camera.002"
    ACT0021.property_name = "Height"
    ACT0021.property_value = 600
    ACT0022.condition = CON0023
    ACT0022.game_object = "NLO:Text.019"
    ACT0022.property_name = "Text"
    ACT0022.property_value = "640x480"
    CON0023.game_object = "NLO:Plane.005"
    CON0023.property_name = "prop"
    CON0023.compare_value = 7
    CON0023.operator = 0
    ACT0024.condition = CON0023
    ACT0024.game_object = "NLO:Camera.002"
    ACT0024.property_name = "Width"
    ACT0024.property_value = 640
    ACT0025.condition = CON0023
    ACT0025.game_object = "NLO:Camera.002"
    ACT0025.property_name = "Height"
    ACT0025.property_value = 480
    CON0026.game_object = "NLO:Plane.005"
    CON0026.property_name = "prop"
    CON0026.compare_value = 2
    CON0026.operator = 0
    ACT0027.condition = CON0026
    ACT0027.game_object = "NLO:Camera.002"
    ACT0027.property_name = "Width"
    ACT0027.property_value = 1366
    ACT0028.condition = CON0026
    ACT0028.game_object = "NLO:Camera.002"
    ACT0028.property_name = "Height"
    ACT0028.property_value = 768
    ACT0029.condition = CON0026
    ACT0029.game_object = "NLO:Text.019"
    ACT0029.property_name = "Text"
    ACT0029.property_value = "1366x768"
    CON0030.game_object = "NLO:Plane.005"
    CON0030.property_name = "prop"
    CON0030.compare_value = 1
    CON0030.operator = 0
    ACT0031.condition = CON0030
    ACT0031.game_object = "NLO:Camera.002"
    ACT0031.property_name = "Width"
    ACT0031.property_value = 1600
    ACT0032.condition = CON0030
    ACT0032.game_object = "NLO:Camera.002"
    ACT0032.property_name = "Height"
    ACT0032.property_value = 900
    ACT0033.condition = CON0030
    ACT0033.game_object = "NLO:Text.019"
    ACT0033.property_name = "Text"
    ACT0033.property_value = "1600x900"
    PAR0034.game_object = "NLO:Camera.002"
    PAR0034.property_name = "Height"
    PAR0035.game_object = "NLO:Camera.002"
    PAR0035.property_name = "Width"
    CON0036.game_object = "NLO:Plane.006"
    CON0036.property_name = "toggle"
    CON0036.compare_value = True
    CON0036.operator = 0
    ACT0037.condition = CON0036
    ACT0037.x_res = PAR0035
    ACT0037.y_res = PAR0034
    ACT0038.condition = ACT0037.OUT
    ACT0038.game_object = "NLO:Plane.006"
    ACT0038.property_name = "toggle"
    ACT0038.property_value = False
    ACT0040.condition = CON0039
    ACT0040.game_object = "NLO:toggleScr.001"
    ACT0040.visible = PAR0055
    ACT0040.recursive = False
    ACT0042.condition = CON0041
    ACT0042.game_object = "NLO:toggleBloom.001"
    ACT0042.visible = PAR0056
    ACT0042.recursive = False
    PAR0044.game_object = "NLO:ao.001"
    PAR0044.property_name = "ao"
    ACT0045.condition = CON0043
    ACT0045.game_object = "NLO:toggleAO.001"
    ACT0045.visible = PAR0044
    ACT0045.recursive = False
    PAR0047.game_object = "NLO:mb.001"
    PAR0047.property_name = "mb"
    ACT0048.condition = CON0046
    ACT0048.game_object = "NLO:toggleMB.001"
    ACT0048.visible = PAR0047
    ACT0048.recursive = False
    PAR0050.game_object = "NLO:bosti.001"
    PAR0050.property_name = "bostil"
    ACT0051.condition = CON0049
    ACT0051.game_object = "NLO:toggleBostil.001"
    ACT0051.visible = PAR0050
    ACT0051.recursive = False
    ACT0052.condition = CON0057
    ACT0052.value = PAR0055
    ACT0053.condition = CON0057
    ACT0053.value = PAR0056
    ACT0054.condition = CON0057
    ACT0054.value = PAR0044
    PAR0055.game_object = "NLO:scr.001"
    PAR0055.property_name = "scr"
    PAR0056.game_object = "NLO:blo.001"
    PAR0056.property_name = "blo"
    ACT0058.condition = CON0061
    ACT0058.vsync_mode = bge.render.VSYNC_OFF
    ACT0059.condition = CON0060
    ACT0059.vsync_mode = bge.render.VSYNC_ON
    CON0060.game_object = "NLO:bosti.001"
    CON0060.property_name = "bostil"
    CON0060.compare_value = True
    CON0060.operator = 0
    CON0061.game_object = "NLO:bosti.001"
    CON0061.property_name = "bostil"
    CON0061.compare_value = False
    CON0061.operator = 0
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
    network.add_cell(CON0036)
    network.add_cell(CON0039)
    network.add_cell(CON0041)
    network.add_cell(CON0043)
    network.add_cell(CON0046)
    network.add_cell(CON0049)
    network.add_cell(PAR0055)
    network.add_cell(CON0057)
    network.add_cell(CON0060)
    network.add_cell(ACT0000)
    network.add_cell(ACT0007)
    network.add_cell(ACT0011)
    network.add_cell(ACT0015)
    network.add_cell(ACT0018)
    network.add_cell(ACT0022)
    network.add_cell(CON0026)
    network.add_cell(ACT0028)
    network.add_cell(ACT0031)
    network.add_cell(PAR0035)
    network.add_cell(ACT0040)
    network.add_cell(PAR0044)
    network.add_cell(PAR0047)
    network.add_cell(PAR0050)
    network.add_cell(ACT0052)
    network.add_cell(ACT0054)
    network.add_cell(ACT0059)
    network.add_cell(CON0002)
    network.add_cell(ACT0004)
    network.add_cell(ACT0009)
    network.add_cell(ACT0017)
    network.add_cell(ACT0024)
    network.add_cell(ACT0029)
    network.add_cell(ACT0037)
    network.add_cell(ACT0045)
    network.add_cell(ACT0051)
    network.add_cell(PAR0056)
    network.add_cell(CON0061)
    network.add_cell(ACT0003)
    network.add_cell(ACT0013)
    network.add_cell(ACT0027)
    network.add_cell(ACT0038)
    network.add_cell(ACT0048)
    network.add_cell(ACT0058)
    network.add_cell(ACT0005)
    network.add_cell(ACT0033)
    network.add_cell(ACT0053)
    network.add_cell(ACT0020)
    network.add_cell(ACT0042)
    owner["IGNLTree_Type.001"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__Type.001')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_Type.001")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
