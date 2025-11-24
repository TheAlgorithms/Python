"""
Simple Interactive 3D Renderer in Tkinter.

- Demonstrates 3D meshes (Cube), perspective projection, camera movement/rotation,
  lighting, and triangle sorting for correct display order.
- Key controls: WASD/Arrow keys to move/rotate camera, Shift/Space to move up/down.

References:
https://en.wikipedia.org/wiki/3D_projection
"""

import math
import os
import tkinter as tk


class Vector3D:
    """
    3D vector class with basic arithmetic, geometric, and transformation operations.

    Examples:
        >>> v1 = Vector3D(1, 2, 3)
        >>> v2 = Vector3D(4, 5, 6)
        >>> v1 + v2
        Vector3D(5, 7, 9)
        >>> v1 - v2
        Vector3D(-3, -3, -3)
        >>> v1 * 2
        Vector3D(2, 4, 6)
        >>> v1.dot(v2)
        32
        >>> v1.cross(v2)
        Vector3D(-3, 6, -3)
        >>> round(v1.magnitude(), 9)
        3.741657387
        >>> v1.normalize()
        Vector3D(0.2672612419124244, 0.5345224838248488, 0.8017837257372732)
        >>> v1.rotate(0, 90, 0)
        Vector3D(3.0, 2.0, -1.0)
    """

    def __init__(
        self,
        x_coordinate: float = 0.0,
        y_coordinate: float = 0.0,
        z_coordinate: float = 0.0,
    ) -> None:
        """Initialize a 3D vector."""
        self.x_coordinate: float = x_coordinate
        self.y_coordinate: float = y_coordinate
        self.z_coordinate: float = z_coordinate

    def __add__(self, other: "Vector3D") -> "Vector3D":
        """Vector addition."""
        return Vector3D(
            self.x_coordinate + other.x_coordinate,
            self.y_coordinate + other.y_coordinate,
            self.z_coordinate + other.z_coordinate,
        )

    def __sub__(self, other: "Vector3D") -> "Vector3D":
        """Vector subtraction."""
        return Vector3D(
            self.x_coordinate - other.x_coordinate,
            self.y_coordinate - other.y_coordinate,
            self.z_coordinate - other.z_coordinate,
        )

    def __mul__(self, scalar: float) -> "Vector3D":
        """Scalar multiplication."""
        return Vector3D(
            self.x_coordinate * scalar,
            self.y_coordinate * scalar,
            self.z_coordinate * scalar,
        )

    def dot(self, other: "Vector3D") -> float:
        """Dot product of two vectors."""
        return (
            self.x_coordinate * other.x_coordinate
            + self.y_coordinate * other.y_coordinate
            + self.z_coordinate * other.z_coordinate
        )

    def cross(self, other: "Vector3D") -> "Vector3D":
        """Cross product of two vectors."""
        return Vector3D(
            self.y_coordinate * other.z_coordinate
            - self.z_coordinate * other.y_coordinate,
            self.z_coordinate * other.x_coordinate
            - self.x_coordinate * other.z_coordinate,
            self.x_coordinate * other.y_coordinate
            - self.y_coordinate * other.x_coordinate,
        )

    def magnitude(self) -> float:
        """Return the magnitude (length) of the vector."""
        return math.sqrt(
            self.x_coordinate**2 + self.y_coordinate**2 + self.z_coordinate**2
        )

    def normalize(self) -> "Vector3D":
        """Return a normalized (unit length) vector."""
        magnitude = self.magnitude()
        if magnitude == 0:
            return Vector3D(0, 0, 0)
        return Vector3D(
            self.x_coordinate / magnitude,
            self.y_coordinate / magnitude,
            self.z_coordinate / magnitude,
        )

    def rotate(
        self, angle_x: float = 0.0, angle_y: float = 0.0, angle_z: float = 0.0
    ) -> "Vector3D":
        """
        Rotate the vector by given Euler angles (degrees): X (pitch), Y (yaw), Z (roll).
        Rotation order: Y -> X -> Z.
        Example:
            v = Vector3D(1, 0, 0)
            v_rot = v.rotate(0, 90, 0)  # Rotate by 90° about Y
        """
        ax = math.radians(angle_x)
        ay = math.radians(angle_y)
        az = math.radians(angle_z)
        # Yaw (Y)
        x = self.x_coordinate * math.cos(ay) + self.z_coordinate * math.sin(ay)
        z = -self.x_coordinate * math.sin(ay) + self.z_coordinate * math.cos(ay)
        y = self.y_coordinate
        # Pitch (X)
        y2 = y * math.cos(ax) - z * math.sin(ax)
        z2 = y * math.sin(ax) + z * math.cos(ax)
        x2 = x
        # Roll (Z)
        x3 = x2 * math.cos(az) - y2 * math.sin(az)
        y3 = x2 * math.sin(az) + y2 * math.cos(az)
        z3 = z2
        return Vector3D(round(x3, 5), round(y3, 5), round(z3, 5))

    def __repr__(self) -> str:
        """String representation of the vector."""
        return (
            f"Vector3D({self.x_coordinate}, {self.y_coordinate}, {self.z_coordinate})"
        )


