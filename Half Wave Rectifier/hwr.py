from __future__ import annotations

from typing import NamedTuple

class Result(NamedTuple):
  name: str
  value: float

def max_load_current(Rf: float, Rs: float, Rl: float, Vm: float) ->tuple:
  """
  This function can calculate the maximum load current(Im) in a half wave rectifier circuit.
  Im = maximum load current
  Rf = Forward Resistance of Diode
  Rs = Transformer secondary winding resistance
  Rl = load resistance
  Vm = maximum volatge or peak voltage
  Cases:-
  >>> max_load_current(Rf=2 , Rs=4 , Rl=6 , Vm=15 )
  Result(name='max_load_current, value=1.25)
  >>> max_load_current(Rf=2 , Rs=4 , Rl=6 , Vm=0 )
  Result(name='max_load_current, value=0.0)
  >>> max_load_current(Rf=2 , Rs=-4 , Rl=6 , Vm=15 )
  Traceback (most recent call last):
      ...
  ValueError: Resistance cannot be negative
  >>> max_load_current(Rf=0 , Rs=0 , Rl=0 , Vm=15 )
  Traceback (most recent call last):
      ...
  ValueError: Atleast one Resistance must be non zero
  """
  if (Rf, Rs, Rl).count(0) == 3:
    raise ValueError("Atleast one Resistance must be non zero")
  elif (Rf<0 or Rs<0 or Rl<0):
    raise ValueError("Resistance cannot be negative")
  elif Vm==0:
    return Result("max_load_current ", Vm/(Rf+Rs+Rl))
  else:
    return Result("max_load_current ", Vm/(Rf+Rs+Rl))

def DC_current(Idc: float, Im: float) ->tuple:
  """
  This function can calculate the Average DC Current(Idc) in a circuit.
  In all cases negative sign shows the opposite direction of current or voltage.
  Idc = average dc current
  Im = maximum current or peak current
  cases:
  >>>DC_current(Im=2)
  Result(name='Idc', value=0.636)
  >>>DC_current(Im=0)
  Result(name='Idc', value=0.0)
  """
  return Result("Idc ", Im*0.318)

def DC_voltage(Vm: float) ->tuple:
  """
  This function can calculate the Average DC Voltage(Vdc) in a circuit.
  In all cases negative sign shows the opposite direction of current or voltage.
  Vdc = average dc current
  Vm = maximum volatge or peak voltage
  cases:
  >>>DC_volatge(Vm=2)
  Result(name='Vdc', value=0.636)
  >>>DC_voltage(Vm=0)
  Result(name='Vdc', value=0.0)
  """
  return Result("Vdc ", 0.318*Vm)

def max_current(Vm: float, Rl: float) ->tuple:
  """
  This function can calculate the maximum current(Im) in a circuit.
  In all cases negative sign shows the opposite direction of current or voltage.
  Vm = maximum voltage or peak voltage
  Rl = load resistance
  cases:
  >>>max_current(Vm=2, Rl=5)
  Result(name='Max_current_Im', value=0.4)
  >>>max_current(Vm=2, Rl=-5)
  Traceback (most recent call last):
      ...
  ValueError: Resistance cannot be negative and equal to zero
  
  """
  if Rl<=0:
    raise ValueError("Resistance cannot be negative and equal to zero")
  else:
    return Result("Max_current_Im ", Vm/Rl)
          
def rms_current(Irms: float, Im: float) ->tuple:
  """
  This function calculate the RMS(Root Mean Square) value of current(Irms).
  In all cases negative sign shows the opposite direction of current or voltage.
  Irms = Root Mean Square Value of current
  Im = maximum current or peak current
  cases:
  >>>rms_current(Im=10)
  Result(name='Irms', value=5.0)
  >>>rms_current(Im=0)
  Result(name='Irms', value=0.0)
  """
  return Result("Irms ", Im/2)

def rms_volatge(Vrms: float, Vm: float) ->tuple:
  """
  This function calculate the RMS(Root Mean Square) value of voltage(Vrms).
  In all cases negative sign shows the opposite direction of current or voltage.
  Vrms = Root Mean Square Value of voltage
  Vm = maximum voltage or peak voltage
  cases:
  >>>rms_voltage(Vm=20)
  Result(name='Vrms', value=10.0)
  >>>rms_voltage(Vm=0)
  Result(name='Vrms', value=0.0)
  """
  return Result("Vrms ", Vm/2)

if __name__ == "__main__":
  import doctest

  doctest.testmod()
