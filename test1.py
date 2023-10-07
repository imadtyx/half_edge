''' Read the Stanford Bunny file in OFF format, refine it using the Loop subdivision method, 
and save the result as an OBJ file.

author:
    zhangsihao yang
'''
print('Starting the program...')

# Path to the Stanford Bunny in OFF format
data_path = 'tests/data/bunny.off'  # Update this path

import mesh

# Load the Stanford Bunny using HalfedgeMesh
bunny_mesh = mesh.HalfedgeMesh(data_path)

# Apply the Loop subdivision method to refine the mesh
bunny_mesh.loop_subdivision()

# Print some basic information about the refined mesh
print(f"Number of vertices after subdivision: {len(bunny_mesh.vertices)}")
print(f"Number of facets after subdivision: {len(bunny_mesh.facets)}")

# Save the refined mesh as an OBJ file
def save_halfmesh_as_obj(mesh, file_name):
    with open(file_name, 'w') as open_file:
        for vertex in mesh.vertices:
            lv = vertex.get_vertex()
            open_file.write("v {} {} {} \n".format(lv[0], lv[1], lv[2]))

        for face in mesh.facets:
            open_file.write("f {} {} {}\n".format(face.a+1, face.b+1, face.c+1))

save_path = 'tests/data/refined_bunny.off'  # Update this path
save_halfmesh_as_obj(bunny_mesh, save_path)

print(f"Refined Stanford Bunny saved as {save_path}")
