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
os.chdir(path15)
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
##############################

##############################
#Parameters
##############################
opacityLow = 2440
opacityHigh = 2800
XCTInnerOpacityLow = 1400
XCTInnerOpacityHigh = 1500
XCTCropOpacityLow = 1750
XCTCropOpacityHigh = 1800
##############################

##############################
# Call the Readers and Actors
##############################
volume_viewer = VolumeInnerViewer("volumeInner",opacityLow,opacityHigh)
inv = volume_viewer.volume
invReader =volume_viewer.vSource

mesh_pt9_viewer = MeshPT9Viewer("XCT Mesh d0pt9 ")
in9 = mesh_pt9_viewer.actor
in9Reader = mesh_pt9_viewer.meshSource


