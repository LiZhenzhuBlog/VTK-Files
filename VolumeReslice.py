import vtk


class VolumeResliceViewer(object):
    def __init__(self, data_dir, PW, reader):

        # Create a greyscale lookup table
        table2 = vtk.vtkLookupTable()
        table2.SetRange(2440, 2800) # image intensity range
        table2.SetValueRange(0.0 , 1) # from black to white
        table2.SetAlphaRange(1.0 ,1.0)
        table2.SetHueRange (0.0 , 0.1)
        table2.SetSaturationRange(0.0, 0.2) # no color saturation
        table2.SetRampToLinear()
        table2.Build()


        grx = PW.GetResliceAxes()

        reslice = vtk.vtkImageReslice()
        reslice.SetInputConnection(reader.GetOutputPort())
        reslice.SetOutputDimensionality(2)
        reslice.SetResliceAxes(grx)
        reslice.SetSlabModeToMax()
        reslice.SetSlabNumberOfSlices(30)
        reslice.SetInterpolationModeToLinear()
        reslice.Update()
        # Map the image through the lookup table
        color = vtk.vtkImageMapToColors()
        color.SetLookupTable(table2)
        color.SetInputConnection(reslice.GetOutputPort())
        actor = vtk.vtkImageActor()
        actor.GetMapper().SetInputConnection(color.GetOutputPort())
        
        self.actor = actor


        
