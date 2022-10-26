"""python application to view audio equalizer*
of input sound source"""
import struct
import sys

import numpy as np
import pyaudio
import pyqtgraph as pg
from pynput.keyboard import Key, Listener
from pyqtgraph.Qt import QtCore, QtGui
from scipy.fftpack import fft


class AudioStream:
    """stream audio from input source (mic) and continuously
    plot (bar) based on audio spectrum from waveform data"""

    def __init__(self, num, symbol):
        self.traces = set()
        self.number = num
        self.symbol = symbol
        # pyaudio setup
        self.FORMAT = pyaudio.paInt16  # bytes / sample
        self.CHANNELS = 1  # mono sound
        self.RATE = 44100  # samples / sec (44.1 kHz)
        self.CHUNK = 1024  # how much audio processed / frame -- set smaller for higher frame rate

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=True,
            frames_per_buffer=self.CHUNK,
        )
        # spectrum x points
        self.f = np.linspace(1, int(self.RATE / 2), 64)

        # pyqtgraph setup
        pg.setConfigOptions(antialias=True)
        self.app = QtGui.QApplication(sys.argv)
        self.win = pg.GraphicsWindow(title="Audio Spectrum")
        self.win.setGeometry(10, 52, 480 * 2, 200 * 2)
        # window content setup
        self.audio_plot = self.win.addPlot(row=1, col=1)
        self.audio_plot.setYRange(0.00, 0.25)
        self.audio_plot.setXRange(2000, int(self.RATE / 2))
        self.audio_plot.showGrid(x=True, y=True)
        self.audio_plot.hideAxis("bottom")
        self.audio_plot.hideAxis("left")

        self.a = {
            "color": "r",
            "colorIndex_x": 100,
            "colorIndex_y": 100,
            "colorIndex_z": 255,
        }

        # graph init
        self.graph = None

    @staticmethod
    def set_gradient_brush():
        """set color gradient, return QtGui.QBrush obj"""
        grad = QtGui.QLinearGradient(0, 0, 0, 1)
        grad.setColorAt(0.1, pg.mkColor("#FF0000"))
        grad.setColorAt(0.24, pg.mkColor("#FF7F00"))
        grad.setColorAt(0.38, pg.mkColor("#FFFF00"))
        grad.setColorAt(0.52, pg.mkColor("#00FF00"))
        grad.setColorAt(0.66, pg.mkColor("#0000FF"))
        grad.setColorAt(0.80, pg.mkColor("#4B0082"))
        grad.setColorAt(0.94, pg.mkColor("#9400D3"))
        grad.setCoordinateMode(QtGui.QGradient.ObjectMode)
        return QtGui.QBrush(grad)

    # Bar Graph
    def set_plotdata_1(self, name, data_x, data_y):
        """set plot with init and new data -- reference
        self.traces to verify init or recurring data input"""
        if name in self.traces:
            # update bar plot content
            self.graph.setOpts(x=data_x, height=data_y, width=350)
        else:
            self.traces.add(name)
            # initial setup of bar plot
            brush = self.set_gradient_brush()
            self.graph = pg.BarGraphItem(
                x=data_x, height=data_y, width=50, brush=brush, pen=(0, 0, 0)
            )
        self.audio_plot.addItem(self.graph)

    # Scatter Plot Graph
    def set_plotdata_2(self, name, data_x, data_y):
        data_y = data_y[:64]
        brush_default = pg.mkBrush(
            self.a["colorIndex_x"], self.a["colorIndex_y"], self.a["colorIndex_z"], 100
        )
        if name in self.traces:
            # update scatter plot content
            self.graph.clear()
            self.graph.setData(data_x, data_y, brush=brush_default)
        else:
            self.traces.add(name)
            # initial setup of scatter plot
            self.graph = pg.ScatterPlotItem(
                x=data_x,
                y=data_y,
                pen=None,
                symbol=self.symbol,
                size=30,
                brush=(100, 100, 255, 100),
            )
        self.audio_plot.addItem(self.graph)

    # Curve Graph
    def set_plotdata_3(self, name, data_x, data_y):
        data_y = data_y[:64]
        if name in self.traces:
            # update curve plot content
            self.graph.clear()
            pen1 = pg.mkPen(
                self.a["colorIndex_x"],
                self.a["colorIndex_y"],
                self.a["colorIndex_z"],
                bright=100,
            )
            self.graph = pg.PlotCurveItem(
                x=data_x,
                y=data_y,
                pen=pen1,
            )
        else:
            self.traces.add(name)
            # initial setup of curve plot
            self.graph = pg.PlotCurveItem(
                x=data_x,
                y=data_y,
                pen="r",
            )
        self.audio_plot.addItem(self.graph)

    # Line Graph
    def set_plotdata_4(self, name, data_x, data_y):
        data_y = data_y[:64]
        if name in self.traces:
            # update curve plot content
            self.graph.clear()
            pen1 = pg.mkPen(
                self.a["colorIndex_x"],
                self.a["colorIndex_y"],
                self.a["colorIndex_z"],
                bright=100,
                width=15,
                style=QtCore.Qt.DashLine,
            )
            self.graph.setData(data_x, data_y, pen=pen1, shadowPen="#19070B")
        else:
            pen1 = pg.mkPen(color=(250, 0, 0), width=15, style=QtCore.Qt.DashLine)
            self.traces.add(name)
            # initial setup of curve plot
            self.graph = pg.PlotCurveItem(
                x=data_x,
                y=data_y,
                pen=pen1,
                shadowPen="r",
            )
        self.audio_plot.addItem(self.graph)

    def update(self):
        """update plot by number which user chose"""
        plot_data = {
            1: self.set_plotdata_1,
            2: self.set_plotdata_2,
            3: self.set_plotdata_3,
            4: self.set_plotdata_4,
        }

        plot_data.get(self.number)(
            name="spectrum", data_x=self.f, data_y=self.calculate_data()
        )

    def calculate_data(self):
        """get sound data and manipulate for plotting using fft"""
        # get and unpack waveform data
        wf_data = self.stream.read(self.CHUNK, exception_on_overflow=False)
        wf_data = struct.unpack(
            str(2 * self.CHUNK) + "B", wf_data
        )  # 2 * self.CHUNK :: wf_data 2x len of CHUNK -- wf_data range(0, 255)
        # generate spectrum data for plotting using fft (fast fourier transform)
        sp_data = fft(
            np.array(wf_data, dtype="int8") - 128
        )  # - 128 :: any int less than 127 will wrap around to 256 down
        # np.abs (below) converts complex num in fft to real magnitude
        sp_data = (
            np.abs(sp_data[0 : int(self.CHUNK)])  # slice: slice first half of our fft
            * 2
            / (256 * self.CHUNK)
        )  # rescale: mult 2, div amp waveform and no. freq in your spectrum
        sp_data[sp_data <= 0.001] = 0
        return sp_data

    @staticmethod
    def start():
        """start application"""
        if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
            QtGui.QApplication.instance().exec_()

    def change_color(self, key):
        """change color in curve graph after start"""
        """
            white : 255,255,255     red : 255, 0, 0       orange : 255, 106, 0
            yellow : 255, 255, 0   green : 0, 255, 0    skyblue : 0, 255, 255
            blue : 0, 0, 255      purple: 166, 0, 255   pink : 255, 0, 255
        """
        color_index = {
            Key.f1: (255, 255, 255),  # white
            Key.f2: (255, 0, 0),  # red
            Key.f3: (255, 106, 255),  # orange
            Key.f4: (255, 255, 0),  # yellow
            Key.f5: (0, 255, 0),  # green
            Key.f6: (0, 255, 255),  # skyblue
            Key.f7: (0, 0, 255),  # blue
            Key.f8: (166, 0, 255),  # purple
            Key.f9: (255, 0, 255),  # pink
        }
        self.color_index_control()

        try:
            if key == Key.up:  # red higher
                AUDIO_APP.a["color_x"] = self.a["colorIndex_x"]
                self.a["colorIndex_x"] += 10
            elif key == Key.right:  # green higher
                AUDIO_APP.a["color_y"] = self.a["colorIndex_y"]
                self.a["colorIndex_y"] += 10
            elif key == Key.left:  # blue higher
                AUDIO_APP.a["color_z"] = self.a["colorIndex_z"]
                self.a["colorIndex_z"] += 10
            else:
                (
                    self.a["colorIndex_x"],
                    self.a["colorIndex_y"],
                    self.a["colorIndex_z"],
                ) = color_index.get(key)
        except Exception as error:
            print(error)

    def color_index_control(self):
        for color_rgb in ("colorIndex_x", "colorIndex_y", "colorIndex_z"):
            if self.a[color_rgb] >= 255:
                self.a[color_rgb] = 0

    def animation(self):
        """call self.start and self.update for continuous
        output application"""
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(20)
        self.start()


