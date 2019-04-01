from __future__ import print_function
import os
import vtk

class MeshInclusionsViewer:
    def __init__(self, data_dir):
        # Read the data
        filename = "inclusions_all.ply"

        # Read Mesh
        meshSource = vtk.vtkPLYReader()
        meshSource.SetFileName(filename)
        meshSource.Update()
        
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(meshSource.GetOutputPort())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetOpacity(0.9)
        self.actor = actor
        self.meshSource = meshSource


