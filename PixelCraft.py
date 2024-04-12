from ursina import * 
from ursina.prefabs.first_person_controller import * 
import random 
from perlin_noise import PerlinNoise
noise = PerlinNoise(octaves=3, seed=random.randint(1, 1000))
app = Ursina()
window.fullscreen=True 
Sky(texture="sky_sunset") 
selected_block = "grass"
player = FirstPersonController(collider='box', speed=10, mouse_sensitivity=Vec2(100,100),
                               position=(0,100,0)) 
block_textures = {
    "grass" : load_texture("grass"),  
    "brick" : load_texture("brick")
} 
class Block(Entity): 
    def __init__(self, position, block_type): 
        super().__init__(
            position=position, 
            model="cube", 
            scale=1, 
            origin_y=-0.5, 
            texture=block_textures.get(block_type), 
            collider='box' 
        )
        self.block_type = block_type 
mini_block = Entity(
    parent=camera, 
    model="cube", 
    scale=0.2, 
    texture=block_textures.get(selected_block), 
    position=(0.35, -0.25, 0.5),
    rotation=(-15, -30, -5)
)
min_height = -3
for x in range(-10, 10): 
    for z in range(-10, 10): 
        height = noise([x * 0.02, z * 0.02])
        height = math.floor(height * 7.5) 
        for y in range(height, min_height - 1, -1): 
            block = Block((x, y + min_height, z), "grass") 
def input(key): 
    global selected_block 
    if key=="t": 
        hit_info = raycast(camera.world_position, camera.forward, distance=10) 
        if hit_info.hit: 
            block = Block(hit_info.entity.position + hit_info.normal, selected_block)
    if key=="y" and mouse.hovered_entity: 
        destroy(mouse.hovered_entity)
    if key=="1": 
        selected_block = "grass"
    if key=="2": 
        selected_block = "brick" 
def update(): 
    mini_block.texture=block_textures.get(selected_block)
app.run()
