import bpy
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
# zemin
bpy.ops.mesh.primitive_plane_add(size=20)
m = bpy.data.materials.new("zemin"); m.use_nodes=True
m.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value=(0.8,0.8,0.85,1)
bpy.context.object.data.materials.append(m)
# top
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(1.5,1,1), segments=48, ring_count=24)
bpy.ops.object.shade_smooth()
t = bpy.data.materials.new("top"); t.use_nodes=True
t.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value=(0.9,0.2,0.1,1)
bpy.context.object.data.materials.append(t)
# yazı
bpy.ops.object.text_add(location=(-3.4,-2.2,0.01)); txt=bpy.context.object
txt.data.body="Merhaba Fizik!"; txt.data.size=0.9; txt.data.extrude=0.08
tm=bpy.data.materials.new("yazi"); tm.use_nodes=True
tm.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value=(0.05,0.2,0.7,1)
txt.data.materials.append(tm)
# ışık ve kamera
bpy.ops.object.light_add(type='SUN', location=(4,-4,8)); bpy.context.object.data.energy=3
bpy.ops.object.camera_add(location=(0,-9,5), rotation=(1.1,0,0)); sc.camera=bpy.context.object
w=bpy.data.worlds.new("w"); sc.world=w; w.use_nodes=True
w.node_tree.nodes["Background"].inputs[0].default_value=(0.25,0.4,0.7,1)
sc.view_settings.view_transform='Standard'
sc.render.engine='CYCLES'; sc.cycles.device='CPU'; sc.cycles.samples=64; sc.cycles.use_denoising=False
sc.render.resolution_x=960; sc.render.resolution_y=540
sc.render.filepath="/home/user/F-Z-K/blender_deneme/deneme.png"
bpy.ops.render.render(write_still=True)
