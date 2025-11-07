import copy
import threading
import time
import tkinter as tk
from collections.abc import Generator
from tkinter import messagebox, ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ===================== Scheduler Engine ===================== #
class SchedulerEngine:
    def __init__(self, processes: list[dict], algorithm: str, quantum: int = 2) -> None:
        """
        Initializes the scheduler engine.

        >>> processes = [{"pid": "P1", "arrival": 0, "burst": 4}]
        >>> engine = SchedulerEngine(processes, "FCFS")
        >>> isinstance(engine, SchedulerEngine)
        True
        """
        self.original = copy.deepcopy(processes)
        self.processes = [p.copy() for p in processes]
        self.algorithm = algorithm
        self.quantum = quantum
        for process in self.processes:
            process["remaining"] = process["burst"]
        self.timeline: list[tuple[int, str]] = []  # [(time, pid)]
        self.stats: list[tuple] = []

    def simulate(self) -> Generator[tuple[int, str | None, list[str]]]:
        """
        Runs the selected CPU scheduling algorithm.

        >>> processes = [{"pid": "P1", "arrival": 0, "burst": 2}]
        >>> engine = SchedulerEngine(processes, "FCFS")
        >>> list(engine.simulate())[:2]
        [(0, 'P1', []), (1, 'P1', [])]
        """
        algo = self.algorithm.lower()
        if algo == "fcfs":
            yield from self._simulate_fcfs()
        elif algo == "sjf (non-preemptive)":
            yield from self._simulate_sjf_np()
        elif algo == "sjf (preemptive)":
            yield from self._simulate_sjf_p()
        elif algo == "priority (non-preemptive)":
            yield from self._simulate_priority_np()
        elif algo == "priority (preemptive)":
            yield from self._simulate_priority_p()
        elif algo == "round robin":
            yield from self._simulate_rr()
        self._calculate_stats()

    # first come first serve
    def _simulate_fcfs(self) -> Generator[tuple[int, str, list[str]]]:
        """
        Simulates First Come First Serve scheduling.

        >>> processes = [{"pid": "P1", "arrival": 0, "burst": 2}]
        >>> engine = SchedulerEngine(processes, "FCFS")
        >>> next(engine._simulate_fcfs())
        (0, 'P1', [])
        """
        t = 0
        processes = sorted(self.processes, key=lambda process: process["arrival"])
        for process in processes:
            t = max(t, process["arrival"])
            for _ in range(process["burst"]):
                self.timeline.append((t, process["pid"]))
                yield (t, process["pid"], [])
                t += 1
            process["completion"] = t

    # shortest job first non preemptive
    def _simulate_sjf_np(self) -> Generator[tuple[int, str | None, list[str]]]:
        """
        Simulates Shortest Job First (Non-Preemptive).

        >>> processes = [{"pid": "P1", "arrival": 0, "burst": 2}]
        >>> engine = SchedulerEngine(processes, "SJF (Non-Preemptive)")
        >>> isinstance(engine._simulate_sjf_np(), Generator)
        True
        """
        t = 0
        processes = sorted(self.processes, key=lambda process: process["arrival"])
        done = 0
        while done < len(processes):
            ready = [
                       process
                       for process in processes
                       if process["arrival"] <= t and "completion" not in process
                    ]
            if not ready:
                t += 1
                yield (t, None, [])
                continue
            process = min(ready, key=lambda x: x["burst"])
            for _ in range(process["burst"]):
                self.timeline.append((t, process["pid"]))
                yield (t, process["pid"], [])
                t += 1
            process["completion"] = t
            done += 1

    # shortest job first preemptive
    def _simulate_sjf_p(self) -> Generator[tuple[int, str | None, list[str]]]:
        """Simulates SJF Preemptive scheduling."""
        t = 0
        processes = sorted(self.processes, key=lambda process: process["arrival"])
        done = 0
        while done < len(processes):
            ready = [
                        process
                        for process in processes
                        if process["arrival"] <= t and process["remaining"] > 0
                    ]
            if not ready:
                t += 1
                yield (t, None, [])
                continue
            process = min(ready, key=lambda x: x["remaining"])
            self.timeline.append((t, process["pid"]))
            yield (t, process["pid"], [])
            process["remaining"] -= 1
            if process["remaining"] == 0:
                process["completion"] = t + 1
                done += 1
            t += 1

    # priority non preemptive
    def _simulate_priority_np(self) -> Generator[tuple[int, str | None, list[str]]]:
        """Simulates Priority (Non-Preemptive) scheduling."""
        t = 0
        done = 0
        while done < len(self.processes):
            ready = [
                      process
                      for process in self.processes
                      if process["arrival"] <= t and "completion" not in process
                   ]
            if not ready:
                t += 1
                yield (t, None, [])
                continue
            process = min(ready, key=lambda x: x["priority"])
            for _ in range(process["burst"]):
                self.timeline.append((t, process["pid"]))
                yield (t, process["pid"], [])
                t += 1
            process["completion"] = t
            done += 1

    # priority preemptive
    def _simulate_priority_p(self) -> Generator[tuple[int, str | None, list[str]]]:
        """Simulates Priority (Preemptive) scheduling."""
        t = 0
        done = 0
        while done < len(self.processes):
            ready = [
                        process
                        for process in self.processes
                        if process["arrival"] <= t and process["remaining"] > 0
                   ]
            if not ready:
                t += 1
                yield (t, None, [])
                continue
            process = min(ready, key=lambda x: x["priority"])
            self.timeline.append((t, process["pid"]))
            yield (t, process["pid"], [])
            process["remaining"] -= 1
            if process["remaining"] == 0:
                process["completion"] = t + 1
                done += 1
            t += 1

    # round robin
    def _simulate_rr(self) -> Generator[tuple[int, str | None, list[str]]]:
        """Simulates Round Robin scheduling."""
        t = 0
        q: list[dict] = []
        processes = sorted(self.processes, key=lambda process: process["arrival"])
        i = 0
        done = 0
        while done < len(processes):
            while i < len(processes) and processes[i]["arrival"] <= t:
                q.append(processes[i])
                i += 1
            if not q:
                t += 1
                yield (t, None, [])
                continue
            process = q.pop(0)
            burst = min(self.quantum, process["remaining"])
            for _ in range(burst):
                self.timeline.append((t, process["pid"]))
                yield (t, process["pid"], [x["pid"] for x in q])
                t += 1
                process["remaining"] -= 1
                while i < len(processes) and processes[i]["arrival"] <= t:
                    q.append(processes[i])
                    i += 1
            if process["remaining"] > 0:
                q.append(process)
            else:
                process["completion"] = t
                done += 1

    def _calculate_stats(self) -> None:
        """Calculates turnaround, waiting, and response times."""
        for process in self.processes:
            pid = process["pid"]
            arrival = process["arrival"]
            burst = process["burst"]
            completion = process["completion"]
            first_exec = next((t for t, pid2 in self.timeline if pid2 == pid), arrival)
            tat = completion - arrival
            wt = tat - burst
            rt = first_exec - arrival
            self.stats.append((pid, arrival, burst, completion, tat, wt, rt))


