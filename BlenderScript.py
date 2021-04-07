import bpy
from math import *
from mathutils import *
import os

input = 'input'
output = 'output'
output_mask = 'output_mask'

teeths = ['all', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
selected_teeths = teeths[1]  # H

targetName = '000003_2'
# set your own target here
path = 'D:\\Renders\\Render_annotation'
target = bpy.data.objects[targetName]
cam = bpy.data.objects['Camera']
t_loc_x = target.location.x
t_loc_y = target.location.y
t_loc_z = target.location.z

my_areas = bpy.context.workspace.screens[0].areas


def setLights(light='STUDIO'):
    for area in my_areas:
        for space in area.spaces:
            if space.type == 'VIEW_3D':
                space.shading.light = light


target.rotation_euler[0] = 0
target.rotation_euler[1] = 0
target.rotation_euler[2] = 0
step = 30

angle = -90  # how many rotation steps
for x in range(angle, abs(angle), step):
    for y in range(angle, abs(angle), step):
        for z in range(angle, abs(angle), step):
            target.rotation_euler[0] = radians(x)
            target.rotation_euler[1] = radians(y)
            target.rotation_euler[2] = radians(z)
            bpy.ops.object.mode_set(mode='SCULPT')
            setLights()

            # bpy.types.View3DShading.light = 'STUDIO';

            file = os.path.join(path, targetName, input, selected_teeths,
                                ('x=' + str(x) + 'y=' + str(y) + 'z=' + str(z)))
            bpy.context.scene.render.filepath = file
            bpy.ops.render.opengl(write_still=True)

            bpy.ops.object.mode_set(mode='VERTEX_PAINT')

            file = os.path.join(path, targetName, output, selected_teeths,
                                ('x=' + str(x) + 'y=' + str(y) + 'z=' + str(z)))

            bpy.context.scene.render.filepath = file
            bpy.ops.render.opengl(write_still=True)

            setLights('FLAT')

            file = os.path.join(path, targetName, output_mask, selected_teeths,
                                ('x=' + str(x) + 'y=' + str(y) + 'z=' + str(z)))
            bpy.context.scene.render.filepath = file
            bpy.ops.render.opengl(write_still=True)