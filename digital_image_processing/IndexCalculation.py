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
            This algorithm consists in calculating vegetation indices, these indices can be used for precision agriculture for example (or remote sensing). There are functions to define the data and to calculate the implemented indices.

        # Vegetation index
            https://en.wikipedia.org/wiki/Vegetation_Index
            A Vegetation Index (VI) is a spectral transformation of two or more bands designed to enhance the contribution of vegetation properties and allow reliable spatial and temporal inter-comparisons of terrestrial photosynthetic activity and canopy structural variations
        
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
            #allIndex = ["ARVI2", "CCCI", "CVI", "GLI", "NDVI", "BNDVI", "redEdgeNDVI", "GNDVI", "GBNDVI", "GRNDVI", "RBNDVI", "PNDVI", "ATSAVI", "BWDRVI", "CIgreen", "CIrededge", "CI", "CTVI", "GDVI", "EVI", "GEMI", "GOSAVI", "GSAVI", "Hue", "IVI", "IPVI", "I", "RVI", "MRVI", "MSAVI", "NormG", "NormNIR", "NormR", "NGRDI", "RI", "S", "IF", "DVI", "TVI", "NDRE"]
        #list of index with not blue channel
            #notBlueIndex = ["ARVI2", "CCCI", "CVI", "NDVI", "redEdgeNDVI", "GNDVI", "GRNDVI", "ATSAVI", "CIgreen", "CIrededge", "CTVI", "GDVI", "GEMI", "GOSAVI", "GSAVI", "IVI", "IPVI", "RVI", "MRVI", "MSAVI", "NormG", "NormNIR", "NormR", "NGRDI", "RI", "DVI", "TVI", "NDRE"]
        #list of index just with RGB channels
            #RGBIndex = ["GLI", "CI", "Hue", "I", "NGRDI", "RI", "S", "IF"]
    """

    def __init__(self, red=None, green=None, blue=None, redEdge=None, nir=None):
        print("Numpy version: " + np.__version__)
        self.red = red
        self.green = green
        self.blue = blue
        self.redEdge = redEdge
        self.nir = nir

    def setMatrices(self, red=None, green=None, blue=None, redEdge=None, nir=None):
        self.red = red
        self.green = green
        self.blue = blue
        self.redEdge = redEdge
        self.nir = nir
        return True

    def calculation(self, index=""):
        """
            performs the calculation of the index with the values instantiated in the class
            :str index: sigla do indice a ser calculado
        """
        if index == "":
            print("Not determined index!")
        elif index == "ARVI2":
            return self.ARVI2(red=self.red, nir=self.nir)
        elif index == "CCCI":
            return self.CCCI(red=self.red, redEdge=self.redEdge, nir=self.nir)
        elif index == "CVI":
            return self.CVI(red=self.red, green=self.green, nir=self.nir)
        elif index == "GLI":
            return self.GLI(red=self.red, green=self.green, blue=self.blue)
        elif index == "NDVI":
            return self.NDVI(red=self.red, nir=self.nir)
        elif index == "BNDVI":
            return self.BNDVI(blue=self.blue, nir=self.nir)
        elif index == "redEdgeNDVI":
            return self.redEdgeNDVI(red=self.red, redEdge=self.redEdge)
        elif index == "GNDVI":
            return self.GNDVI(green=self.green, nir=self.nir)
        elif index == "GBNDVI":
            return self.GBNDVI(green=self.green, blue=self.blue, nir=self.nir)
        elif index == "GRNDVI":
            return self.GRNDVI(red=self.red, green=self.green, nir=self.nir)
        elif index == "RBNDVI":
            return self.RBNDVI(red=self.red, blue=self.blue, nir=self.nir)
        elif index == "PNDVI":
            return self.PNDVI(
                red=self.red, green=self.green, blue=self.blue, nir=self.nir
            )
        elif index == "ATSAVI":
            return self.ATSAVI(red=self.red, nir=self.nir, X=0.08, a=1.22, b=0.03)
        elif index == "BWDRVI":
            return self.BWDRVI(blue=self.blue, nir=self.nir)
        elif index == "CIgreen":
            return self.CIgreen(green=self.green, nir=self.nir)
        elif index == "CIrededge":
            return self.CIrededge(redEdge=self.redEdge, nir=self.nir)
        elif index == "CI":
            return self.CI(red=self.red, blue=self.blue)
        elif index == "CTVI":
            return self.CTVI(red=self.red, nir=self.nir)
        elif index == "GDVI":
            return self.GDVI(green=self.green, nir=self.nir)
        elif index == "EVI":
            return self.EVI(red=self.red, blue=self.blue, nir=self.nir)
        elif index == "GEMI":
            return self.GEMI(red=self.red, nir=self.nir)
        elif index == "GOSAVI":
            return self.GOSAVI(green=self.green, nir=self.nir, Y=0.16)
        elif index == "GSAVI":
            return self.GSAVI(green=self.green, nir=self.nir, L=0.5)
        elif index == "Hue":
            return self.Hue(red=self.red, green=self.green, blue=self.blue)
        elif index == "IVI":
            return self.IVI(red=self.red, nir=self.nir, a=1, b=1)
        elif index == "IPVI":
            return self.IPVI(red=self.red, nir=self.nir)
        elif index == "I":
            return self.I(red=self.red, green=self.green, blue=self.blue)
        elif index == "RVI":
            return self.RVI(red=self.red, nir=self.nir)
        elif index == "MRVI":
            return self.MRVI(red=self.red, nir=self.nir)
        elif index == "MSAVI":
            return self.MSAVI(red=self.red, nir=self.nir)
        elif index == "NormG":
            return self.NormG(red=self.red, green=self.green, nir=self.nir)
        elif index == "NormNIR":
            return self.NormNIR(red=self.red, green=self.green, nir=self.nir)
        elif index == "NormR":
            return self.NormR(red=self.red, green=self.green, nir=self.nir)
        elif index == "NGRDI":
            return self.NGRDI(red=self.red, green=self.green)
        elif index == "RI":
            return self.RI(red=self.red, green=self.green)
        elif index == "S":
            return self.S(red=self.red, green=self.green, blue=self.blue)
        elif index == "IF":
            return self.IF(red=self.red, green=self.green, blue=self.blue)
        elif index == "DVI":
            return self.DVI(red=self.red, nir=self.nir)
        elif index == "TVI":
            return self.TVI(red=self.red, nir=self.nir)
        elif index == "NDRE":
            return self.NDRE(redEdge=self.redEdge, nir=self.nir)
        else:
            print("Index not list!")

        return False

    def directCalculation(
        self, index="", red=None, green=None, blue=None, redEdge=None, nir=None
    ):
        """
            performs the calculation of the index with the values passed by parameter
            39 indices cadastrados
            :str index: sigla do indice a ser calculado
        """
        if index == "":
            print("Not determined index!")
        elif index == "ARVI2":
            return self.ARVI2(red=red, nir=nir)
        elif index == "CCCI":
            return self.CCCI(red=red, redEdge=redEdge, nir=nir)
        elif index == "CVI":
            return self.CVI(red=red, green=green, nir=nir)
        elif index == "GLI":
            return self.GLI(red=red, green=green, blue=blue)
        elif index == "NDVI":
            return self.NDVI(red=red, nir=nir)
        elif index == "BNDVI":
            return self.BNDVI(blue=blue, nir=nir)
        elif index == "redEdgeNDVI":
            return self.redEdgeNDVI(red=red, redEdge=redEdge)
        elif index == "GNDVI":
            return self.GNDVI(green=green, nir=nir)
        elif index == "GBNDVI":
            return self.GBNDVI(green=green, blue=blue, nir=nir)
        elif index == "GRNDVI":
            return self.GRNDVI(red=red, green=green, nir=nir)
        elif index == "RBNDVI":
            return self.RBNDVI(red=red, blue=blue, nir=nir)
        elif index == "PNDVI":
            return self.PNDVI(red=red, green=green, blue=blue, nir=nir)
        elif index == "ATSAVI":
            return self.ATSAVI(red=red, nir=nir, X=0.08, a=1.22, b=0.03)
        elif index == "BWDRVI":
            return self.BWDRVI(blue=blue, nir=nir)
        elif index == "CIgreen":
            return self.CIgreen(green=green, nir=nir)
        elif index == "CIrededge":
            return self.CIrededge(redEdge=redEdge, nir=nir)
        elif index == "CI":
            return self.CI(red=red, blue=blue)
        elif index == "CTVI":
            return self.CTVI(red=red, nir=nir)
        elif index == "GDVI":
            return self.GDVI(green=green, nir=nir)
        elif index == "EVI":
            return self.EVI(red=red, blue=blue, nir=nir)
        elif index == "GEMI":
            return self.GEMI(red=red, nir=nir)
        elif index == "GOSAVI":
            return self.GOSAVI(green=green, nir=nir, Y=0.16)
        elif index == "GSAVI":
            return self.GSAVI(green=green, nir=nir, L=0.5)
        elif index == "Hue":
            return self.Hue(red=red, green=green, blue=blue)
        elif index == "IVI":
            return self.IVI(red=red, nir=nir, a=1, b=1)
        elif index == "IPVI":
            return self.IPVI(red=red, nir=nir)
        elif index == "I":
            return self.I(red=red, green=green, blue=blue)
        elif index == "RVI":
            return self.RVI(red=red, nir=nir)
        elif index == "MRVI":
            return self.MRVI(red=red, nir=nir)
        elif index == "MSAVI":
            return self.MSAVI(red=red, nir=nir)
        elif index == "NormG":
            return self.NormG(red=red, green=green, nir=nir)
        elif index == "NormNIR":
            return self.NormNIR(red=red, green=green, nir=nir)
        elif index == "NormR":
            return self.NormR(red=red, green=green, nir=nir)
        elif index == "NGRDI":
            return self.NGRDI(red=red, green=green)
        elif index == "RI":
            return self.RI(red=red, green=green)
        elif index == "S":
            return self.S(red=red, green=green, blue=blue)
        elif index == "IF":
            return self.IF(red=red, green=green, blue=blue)
        elif index == "DVI":
            return self.DVI(red=red, nir=nir)
        elif index == "TVI":
            return self.TVI(red=red, nir=nir)
        elif index == "NDRE":
            return self.NDRE(redEdge=redEdge, nir=nir)
        else:
            print("Index not list!")

        return False

    def ARVI2(self, red=None, nir=None):
        """
            Atmospherically Resistant Vegetation Index 2
            https://www.indexdatabase.de/db/i-single.php?id=396
            :return: index
             	−0.18+1.17*(NIR−RED)/(NIR+RED)
        """
        return -0.18 + (1.17 * ((nir - red) / (nir + red)))

    def CCCI(self, red=None, redEdge=None, nir=None):
        """
            Canopy Chlorophyll Content Index
            https://www.indexdatabase.de/db/i-single.php?id=224
            :return: index
        """
        return ((nir - redEdge) / (nir + redEdge)) / ((nir - red) / (nir + red))

    def CVI(self, red=None, green=None, nir=None):
        """
            Chlorophyll vegetation index
            https://www.indexdatabase.de/db/i-single.php?id=391
            :return: index
        """
        return nir * (red / (green ** 2))

    def GLI(self, red=None, green=None, blue=None):
        """
            Green leaf index
            https://www.indexdatabase.de/db/i-single.php?id=375
            :return: index
        """
        return (2 * green - red - blue) / (2 * green + red + blue)

    def NDVI(self, red=None, nir=None):
        """
            Normalized Difference NIR/Red Normalized Difference Vegetation Index, Calibrated NDVI - CDVI
            https://www.indexdatabase.de/db/i-single.php?id=58
            :return: index
        """
        return (nir - red) / (nir + red)

    def BNDVI(self, blue=None, nir=None):
        """
            Normalized Difference NIR/Blue Blue-normalized difference vegetation index
            https://www.indexdatabase.de/db/i-single.php?id=135
            :return: index
        """
        return (nir - blue) / (nir + blue)

    def redEdgeNDVI(self, red=None, redEdge=None):
        """
            Normalized Difference Rededge/Red
            https://www.indexdatabase.de/db/i-single.php?id=235
            :return: index
        """
        return (redEdge - red) / (redEdge + red)

    def GNDVI(self, green=None, nir=None):
        """
            Normalized Difference NIR/Green Green NDVI
            https://www.indexdatabase.de/db/i-single.php?id=401
            :return: index
        """
        return (nir - green) / (nir + green)

    def GBNDVI(self, green=None, blue=None, nir=None):
        """
            Green-Blue NDVI
            https://www.indexdatabase.de/db/i-single.php?id=186
            :return: index
        """
        return (nir - (green + blue)) / (nir + (green + blue))

    def GRNDVI(self, red=None, green=None, nir=None):
        """
            Green-Red NDVI
            https://www.indexdatabase.de/db/i-single.php?id=185
            :return: index
        """
        return (nir - (green + red)) / (nir + (green + red))

    def RBNDVI(self, red=None, blue=None, nir=None):
        """
            Red-Blue NDVI
            https://www.indexdatabase.de/db/i-single.php?id=187
            :return: index
        """
        return (nir - (blue + red)) / (nir + (blue + red))

    def PNDVI(self, red=None, green=None, blue=None, nir=None):
        """
            Pan NDVI
            https://www.indexdatabase.de/db/i-single.php?id=188
            :return: index
        """
        return (nir - (green + red + blue)) / (nir + (green + red + blue))

    def ATSAVI(self, red=None, nir=None, X=0.08, a=1.22, b=0.03):
        """
            Adjusted transformed soil-adjusted VI
            https://www.indexdatabase.de/db/i-single.php?id=209
            :return: index
        """
        return a * ((nir - a * red - b) / (a * nir + red - a * b + X * (1 + a ** 2)))

    def BWDRVI(self, blue=None, nir=None):
        """
            Blue-wide dynamic range vegetation index
            https://www.indexdatabase.de/db/i-single.php?id=136
            :return: index
        """
        return (0.1 * nir - blue) / (0.1 * nir + blue)

    def CIgreen(self, green=None, nir=None):
        """
            Chlorophyll Index Green
            https://www.indexdatabase.de/db/i-single.php?id=128
            :return: index
        """
        return (nir / green) - 1

    def CIrededge(self, redEdge=None, nir=None):
        """
            Chlorophyll Index RedEdge
            https://www.indexdatabase.de/db/i-single.php?id=131
            :return: index
        """
        return (nir / redEdge) - 1

    def CI(self, red=None, blue=None):
        """
            Coloration Index
            https://www.indexdatabase.de/db/i-single.php?id=11
            :return: index
        """
        return (red - blue) / red

    def CTVI(self, red=None, nir=None):
        """
            Corrected Transformed Vegetation Index
            https://www.indexdatabase.de/db/i-single.php?id=244
            :return: index
        """
        ndvi = self.NDVI(red=red, nir=nir)
        return ((ndvi + 0.5) / (abs(ndvi + 0.5))) * (abs(ndvi + 0.5) ** (1 / 2))

    def GDVI(self, green=None, nir=None):
        """
            Difference NIR/Green Green Difference Vegetation Index
            https://www.indexdatabase.de/db/i-single.php?id=27
            :return: index
        """
        return nir - green

    def EVI(self, red=None, blue=None, nir=None):
        """
            Enhanced Vegetation Index
            https://www.indexdatabase.de/db/i-single.php?id=16
            :return: index
        """
        return 2.5 * ((nir - red) / (nir + 6 * red - 7.5 * blue + 1))

    def GEMI(self, red=None, nir=None):
        """
            Global Environment Monitoring Index
            https://www.indexdatabase.de/db/i-single.php?id=25
            :return: index
        """
        n = (2 * (nir ** 2 - red ** 2) + 1.5 * nir + 0.5 * red) / (nir + red + 0.5)
        return n * (1 - 0.25 * n) - (red - 0.125) / (1 - red)

    def GOSAVI(self, green=None, nir=None, Y=0.16):
        """
            Green Optimized Soil Adjusted Vegetation Index
            https://www.indexdatabase.de/db/i-single.php?id=29
            mit Y = 0,16
            :return: index
        """
        return (nir - green) / (nir + green + Y)

    def GSAVI(self, green=None, nir=None, L=0.5):
        """
            Green Soil Adjusted Vegetation Index
            https://www.indexdatabase.de/db/i-single.php?id=31
            mit L = 0,5
            :return: index
        """
        return ((nir - green) / (nir + green + L)) * (1 + L)

    def Hue(self, red=None, green=None, blue=None):
        """
            Hue
            https://www.indexdatabase.de/db/i-single.php?id=34
            :return: index
        """
        return np.arctan((((2 * red - green - blue) / 30.5) * (green - blue)))

    def IVI(self, red=None, nir=None, a=None, b=None):
        """
            Ideal vegetation index
            https://www.indexdatabase.de/db/i-single.php?id=276
            b=intercept of vegetation line
            a=soil line slope
            :return: index
        """
        return (nir - b) / (a * red)

    def IPVI(self, red=None, nir=None):
        """
            Infrared percentage vegetation index
            https://www.indexdatabase.de/db/i-single.php?id=35
            :return: index
        """
        return (nir / ((nir + red) / 2)) * (self.NDVI(red=red, nir=nir) + 1)

    def I(self, red=None, green=None, blue=None):
        """
            Intensity
            https://www.indexdatabase.de/db/i-single.php?id=36
            :return: index
        """
        return (red + green + blue) / 30.5

    def RVI(self, red=None, nir=None):
        """
            Ratio-Vegetation-Index
            http://www.seos-project.eu/modules/remotesensing/remotesensing-c03-s01-p01.html
            :return: index
        """
        return nir / red

    def MRVI(self, red=None, nir=None):
        """
            Modified Normalized Difference Vegetation Index RVI
            https://www.indexdatabase.de/db/i-single.php?id=275
            :return: index
        """
        return (self.RVI(red=red, nir=nir) - 1) / (self.RVI(red=red, nir=nir) + 1)

    def MSAVI(self, red=None, nir=None):
        """
            Modified Soil Adjusted Vegetation Index
            https://www.indexdatabase.de/db/i-single.php?id=44
            :return: index
        """
        return ((2 * nir + 1) - ((2 * nir + 1) ** 2 - 8 * (nir - red)) ** (1 / 2)) / 2

    def NormG(self, red=None, green=None, nir=None):
        """
            Norm G
            https://www.indexdatabase.de/db/i-single.php?id=50
            :return: index
        """
        return green / (nir + red + green)

    def NormNIR(self, red=None, green=None, nir=None):
        """
            Norm NIR
            https://www.indexdatabase.de/db/i-single.php?id=51
            :return: index
        """
        return nir / (nir + red + green)

    def NormR(self, red=None, green=None, nir=None):
        """
            Norm R
            https://www.indexdatabase.de/db/i-single.php?id=52
            :return: index
        """
        return red / (nir + red + green)

    def NGRDI(self, red=None, green=None):
        """
            Normalized Difference Green/Red Normalized green red difference index, Visible Atmospherically Resistant Indices Green (VIgreen)
            https://www.indexdatabase.de/db/i-single.php?id=390
            :return: index
        """
        return (green - red) / (green + red)

    def RI(self, red=None, green=None):
        """
            Normalized Difference Red/Green Redness Index
            https://www.indexdatabase.de/db/i-single.php?id=74
            :return: index
        """
        return (red - green) / (red + green)

    def S(self, red=None, green=None, blue=None):
        """
            Saturation
            https://www.indexdatabase.de/db/i-single.php?id=77
            :return: index
        """
        max = np.max([np.max(red), np.max(green), np.max(blue)])
        min = np.min([np.min(red), np.min(green), np.min(blue)])
        return (max - min) / max

    def IF(self, red=None, green=None, blue=None):
        """
            Shape Index
            https://www.indexdatabase.de/db/i-single.php?id=79
            :return: index
        """
        return (2 * red - green - blue) / (green - blue)

    def DVI(self, red=None, nir=None):
        """
            Simple Ratio NIR/RED Difference Vegetation Index, Vegetation Index Number (VIN)
            https://www.indexdatabase.de/db/i-single.php?id=12
            :return: index
        """
        return nir / red

    def TVI(self, red=None, nir=None):
        """
            Transformed Vegetation Index
            https://www.indexdatabase.de/db/i-single.php?id=98
            :return: index
        """
        return (self.NDVI(red=red, nir=nir) + 0.5) ** (1 / 2)

    def NDRE(self, redEdge=None, nir=None):
        return (nir - redEdge) / (nir + redEdge)


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

# how set the values after instantiate the class cl, (for update the data or when dont instantiating the class with the values)
cl.setMatrices(red=red, green=green, blue=blue, redEdge=redEdge, nir=nir)

# calculating the indices for the instantiated values in the class
indexValue    = cl.calculation("CCCI").astype(np.float64)

# calculating the index with the values directly 
#indexValue    = cl.directCalculation("CCCI",red=red, green=green, blue=blue, redEdge=redEdge, nir=nir).astype(np.float64)


print(np.array2string(indexValue, precision=20, separator=', ', floatmode='maxprec_equal'))
# A list of examples results for different type of data at 'calculation' or 'directCalculation' 
# float16 ->    0.31567383              #NDVI (red = 50, nir = 100)
# float32 ->    0.31578946              #NDVI (red = 50, nir = 100)
# float64 ->    0.3157894736842105      #NDVI (red = 50, nir = 100)
# longdouble -> 0.3157894736842105      #NDVI (red = 50, nir = 100)
"""
