from __future__ import print_function
import os
import vtk

class XCTCropViewer:
    def __init__(self, data_dir,opacityL,opacityH):
        # Read the data
        filename = "xct_crop.vti"
        vSource = vtk.vtkXMLImageDataReader()
        vSource.SetFileName(filename)
        vSource.Update()
     
        #blocks = reader1.GetOutput()
        #b0 = blocks.GetBlock(0)

        # Setup VTK environment

        #Create a mapper and actor
        opacityTransferFunction = vtk.vtkPiecewiseFunction()
        opacityTransferFunction.AddPoint(opacityL, 0.05)
        opacityTransferFunction.AddPoint( opacityH,0.06)

        colorTransferFunction = vtk.vtkColorTransferFunction()
        colorTransferFunction.AddRGBPoint(0.0, 0.0, 0.0, 0.0)
        colorTransferFunction.AddRGBPoint(64.0, 1.0, 0.2, 0.4)
        #colorTransferFunction.AddRGBPoint(128.0, 0.0, 0.0, 1.0)
        #colorTransferFunction.AddRGBPoint(192.0, 0.0, 1.0, 0.0)

        volumeProperty = vtk.vtkVolumeProperty()
        volumeProperty.SetColor(colorTransferFunction)
        #volumeProperty.SetGradientOpacity(gradientTransferFunction)
        volumeProperty.SetScalarOpacity(opacityTransferFunction)
        #volumeProperty.ShadeOn()
        volumeProperty.SetInterpolationTypeToLinear()
        volumeProperty.SetAmbient(1.0)
        volumeProperty.SetDiffuse(0.7)
        volumeProperty.SetSpecular(0.5)
        volumeMapper = vtk.vtkSmartVolumeMapper()
        volumeMapper.SetInputConnection(vSource.GetOutputPort())
        #volumeMapper.CroppingOn()
        volume = vtk.vtkVolume()
        volume.SetMapper(volumeMapper)
        volume.SetProperty(volumeProperty)
        volume.Update()
        #renderer.AddVolume(volume)

        # Mapper
        #glyph_mapper =  vtk.vtkPolyDataMapper()
        #glyph_mapper.SetInputConnection(glyphs.GetOutputPort())
        #glyph_actor = vtk.vtkActor()
        #glyph_actor.SetMapper(glyph_mapper)


        #self.b0 = b0
        self.volume = volume
        self.vSource = vSource
        #self.renderer = renderer
        #self.interactor = interactor
        #self.threshold = threshold

