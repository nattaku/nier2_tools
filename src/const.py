# Block Info order:
# Bone, Unk1, Geo, SubMesh, Lod, Unk2, BoneMap, BoneSet, Mat, MeshGroup, MeshGrpMat, Unk3
# Corresponding Block Data order:
# Bone, Unk1, Geo, SubMesh, Lod, MeshGrpMat, Unk2, Boneset, BoneMap, MeshGroup, Mat, Unk3

WMB_BLK_BONE = 0
WMB_BLK_UNK1 = 1
WMB_BLK_GEO = 2
WMB_BLK_SUBMESH = 3
WMB_BLK_LOD = 4
WMB_BLK_UNK2 = 5
WMB_BLK_BONEMAP = 6
WMB_BLK_BONESET = 7
WMB_BLK_MAT = 8
WMB_BLK_MESHGROUP = 9
WMB_BLK_MESHGRPMAT = 10
WMB_BLK_UNK3 = 11

# D => Data
# E => Entry
ORDER_D2E = [
	WMB_BLK_BONE,
	WMB_BLK_UNK1,
	WMB_BLK_GEO,
	WMB_BLK_SUBMESH,
	WMB_BLK_LOD,
	WMB_BLK_MESHGRPMAT,
	WMB_BLK_UNK2,
	WMB_BLK_BONESET,
	WMB_BLK_BONEMAP,
	WMB_BLK_MESHGROUP,
	WMB_BLK_MAT,
	WMB_BLK_UNK3,
]

WMB_BLOCK_COUNT = len(ORDER_D2E)