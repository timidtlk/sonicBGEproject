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
    CON0003 = nodes.ObjectPropertyOperator()
    CON0004 = nodes.ConditionOrList()
    ACT0005 = nodes.ActionTimeFilter()
    ACT0006 = nodes.ActionSetGameObjectVisibility()
    ACT0007 = nodes.ActionSetGameObjectVisibility()
    ACT0008 = nodes.ActionApplyForce()
    CON0009 = nodes.ObjectPropertyOperator()
    CON0010 = nodes.ObjectPropertyOperator()
    CON0011 = nodes.ConditionAndList()
    CON0012 = nodes.ConditionNot()
    CON0013 = nodes.ConditionCollision()
    CON0014 = nodes.ConditionCollision()
    CON0015 = nodes.ConditionAnd()
    ACT0016 = nodes.ActionSetGameObjectGameProperty()
    CON0017 = nodes.ConditionAnd()
    ACT0018 = nodes.ActionSetGameObjectGameProperty()
    ACT0019 = nodes.ActionSetGameObjectGameProperty()
    CON0020 = nodes.ObjectPropertyOperator()
    CON0021 = nodes.ConditionAnd()
    ACT0022 = nodes.ActionSetGameObjectGameProperty()
    CON0023 = nodes.ObjectPropertyOperator()
    ACT0024 = nodes.ActionSetGameObjectGameProperty()
    ACT0025 = nodes.ActionAddToGameObjectGameProperty()
    ACT0026 = nodes.ActionSetGameObjectGameProperty()
    CON0027 = nodes.ConditionOr()
    CON0028 = nodes.ConditionAnd()
    ACT0029 = nodes.ActionSetGameObjectVisibility()
    ACT0030 = nodes.ActionSetGameObjectVisibility()
    CON0031 = nodes.ObjectPropertyOperator()
    CON0032 = nodes.ObjectPropertyOperator()
    CON0033 = nodes.ObjectPropertyOperator()
    CON0034 = nodes.ObjectPropertyOperator()
    PAR0035 = nodes.ParameterObjectAttribute()
    CON0036 = nodes.ConditionNot()
    PAR0037 = nodes.ParameterObjectAttribute()
    ACT0038 = nodes.ActionRayPick()
    CON0039 = nodes.ConditionOr()
    CON0040 = nodes.ConditionKeyPressed()
    CON0041 = nodes.ConditionAnd()
    CON0042 = nodes.ConditionGamepadButtons()
    ACT0043 = nodes.ActionApplyForce()
    ACT0044 = nodes.ActionSetGameObjectGameProperty()
    ACT0045 = nodes.ActionSetGameObjectGameProperty()
    ACT0046 = nodes.ActionSetGameObjectGameProperty()
    CON0047 = nodes.ConditionAnd()
    CON0048 = nodes.ConditionOr()
    CON0049 = nodes.ConditionAnd()
    CON0050 = nodes.ObjectPropertyOperator()
    CON0051 = nodes.ObjectPropertyOperator()
    CON0052 = nodes.ObjectPropertyOperator()
    ACT0053 = nodes.ActionSetGameObjectGameProperty()
    PAR0054 = nodes.ParameterObjectProperty()
    CON0055 = nodes.ObjectPropertyOperator()
    ACT0056 = nodes.ActionSetGameObjectGameProperty()
    CON0057 = nodes.ObjectPropertyOperator()
    ACT0058 = nodes.ActionSetGameObjectGameProperty()
    CON0059 = nodes.ConditionOnUpdate()
    PAR0060 = nodes.ParameterVector3Simple()
    CON0061 = nodes.ConditionOr()
    CON0062 = nodes.ConditionGamepadButtons()
    ACT0063 = nodes.ActionApplyForce()
    CON0064 = nodes.ConditionKeyPressed()
    CON0065 = nodes.ConditionAnd()
    CON0066 = nodes.ObjectPropertyOperator()
    ACT0000.condition = ACT0005
    ACT0000.game_object = "NLO:CharacterController"
    ACT0000.property_name = "idle"
    ACT0000.property_value = 0.0
    CON0001.game_object = "NLO:CharacterController"
    CON0001.property_name = "Speed"
    CON0001.compare_value = 0.029999999329447746
    CON0001.operator = 2
    CON0002.game_object = "NLO:CharacterController"
    CON0002.property_name = "isFalling"
    CON0002.compare_value = True
    CON0002.operator = 2
    CON0003.game_object = "NLO:CharacterController"
    CON0003.property_name = "isJumping"
    CON0003.compare_value = True
    CON0003.operator = 2
    CON0004.ca = CON0001
    CON0004.cb = CON0003
    CON0004.cc = CON0002
    CON0004.cd = CON0012
    CON0004.ce = None
    CON0004.cf = None
    ACT0005.condition = CON0004
    ACT0005.delay = 0.0
    ACT0006.condition = CON0028
    ACT0006.game_object = "NLO:SonicBall"
    ACT0006.visible = True
    ACT0006.recursive = False
    ACT0007.condition = CON0027
    ACT0007.game_object = "NLO:SonicBall"
    ACT0007.visible = False
    ACT0007.recursive = False
    ACT0008.local = True
    ACT0008.condition = CON0011
    ACT0008.game_object = "NLO:CharacterController"
    ACT0008.force = mathutils.Vector((0.0, 1500.0, 0.0))
    CON0009.game_object = "NLO:CharacterController"
    CON0009.property_name = "jump"
    CON0009.compare_value = 2
    CON0009.operator = 0
    CON0010.game_object = "NLO:CharacterController"
    CON0010.property_name = "isHommiable"
    CON0010.compare_value = False
    CON0010.operator = 0
    CON0011.ca = CON0061
    CON0011.cb = CON0009
    CON0011.cc = CON0010
    CON0011.cd = True
    CON0011.ce = True
    CON0011.cf = True
    CON0012.condition = CON0013
    CON0013.game_object = "NLO:groundSensor"
    CON0013.use_mat = False
    CON0013.prop = "obstacle"
    CON0013.material = None
    CON0013.pulse = True
    CON0014.game_object = "NLO:groundSensor"
    CON0014.use_mat = False
    CON0014.prop = "obstacle"
    CON0014.material = None
    CON0014.pulse = False
    CON0015.condition_a = CON0036
    CON0015.condition_b = CON0033
    ACT0016.condition = CON0015
    ACT0016.game_object = "NLO:CharacterController"
    ACT0016.property_name = "isFalling"
    ACT0016.property_value = True
    CON0017.condition_a = CON0023
    CON0017.condition_b = CON0012
    ACT0018.condition = CON0013
    ACT0018.game_object = "NLO:CharacterController"
    ACT0018.property_name = "isFalling"
    ACT0018.property_value = False
    ACT0019.condition = CON0017
    ACT0019.game_object = "NLO:CharacterController"
    ACT0019.property_name = "jump"
    ACT0019.property_value = 2
    CON0020.game_object = "NLO:CharacterController"
    CON0020.property_name = "jump"
    CON0020.compare_value = 2
    CON0020.operator = 4
    CON0021.condition_a = CON0020
    CON0021.condition_b = CON0014
    ACT0022.condition = CON0021
    ACT0022.game_object = "NLO:CharacterController"
    ACT0022.property_name = "isJumping"
    ACT0022.property_value = False
    CON0023.game_object = "NLO:CharacterController"
    CON0023.property_name = "jump"
    CON0023.compare_value = 1
    CON0023.operator = 0
    ACT0024.condition = CON0061
    ACT0024.game_object = "NLO:CharacterController"
    ACT0024.property_name = "isJumping"
    ACT0024.property_value = True
    ACT0025.operator = nodes.ActionAddToGameObjectGameProperty.op_by_code("ADD")
    ACT0025.condition = CON0061
    ACT0025.game_object = "NLO:CharacterController"
    ACT0025.property_name = "jump"
    ACT0025.property_value = 1.0
    ACT0026.condition = CON0013
    ACT0026.game_object = "NLO:CharacterController"
    ACT0026.property_name = "jump"
    ACT0026.property_value = 1
    CON0027.condition_a = CON0033
    CON0027.condition_b = CON0034
    CON0028.condition_a = CON0031
    CON0028.condition_b = CON0032
    ACT0029.condition = CON0027
    ACT0029.game_object = "NLO:chr_Sonic_HD"
    ACT0029.visible = True
    ACT0029.recursive = True
    ACT0030.condition = CON0028
    ACT0030.game_object = "NLO:chr_Sonic_HD"
    ACT0030.visible = False
    ACT0030.recursive = True
    CON0031.game_object = "NLO:CharacterController"
    CON0031.property_name = "isStomping"
    CON0031.compare_value = False
    CON0031.operator = 0
    CON0032.game_object = "NLO:CharacterController"
    CON0032.property_name = "isJumping"
    CON0032.compare_value = True
    CON0032.operator = 0
    CON0033.game_object = "NLO:CharacterController"
    CON0033.property_name = "isJumping"
    CON0033.compare_value = False
    CON0033.operator = 0
    CON0034.game_object = "NLO:CharacterController"
    CON0034.property_name = "isStomping"
    CON0034.compare_value = True
    CON0034.operator = 0
    PAR0035.game_object = "NLO:RayRotate"
    PAR0035.attribute_name = "worldPosition"
    CON0036.condition = ACT0038
    PAR0037.game_object = "NLO:CharacterController"
    PAR0037.attribute_name = "worldPosition"
    ACT0038.condition = CON0059
    ACT0038.origin = PAR0037
    ACT0038.destination = PAR0035
    ACT0038.local = False
    ACT0038.property_name = "obstacle"
    ACT0038.xray = False
    ACT0038.custom_dist = False
    ACT0038.distance = 0.0
    ACT0038.visualize = False
    CON0039.condition_a = CON0042.BUTTON
    CON0039.condition_b = CON0040
    CON0040.key_code = bge.events.FKEY
    CON0040.pulse = False
    CON0041.condition_a = CON0014
    CON0041.condition_b = CON0051
    CON0042.index = 0
    CON0042.pulse = False
    CON0042.button = 1
    ACT0043.local = True
    ACT0043.condition = CON0047
    ACT0043.game_object = "NLO:CharacterController"
    ACT0043.force = mathutils.Vector((0.0, 0.0, -2000.0))
    ACT0044.condition = CON0049
    ACT0044.game_object = "NLO:CharacterController"
    ACT0044.property_name = "isStomping"
    ACT0044.property_value = True
    ACT0045.condition = CON0049
    ACT0045.game_object = "NLO:CharacterController"
    ACT0045.property_name = "isFalling"
    ACT0045.property_value = False
    ACT0046.condition = CON0041
    ACT0046.game_object = "NLO:CharacterController"
    ACT0046.property_name = "isStomping"
    ACT0046.property_value = False
    CON0047.condition_a = CON0039
    CON0047.condition_b = CON0048
    CON0048.condition_a = CON0052
    CON0048.condition_b = CON0050
    CON0049.condition_a = CON0039
    CON0049.condition_b = CON0012
    CON0050.game_object = "NLO:CharacterController"
    CON0050.property_name = "jump"
    CON0050.compare_value = 3
    CON0050.operator = 0
    CON0051.game_object = "NLO:CharacterController"
    CON0051.property_name = "isStomping"
    CON0051.compare_value = True
    CON0051.operator = 4
    CON0052.game_object = "NLO:CharacterController"
    CON0052.property_name = "jump"
    CON0052.compare_value = 2
    CON0052.operator = 0
    ACT0053.condition = ACT0044.OUT
    ACT0053.game_object = "NLO:CharacterController"
    ACT0053.property_name = "jump"
    ACT0053.property_value = 4
    PAR0054.game_object = "NLO:U_O"
    PAR0054.property_name = "jump_force"
    CON0055.game_object = "NLO:U_O"
    CON0055.property_name = "isOnWaterP"
    CON0055.compare_value = True
    CON0055.operator = 0
    ACT0056.condition = CON0055
    ACT0056.game_object = "NLO:U_O"
    ACT0056.property_name = "jump_force"
    ACT0056.property_value = 1000.0
    CON0057.game_object = "NLO:U_O"
    CON0057.property_name = "isOnWaterP"
    CON0057.compare_value = False
    CON0057.operator = 0
    ACT0058.condition = CON0057
    ACT0058.game_object = "NLO:U_O"
    ACT0058.property_name = "jump_force"
    ACT0058.property_value = 1500.0
    PAR0060.input_x = 0.0
    PAR0060.input_y = 0.0
    PAR0060.input_z = PAR0054
    CON0061.condition_a = CON0064
    CON0061.condition_b = CON0062.BUTTON
    CON0062.index = 0
    CON0062.pulse = False
    CON0062.button = 0
    ACT0063.local = True
    ACT0063.condition = CON0065
    ACT0063.game_object = "NLO:CharacterController"
    ACT0063.force = PAR0060.OUTV
    CON0064.key_code = bge.events.SPACEKEY
    CON0064.pulse = False
    CON0065.condition_a = CON0066
    CON0065.condition_b = CON0061
    CON0066.game_object = "NLO:CharacterController"
    CON0066.property_name = "jump"
    CON0066.compare_value = 1
    CON0066.operator = 0
    network.add_cell(CON0001)
    network.add_cell(CON0003)
    network.add_cell(CON0009)
    network.add_cell(CON0013)
    network.add_cell(ACT0018)
    network.add_cell(CON0020)
    network.add_cell(CON0023)
    network.add_cell(ACT0026)
    network.add_cell(CON0031)
    network.add_cell(CON0033)
    network.add_cell(PAR0035)
    network.add_cell(PAR0037)
    network.add_cell(CON0040)
    network.add_cell(CON0042)
    network.add_cell(CON0050)
    network.add_cell(CON0052)
    network.add_cell(PAR0054)
    network.add_cell(CON0057)
    network.add_cell(CON0059)
    network.add_cell(CON0062)
    network.add_cell(CON0064)
    network.add_cell(CON0066)
    network.add_cell(CON0002)
    network.add_cell(CON0010)
    network.add_cell(CON0012)
    network.add_cell(CON0017)
    network.add_cell(CON0032)
    network.add_cell(ACT0038)
    network.add_cell(CON0048)
    network.add_cell(CON0051)
    network.add_cell(CON0055)
    network.add_cell(ACT0058)
    network.add_cell(CON0061)
    network.add_cell(CON0065)
    network.add_cell(CON0004)
    network.add_cell(CON0011)
    network.add_cell(ACT0019)
    network.add_cell(ACT0024)
    network.add_cell(CON0028)
    network.add_cell(ACT0030)
    network.add_cell(CON0036)
    network.add_cell(ACT0056)
    network.add_cell(ACT0005)
    network.add_cell(ACT0008)
    network.add_cell(CON0015)
    network.add_cell(ACT0025)
    network.add_cell(CON0034)
    network.add_cell(PAR0060)
    network.add_cell(ACT0000)
    network.add_cell(CON0014)
    network.add_cell(CON0021)
    network.add_cell(CON0027)
    network.add_cell(CON0039)
    network.add_cell(CON0047)
    network.add_cell(ACT0063)
    network.add_cell(ACT0006)
    network.add_cell(ACT0016)
    network.add_cell(ACT0029)
    network.add_cell(ACT0043)
    network.add_cell(CON0049)
    network.add_cell(ACT0007)
    network.add_cell(CON0041)
    network.add_cell(ACT0045)
    network.add_cell(ACT0022)
    network.add_cell(ACT0046)
    network.add_cell(ACT0044)
    network.add_cell(ACT0053)
    owner["IGNLTree_jump"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__jump')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_jump")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
