import Draft

obj = FreeCADGui.Selection.getSelection()
obj.sort(key=lambda x: x.Placement.Base.z, reverse=False)
#step = max(n.Shape.BoundBox.ZLength for n in obj)

doc = App.activeDocument()
group = doc.addObject("App::DocumentObjectGroup", "ExplodedView")
z = 0
zLevel = False
first = True
for n in obj:
    if first == True:
        first = False
        print("is false")
        zLevel = n.Placement.Base.z
        if(zLevel == False):
            print("Zlevel is false")
        print("new object's z: {}",n.Placement.Base.z)
        print("z level: {}",zLevel)
    else:
        print("new object's z: {}",n.Placement.Base.z)
        print("z level: {}",zLevel)
        if abs(abs(n.Placement.Base.z) - abs(zLevel)) > .001:
            print("is greater")
            z=z+100
            zLevel = n.Placement.Base.z

    # n.ViewObject.Visibility = False
    clone = Draft.clone(n)
    print("z is{}",z)
    print("new z is {}",n.Placement.Base.z + z)

    clone.Placement = App.Placement(App.Vector(n.Placement.Base.x,n.Placement.Base.y,n.Placement.Base.z + z),n.Placement.Rotation)
    group.addObject(clone)
