import Draft

obj = FreeCADGui.Selection.getSelection()
obj.sort(key=lambda x: x.Placement.Base.z, reverse=False)

vDistance = 0
zLevel = False
first = True
for x in obj:
    if first == True:
        first = False
        vDistance = x.Shape.BoundBox.ZLength
        zLevel = x.Placement.Base.z + x.Shape.BoundBox.ZLength
        print(zLevel)
    else:
        if abs(x.Placement.Base.z) <= abs(zLevel)+.001:
            print("{} is >= {}".format(x.Placement.Base.z,zLevel))
            vDistance += x.Shape.BoundBox.ZLength
            zLevel = x.Placement.Base.z + x.Shape.BoundBox.ZLength
        else:
            print("{} is < {}".format(x.Placement.Base.z,zLevel))

stackCount = 5
doc = App.activeDocument()
group = doc.addObject("App::DocumentObjectGroup", "Full stack")
z = 0
multiplier = 1
for i in range(1,stackCount):
    for n in obj:

        # n.ViewObject.Visibility = False
        clone = Draft.clone(n)
        clone.Placement = App.Placement(App.Vector(n.Placement.Base.x,n.Placement.Base.y,n.Placement.Base.z + vDistance * multiplier),n.Placement.Rotation)
        group.addObject(clone)
    multiplier+=1