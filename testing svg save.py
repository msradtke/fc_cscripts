page = App.ActiveDocument.addObject('Drawing::FeaturePage','Page100')
page.Template = r'C:\Users\MICK\Dropbox\Mick\Drawings\Templates\500x500 Page.svg'

view = App.ActiveDocument.addObject('Drawing::FeatureViewPart','View100')
selectedObject = FreeCADGui.Selection.getSelection()[0]

xBoundLength = selectedObject.Shape.BoundBox.XLength
yBoundLength = selectedObject.Shape.BoundBox.YLength
xPlacement = selectedObject.Placement.Base.x
yPlacement = selectedObject.Placement.Base.y

#FreeCADGui.ActiveDocument.getObject(page.Name).HintOffsetX = selectedObject.Placement.Base.x
#FreeCADGui.ActiveDocument.getObject(page.Name).HintOffsetY = selectedObject.Placement.Base.y
#FreeCADGui.ActiveDocument.getObject(page.Name).HintScale = 1

pageWidth = 500
pageHeight = 500
margin = 10

scale = desiredImageSize / greaterLength

height = yBoundLength * scale
width = xBoundLength * scale

if yBoundLength > xBoundLength:
	desiredImageSize = pageWidth - (margin * 2)
	greaterLength = yBoundLength
	lesserLength = xBoundLength
	scale = desiredImageSize / greaterLength
	centerSpace = (pageWidth - width) / 2
	yViewPlacement = (yPlacement * scale) + margin + height
	xViewPlacement = -(xPlacement * scale) + centerSpace
else:
	desiredImageSize = pageHeight - (margin * 2)
	greaterLength = xBoundLength
	lesserLength = yBoundLength
	scale = desiredImageSize / greaterLength
	centerSpace = (pageHeight - height) / 2
	yViewPlacement = (yPlacement * scale) + centerSpace + height
	xViewPlacement = -(xPlacement * scale) + margin


view.Source = selectedObject
view.Direction = (0.0,0.0,1.0)
view.Scale = scale

view.X = xViewPlacement
view.Y = yViewPlacement
page.addObject(view)


