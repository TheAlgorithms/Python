<div align="center">

# 🖥️ CPU Scheduling Visualizer (Python + Tkinter)

</div>

A **GUI-based CPU Scheduling Algorithm Visualizer** built using **Python**, **Tkinter**, and **Matplotlib**.  
It allows users to add custom processes and simulate various scheduling algorithms with **real-time Gantt chart animation**, **ready queue visualization**, and **performance statistics**.

---

## 🚀 Features

✅ Interactive **Tkinter GUI**  
✅ Supports multiple **CPU scheduling algorithms**  
✅ Real-time **Gantt chart animation** using Matplotlib  
✅ Displays **Ready Queue** (for Round Robin & Preemptive algorithms)  
✅ Shows **average waiting time**, **turnaround time**, and **response time**  
✅ Add or delete processes dynamically  
✅ Clean and responsive design  

---

## ⚙️ Supported Algorithms

| Type |                  Algorithm                | Preemptive  | Non-Preemptive |
|------|-------------------------------------------|-------------|----------------|
| 🔹   | **First Come First Serve (FCFS)**         |      ❌     |     ✅        |
| 🔹   | **Shortest Job First (SJF)**              |      ✅     |     ✅        |
| 🔹   | **Priority Scheduling**                   |      ✅     |     ✅        |
| 🔹   | **Round Robin (RR)**                      |      ✅     |     ❌        |

---

## 🧮 Example Input

| PID | Arrival | Burst | Priority |
|-----|----------|--------|-----------|
| P1  | 0        | 5      | 2         |
| P2  | 1        | 3      | 1         |
| P3  | 2        | 8      | 3         |

---

## 📊 Output Example

### ➤ Gantt Chart (Animated)
Displays process execution in timeline order, showing process IDs along the time axis.

### ➤ Results Table
| PID | Arrival | Burst | Completion | TAT | WT | RT |
|-----|----------|--------|-------------|------|------|------|
| P1  | 0 | 5 | 5 | 5 | 0 | 0 |
| P2  | 1 | 3 | 8 | 7 | 4 | 4 |
| P3  | 2 | 8 | 16 | 14 | 6 | 6 |

**AVG WT = 3.33 | AVG TAT = 8.67 | AVG RT = 3.33**

---

## 🧠 Working

1. Enter process details (`PID`, `Arrival`, `Burst`, `Priority`)  
2. Choose your desired **Scheduling Algorithm**
3. (Optional) Enter Quantum value (for Round Robin)
4. Click **Run**
5. Watch the **live animation** of process execution
6. View detailed results with averages

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Tkinter** → GUI Framework  
- **Matplotlib** → Animation and Gantt Chart  
- **Threading** → Live simulation without freezing GUI  

---

## 📦 Installation & Setup

### 1️⃣ Clone this repository
```bash
git clone https://github.com/yourusername/Python
cd Python
cd scheduling
```

### 2️⃣ Install dependencies
```bash
pip install matplotlib
```

### 3️⃣ Run the application
```bash
python cpu_scheduling_interface.py
```

or

```bash
python3 cpu_scheduling_interface.py
```

## 🎥 Demo (Preview)



#### 👨‍💻 Author
Shashwat

⭐ If you find this helpful, don’t forget to star the repository!
<div align="center">

Made with ❤️ using Python & Tkinter

</div> 
