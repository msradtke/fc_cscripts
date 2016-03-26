import os

page = App.ActiveDocument.addObject('Drawing::FeaturePage')
page.Template = os.environ['USERPROFILE'] + r'\Dropbox\Mick\Drawings\Templates\500x500 Page.svg'

view = App.ActiveDocument.addObject('Drawing::FeatureViewPart')
selectedObject = FreeCADGui.Selection.getSelection()[0]
fileLocation = os.environ['USERPROFILE'] + r"/Dropbox/Mick/Drawings/Drawing Test/"

xBoundLength = selectedObject.Shape.BoundBox.XLength
zBoundLength = selectedObject.Shape.BoundBox.ZLength
xPlacement = selectedObject.Placement.Base.x
print(xPlacement)
zPlacement = selectedObject.Placement.Base.z
print(yPlacement)
#FreeCADGui.ActiveDocument.getObject(page.Name).HintOffsetX = selectedObject.Placement.Base.x
#FreeCADGui.ActiveDocument.getObject(page.Name).HintOffsetY = selectedObject.Placement.Base.y
#FreeCADGui.ActiveDocument.getObject(page.Name).HintScale = 1

pageWidth = 500
pageHeight = 500
margin = 10



if zBoundLength > xBoundLength:
	print("yBoundLength is greater")
	desiredImageSize = pageWidth - (margin * 2)
	greaterLength = zBoundLength
	lesserLength = xBoundLength
	scale = desiredImageSize / greaterLength
	height = zBoundLength * scale
	width = xBoundLength * scale
	xMin = selectedObject.Shape.BoundBox.XMin
	zMax = selectedObject.Shape.BoundBox.YMax
	centerSpace = (pageWidth - width) / 2
	yViewPlacement = zPlacement * scale + (zMax - zPlacement )* scale + margin
	xViewPlacement = -xPlacement * scale + (xPlacement - xMin) * scale + centerSpace
	print(xPlacement)
	if xPlacement < 0:
		xViewPlacement += width
else:
	desiredImageSize = pageHeight - (margin * 2)
	greaterLength = xBoundLength
	lesserLength = zBoundLength
	scale = desiredImageSize / greaterLength
	height = zBoundLength * scale
	width = xBoundLength * scale
	xMin = selectedObject.Shape.BoundBox.XMin
	zMax = selectedObject.Shape.BoundBox.ZMax
	centerSpace = (pageHeight - height) / 2
	yViewPlacement = zPlacement * scale + (zMax - zPlacement )* scale + centerSpace
	xViewPlacement = -xPlacement * scale + (xPlacement - xMin) * scale + margin


view.Source = selectedObject
view.Direction = (1.0,-1.0,1.0)
view.Rotation = 60
view.Scale = scale

view.X = xViewPlacement
view.Y = yViewPlacement
page.addObject(view)

App.ActiveDocument.recompute()

filePath = fileLocation + view.Label + ".svg"

PageFile = open(page.PageResult,'r')
OutFile = open(filePath,'w')
OutFile.write(PageFile.read())
del OutFile,PageFile
