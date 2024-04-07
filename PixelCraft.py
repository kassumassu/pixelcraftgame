from ursina import * 
from ursina.prefabs.first_person_controller import * 
from ursina.prefabs.health_bar import * 
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
            position=position
        ) 
    def input(self, key): 
        if self.hovered: 
            if key=="t": 
                voxel = Voxel(self.position + mouse.normal) 
            if key=="y": 
                destroy(self) 
        if key=="o": 
            player.speed=15 
        if key=="p": 
            player.speed=10 
for x in range(30): 
    for z in range(30): 
        voxel = Voxel(position=(x,0,z)) 
app.run()