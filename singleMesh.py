import xml.etree.ElementTree as et

import glob

mylist = [f for f in glob.glob("*.vtu")]



el_vtk = et.Element("VTKFile")
el_vtk.set("type", "Collection")
el_vtk.set("version", "0.1")
el_col = et.SubElement(el_vtk, "Collection")
for i in sorted(mylist):
     el_dst = et.SubElement(el_col, "DataSet")
     el_dst.set("file", str(i))
tree = et.ElementTree(el_vtk)
tree.write("solution_uHh.pvd")
