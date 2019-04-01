import vtk


class BoxSliceViewer(object):
    def __init__(self, data_dir,reader):

        tfun = vtk.vtkPiecewiseFunction()
        tfun.AddPoint(2440.0, 0.0)
        tfun.AddPoint(2800.0, 0.85)

        ctfun = vtk.vtkColorTransferFunction()
        ctfun.AddRGBPoint(0.0, 0.5, 0.0, 0.0)
        ctfun.AddRGBPoint(600.0, 1.0, 0.5, 0.5)
        ctfun.AddRGBPoint(1280.0, 0.9, 0.2, 0.3)
        ctfun.AddRGBPoint(1960.0, 0.81, 0.27, 0.1)
        ctfun.AddRGBPoint(4095.0, 0.5, 0.5, 0.5)

        volumeMapper = vtk.vtkGPUVolumeRayCastMapper()
        volumeMapper.SetInputConnection(reader.GetOutputPort())
        volumeMapper.SetBlendModeToComposite()

        volumeProperty = vtk.vtkVolumeProperty()
        #volumeProperty.SetColor(ctfun)
        volumeProperty.SetScalarOpacity(tfun)
        volumeProperty.SetInterpolationTypeToLinear()
        #volumeProperty.ShadeOn()

        newvol = vtk.vtkVolume()
        newvol.SetMapper(volumeMapper)
        newvol.SetProperty(volumeProperty)
        # The SetInteractor method is how 3D widgets are associated with the
        # render window interactor. Internally, SetInteractor sets up a bunch
        # of callbacks using the Command/Observer mechanism (AddObserver()).
        boxWidget = vtk.vtkBoxWidget()
        #boxWidget.SetInteractor(iren)
        boxWidget.SetPlaceFactor(1.0)


        # The implicit function vtkPlanes is used in conjunction with the
        # volume ray cast mapper to limit which portion of the volume is
        # volume rendered.
        planes = vtk.vtkPlanes()
        self.planes = planes
        def ClipVolumeRender(obj, event):
            #global self.planes, volumeMapper
            obj.GetPlanes(self.planes)
            volumeMapper.SetClippingPlanes(self.planes)


        # Place the interactor initially. The output of the reader is used to
        # place the box widget.
        boxWidget.SetInputConnection(reader.GetOutputPort())
        boxWidget.PlaceWidget()
        boxWidget.InsideOutOn()
 
        boxWidget.AddObserver("InteractionEvent", ClipVolumeRender)
        self.boxWidget = boxWidget
