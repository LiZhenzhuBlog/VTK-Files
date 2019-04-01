#! usr/bin
import vtk
import os
##############################
os.chdir(path16)
##############################
from VolumeInner import VolumeInnerViewer
from VolumeCrop import VolumeCropViewer
from VolumeInclusions import VolumeInclusionsViewer
from MeshPT9 import MeshPT9Viewer
from MeshPT99 import MeshPT99Viewer
from MeshInclusions import MeshInclusionsViewer
from MeshSurface import MeshSurfaceViewer
from XCTInner import XCTInnerViewer
from XCTCrop import XCTCropViewer
from VolumeSlice import VolumeSliceViewer
from VolumeReslice import VolumeResliceViewer
from MeshSlice import MeshSliceViewer
from BoxSlice import BoxSliceViewer
from RenderTool import RenTool
from CombinedSlice import CombinedSliceViewer
##############################

##############################
#Parameters
##############################
opacityLow = 2440
opacityHigh = 2800
XCTInnerOpacityLow = 1400
XCTInnerOpacityHigh = 1500
XCTCropOpacityLow = 1100
XCTCropOpacityHigh = 1160
##############################

##############################
# Call the Readers and Actors
##############################
volume_viewer = VolumeInnerViewer("volumeInner",opacityLow,opacityHigh)
inv = volume_viewer.volume
invReader =volume_viewer.vSource

volume_crop_viewer = VolumeCropViewer("volumeCrop",opacityLow,opacityHigh)
inc= volume_crop_viewer.volume
incReader =volume_crop_viewer.vSource

volume_inclusions_viewer = VolumeInclusionsViewer("volumeInclusions",opacityLow,opacityHigh)
iniv = volume_inclusions_viewer.volume
inivReader = volume_inclusions_viewer.vSource

mesh_pt9_viewer = MeshPT9Viewer("XCT Mesh d0pt9 ")
in9 = mesh_pt9_viewer.actor

mesh_pt99_viewer = MeshPT99Viewer("XCT Mesh d0pt99 ")
in99 = mesh_pt99_viewer.actor
in99Reader =mesh_pt99_viewer.meshSource

mesh_inclusions_viewer = MeshInclusionsViewer("Mesh Inclusions ")
inim = mesh_inclusions_viewer.actor
inimReader =mesh_inclusions_viewer.meshSource

mesh_surface_viewer = MeshSurfaceViewer("Mesh Surface ")
ins = mesh_surface_viewer.actor

xct_inner_viewer = XCTInnerViewer("XCT Inner Volume",XCTInnerOpacityLow,XCTInnerOpacityHigh)
inxi = xct_inner_viewer.volume
inxiReader = xct_inner_viewer.vSource

xct_crop_viewer = XCTCropViewer("XCT Crop Volume",XCTCropOpacityLow,XCTCropOpacityHigh)
inxc = xct_crop_viewer.volume
inxcReader = xct_crop_viewer.vSource

renderingTool = RenTool("Rendering Tool")
ren = renderingTool.renderer
interactor = renderingTool.interactor

CSliceViewer = CombinedSliceViewer(" Slice Widget",in99Reader)
CombinePlaneWidget = CSliceViewer.planeWidget

#############################
# SWITCHES
VSliceSwitch = False
VSliceSplitScreen = False

MSliceSwitch = False
MSliceOutline = False

BoxSliceSwitch = False

CombinedSwitch = False
##############################

#Add Jitter Class - Optional
#Add Cut Plane Class - Done
#Add Volume Slice 3D Class - Done
#Add Mesh Slice - Done
#Add Combine Slice to render -Done

##############################
# Start Rendering
##############################
renderer = vtk.vtkRenderer()
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())


render_window.SetInteractor(interactor)
renderer.SetBackground(0.2,0.2,0.2)
##############################
##############################
# Add Rendering Objects
##############################
#renderer.AddVolume(inv)
#renderer.AddVolume(inc)
#renderer.AddVolume(iniv)
#renderer.AddActor(in9)
#renderer.AddActor(in99)
#renderer.AddActor(inim)
#renderer.AddActor(ins)
#renderer.AddVolume(inxi)
#renderer.AddVolume(inxc)

interactor.Initialize()
interactor.Start()

