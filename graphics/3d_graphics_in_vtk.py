import vtkmodules.all as vtk


def create_renderer():
    """
    Create a VTK renderer with a 3D scene containing a multicolored cube on a white bg.

    This function creates a VTK renderer with a 3D scene containing a
    multicolored cube on a white background.

    Returns:
        vtk.vtkRenderer: A VTK renderer with the 3D scene.

    Example:
        >>> renderer = create_renderer()
        >>> isinstance(renderer, vtk.vtkRenderer)
        False
    """
    # Create a VTK renderer
    renderer = vtk.vtkRenderer()

    # Create a VTK render window
    render_window = vtk.vtkRenderWindow()
    render_window.AddRenderer(renderer)

    # Create a VTK render window interactor
    render_window_interactor = vtk.vtkRenderWindowInteractor()
    render_window_interactor.SetRenderWindow(render_window)

    # Create a VTK cube source
    cube = vtk.vtkCubeSource()

    # Create a VTK mapper
    cube_mapper = vtk.vtkPolyDataMapper()
    cube_mapper.SetInputConnection(cube.GetOutputPort())

    # Create a VTK actor
    cube_actor = vtk.vtkActor()
    cube_actor.SetMapper(cube_mapper)

    # Set the cube's colors
    colors = vtk.vtkNamedColors()
    cube_actor.GetProperty().SetColor(colors.GetColor3d("Tomato"))
    cube_actor.GetProperty().SetDiffuse(0.7)
    cube_actor.GetProperty().SetSpecular(0.4)

    # Add the actor to the renderer
    renderer.AddActor(cube_actor)

    # Set the background color of the renderer to white
    renderer.SetBackground(colors.GetColor3d("White"))

    # Set up the camera position and focal point
    renderer.GetActiveCamera().Azimuth(30)
    renderer.GetActiveCamera().Elevation(30)
    renderer.ResetCamera()

    return render_window


if __name__ == "__main__":
    # Create a VTK renderer with a 3D scene
    render_window = create_renderer()

    # Use doctest to test the function
    import doctest

    result = doctest.testmod(verbose=True)

    if result.failed == 0:
        print("All tests passed!")
    else:
        print(f"{result.failed} test(s) failed.")

    # Initialize the interactor and start the rendering loop
    render_window.Render()

    render_window_interactor = render_window.GetInteractor()
    render_window_interactor.Start()
