# Simulated Annealing - Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SIMULATED ANNEALING IMPLEMENTATION                    │
└─────────────────────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────────────────────┐
│                              MODULE STRUCTURE                                  │
├───────────────────────────────────────────────────────────────────────────────┤
│                                                                                │
│  searches/                                                                     │
│  ├── simulated_annealing.py                  [Original Implementation]        │
│  │   ├── SearchProblem (class)               2D function optimization         │
│  │   └── simulated_annealing(function)       Basic SA algorithm               │
│  │                                                                             │
│  ├── simulated_annealing_with_gui.py         [Enhanced Implementation]        │
│  │   ├── SimulatedAnnealingOptimizer         Generic optimizer class          │
│  │   │   ├── __init__()                      Setup parameters                 │
│  │   │   ├── step()                          Single iteration                 │
│  │   │   ├── optimize()                      Complete run                     │
│  │   │   └── _generate_neighbor()            Neighbor generation              │
│  │   │                                                                         │
│  │   └── SimulatedAnnealingGUI               GUI application                  │
│  │       ├── __init__()                      Setup UI                         │
│  │       ├── _create_widgets()               Build interface                  │
│  │       ├── _start_optimization()           Run algorithm                    │
│  │       ├── _animate()                      Animation loop                   │
│  │       └── _update_plots()                 Refresh visualizations           │
│  │                                                                             │
│  ├── simulated_annealing_tsp.py              [TSP Specialization]             │
│  │   ├── City (class)                        City representation              │
│  │   │   └── distance_to()                   Calculate distance               │
│  │   │                                                                         │
│  │   ├── TSPRoute (class)                    Route representation             │
│  │   │   ├── total_distance()                Calculate route cost             │
│  │   │   ├── swap_cities()                   Simple swap                      │
│  │   │   └── reverse_segment()               2-opt move                       │
│  │   │                                                                         │
│  │   ├── TSPSimulatedAnnealing               TSP solver                       │
│  │   │   ├── __init__()                      Setup with cities                │
│  │   │   ├── step()                          TSP iteration                    │
│  │   │   └── solve()                         Find best route                  │
│  │   │                                                                         │
│  │   └── TSPGUI                              TSP visualization                │
│  │       ├── _generate_random_cities()       Create problem                   │
│  │       ├── _start_optimization()           Run TSP solver                   │
│  │       └── _update_plots()                 Update route display             │
│  │                                                                             │
│  ├── test_simulated_annealing.py             [Testing Suite]                  │
│  │   ├── test_basic_simulated_annealing()    Test original                    │
│  │   ├── test_optimizer_with_gui_module()    Test enhanced                    │
│  │   └── test_tsp_solver()                   Test TSP                         │
│  │                                                                             │
│  ├── README.md                                [Documentation]                 │
│  ├── SIMULATED_ANNEALING_GUIDE.md            [Detailed Guide]                 │
│  └── QUICK_START.md                          [Quick Reference]                │
│                                                                                │
└───────────────────────────────────────────────────────────────────────────────┘


