#! usr/bin
import vtk
import os
### ANU SAMPLE FOLDERS ####
### ANU 10 - Lot10_Yshape_CF8_2AR125.5
### ANU 11 - Stone1_TwoAR1265_3.4MM_CF8_10um
### ANU 12 - Stone2_Triangularprism_CF8_2AR126.5
### ANU 13 - Stone3_Concavesurf_CF8_TwoAR126
### ANU 14 - Stone4_CF8_2AR126_ReM2Rep1
### ANU 15 - Stone5_Cuboidroughsurf2_CF8_2AR126
### ANU 16 - Stone6_Starshape_CF8_TwoAR126
### ANU 17 - Stone7_Pyramid_CF8_2AR125.5
### ANU 18 - Stone7_Pyramid_CF8_2AR125.5
### ANU 19 - Stone9_Smalltriangle_CF8_2AR125.5
##############################
##############################
path10 = "D:/DMY Projects/DiamondSample/ANU10-AT074/Lot10_Yshape_CF8_2AR125.5/"
path11 = "D:/DMY Projects/DiamondSample/ANU11-AR112/Stone1_TwoAR1265_3.4MM_CF8_10um/"
path12 = "D:/DMY Projects/DiamondSample/ANU12-AP160RW/Stone2_Triangularprism_CF8_2AR126.5/"
path13 = "D:/DMY Projects/DiamondSample/ANU13-AP145RW/Stone3_Concavesurf_CF8_TwoAR126/"
path14 = "D:/DMY Projects/DiamondSample/ANU14-AR371/Stone4_CF8_2AR126_ReM2Rep1/"
path15 = "D:/DMY Projects/DiamondSample/ANU15-AR392/Stone5_Cuboidroughsurf2_CF8_2AR126/"
path16 = "D:/DMY Projects/DiamondSample/ANU16-PG0340/Stone6_Starshape_CF8_TwoAR126/"
path17 = "D:/DMY Projects/DiamondSample/ANU17-PG0349/Stone7_Pyramid_CF8_2AR125.5/"
path18 = "D:/DMY Projects/DiamondSample/ANU18-PG0155/Stone8_ReM1_DeepFcs_TwoAR1255_CF8/"
path19 = "D:/DMY Projects/DiamondSample/ANU19-AT021/Stone9_Smalltriangle_CF8_2AR125.5/"
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

#Add Jitter Class
#Add Cut Plane Class - Done
#Add Volume Slice 3D Class - Done
#Add Mesh Slice - Done
#Add Combine Slice to render -Done/Not Accurate

##############################
# Start Rendering
##############################
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

#if CombinedSwitch == True:
    
    

            
ren.AddActor(in99)
ren.AddVolume(inv)
CombinePlaneWidget.PlaceWidget()
CombinePlaneWidget.SetInteractor(interactor)
CombinePlaneWidget.On()
interactor.Initialize()
interactor.Start()

