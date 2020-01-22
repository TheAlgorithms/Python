# Author: João Gustavo A. Amorim
# Author email: joaogustavoamorim@gmail.com
# Coding date:  jan 2019
# python/black: True

# Imports
import numpy as np

# Class implemented to calculus the index
class IndexCalculation:
    """
        # Class Summary
                This algorithm consists in calculating vegetation indices, these indices 
            can be used for precision agriculture for example (or remote sensing). There are
            functions to define the data and to calculate the implemented indices.

        # Vegetation index
            https://en.wikipedia.org/wiki/Vegetation_Index
            A Vegetation Index (VI) is a spectral transformation of two or more bands designed 
            to enhance the contribution of vegetation properties and allow reliable spatial and 
            temporal inter-comparisons of terrestrial photosynthetic activity and canopy 
            structural variations
        
        # Information about channels (Wavelength range for each)
            * nir - near-infrared
                https://www.malvernpanalytical.com/br/products/technology/near-infrared-spectroscopy
                Wavelength Range 700 nm to 2500 nm
            * Red Edge 
                https://en.wikipedia.org/wiki/Red_edge
                Wavelength Range 680 nm to 730 nm
            * red
                https://en.wikipedia.org/wiki/Color
                Wavelength Range 635 nm to 700 nm
            * blue
                https://en.wikipedia.org/wiki/Color
                Wavelength Range 450 nm to 490 nm
            * green
                https://en.wikipedia.org/wiki/Color
                Wavelength Range 520 nm to 560 nm

                
        # Implemented index list
                #"abbreviationOfIndexName" -- list of channels used

                #"ARVI2"            --  red, nir
                #"CCCI"             --  red, redEdge, nir
                #"CVI"              --  red, green, nir
                #"GLI"              --  red, green, blue
                #"NDVI"             --  red, nir
                #"BNDVI"            --  blue, nir
                #"redEdgeNDVI"      --  red, redEdge
                #"GNDVI"            --  green, nir
                #"GBNDVI"           --  green, blue, nir
                #"GRNDVI"           --  red, green, nir
                #"RBNDVI"           --  red, blue, nir
                #"PNDVI"            --  red, green, blue, nir
                #"ATSAVI"           --  red, nir
                #"BWDRVI"           --  blue, nir
                #"CIgreen"          --  green, nir
                #"CIrededge"        --  redEdge, nir
                #"CI"               --  red, blue
                #"CTVI"             --  red, nir
                #"GDVI"             --  green, nir
                #"EVI"              --  red, blue, nir
                #"GEMI"             --  red, nir
                #"GOSAVI"           --  green, nir
                #"GSAVI"            --  green, nir
                #"Hue"              --  red, green, blue
                #"IVI"              --  red, nir
                #"IPVI"             --  red, nir
                #"I"                --  red, green, blue
                #"RVI"              --  red, nir
                #"MRVI"             --  red, nir
                #"MSAVI"            --  red, nir
                #"NormG"            --  red, green, nir
                #"NormNIR"          --  red, green, nir
                #"NormR"            --  red, green, nir
                #"NGRDI"            --  red, green
                #"RI"               --  red, green
                #"S"                --  red, green, blue
                #"IF"               --  red, green, blue
                #"DVI"              --  red, nir
                #"TVI"              --  red, nir
                #"NDRE"               --  redEdge, nir

        #list of all index implemented
            #allIndex = ["ARVI2", "CCCI", "CVI", "GLI", "NDVI", "BNDVI", "redEdgeNDVI", "GNDVI", 
                        "GBNDVI", "GRNDVI", "RBNDVI", "PNDVI", "ATSAVI", "BWDRVI", "CIgreen", 
                        "CIrededge", "CI", "CTVI", "GDVI", "EVI", "GEMI", "GOSAVI", "GSAVI", 
                        "Hue", "IVI", "IPVI", "I", "RVI", "MRVI", "MSAVI", "NormG", "NormNIR", 
                        "NormR", "NGRDI", "RI", "S", "IF", "DVI", "TVI", "NDRE"]

        #list of index with not blue channel
            #notBlueIndex = ["ARVI2", "CCCI", "CVI", "NDVI", "redEdgeNDVI", "GNDVI", "GRNDVI", 
                            "ATSAVI", "CIgreen", "CIrededge", "CTVI", "GDVI", "GEMI", "GOSAVI", 
                            "GSAVI", "IVI", "IPVI", "RVI", "MRVI", "MSAVI", "NormG", "NormNIR", 
                            "NormR", "NGRDI", "RI", "DVI", "TVI", "NDRE"]

        #list of index just with RGB channels
            #RGBIndex = ["GLI", "CI", "Hue", "I", "NGRDI", "RI", "S", "IF"]
    """

    def __init__(self, red=None, green=None, blue=None, redEdge=None, nir=None):
        # print("Numpy version: " + np.__version__)
        self.setMatrices(red=red, green=green, blue=blue, redEdge=redEdge, nir=nir)

    def setMatrices(self, red=None, green=None, blue=None, redEdge=None, nir=None):
        if red is not None:
            self.red = red
        if green is not None:
            self.green = green
        if blue is not None:
            self.blue = blue
        if redEdge is not None:
            self.redEdge = redEdge
        if nir is not None:
            self.nir = nir
        return True

    def calculation(
        self, index="", red=None, green=None, blue=None, redEdge=None, nir=None
    ):
        """
            performs the calculation of the index with the values instantiated in the class
            :str index: abbreviation of index name to perform
        """
        self.setMatrices(red=red, green=green, blue=blue, redEdge=redEdge, nir=nir)
        funcs = {
            "ARVI2": self.ARVI2,
            "CCCI": self.CCCI,
            "CVI": self.CVI,
            "GLI": self.GLI,
            "NDVI": self.NDVI,
            "BNDVI": self.BNDVI,
            "redEdgeNDVI": self.redEdgeNDVI,
            "GNDVI": self.GNDVI,
            "GBNDVI": self.GBNDVI,
            "GRNDVI": self.GRNDVI,
            "RBNDVI": self.RBNDVI,
            "PNDVI": self.PNDVI,
            "ATSAVI": self.ATSAVI,
            "BWDRVI": self.BWDRVI,
            "CIgreen": self.CIgreen,
            "CIrededge": self.CIrededge,
            "CI": self.CI,
            "CTVI": self.CTVI,
            "GDVI": self.GDVI,
            "EVI": self.EVI,
            "GEMI": self.GEMI,
            "GOSAVI": self.GOSAVI,
            "GSAVI": self.GSAVI,
            "Hue": self.Hue,
            "IVI": self.IVI,
            "IPVI": self.IPVI,
            "I": self.I,
            "RVI": self.RVI,
            "MRVI": self.MRVI,
            "MSAVI": self.MSAVI,
            "NormG": self.NormG,
            "NormNIR": self.NormNIR,
            "NormR": self.NormR,
            "NGRDI": self.NGRDI,
            "RI": self.RI,
            "S": self.S,
            "IF": self.IF,
            "DVI": self.DVI,
            "TVI": self.TVI,
            "NDRE": self.NDRE,
        }

        try:
            return funcs[index]()
        except KeyError:
            print("Index not in the list!")
            return False

    def ARVI2(self):
        """
        Atmospherically Resistant Vegetation Index 2
        https://www.indexdatabase.de/db/i-single.php?id=396
        :return: index
            −0.18+1.17*(self.nir−self.red)/(self.nir+self.red)
        """
        return -0.18 + (1.17 * ((self.nir - self.red) / (self.nir + self.red)))

    def CCCI(self):
        """
            Canopy Chlorophyll Content Index
            https://www.indexdatabase.de/db/i-single.php?id=224
            :return: index
        """
        return ((self.nir - self.redEdge) / (self.nir + self.redEdge)) / (
            (self.nir - self.red) / (self.nir + self.red)
        )

    def CVI(self):
        """
            Chlorophyll vegetation index
            https://www.indexdatabase.de/db/i-single.php?id=391
            :return: index
        """
        return self.nir * (self.red / (self.green ** 2))

    def GLI(self):
        """
            self.green leaf index
            https://www.indexdatabase.de/db/i-single.php?id=375
            :return: index
        """
        return (2 * self.green - self.red - self.blue) / (
            2 * self.green + self.red + self.blue
        )

    def NDVI(self):
        """
                Normalized Difference self.nir/self.red Normalized Difference Vegetation Index, 
            Calibrated NDVI - CDVI
            https://www.indexdatabase.de/db/i-single.php?id=58
            :return: index
        """
        return (self.nir - self.red) / (self.nir + self.red)

    def BNDVI(self):
        """
                Normalized Difference self.nir/self.blue self.blue-normalized difference 
            vegetation index
            https://www.indexdatabase.de/db/i-single.php?id=135
            :return: index
        """
        return (self.nir - self.blue) / (self.nir + self.blue)

    def redEdgeNDVI(self):
        """
            Normalized Difference self.rededge/self.red
            https://www.indexdatabase.de/db/i-single.php?id=235
            :return: index
        """
        return (self.redEdge - self.red) / (self.redEdge + self.red)

    def GNDVI(self):
        """
            Normalized Difference self.nir/self.green self.green NDVI
            https://www.indexdatabase.de/db/i-single.php?id=401
            :return: index
        """
        return (self.nir - self.green) / (self.nir + self.green)

    def GBNDVI(self):
        """
            self.green-self.blue NDVI
            https://www.indexdatabase.de/db/i-single.php?id=186
            :return: index
        """
        return (self.nir - (self.green + self.blue)) / (
            self.nir + (self.green + self.blue)
        )

    def GRNDVI(self):
        """
            self.green-self.red NDVI
            https://www.indexdatabase.de/db/i-single.php?id=185
            :return: index
        """
        return (self.nir - (self.green + self.red)) / (
            self.nir + (self.green + self.red)
        )

    def RBNDVI(self):
        """
            self.red-self.blue NDVI
            https://www.indexdatabase.de/db/i-single.php?id=187
            :return: index
        """
        return (self.nir - (self.blue + self.red)) / (self.nir + (self.blue + self.red))

    def PNDVI(self):
        """
            Pan NDVI
            https://www.indexdatabase.de/db/i-single.php?id=188
            :return: index
        """
        return (self.nir - (self.green + self.red + self.blue)) / (
            self.nir + (self.green + self.red + self.blue)
        )

    def ATSAVI(self, X=0.08, a=1.22, b=0.03):
        """
            Adjusted transformed soil-adjusted VI
            https://www.indexdatabase.de/db/i-single.php?id=209
            :return: index
        """
        return a * (
            (self.nir - a * self.red - b)
            / (a * self.nir + self.red - a * b + X * (1 + a ** 2))
        )

    def BWDRVI(self):
        """
            self.blue-wide dynamic range vegetation index
            https://www.indexdatabase.de/db/i-single.php?id=136
            :return: index
        """
        return (0.1 * self.nir - self.blue) / (0.1 * self.nir + self.blue)

    def CIgreen(self):
        """
            Chlorophyll Index self.green
            https://www.indexdatabase.de/db/i-single.php?id=128
            :return: index
        """
        return (self.nir / self.green) - 1

    def CIrededge(self):
        """
            Chlorophyll Index self.redEdge
            https://www.indexdatabase.de/db/i-single.php?id=131
            :return: index
        """
        return (self.nir / self.redEdge) - 1

    def CI(self):
        """
            Coloration Index
            https://www.indexdatabase.de/db/i-single.php?id=11
            :return: index
        """
        return (self.red - self.blue) / self.red

    def CTVI(self):
        """
            Corrected Transformed Vegetation Index
            https://www.indexdatabase.de/db/i-single.php?id=244
            :return: index
        """
        ndvi = self.NDVI()
        return ((ndvi + 0.5) / (abs(ndvi + 0.5))) * (abs(ndvi + 0.5) ** (1 / 2))

    def GDVI(self):
        """
            Difference self.nir/self.green self.green Difference Vegetation Index
            https://www.indexdatabase.de/db/i-single.php?id=27
            :return: index
        """
        return self.nir - self.green

    def EVI(self):
        """
            Enhanced Vegetation Index
            https://www.indexdatabase.de/db/i-single.php?id=16
            :return: index
        """
        return 2.5 * (
            (self.nir - self.red) / (self.nir + 6 * self.red - 7.5 * self.blue + 1)
        )

    def GEMI(self):
        """
            Global Environment Monitoring Index
            https://www.indexdatabase.de/db/i-single.php?id=25
            :return: index
        """
        n = (2 * (self.nir ** 2 - self.red ** 2) + 1.5 * self.nir + 0.5 * self.red) / (
            self.nir + self.red + 0.5
        )
        return n * (1 - 0.25 * n) - (self.red - 0.125) / (1 - self.red)

    def GOSAVI(self, Y=0.16):
        """
            self.green Optimized Soil Adjusted Vegetation Index
            https://www.indexdatabase.de/db/i-single.php?id=29
            mit Y = 0,16
            :return: index
        """
        return (self.nir - self.green) / (self.nir + self.green + Y)

    def GSAVI(self, L=0.5):
        """
            self.green Soil Adjusted Vegetation Index
            https://www.indexdatabase.de/db/i-single.php?id=31
            mit L = 0,5
            :return: index
        """
        return ((self.nir - self.green) / (self.nir + self.green + L)) * (1 + L)

    def Hue(self):
        """
            Hue
            https://www.indexdatabase.de/db/i-single.php?id=34
            :return: index
        """
        return np.arctan(
            (
                ((2 * self.red - self.green - self.blue) / 30.5)
                * (self.green - self.blue)
            )
        )

    def IVI(self, a=None, b=None):
        """
            Ideal vegetation index
            https://www.indexdatabase.de/db/i-single.php?id=276
            b=intercept of vegetation line
            a=soil line slope
            :return: index
        """
        return (self.nir - b) / (a * self.red)

    def IPVI(self):
        """
            Infraself.red percentage vegetation index
            https://www.indexdatabase.de/db/i-single.php?id=35
            :return: index
        """
        return (self.nir / ((self.nir + self.red) / 2)) * (self.NDVI() + 1)

    def I(self):
        """
            Intensity
            https://www.indexdatabase.de/db/i-single.php?id=36
            :return: index
        """
        return (self.red + self.green + self.blue) / 30.5

    def RVI(self):
        """
            Ratio-Vegetation-Index
            http://www.seos-project.eu/modules/remotesensing/remotesensing-c03-s01-p01.html
            :return: index
        """
        return self.nir / self.red

    def MRVI(self):
        """
            Modified Normalized Difference Vegetation Index RVI
            https://www.indexdatabase.de/db/i-single.php?id=275
            :return: index
        """
        return (self.RVI() - 1) / (self.RVI() + 1)

    def MSAVI(self):
        """
            Modified Soil Adjusted Vegetation Index
            https://www.indexdatabase.de/db/i-single.php?id=44
            :return: index
        """
        return (
            (2 * self.nir + 1)
            - ((2 * self.nir + 1) ** 2 - 8 * (self.nir - self.red)) ** (1 / 2)
        ) / 2

    def NormG(self):
        """
            Norm G
            https://www.indexdatabase.de/db/i-single.php?id=50
            :return: index
        """
        return self.green / (self.nir + self.red + self.green)

    def NormNIR(self):
        """
            Norm self.nir
            https://www.indexdatabase.de/db/i-single.php?id=51
            :return: index
        """
        return self.nir / (self.nir + self.red + self.green)

    def NormR(self):
        """
            Norm R
            https://www.indexdatabase.de/db/i-single.php?id=52
            :return: index
        """
        return self.red / (self.nir + self.red + self.green)

    def NGRDI(self):
        """
                Normalized Difference self.green/self.red Normalized self.green self.red 
            difference index, Visible Atmospherically Resistant Indices self.green (VIself.green)
            https://www.indexdatabase.de/db/i-single.php?id=390
            :return: index
        """
        return (self.green - self.red) / (self.green + self.red)

    def RI(self):
        """
            Normalized Difference self.red/self.green self.redness Index
            https://www.indexdatabase.de/db/i-single.php?id=74
            :return: index
        """
        return (self.red - self.green) / (self.red + self.green)

    def S(self):
        """
            Saturation
            https://www.indexdatabase.de/db/i-single.php?id=77
            :return: index
        """
        max = np.max([np.max(self.red), np.max(self.green), np.max(self.blue)])
        min = np.min([np.min(self.red), np.min(self.green), np.min(self.blue)])
        return (max - min) / max

    def IF(self):
        """
            Shape Index
            https://www.indexdatabase.de/db/i-single.php?id=79
            :return: index
        """
        return (2 * self.red - self.green - self.blue) / (self.green - self.blue)

    def DVI(self):
        """
                Simple Ratio self.nir/self.red Difference Vegetation Index, Vegetation Index 
            Number (VIN)
            https://www.indexdatabase.de/db/i-single.php?id=12
            :return: index
        """
        return self.nir / self.red

    def TVI(self):
        """
            Transformed Vegetation Index
            https://www.indexdatabase.de/db/i-single.php?id=98
            :return: index
        """
        return (self.NDVI() + 0.5) ** (1 / 2)

    def NDRE(self):
        return (self.nir - self.redEdge) / (self.nir + self.redEdge)