class Mesh:
    """
    Mesh with vertices, triangles (by indices), and auto-calculated normals.

    Examples:
        >>> m = Mesh()
        >>> m.vertices = [Vector3D(0,0,0), Vector3D(1,0,0), Vector3D(0,1,0)]
        >>> m.triangles = [(0,1,2)]
        >>> m.calculate_normals()
        >>> m.normals[0]
        Vector3D(0.0, 0.0, 1.0)
    """

    def __init__(self) -> None:
        self.vertices: list[Vector3D] = []
        self.triangles: list[tuple[int, int, int]] = []
        self.normals: list[Vector3D] = []
        self.position: Vector3D = Vector3D(0, 0, 0)
        self.rotation: Vector3D = Vector3D(0, 0, 0)

    def calculate_normals(self) -> None:
        """
        Recalculate the normals for every triangle (call after modifying geometry).

        Example:
            mesh.calculate_normals()
        """
        self.normals = []
        for tri in self.triangles:
            v1 = self.vertices[tri[0]]
            v2 = self.vertices[tri[1]]
            v3 = self.vertices[tri[2]]
            edge1 = v2 - v1
            edge2 = v3 - v1
            normal = edge1.cross(edge2).normalize()
            self.normals.append(normal)


class Cube(Mesh):
    """
    Unit cube mesh centered at origin.

    Examples:
        >>> c = Cube()
        >>> len(c.vertices)
        8
        >>> len(c.triangles)
        12
        >>> c.normals[0]
        Vector3D(0.0, 0.0, 1.0)
    """

    def __init__(self) -> None:
        super().__init__()
        self.vertices = [
            Vector3D(0, 0, 0),
            Vector3D(1, 0, 0),
            Vector3D(1, 1, 0),
            Vector3D(0, 1, 0),
            Vector3D(0, 0, 1),
            Vector3D(1, 0, 1),
            Vector3D(1, 1, 1),
            Vector3D(0, 1, 1),
        ]
        self.triangles = [
            # Bottom
            (0, 1, 2),
            (0, 2, 3),
            # Top
            (4, 6, 5),
            (4, 7, 6),
            # Front
            (0, 4, 5),
            (0, 5, 1),
            # Back
            (3, 2, 6),
            (3, 6, 7),
            # Left
            (0, 3, 7),
            (0, 7, 4),
            # Right
            (1, 5, 6),
            (1, 6, 2),
        ]
        self.calculate_normals()


class Camera:
    """
    Camera with position, yaw/pitch orientation, and perspective projection.

    Examples:
        >>> cam = Camera(position=Vector3D(0,0,10))
        >>> dir = cam.get_view_direction()
        >>> dir
        Vector3D(0.0, 0.0, -1.0)
        >>> cam.rotate(dyaw=90)
        >>> cam.get_view_direction()
        Vector3D(1.0, 0.0, -6.123233995736766e-17)
        >>> cam.move(1, 2, 3)
        >>> cam.position
        Vector3D(1, 2, 13)
    """

    def __init__(self, position: Vector3D, fov: float = 90) -> None:
        self.position = position
        self.fov = fov
        self.yaw = 0.0
        self.pitch = 0.0

    def move(self, dx: float, dy: float, dz: float) -> None:
        """Move the camera in 3D."""
        self.position.x_coordinate += dx
        self.position.y_coordinate += dy
        self.position.z_coordinate += dz

    def rotate(self, dyaw: float = 0.0, dpitch: float = 0.0) -> None:
        """Rotate camera view direction by given yaw/pitch degrees."""
        self.yaw += dyaw
        self.pitch += dpitch
        self.pitch = max(-89, min(89, self.pitch))

    def get_view_direction(self) -> Vector3D:
        """
        Get the current forward/look direction of the camera as a unit vector.

        Example:
            dir = camera.get_view_direction()
        """
        rad_yaw = math.radians(self.yaw)
        rad_pitch = math.radians(self.pitch)
        x = math.cos(rad_pitch) * math.sin(rad_yaw)
        y = math.sin(rad_pitch)
        z = -math.cos(rad_pitch) * math.cos(rad_yaw)
        return Vector3D(x, y, z).normalize()


