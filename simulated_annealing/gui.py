import threading
import tkinter as tk
from tkinter import ttk, messagebox
from typing import Optional

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from .simulated_annealing import SimulatedAnnealing
from .example import example_functions


class SA_GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulated Annealing Explorer")
        self.geometry("800x600")

        # Left: controls
        ctrl = ttk.Frame(self)
        ctrl.pack(side=tk.LEFT, fill=tk.Y, padx=8, pady=8)

        ttk.Label(ctrl, text="Function:").pack(anchor=tk.W)
        self.func_var = tk.StringVar(value="sphere")
        func_menu = ttk.Combobox(ctrl, textvariable=self.func_var, values=list(example_functions.keys()), state="readonly")
        func_menu.pack(fill=tk.X)

        ttk.Label(ctrl, text="Initial (comma-separated)").pack(anchor=tk.W, pady=(8, 0))
        self.init_entry = ttk.Entry(ctrl)
        self.init_entry.insert(0, "5, -3")
        self.init_entry.pack(fill=tk.X)

        ttk.Label(ctrl, text="Bounds (lo:hi comma-separated for each)").pack(anchor=tk.W, pady=(8, 0))
        self.bounds_entry = ttk.Entry(ctrl)
        self.bounds_entry.insert(0, "-10:10, -10:10")
        self.bounds_entry.pack(fill=tk.X)

        ttk.Label(ctrl, text="Temperature").pack(anchor=tk.W, pady=(8, 0))
        self.temp_entry = ttk.Entry(ctrl)
        self.temp_entry.insert(0, "50")
        self.temp_entry.pack(fill=tk.X)

        ttk.Label(ctrl, text="Cooling rate").pack(anchor=tk.W, pady=(8, 0))
        self.cool_entry = ttk.Entry(ctrl)
        self.cool_entry.insert(0, "0.95")
        self.cool_entry.pack(fill=tk.X)

        ttk.Label(ctrl, text="Iterations per temp").pack(anchor=tk.W, pady=(8, 0))
        self.iter_entry = ttk.Entry(ctrl)
        self.iter_entry.insert(0, "200")
        self.iter_entry.pack(fill=tk.X)

        self.run_btn = ttk.Button(ctrl, text="Run", command=self._on_run)
        self.run_btn.pack(fill=tk.X, pady=(12, 0))

        self.stop_flag = threading.Event()
        self.stop_btn = ttk.Button(ctrl, text="Stop", command=self._on_stop, state=tk.DISABLED)
        self.stop_btn.pack(fill=tk.X, pady=(6, 0))

        # Right: plot
        fig, self.ax = plt.subplots(figsize=(5, 4))
        self.fig = fig
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

        self._plot_line, = self.ax.plot([], [], label="best_cost")
        self.ax.set_xlabel("Iterations")
        self.ax.set_ylabel("Best cost")
        self.ax.grid(True)

    def _parse_initial(self) -> list:
        raw = self.init_entry.get().strip()
        parts = [p.strip() for p in raw.split(",") if p.strip()]
        return [float(p) for p in parts]

    def _parse_bounds(self, dim: int):
        raw = self.bounds_entry.get().strip()
        parts = [p.strip() for p in raw.split(",") if p.strip()]
        bounds = []
        for p in parts:
            if ":" in p:
                lo, hi = p.split(":", 1)
                bounds.append((float(lo), float(hi)))
            else:
                # single number -> symmetric
                val = float(p)
                bounds.append((-abs(val), abs(val)))
        # if fewer provided, extend with wide bounds
        while len(bounds) < dim:
            bounds.append((-1e6, 1e6))
        return bounds[:dim]

    def _on_run(self):
        try:
            initial = self._parse_initial()
        except Exception as e:
            messagebox.showerror("Input error", f"Invalid initial: {e}")
            return

        func_name = self.func_var.get()
        func = example_functions.get(func_name)
        if func is None:
            messagebox.showerror("Input error", "Unknown function")
            return

        try:
            temp = float(self.temp_entry.get())
            cooling = float(self.cool_entry.get())
            iterations = int(self.iter_entry.get())
        except Exception as e:
            messagebox.showerror("Input error", f"Invalid numeric param: {e}")
            return

        bounds = self._parse_bounds(len(initial))

        self.run_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.stop_flag.clear()

        def worker():
            sa = SimulatedAnnealing(func, initial, bounds=bounds, temperature=temp, cooling_rate=cooling, iterations_per_temp=iterations)
            best, cost, history = sa.optimize()
            # update plot on main thread
            self.after(0, lambda: self._on_complete(best, cost, history))

        t = threading.Thread(target=worker, daemon=True)
        t.start()

    def _on_stop(self):
        # currently we don't have a cooperative stop in the algorithm; inform user
        messagebox.showinfo("Stop", "Stop requested, but immediate stop is not implemented. The run will finish current loop.")

    def _on_complete(self, best, cost, history):
        x = list(range(len(history.get("best_costs", []))))
        y = history.get("best_costs", [])
        self.ax.clear()
        self.ax.plot(x, y, label="best_cost")
        self.ax.set_xlabel("Iterations")
        self.ax.set_ylabel("Best cost")
        self.ax.grid(True)
        self.ax.legend()
        self.canvas.draw()

        messagebox.showinfo("Done", f"Best cost: {cost:.6g}\nBest solution: {best}")
        self.run_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)


def main():
    app = SA_GUI()
    app.mainloop()


if __name__ == "__main__":
    main()
