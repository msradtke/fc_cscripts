import Draft

obj = FreeCADGui.Selection.getSelection()
obj.sort(key=lambda x: x.Placement.Base.z, reverse=False)

vDistance = 0
zLevel = False
vDistance = obj[-1].Placement.Base.z + abs(obj[0].Shape.BoundBox.ZLength - obj[0].Placement.Base.z)
print(vDistance)
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