# ===================== Interface ===================== #
class CPUSchedulerGUI:
    def __init__(self, root: tk.Tk) -> None:
        """Initializes the GUI window."""
        self.root = root
        self.root.title("CPU Scheduling Visualizer")
        self.root.geometry("1000x700")
        self.processes: list[dict] = []
        self.setup_ui()

    def setup_ui(self) -> None:
        """Sets up GUI widgets."""
        top_frame = ttk.Frame(self.root)
        top_frame.pack(pady=10)

        self.tree = ttk.Treeview(
            top_frame,
            columns=("pid", "arrival", "burst", "priority"),
            show="headings",
        )
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.capitalize())
        self.tree.pack(side="left")

        form = ttk.Frame(top_frame)
        form.pack(side="left", padx=10)
        ttk.Label(form, text="PID").grid(row=0, column=0)
        ttk.Label(form, text="Arrival").grid(row=1, column=0)
        ttk.Label(form, text="Burst").grid(row=2, column=0)
        ttk.Label(form, text="Priority").grid(row=3, column=0)
        self.pid_e = ttk.Entry(form)
        self.arrival_e = ttk.Entry(form)
        self.burst_e = ttk.Entry(form)
        self.priority_e = ttk.Entry(form)
        self.pid_e.grid(row=0, column=1)
        self.arrival_e.grid(row=1, column=1)
        self.burst_e.grid(row=2, column=1)
        self.priority_e.grid(row=3, column=1)
        ttk.Button(
                     form,
                     text="Add",
                      command=self.add_process,
                   ).grid(row=4, column=0, pady=5)
        ttk.Button(
                     form,
                     text="Delete",
                     command=self.delete_process,
                   ).grid(row=4, column=1)
        algo_frame = ttk.Frame(self.root)
        algo_frame.pack(pady=10)
        ttk.Label(algo_frame, text="Algorithm:").pack(side="left")
        self.algo_cb = ttk.Combobox(
            algo_frame,
            values=[
                "FCFS",
                "SJF (Non-Preemptive)",
                "SJF (Preemptive)",
                "Priority (Non-Preemptive)",
                "Priority (Preemptive)",
                "Round Robin",
            ],
        )
        self.algo_cb.current(0)
        self.algo_cb.pack(side="left", padx=5)
        ttk.Label(algo_frame, text="Quantum:").pack(side="left")
        self.quantum_e = ttk.Entry(algo_frame, width=5)
        self.quantum_e.insert(0, "2")
        self.quantum_e.pack(side="left")
        ttk.Button(
                     algo_frame,
                     text="Run",
                     command=self.run_scheduling,
                  ).pack(side="left", padx=10)
        self.ready_label = ttk.Label(self.root, text="Ready Queue:")
        self.ready_list = tk.Listbox(self.root, height=3)
        self.ready_label.pack_forget()
        self.ready_list.pack_forget()

        self.figure, self.ax = plt.subplots(figsize=(8, 3))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack()

        self.result_box = ttk.Treeview(
            self.root,
            columns=("pid", "arrival", "burst", "completion", "tat", "wt", "rt"),
            show="headings",
            height=6,
        )
        for col in self.result_box["columns"]:
            self.result_box.heading(col, text=col.upper())
        self.result_box.pack(pady=10)

        self.avg_label = ttk.Label(self.root, text="", font=("Arial", 11, "bold"))
        self.avg_label.pack()

    def add_process(self) -> None:
        """Adds a new process entry to the table."""
        try:
            pid = self.pid_e.get()
            arrival = int(self.arrival_e.get())
            burst = int(self.burst_e.get())
            priority = int(self.priority_e.get() or 0)
            self.processes.append(
                {"pid": pid, "arrival": arrival, "burst": burst, "priority": priority}
            )
            self.tree.insert("", "end", values=(pid, arrival, burst, priority))
        except ValueError:
            messagebox.showerror("Error", "Invalid input")

    def delete_process(self) -> None:
        """Deletes a selected process."""
        if sel := self.tree.selection():
            pid = self.tree.item(sel[0])["values"][0]
            self.processes = [p for p in self.processes if p["pid"] != pid]
            self.tree.delete(sel[0])

    def run_scheduling(self) -> None:
        """Runs the selected scheduling algorithm."""
        algo = self.algo_cb.get()
        quantum = int(self.quantum_e.get() or 2)
        if algo.lower() == "round robin":
            self.ready_label.pack()
            self.ready_list.pack()
        else:
            self.ready_label.pack_forget()
            self.ready_list.pack_forget()

        self.engine = SchedulerEngine(self.processes, algo, quantum)
        threading.Thread(target=self.animate, daemon=True).start()

    def animate(self) -> None:
        """Animates the scheduling visualization."""
        self.ax.clear()
        x: int = 0
        colors: dict[str, any] = {}
        current_pid: str | None = None
        for step in self.engine.simulate():
            _, pid, rq = step
            if pid:
                if pid != current_pid:
                    self.ax.axvline(x, color="black", linewidth=0.8)
                    current_pid = pid
                colors.setdefault(pid, plt.cm.tab20(len(colors) % 20))
                self.ax.barh(0, 1, left=x, color=colors[pid])
                self.ax.text(
                               x + 0.5,
                               0,
                               pid,
                               ha="center",
                               va="center",
                               color="white",
                               fontsize=9,
                         )
                x += 1
                self.ax.set_xticks(range(x + 1))
                self.ax.set_yticks([])
                self.ax.set_xlabel("Time")
                self.canvas.draw()
                if rq:
                    self.ready_list.delete(0, tk.END)
                    for pid_r in rq:
                        self.ready_list.insert(tk.END, pid_r)
            time.sleep(0.3)
        self.show_results()

    def show_results(self) -> None:
        """Displays scheduling results."""
        for item in self.result_box.get_children():
            self.result_box.delete(item)
        total_wt = total_tat = total_rt = 0
        for row in self.engine.stats:
            self.result_box.insert("", "end", values=row)
            total_wt += row[5]
            total_tat += row[4]
            total_rt += row[6]
        n = len(self.engine.stats) or 1
        self.avg_label.config(
            text=(
                   f"AVG WT = {total_wt/n:.2f} | "
                   f"AVG TAT = {total_tat/n:.2f} | "
                   f"AVG RT = {total_rt/n:.2f}"
                 )
        )
if __name__ == "__main__":
    root = tk.Tk()
    CPUSchedulerGUI(root)
    root.mainloop()