┌───────────────────────────────────────────────────────────────────────────────┐
│                            ALGORITHM FLOW                                      │
├───────────────────────────────────────────────────────────────────────────────┤
│                                                                                │
│                        ┌──────────────────┐                                   │
│                        │   START          │                                   │
│                        │  T = T_initial   │                                   │
│                        │  state = random  │                                   │
│                        └────────┬─────────┘                                   │
│                                 │                                             │
│                                 ▼                                             │
│                        ┌────────────────────┐                                │
│                        │ Generate Neighbor  │                                │
│                        │   new_state        │                                │
│                        └────────┬───────────┘                                │
│                                 │                                             │
│                                 ▼                                             │
│                        ┌────────────────────┐                                │
│                        │ Calculate          │                                │
│                        │ ΔE = E_new - E_old │                                │
│                        └────────┬───────────┘                                │
│                                 │                                             │
│                    ┌────────────┴────────────┐                               │
│                    ▼                          ▼                               │
│           ┌─────────────┐            ┌──────────────┐                        │
│           │  ΔE < 0 ?   │            │   ΔE ≥ 0     │                        │
│           │   (Better)  │            │   (Worse)    │                        │
│           └──────┬──────┘            └──────┬───────┘                        │
│                  │                           │                                │
│                  ▼                           ▼                                │
│           ┌─────────────┐         ┌───────────────────┐                      │
│           │   ACCEPT    │         │ P = exp(-ΔE/T)    │                      │
│           │  new_state  │         │ if random() < P   │                      │
│           └──────┬──────┘         │   ACCEPT          │                      │
│                  │                │ else              │                      │
│                  │                │   REJECT          │                      │
│                  │                └────────┬──────────┘                      │
│                  │                         │                                 │
│                  └────────────┬────────────┘                                 │
│                               │                                              │
│                               ▼                                              │
│                      ┌────────────────┐                                      │
│                      │ Update Best    │                                      │
│                      │ if improved    │                                      │
│                      └────────┬───────┘                                      │
│                               │                                              │
│                               ▼                                              │
│                      ┌────────────────┐                                      │
│                      │  Cool Down     │                                      │
│                      │ T = T × α      │                                      │
│                      └────────┬───────┘                                      │
│                               │                                              │
│                    ┌──────────┴──────────┐                                   │
│                    ▼                      ▼                                   │
│           ┌─────────────┐        ┌──────────────┐                            │
│           │ T < T_min   │   OR   │ iter > max   │                            │
│           └──────┬──────┘        └──────┬───────┘                            │
│                  │                      │                                    │
│                  └──────────┬───────────┘                                    │
│                             │                                                │
│                    ┌────────┴────────┐                                       │
│                    ▼                 ▼                                       │
│              ┌──────────┐      ┌─────────┐                                  │
│              │   STOP   │      │ CONTINUE│                                  │
│              │  Return  │      │  Loop   │                                  │
│              │   Best   │      └────┬────┘                                  │
│              └──────────┘           │                                       │
│                                     │                                       │
│                                     └───────────────┐                        │
│                                                     │                        │
│                                                     ▼                        │
│                                          ┌────────────────┐                  │
│                                          │ Next Iteration │                  │
│                                          └────────────────┘                  │
│                                                                               │
└───────────────────────────────────────────────────────────────────────────────┘


┌───────────────────────────────────────────────────────────────────────────────┐
│                              GUI ARCHITECTURE                                  │
├───────────────────────────────────────────────────────────────────────────────┤
│                                                                                │
│  ┌─────────────────────────────────────────────────────────────────────────┐  │
│  │                           Tkinter Window                                 │  │
│  ├─────────────────────────────────────────────────────────────────────────┤  │
│  │  ┌───────────────────────────────────────────────────────────────────┐  │  │
│  │  │                         Control Panel                              │  │  │
│  │  ├───────────────────────────────────────────────────────────────────┤  │  │
│  │  │ Problem: [Dropdown]  Temp: [____]  Rate: [____]  Iter: [____]    │  │  │
│  │  │                                                                   │  │  │
│  │  │         [Start]  [Pause]  [Reset]                                │  │  │
│  │  │                                                                   │  │  │
│  │  │ Status: Iteration X | Cost: Y | Temp: Z                          │  │  │
│  │  └───────────────────────────────────────────────────────────────────┘  │  │
│  │                                                                           │  │
│  │  ┌───────────────────────────────────────────────────────────────────┐  │  │
│  │  │                    Matplotlib Canvas                               │  │  │
│  │  ├───────────────────────────────────────────────────────────────────┤  │  │
│  │  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐               │  │  │
│  │  │  │ Cost History│  │ Temperature │  │ Acceptance  │               │  │  │
│  │  │  │             │  │             │  │    Rate     │               │  │  │
│  │  │  │   ╱─────    │  │   ╲         │  │   ───╲     │               │  │  │
│  │  │  │  ╱          │  │    ╲        │  │       ╲    │               │  │  │
│  │  │  │ ╱           │  │     ╲       │  │        ╲___│               │  │  │
│  │  │  │─            │  │      ─      │  │            │               │  │  │
│  │  │  └─────────────┘  └─────────────┘  └─────────────┘               │  │  │
│  │  │                                                                   │  │  │
│  │  └───────────────────────────────────────────────────────────────────┘  │  │
│  └─────────────────────────────────────────────────────────────────────────┘  │
│                                                                                │
│  Data Flow:                                                                    │
│  1. User clicks "Start"                                                       │
│  2. GUI creates SimulatedAnnealingOptimizer                                   │
│  3. Animation loop calls optimizer.step()                                     │
│  4. Each step updates internal state                                          │
│  5. GUI reads history arrays                                                  │
│  6. Matplotlib plots are refreshed                                            │
│  7. Tkinter canvas is redrawn                                                 │
│  8. Loop continues until done                                                 │
│                                                                                │
└───────────────────────────────────────────────────────────────────────────────┘


