import ifcopenshell

ifc_file = ifcopenshell.open("AC20-FZK-Haus.ifc")
print(f"IFC file loaded:", ifc_file.schema)

project = ifc_file.by_type("IfcProject")[0]
project_name = project.Name 
print(f"Project Name: {project_name}")
print()

stairs = ifc_file.by_type("IFCStair")
print(f"Number of stairs: {len(stairs)}")

for stair in stairs:
	print(stair.GlobalId, stair.Name)

slabs = ifc_file.by_type("IFCSlab")
print(f"Number of slabs: {len(slabs)}")

slabs = ifc_file.by_type("IfcSlab")
for i, slab in enumerate(slabs,1):
	slab.Name = f"Renamed_Slab_{i}"
	print(f"Updated Slab: {slab.GlobalId} → {slab.Name}")
print()

project = ifc_file.by_type("IfcProject")[0]
for site in project.IsDecomposedBy[0].RelatedObjects:
	for building in site.IsDecomposedBy[0].RelatedObjects:
		for storey in building.IsDecomposedBy[0].RelatedObjects:
			print("Storey", storey.Name, "Elevation", storey.Elevation)
print()

types = set(el.is_a() for el in ifc_file)
PREFIX_TO_REMOVE = "Object Types in Files: "
object_types = list(types)
print(PREFIX_TO_REMOVE, end="")
first_object = True
for element in object_types:
	if not first_object:
		print(", ", end="")
	print(element, end="")
	first_object = False
print()

ifc_file.write("AC20-FZK-Haus_renamed.ifc")