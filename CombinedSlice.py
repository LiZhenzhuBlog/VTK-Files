import vtk


class CombinedSliceViewer(object):
    def __init__(self, data_dir,Mreader,Vreader):
        # inv,inc,iniv,inxi,inxc Volume
        # in9,in99,inim,ins Actors
        planes = vtk.vtkPlane()
        #planes.SetOrigin(0,-1,0)
        #planes.SetNormal(1,0,0)
        planeC = vtk.vtkPlaneCollection()
        planeC.AddItem(planes)
        ######################################################
        # Strip, Clip, Mapper, Actor

        # Stripper for getting smooth poly outlines,
        # gives circle and not random triangles
        stripper = vtk.vtkStripper()
        stripper.SetInputConnection(Mreader.GetOutputPort())
        # Clipper for PLANE 1 Stripper 1
        clipper = vtk.vtkClipClosedSurface()
        clipper.SetInputConnection(stripper.GetOutputPort())

        #clip.Update()

        clipperOutline = vtk.vtkClipClosedSurface()
        clipperOutline.SetInputConnection(stripper.GetOutputPort())
        clipperOutline.SetClippingPlanes(planeC)
        clipperOutline.GenerateFacesOff()
        clipperOutline.GenerateOutlineOn()

        innerNorms = vtk.vtkTriangleMeshPointNormals()
        innerNorms.SetInputConnection(Mreader.GetOutputPort())
        innerMapper = vtk.vtkOpenGLPolyDataMapper()
        innerMapper.SetInputConnection(innerNorms.GetOutputPort())
        innerActor = vtk.vtkActor()
        innerActor.SetMapper(innerMapper)

        clipMapper = vtk.vtkImageFlip()
        clipMapper = vtk.vtkPolyDataMapper()
        clipMapper.SetInputConnection(clipper.GetOutputPort())
        clipActor = vtk.vtkActor()
        clipActor.SetMapper(clipMapper)
        clipActor.GetProperty().SetColor(1,0.5,0.5)
        clipActor.GetProperty().SetOpacity(0.5)
        clipActor.SetPosition(0.001,0.001,0.001)

        clipperOutlineMapper = vtk.vtkPolyDataMapper()
        clipperOutlineMapper.SetInputConnection(clipperOutline.GetOutputPort())
        clipOutlineActor = vtk.vtkActor()
        clipOutlineActor.SetMapper(clipperOutlineMapper)
        clipOutlineActor.GetProperty().SetColor(0,1,0)
        clipOutlineActor.SetPosition(0.001,0.001,0.001)


        tfun = vtk.vtkPiecewiseFunction()
        tfun.AddPoint(0,0)
        tfun.AddPoint(1600,0.05)
        tfun.AddPoint(2500,0.15)
        tfun.AddPoint(2400, 0.0)
        tfun.AddPoint(2540, 0.97)



        volumeMapper = vtk.vtkGPUVolumeRayCastMapper()
        volumeMapper.SetInputConnection(Vreader.GetOutputPort())
        volumeMapper.SetBlendModeToComposite()


        volumeProperty = vtk.vtkVolumeProperty()
        volumeProperty.SetScalarOpacity(tfun)
        volumeProperty.SetInterpolationTypeToLinear()
        volumeProperty.ShadeOn()

        newvol = vtk.vtkVolume()
        newvol.SetMapper(volumeMapper)
        newvol.SetProperty(volumeProperty)
        #######################
        planeWidget = vtk.vtkImagePlaneWidget()
        planeWidget.RestrictPlaneToVolumeOn()
        planeWidget.SetInputConnection(Mreader.GetOutputPort())
        planeWidget.RestrictPlaneToVolumeOn()
        planeWidget.GetResliceOutput()
        rsx = planeWidget.GetResliceAxes()
        #planeWidget.SetSliceIndex(52)
        #planeWidget.SetOrigin(1,-1,-1)
        planeWidget.SetResliceInterpolateToLinear()
        planeWidget.PlaceWidget()
        #planeWidget.SetInteractor(iren)


        px = planeWidget.GetSlicePosition()
        #Cut(px)

        #clipActor.VisibilityOn()
        def UpdateMesh(obj, event):
            #global planes, clipActor
            obj.GetNormal()
            planes.SetNormal(obj.GetNormal())
            planes.SetOrigin(obj.GetOrigin())
            clipper.SetClippingPlanes(planeC)
            clipActor.VisibilityOn()
        planesS = vtk.vtkPlanes()
        def ClipVolumeRender(obj, event):
            #global planes, volumeMapper
            planes.SetOrigin(obj.GetOrigin())
            x2 = obj.GetOrigin()[0]
            y2 = obj.GetOrigin()[1]
            z2 = obj.GetOrigin()[2]
            x3 = obj.GetPoint1()[0]
            y3 = obj.GetPoint1()[1]
            z3 = obj.GetPoint1()[2]
            x1 = obj.GetPoint2()[0]
            y1 = obj.GetPoint2()[1]
            z1 = obj.GetPoint2()[2]
            a1 = x2 - x1 
            b1 = y2 - y1 
            c1 = z2 - z1 
            a2 = x3 - x1 
            b2 = y3 - y1 
            c2 = z3 - z1 
            a = b1 * c2 - b2 * c1 
            b = a2 * c1 - a1 * c2 
            c = a1 * b2 - b1 * a2 
            d = (- a * x1 - b * y1 - c * z1) 

            #level1 = list([x,y,z,0,x,y,z,0,x,y,z,0,x,y,z,0,x,y,z,0,x,y,z,0])
            level1 = list([-a,-b,-c,-d,-a,-b,-c,-d,-a,-b,-c,-d,-a,-b,-c,-d,-a,-b,-c,-d,-a,-b,-c,-d])
            print(a,b,c,d)
            planesS.SetFrustumPlanes(level1)

            #level2 = list([xMin,xMax, yMin,yMax,zMin,zMax])
            #planesS.SetBounds(level2)
            #planesS.SetNormals(obj.GetNormal())
            #planesS.GetPlane(0,planes)
            volumeMapper.SetClippingPlanes(planesS)
            #print(planesS.GetPoints())
            newvol.VisibilityOn()
            
        ClipVolumeRender(planeWidget, "STR")
        UpdateMesh(planeWidget, "STR")
        #planeWidget.AddObserver("EndInteractionEvent", CutMesh)
        #planeWidget.AddObserver("StartInteractionEvent", StartInteraction)
        planeWidget.AddObserver("InteractionEvent", UpdateMesh)
        #planeWidget.AddObserver("EndInteractionEvent", CutMesh) 
        planeWidget.AddObserver("InteractionEvent", ClipVolumeRender)
        #planeWidget.AddObserver("EndInteractionEvent", EndInteraction)
        self.planeWidget = planeWidget
        #self.reader = reader
        self.clipActor = clipActor
        #ren1.AddActor(VActor)
        self.newvol = newvol
        self.clipOutlineActor = clipOutlineActor
