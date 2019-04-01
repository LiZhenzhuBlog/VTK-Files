import vtk


class VolumeSliceViewer(object):
    def __init__(self, data_dir,reader):
        

        table = vtk.vtkLookupTable()
        table.SetRange(2440, 2800) # image intensity range
        table.SetValueRange(0.0 , 1) # from black to white
        #table.SetAlphaRange(1.0 ,1.0)
        table.SetHueRange (0.0 , 0.1)
        table.SetSaturationRange(0.0, 0.2) # no color saturation
        table.SetRampToLinear()
        table.Build()

        planeWidget = vtk.vtkImagePlaneWidget()
        planeWidget.SetInputConnection(reader.GetOutputPort())
        planeWidget.RestrictPlaneToVolumeOn()
        planeWidget.SetResliceInterpolateToLinear()
        planeWidget.SetPlaneOrientationToXAxes()
        planeWidget.SetLookupTable(table)
        planeWidget.PlaceWidget()
        
        
        #To Update Placement of Plane Widget in MainProgram
        self.planeWidget = planeWidget
        self.reader = reader

        
        
