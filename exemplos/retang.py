# -*- coding: cp1252 -*-

import vtk

cs = vtk.vtkCubeSource()
cs.SetXLength(5.0)
cs.SetYLength(2.0)
cs.SetZLength(4.5)
cs.Update()

m = vtk.vtkPolyDataMapper()
m.SetInput(cs.GetOutput())
m.Update()

a = vtk.vtkActor()
a.SetMapper(m)
a.GetProperty().SetColor(0, 0, 1)

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
