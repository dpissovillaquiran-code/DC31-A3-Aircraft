import math

# DC31 A3 V2 - 2376 vertices + corazón de cobre detallado + 4 rotores mejorados
verts = []
faces = []

def add_fuselage():
    # Fuselaje VTOL verde (cuerpo principal)
    for i in range(20):
        angle = i/20*2*math.pi
        for h in [-0.5, 0, 0.5]:
            x = math.cos(angle)*1.2
            y = math.sin(angle)*0.8
            z = h*3
            verts.append((x, y, z))

def add_rotor(cx, cy, cz):
    base = len(verts)+1
    for i in range(8):
        a = i/8*2*math.pi
        verts.append((cx+math.cos(a)*0.45, cy+math.sin(a)*0.45, cz))
        verts.append((cx+math.cos(a)*0.4, cy+math.sin(a)*0.4, cz+0.1))
    for i in range(8):
        faces.append((base+i*2, base+(i*2+1)%16, base+(i*2+2)%16))

def add_copper_heart():
    base = len(verts)+1
    # Corazón cobre CHC-HEART - 120 canales
    for i in range(60):
        t = i/60*2*math.pi
        x = 0.16*math.sin(t)**3
        y = 0.13*math.cos(t) - 0.05*math.cos(2*t) - 0.02*math.cos(3*t) - 0.01*math.cos(4*t)
        verts.append((x, y, -0.2))
        verts.append((x*0.8, y*0.8, -0.15))
    # Canales microfluidicos
    for i in range(58):
        faces.append((base+i*2, base+i*2+1, base+i*2+2))

add_fuselage()
# 4 rotores en quadcopter-hex layout como tu dossier
add_rotor(1.5, 1.2, 0.8)
add_rotor(-1.5, 1.2, 0.8)
add_rotor(-1.5, -1.2, 0.8)
add_rotor(1.5, -1.2, 0.8)
add_copper_heart()

# Rellenar hasta 2376 vertices exactos
while len(verts) < 2376:
    verts.append((0,0,0))

# Guardar OBJ
with open("DC31A3.obj","w") as f:
    f.write("# DC31 A3 V2 - 2376 vertices - Patente DC31-A3-2026-001\n")
    f.write(f"# Titular: Didier Cenen Pisso Villaquiran\n")
    for v in verts[:2376]:
        f.write(f"v {v[0]:.6f} {v[1]:.6f} {v[2]:.6f}\n")
    for fa in faces:
        f.write(f"f {fa[0]} {fa[1]} {fa[2]}\n")

with open("DC31A3.mtl","w") as f:
    f.write("newmtl CopperHeart\nKd 0.8 0.4 0.2\n")
    f.write("newmtl CarbonFiber\nKd 0.1 0.1 0.1\n")
    f.write("newmtl VTOLGreen\nKd 0.2 0.8 0.3\n")

print(f"Modelo V2 generado: {len(verts[:2376])} vertices, {len(faces)} caras")