def int_to_symbol(symbol):
    symbol_to_char = {1: "d", 2: "o", 3: "x", 4: "t", 5: "s"}

    return symbol_to_char.get(symbol)


if __name__ == "__main__":
    # commonly used cout messages -------------------
    line_break = "-" * 20
    out_of_range = "Out of range! try again: "
    # -----------------------------------------------

    print("Choose and type number.")
    print(line_break)
    print("1: Bar Graph")
    print("2: Scatter Graph")
    print("3: Curve Graph")
    print("4: Line Graph")
    print("5: quit")
    print(line_break)
    symbol = "o"  # default symbol to instantiate AudioStream class
    number_input = input("Graph Type: ")
    while True:
        try:
            number = int(number_input)
            if number >= 1 and number <= 5:
                break
        except ValueError:  # i.e. not a number
            pass
        number_input = input(out_of_range)

    if number == 2:
        print("Choose symbol")
        print(line_break)
        print("1: Diamond")
        print("2: Circular")
        print("3: Cross")
        print("4: Triangular")
        print("5: Square")
        print(line_break)
        symbol = int(input("Symbol: "))
        while symbol < 1 or symbol > 5:
            symbol = int(input(out_of_range))
        symbol = int_to_symbol(symbol)
    elif number == 5:
        exit()

    AUDIO_APP = AudioStream(number, symbol)
    with Listener(on_press=AUDIO_APP.change_color) as listener:
        AUDIO_APP.animation()
    listener.join()