"""
# genering a random matrices to test this class
red     = np.ones((1000,1000, 1),dtype="float64") * 46787
green   = np.ones((1000,1000, 1),dtype="float64") * 23487
blue    = np.ones((1000,1000, 1),dtype="float64") * 14578
redEdge = np.ones((1000,1000, 1),dtype="float64") * 51045
nir     = np.ones((1000,1000, 1),dtype="float64") * 52200

# Examples of how to use the class

# instantiating the class 
cl = IndexCalculation()

# instantiating the class with the values
#cl = indexCalculation(red=red, green=green, blue=blue, redEdge=redEdge, nir=nir)

# how set the values after instantiate the class cl, (for update the data or when dont 
# instantiating the class with the values)
cl.setMatrices(red=red, green=green, blue=blue, redEdge=redEdge, nir=nir)

# calculating the indices for the instantiated values in the class
    # Note: the CCCI index can be changed to any index implemented in the class.
indexValue_form1    = cl.calculation("CCCI", red=red, green=green, blue=blue,
                                     redEdge=redEdge, nir=nir).astype(np.float64)
indexValue_form2    = cl.CCCI()

# calculating the index with the values directly -- you can set just the values preferred -- 
# note: the *calculation* fuction performs the function *setMatrices*
indexValue_form3    = cl.calculation("CCCI", red=red, green=green, blue=blue,
                                     redEdge=redEdge, nir=nir).astype(np.float64)

print("Form 1: "+np.array2string(indexValue_form1, precision=20, separator=', ', floatmode='maxprec_equal'))
print("Form 2: "+np.array2string(indexValue_form2, precision=20, separator=', ', floatmode='maxprec_equal'))
print("Form 3: "+np.array2string(indexValue_form3, precision=20, separator=', ', floatmode='maxprec_equal'))

# A list of examples results for different type of data at NDVI
# float16 ->    0.31567383              #NDVI (red = 50, nir = 100)
# float32 ->    0.31578946              #NDVI (red = 50, nir = 100)
# float64 ->    0.3157894736842105      #NDVI (red = 50, nir = 100)
# longdouble -> 0.3157894736842105      #NDVI (red = 50, nir = 100)
"""
