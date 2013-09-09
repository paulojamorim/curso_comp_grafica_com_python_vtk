# -*- coding: cp1252 -*-

import vtk

pdb0 = vtk.vtkPDBReader()
pdb0.SetFileName("caffeine.pdb")

sp = vtk.vtkSphereSource()

gly = vtk.vtkGlyph3D()
gly.SetInput(pdb0.GetOutput())
gly.SetColorMode(1)
gly.SetScaleMode(2)
gly.SetScaleFactor(0.5)
gly.SetSource(sp.GetOutput())

tb = vtk.vtkTubeFilter()
tb.SetInput(pdb0.GetOutput())
tb.SetNumberOfSides(20)
tb.SetRadius(0.2)

app = vtk.vtkAppendPolyData()
app.AddInput(gly.GetOutput())
app.AddInput(tb.GetOutput())

m = vtk.vtkPolyDataMapper()
m.SetInput(app.GetOutput())
m.Update()

a = vtk.vtkActor()
a.SetMapper(m)

ren = vtk.vtkRenderer()
ren.SetBackground(1, 1, 1)
ren.AddActor(a)
ren.ResetCamera()

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

rwi = vtk.vtkRenderWindowInteractor()
rwi.SetRenderWindow(renWin)
rwi.Initialize()
rwi.Render()
rwi.Start()
