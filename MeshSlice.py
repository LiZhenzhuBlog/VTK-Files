import vtk


class MeshSliceViewer(object):
    def __init__(self, data_dir,reader):
        planes = vtk.vtkPlane()
        planeC = vtk.vtkPlaneCollection()
        planeC.AddItem(planes)
        # Stripper for getting smooth poly outlines,
        # gives circle and not random triangles
        stripper = vtk.vtkStripper()
        stripper.SetInputConnection(reader.GetOutputPort())
        # Clipper for PLANE
        
        clipper = vtk.vtkClipClosedSurface()
        clipper.SetInputConnection(stripper.GetOutputPort())
        clipper.SetClippingPlanes(planeC)
        clipMapper = vtk.vtkImageFlip()
        clipMapper = vtk.vtkPolyDataMapper()
        clipMapper.SetInputConnection(clipper.GetOutputPort())
        clipActor = vtk.vtkActor()
        clipActor.SetMapper(clipMapper)
        clipActor.GetProperty().SetColor(0.5,0.5,0.5)
        clipActor.GetProperty().SetOpacity(0.5)
        clipActor.SetPosition(0.001,0.001,0.001)

        clipperOutline = vtk.vtkClipClosedSurface()
        clipperOutline.SetInputConnection(stripper.GetOutputPort())
        clipperOutline.SetClippingPlanes(planeC)
        clipperOutline.GenerateFacesOff()
        clipperOutline.GenerateOutlineOn()
        innerNorms = vtk.vtkTriangleMeshPointNormals()
        innerNorms.SetInputConnection(reader.GetOutputPort())
        innerMapper = vtk.vtkOpenGLPolyDataMapper()
        innerMapper.SetInputConnection(innerNorms.GetOutputPort())
        innerActor = vtk.vtkActor()
        innerActor.SetMapper(innerMapper)

        clipperOutlineMapper = vtk.vtkPolyDataMapper()
        clipperOutlineMapper.SetInputConnection(clipperOutline.GetOutputPort())
        clipOutlineActor = vtk.vtkActor()
        clipOutlineActor.SetMapper(clipperOutlineMapper)
        clipOutlineActor.GetProperty().SetColor(0,1,0)
        clipOutlineActor.SetPosition(0.001,0.001,0.001)


        planeWidget = vtk.vtkImagePlaneWidget()
        planeWidget.SetInputConnection(reader.GetOutputPort())
        planeWidget.RestrictPlaneToVolumeOn()
        planeWidget.GetResliceOutput()
        rsx = planeWidget.GetResliceAxes()
        #planeWidget.SetSliceIndex(52)
        #planeWidget.SetOrigin(1,-1,-1)
        planeWidget.SetResliceInterpolateToLinear()
        self.clipActor = clipActor

        self.planes = planes
        self.planeWidget = planeWidget
        self.innerActor = innerActor
        self.clipOutlineActor = clipOutlineActor
        


        px = planeWidget.GetSlicePosition()
        #Cut(px)
            
            #clipActor.VisibilityOn()
        def UpdateMesh(obj, event):
            obj.GetNormal()
            self.planes.SetNormal(obj.GetNormal())
            self.planes.SetOrigin(obj.GetOrigin())
            self.clipActor.VisibilityOn()
            
        #planeWidget.AddObserver("EndInteractionEvent", CutMesh) 
        planeWidget.AddObserver("InteractionEvent", UpdateMesh)
        self.planeWidget = planeWidget
                                
