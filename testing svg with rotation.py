import os
import Draft

page = App.ActiveDocument.addObject('Drawing::FeaturePage')
page.Template = os.environ['USERPROFILE'] + r'\Dropbox\Mick\Drawings\Templates\500x500 Page.svg'

view = App.ActiveDocument.addObject('Drawing::FeatureViewPart')
originalObject = FreeCADGui.Selection.getSelection()[0]
selectedObject = Draft.clone(originalObject,FreeCAD.Vector(0,0,0))
fileLocation = os.environ['USERPROFILE'] + r"/Dropbox/Mick/Drawings/Drawing Test/"

Draft.rotate(selectedObject,80.0,FreeCAD.Vector(0.0,0.0,0.0),axis=FreeCAD.Vector(-0.85,-.30,-0.43),copy=False)


print(selectedObject.Placement.Rotation.Axis.x)
print(selectedObject.Placement.Rotation.Axis.y)
print(selectedObject.Placement.Rotation.Axis.z)
print(selectedObject.Placement.Rotation.Angle)


xBoundLength = selectedObject.Shape.BoundBox.XLength
yBoundLength = selectedObject.Shape.BoundBox.YLength
zBoundLength = selectedObject.Shape.BoundBox.YLength

xPlacement = selectedObject.Placement.Base.x
print(xPlacement)
yPlacement = selectedObject.Placement.Base.y
print(yPlacement)
zPlacement = selectedObject.Placement.Base.z

greaterAxis = "x"
pageWidth = 500
pageHeight = 500
margin = 10
greaterLength = xBoundLength
if(yBoundLength > greaterLength):
    greaterLength = yBoundLength
    greaterAxis = "y"

if greaterAxis == "y":
	print("yBoundLength is greater")
	desiredImageSize = pageWidth - (margin * 2)
	greaterLength = yBoundLength
	lesserLength = xBoundLength
	scale = desiredImageSize / greaterLength
	height = yBoundLength * scale
	width = xBoundLength * scale
	xMin = selectedObject.Shape.BoundBox.XMin
	yMax = selectedObject.Shape.BoundBox.YMax
	centerSpace = (pageWidth - width) / 2
	yViewPlacement = yPlacement * scale + (yMax - yPlacement )* scale + margin
	xViewPlacement = -xPlacement * scale + (xPlacement - xMin) * scale + centerSpace
	#print(xPlacement)
	#if xPlacement < 0:
	#	xViewPlacement += width
else:
	desiredImageSize = pageHeight - (margin * 2)
	greaterLength = xBoundLength
	lesserLength = yBoundLength
	scale = desiredImageSize / greaterLength
	height = yBoundLength * scale
	width = xBoundLength * scale
	xMin = selectedObject.Shape.BoundBox.XMin
	yMax = selectedObject.Shape.BoundBox.YMax
	centerSpace = (pageHeight - height) / 2
	yViewPlacement = yPlacement * scale + (yMax - yPlacement )* scale + centerSpace
	xViewPlacement = -xPlacement * scale + (xPlacement - xMin) * scale + margin


view.Source = selectedObject
view.Direction = (0. ,0. ,1)
view.Rotation = 0
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