┌───────────────────────────────────────────────────────────────────────────────┐
│                          TSP SPECIFIC ARCHITECTURE                             │
├───────────────────────────────────────────────────────────────────────────────┤
│                                                                                │
│  City Representation:                                                         │
│  ┌─────────────────────────────────────────────────────┐                     │
│  │ City(x, y, name)                                     │                     │
│  │   - x: float                                         │                     │
│  │   - y: float                                         │                     │
│  │   - name: str                                        │                     │
│  │   - distance_to(other): float                       │                     │
│  └─────────────────────────────────────────────────────┘                     │
│                                                                                │
│  Route Representation:                                                        │
│  ┌─────────────────────────────────────────────────────┐                     │
│  │ TSPRoute(cities, order)                              │                     │
│  │   - cities: List[City]                               │                     │
│  │   - order: List[int]  (e.g., [0,2,1,3,4])           │                     │
│  │   - total_distance(): float                          │                     │
│  │   - swap_cities(i, j): TSPRoute                      │                     │
│  │   - reverse_segment(i, j): TSPRoute (2-opt)         │                     │
│  └─────────────────────────────────────────────────────┘                     │
│                                                                                │
│  Example Route:                                                               │
│  Cities: A(0,0), B(2,5), C(8,3), D(5,8), E(9,9)                              │
│  Order: [0, 2, 4, 3, 1]                                                       │
│  Path: A → C → E → D → B → A                                                 │
│                                                                                │
│  2-opt Move Example:                                                          │
│  Original: A → B → C → D → E → A                                             │
│  Reverse segment [1:3]: A → C → B → D → E → A                               │
│                                                                                │
│  Visualization:                                                               │
│  ┌────────────────────────────────────┐                                      │
│  │  10│         ●D        ●E            │                                      │
│  │    │         │        ╱              │                                      │
│  │   8│         │      ╱                │                                      │
│  │    │         │    ╱                  │                                      │
│  │   6│         │  ╱                    │                                      │
│  │    │         │╱                      │                                      │
│  │   4│    ●B──┘        ●C             │                                      │
│  │    │    │             │              │                                      │
│  │   2│    │             │              │                                      │
│  │    │    │             │              │                                      │
│  │   0│●A──┘             │              │                                      │
│  │    └──────────────────────────────   │                                      │
│  │       0  2  4  6  8 10               │                                      │
│  └────────────────────────────────────┘                                      │
│                                                                                │
└───────────────────────────────────────────────────────────────────────────────┘


┌───────────────────────────────────────────────────────────────────────────────┐
│                            DEPENDENCIES                                        │
├───────────────────────────────────────────────────────────────────────────────┤
│                                                                                │
│  External Dependencies:                                                       │
│  ├── matplotlib >= 3.9.3      (Plotting and visualization)                   │
│  ├── tkinter                  (GUI framework - bundled with Python)           │
│  └── typing                   (Type hints - standard library)                 │
│                                                                                │
│  Standard Library:                                                            │
│  ├── math                     (Mathematical functions)                        │
│  ├── random                   (Random number generation)                      │
│  └── typing                   (Type annotations)                              │
│                                                                                │
│  Internal Dependencies:                                                       │
│  └── searches.hill_climbing   (SearchProblem class for original SA)          │
│                                                                                │
└───────────────────────────────────────────────────────────────────────────────┘


┌───────────────────────────────────────────────────────────────────────────────┐
│                        FILE ORGANIZATION                                       │
├───────────────────────────────────────────────────────────────────────────────┤
│                                                                                │
│  searches/                                                                     │
│  ├── simulated_annealing.py              [~150 lines] Original                │
│  ├── simulated_annealing_with_gui.py     [~600 lines] Enhanced                │
│  ├── simulated_annealing_tsp.py          [~600 lines] TSP Solver              │
│  ├── test_simulated_annealing.py         [~250 lines] Tests                   │
│  ├── README.md                            [~200 lines] Overview                │
│  ├── SIMULATED_ANNEALING_GUIDE.md        [~400 lines] Detailed Guide          │
│  └── QUICK_START.md                      [~250 lines] Quick Reference         │
│                                                                                │
│  Total New Code:   ~2,450 lines                                               │
│  Total New Docs:   ~850 lines                                                 │
│  Total:            ~3,300 lines                                               │
│                                                                                │
└───────────────────────────────────────────────────────────────────────────────┘
```
