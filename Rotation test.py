import FreeCAD
selectedObject = FreeCADGui.Selection.getSelection()[0]                     # our box
rot = FreeCAD.Rotation(FreeCAD.Vector(-0.85,-.30,-0.43),80)   # 45° about Z
#rot = FreeCAD.Rotation(FreeCAD.Vector(1,0,1),45)   # 45° about X and 45° about Z
#rot = FreeCAD.Rotation(10,20,30)                   # here example with Euler angle Yaw = 10 degrees (Z), Pitch = 20 degrees (Y), Roll = 30 degrees (X)
#centre = FreeCAD.Vector(selectedObject.Placement.Base.x,selectedObject.Placement.Base.y,selectedObject.Placement.Base.z)                  # central point of box
pos = selectedObject.Placement.Base                           # position point of box
newplace = FreeCAD.Placement(pos,rot)       # make a new Placement object
selectedObject.Placement = selectedObject.Placement.multiply(newplace)                        # spin the box


selectedObject = FreeCADGui.Selection.getSelection()[0]
Draft.rotate(selectedObject,80.0,FreeCAD.Vector(0.0,0.0,0.0),axis=FreeCAD.Vector(-0.85,-.30,-0.43),copy=False)