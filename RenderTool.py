import vtk


class RenTool(object):
    def __init__(self, data_dir):
        renderer = vtk.vtkRenderer()
        render_window = vtk.vtkRenderWindow()
        render_window.AddRenderer(renderer)
        interactor = vtk.vtkRenderWindowInteractor()
        interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
        render_window.SetInteractor(interactor)
        renderer.SetBackground(0.2,0.2,0.2)

        self.renderer = renderer
        self.interactor = interactor
        
                
