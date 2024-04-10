from ursina import * 
from ursina.prefabs.first_person_controller import * 
from ursina.prefabs.health_bar import * 
import random 
from perlin_noise import PerlinNoise 
noise = PerlinNoise(octaves=3, seed=random.randint(1, 1000)) 
app = Ursina()
window.fullscreen=True 
Sky(texture="sky_sunset") 
player=FirstPersonController(collider='box', speed=10) 
class Voxel(Button): 
    def __init__(self, position=(0,0,0)): 
        super().__init__(
            model="cube",
            parent=scene, 
            color=color.green, 
            texture="grass", 
            collider="box", 
            position=position, 
            highlight_color=color.lime
        ) 
    def input(self, key): 
        if self.hovered: 
            if key=="t": 
                arm.position=(0.6, -0.5)
                voxel = Voxel(self.position + mouse.normal) 
            elif key=="y": 
                arm.position=(0.6, -0.5)
                destroy(self) 
            else: 
                arm.position=(0.75, -0.4)
        if key=="o": 
            player.speed=15 
        if key=="p": 
            player.speed=10
for x in range(-10, 10): 
    for z in range(-10, 10): 
        height=noise([x * 0.02, z * 0.02])
        height=math.floor(height * 7.5)
        voxel = Voxel(position=(x,height,z)) 
arm=Entity(
    model="cube", 
    parent=camera.ui,  
    scale=(0.2, 0.2, 0.5), 
    position=(0.75, -0.4), 
    rotation=(-150, -5, 6), 
    texture="grass", 
    color=color.green
)
app.run()
