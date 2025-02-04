import trimesh

# Load STL file
mesh = trimesh.load_mesh("model.stl")

# Export as GLB file
mesh.export("model.glb")