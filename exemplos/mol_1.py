# -*- coding: cp1252 -*-

import vtk

b = vtk.vtkPDBReader()
b.SetFileName("caffeine.pdb")

m = vtk.vtkPolyDataMapper()
m.SetInput(b.GetOutput())
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
