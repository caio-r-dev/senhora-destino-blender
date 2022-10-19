import bpy
import random

collection = bpy.data.collections['Cutouts']

objects = collection.objects
i = 0
offsetX = i
for object in objects:
            
    activeMaterial = object.active_material
    
    imageTextureNode = activeMaterial.node_tree.nodes.get("Image Texture")
    imageTextureNode.location = (-700,300)
    hueSaturationNode = activeMaterial.node_tree.nodes.new('ShaderNodeHueSaturation')
    hueSaturationNode.location = (-300,300)
    principledBDSFNode = activeMaterial.node_tree.nodes.get("Principled BSDF")
    
    link = activeMaterial.node_tree.links.new
    link(imageTextureNode.outputs[0],hueSaturationNode.inputs[4])
    link(hueSaturationNode.outputs[0],principledBDSFNode.inputs[0])

    hueSaturationNode.inputs[1].default_value = 0.000
    hueSaturationNode.inputs[2].default_value = 0.300
    
    
    if activeMaterial:
        object.active_material = activeMaterial.copy()
        
    object.active_material.blend_method = 'CLIP'
    object.active_material.shadow_method = 'CLIP'

    rowSize = 50
    offsetY = i * 0.95
    if(i % rowSize == 0):
        offsetX =  offsetX + 2.70
        i = 0
    
    variationX = random.uniform(-0.2, 0.2)
    variationY = random.uniform(-0.2, 0.2)
    #variationX = 0
    #variationY = 0
    object.location = (offsetX + variationX, 2 + offsetY + variationY, 0)
    
    i = i +1 
  
