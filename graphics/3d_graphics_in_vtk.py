import vtkmodules.all as vtk
from vtkmodules.util.colors import tomato, white


def create_renderer() -> vtk.vtkRenderWindowInteractor:
    """
    Create a VTK renderer with a 3D scene containing a multicolored cube 
    on a white background.

    This function creates a VTK renderer with a 3D scene containing a
    multicolored cube on a white background.

    Returns:
        vtk.vtkRenderWindowInteractor: A VTK render window interactor for interaction.

    Example:
        >>> render_window_interactor = create_renderer()
        >>> isinstance(render_window_interactor, vtk.vtkRenderWindowInteractor)
        True
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
    cube_actor.GetProperty().SetColor(tomato)
    cube_actor.GetProperty().SetDiffuse(0.7)
    cube_actor.GetProperty().SetSpecular(0.4)

    # Add the actor to the renderer
    renderer.AddActor(cube_actor)

    # Set the background color of the renderer to white
    renderer.SetBackground(white)

    # Set up the camera position and focal point
    renderer.GetActiveCamera().Azimuth(30)
    renderer.GetActiveCamera().Elevation(30)
    renderer.ResetCamera()

    return render_window_interactor


if __name__ == "__main__":
    # Create a VTK renderer with a 3D scene
    render_window_interactor = create_renderer()

    # Use doctest to test the function
    import doctest

    result = doctest.testmod(verbose=True)

    if result.failed == 0:
        print("All tests passed!")
    else:
        print(f"{result.failed} test(s) failed.")

    # Initialize the interactor and start the rendering loop
    render_window_interactor.Start()