def project_point(
    point: Vector3D, camera: Camera, canvas_width: int, canvas_height: int
) -> tuple[float, float]:
    """
    Projects a 3D point to 2D screen coordinates using the camera's perspective.

    Examples:
        >>> cam = Camera(position=Vector3D(0, 0, 10))
        >>> project_point(Vector3D(1, 1, 1), cam, 400, 300)
        (222.22222222222223, 172.22222222222223)
    """
    rel = point - camera.position
    view_dir = camera.get_view_direction()
    up = Vector3D(0, 1, 0)
    right = view_dir.cross(up).normalize()
    up = right.cross(view_dir).normalize()
    x_c = rel.dot(right)
    y_c = rel.dot(up)
    z_c = rel.dot(view_dir)
    focal_length = (canvas_width / 2) / math.tan(math.radians(camera.fov / 2))
    if z_c == 0:
        z_c = 0.0000001
    x_proj = (x_c * focal_length) / z_c + canvas_width / 2
    y_proj = (y_c * focal_length) / z_c + canvas_height / 2
    return x_proj, y_proj


class GraphicsWindow:
    """
    Tkinter window renderer for real-time 3D mesh display and camera control.

    Examples:
        >>> import os
        >>> if os.environ.get("DISPLAY") or os.name == "nt":
        ...     win = GraphicsWindow(width=200, height=100)  # doctest: +SKIP
        ...     isinstance(win, GraphicsWindow)  # doctest: +SKIP
        True

    Interactive controls:
        - W/A/S/D: Move camera (forward, left, back, right)
        - Up/Down/Left/Right: Rotate camera
        - Shift/Space: Move camera up/down
    """

    def __init__(
        self,
        width: int = 400,
        height: int = 300,
        title: str = "Tkinter Graphics Window",
    ) -> None:
        if not (os.environ.get("DISPLAY") or os.name == "nt"):
            raise RuntimeError("No display detected. GUI cannot be initialized")
        self.root = tk.Tk()
        self.root.title(title)
        self.width = width
        self.height = height
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="gray")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.running = True
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.meshes: list[Mesh] = []
        self.root.minsize(width, height)
        self.root.bind("<Configure>", self.on_resize)
        self.root.bind("<KeyPress>", self.on_key)
        self.root.focus_set()
        self.camera = Camera(position=Vector3D(0, 0, 10))
        # Add initial mesh
        cube = Cube()
        cube.position = Vector3D(-0.5, -0.5, 3)
        self.meshes.append(cube)

    def on_key(self, event: tk.Event) -> None:
        """
        Handle keyboard controls for interactive camera movement and rotation.
        """
        step = 0.22
        angle_step = 3
        if event.keysym == "w":
            move = self.camera.get_view_direction() * step
            self.camera.move(move.x_coordinate, move.y_coordinate, move.z_coordinate)
        elif event.keysym == "s":
            move = self.camera.get_view_direction() * -step
            self.camera.move(move.x_coordinate, move.y_coordinate, move.z_coordinate)
        elif event.keysym == "a":
            view_dir = self.camera.get_view_direction()
            right = view_dir.cross(Vector3D(0, 1, 0)).normalize()
            self.camera.move(
                -right.x_coordinate * step,
                -right.y_coordinate * step,
                -right.z_coordinate * step,
            )
        elif event.keysym == "d":
            view_dir = self.camera.get_view_direction()
            right = view_dir.cross(Vector3D(0, 1, 0)).normalize()
            self.camera.move(
                right.x_coordinate * step,
                right.y_coordinate * step,
                right.z_coordinate * step,
            )
        elif event.keysym == "space":
            self.camera.move(0, -step, 0)
        elif event.keysym == "Shift_L":
            self.camera.move(0, step, 0)
        elif event.keysym == "Up":
            self.camera.rotate(dpitch=angle_step)
        elif event.keysym == "Down":
            self.camera.rotate(dpitch=-angle_step)
        elif event.keysym == "Left":
            self.camera.rotate(dyaw=-angle_step)
        elif event.keysym == "Right":
            self.camera.rotate(dyaw=angle_step)

    def on_resize(self, event: tk.Event) -> None:
        """Resize canvas and update projection parameters on window resize."""
        if event.widget == self.root:
            self.width = event.width
            self.height = event.height
            self.canvas.config(width=self.width, height=self.height)

    def update(self) -> None:
        """
        Animate mesh rotation or handle other per-frame updates.

        Example:
            for mesh in self.meshes:
                mesh.rotation.y_coordinate += 2
        """
        for mesh in self.meshes:
            mesh.rotation.y_coordinate += 2

    def mainloop(self) -> None:
        """Start the animation and rendering loop."""

        def loop() -> None:
            if self.running:
                self.update()
                self.canvas.delete("all")
                self.render()
                self.root.after(16, loop)  # ~60 FPS

        loop()
        self.root.mainloop()

    def close(self) -> None:
        """Close the Tkinter window and stop the rendering loop."""
        self.running = False
        self.root.destroy()

    def render(self) -> None:
        """
        Render all meshes with current camera and lighting.

        Example:
            win.render()
        """
        to_draw = []
        for mesh in self.meshes:
            for i, tri in enumerate(mesh.triangles):
                # Rotate normal for lighting/culling
                normal = mesh.normals[i].rotate(
                    mesh.rotation.x_coordinate,
                    mesh.rotation.y_coordinate,
                    mesh.rotation.z_coordinate,
                )
                # Camera looks along -Z
                view_dir = self.camera.get_view_direction()
                if normal.dot(view_dir) < 0:
                    continue  # Backface culling
                light_direction = view_dir
                intensity = max(0.15, normal.dot(light_direction))
                intensity = min(1, intensity)
                shade = int(255 * intensity)
                hex_color = f"#{shade:02x}{shade:02x}{shade:02x}"

                v1 = (
                    mesh.vertices[tri[0]].rotate(
                        mesh.rotation.x_coordinate,
                        mesh.rotation.y_coordinate,
                        mesh.rotation.z_coordinate,
                    )
                    + mesh.position
                )
                v2 = (
                    mesh.vertices[tri[1]].rotate(
                        mesh.rotation.x_coordinate,
                        mesh.rotation.y_coordinate,
                        mesh.rotation.z_coordinate,
                    )
                    + mesh.position
                )
                v3 = (
                    mesh.vertices[tri[2]].rotate(
                        mesh.rotation.x_coordinate,
                        mesh.rotation.y_coordinate,
                        mesh.rotation.z_coordinate,
                    )
                    + mesh.position
                )
                x1, y1 = project_point(v1, self.camera, self.width, self.height)
                x2, y2 = project_point(v2, self.camera, self.width, self.height)
                x3, y3 = project_point(v3, self.camera, self.width, self.height)

                rel1 = v1 - self.camera.position
                rel2 = v2 - self.camera.position
                rel3 = v3 - self.camera.position
                view_dir = self.camera.get_view_direction()
                z1 = rel1.dot(view_dir)
                z2 = rel2.dot(view_dir)
                z3 = rel3.dot(view_dir)
                avg_z = (z1 + z2 + z3) / 3.0
                to_draw.append((avg_z, (x1, y1, x2, y2, x3, y3), hex_color))

        to_draw.sort(key=lambda triangle: triangle[0], reverse=True)
        for _, verts, color in to_draw:
            self.canvas.create_polygon(*verts, outline="", fill=color, width=1)


if __name__ == "__main__":
    """
    Launch the interactive 3D cube renderer.
    A window will appear; use keyboard controls to move and rotate camera.
    """

    win = GraphicsWindow()
    win.mainloop()
