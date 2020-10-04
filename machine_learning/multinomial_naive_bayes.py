import math
import sys
import pickle 
from collections import Counter 

class MNB:
    def __init__(self, debug=False, smoothing=False, idf=False):

        '''
        Log Debug Print [True|False]
        '''
        self.debug = debug

        '''
        Laplace Smoothing [True|False]
        '''
        self.smoothing = smoothing

        '''
        VOCABULARY - inisiasi vocabulary |V| (daftar tag unik dari semua entitas)
        '''
        self.vocabulary = []

        '''
        PRIOR PROBABILITY: P(C) = docCount(C) / Ndoc
            docCount => jumlah dokumen entitas
            Ndoc => jumlah dokumen seluruh entitas
        '''
        self.docFrequencyCount = {} # docCount(entitas)
        self.totalNumberOfDocuments = 0 # docCount(all)

        '''
        ENTITAS - inisiasi daftar entitas
            "entitas" => nama entitas
            "tokens" => daftar token
            "countToken" => jumlah token
            "frekuensiTokens" => frekuensi token count(w,c)
        '''
        self.daftarEntitas = []

    # count(c) => itung jumlah keseluruhan kata di kelas c
    def countToken(self, namaEntitas):
        index = [i for i, de in enumerate(self.daftarEntitas) if de["entitas"]==namaEntitas]
        
        return self.daftarEntitas[index[0]]["countToken"] if len(index) > 0 else 0

    # semua frekuensi token per entitas
    def getAllFrekuensi(self, namaEntitas):
        index = [i for i, de in enumerate(self.daftarEntitas) if de["entitas"]==namaEntitas]
        
        return self.daftarEntitas[index[0]]["frekuensiTokens"] if len(index) > 0 else {}

    # count(w,c) => itung jumlah kata w di dalem kelas c
    def getFrekuensi(self, token, namaEntitas):
        if token in self.getAllFrekuensi(namaEntitas):
            frekuensi = self.getAllFrekuensi(namaEntitas)[token]
        else:
            frekuensi = 0
        
        return frekuensi

    def getOrCreateEntitasToken(self, teks, namaEntitas):
        if namaEntitas=="" or type(namaEntitas) is not str:
            print('Nama entitas tidak sesuai: `' + namaEntitas + '`. Harus String bro.')
            exit

        # simple singleton for each entitas
        if namaEntitas not in [e["entitas"] for e in self.daftarEntitas]:
            # init counter
            self.docFrequencyCount[namaEntitas] = 0

            # tambah entitas ke list
            self.daftarEntitas.append({
                "entitas" : namaEntitas, # entitas
                "tokens" : teks.split(), # list token
                "countToken" : len(teks.split()), # jumlah token
                "frekuensiTokens" : dict(Counter(teks.split())) # frekuensi token
            })
        
        else:
            index = [i for i, de in enumerate(self.daftarEntitas) if de["entitas"]==namaEntitas ][0]

            for tok in teks.split():
                self.daftarEntitas[index]["tokens"].append(tok)
            
            # itung jumlah dan frequensi token
            self.daftarEntitas[index]["countToken"] = len(self.daftarEntitas[index]["tokens"])
            self.daftarEntitas[index]["frekuensiTokens"] = dict(Counter(self.daftarEntitas[index]["tokens"]))
        
        return namaEntitas if namaEntitas in [e["entitas"] for e in self.daftarEntitas] else None

    # |v| [kamus/kata unik]
    def tambahKeVocab(self, kata):
        if kata not in self.vocabulary:
            self.vocabulary.append(kata)

        return ""

    # prior probability
    # P(c) = docCount(class)/nDocTraining
    def prior(self, entitas):
        
        if self.debug:
            print("P("+entitas+") = ",str(self.docFrequencyCount[entitas])+"/"+str(self.totalNumberOfDocuments)+" ("+str(self.docFrequencyCount[entitas]/self.totalNumberOfDocuments)+")", "[prior probability]")

        prior = self.docFrequencyCount[entitas]/self.totalNumberOfDocuments

        return prior

    # prior probability
    # P(w|c) = (count(w,c))/count(c)   
    def likelihood(self, word, entitas):
        # inisiasi
        tokenProbability = 0 # P(w|c) = 0
        v = len(self.vocabulary) # |V|

        # count(w,c) => itung jumlah kata w di dalem kelas c
        nTok = self.getFrekuensi(word, entitas)
        # count(c) => itung jumlah keseluruhan kata di kelas c
        nTokAll = self.countToken(entitas)

        # likelihood
        if self.smoothing:
            if self.debug:
                print("P("+str(word)+" | "+str(entitas)+") = (%d)+1/(%d+%d) = %d/%d (%f) [likelihood]" % ( nTok, nTokAll, v, nTok+1, nTokAll+v, (nTok+1)/(nTokAll+v) ))

            # laplace Add-1 Smoothing
            # => P(w|c) = ( count(w,c) + 1 ) / ( count(w,c) + |V| )
            tokenProbability = (nTok+1)/(nTokAll+v)

        else:
            # => P(w | c) = (count(w,c))/count(c) 
            if self.debug:
                print("P("+str(word)+" | "+str(entitas)+") = (%d)/(%d) = %d/%d (%f) [likelihood]" % ( nTok, nTokAll, nTok, nTokAll, (nTok)/(nTokAll) ))
            tokenProbability = (nTok)/(nTokAll)

        return tokenProbability

    '''
        TRAINING

        @input
            teks
            entitas
    '''
    def learn(self, teks, entitas):
        entitas = self.getOrCreateEntitasToken(teks, entitas)

        # tambah frekuensi nya 1 (Prior)
        self.docFrequencyCount[entitas] += 1 #per dokumen kelas/entitas
        self.totalNumberOfDocuments += 1 #buat semua dokumen

        for kata in teks.split(" "):
            # tambah kata ke vocab |V|
            self.tambahKeVocab(kata)

    def saveModel(self, filename):

        datas = {
            "vocabulary" : self.vocabulary,
            "docFrequencyCount" : self.docFrequencyCount,
            "totalNumberOfDocuments" : self.totalNumberOfDocuments,
            "daftarEntitas" : self.daftarEntitas
        }

        try:
            with open(filename + '.pkl', 'wb') as f:
                pickle.dump(datas, f, pickle.HIGHEST_PROTOCOL)

        except OSError as err:
            print("OS error: {0}".format(err))
        except ValueError:
            print("Could not convert data to an integer.")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

        return "Saved: "+filename+".pkl"

    def loadModel(self, filename):
        model = {
            "vocabulary" : self.vocabulary,
            "docFrequencyCount" : self.docFrequencyCount,
            "totalNumberOfDocuments" : self.totalNumberOfDocuments,
            "daftarEntitas" : self.daftarEntitas
        }

        with open(filename, 'rb') as f:
            model = pickle.load(f)

        self.vocabulary = model["vocabulary"]
        self.docFrequencyCount = model["docFrequencyCount"]
        self.totalNumberOfDocuments = model["totalNumberOfDocuments"]
        self.daftarEntitas = model["daftarEntitas"]

        return "Loaded"

    '''
        @input
            teks : kata/kalimat yang akan di klasifikasikan
        @output
            entitas : entitas diambil dari probabilitas paling tinggi
            probabilitas : nilai probabilitas entitas yang tinggi
            probabilitasEntitas : nilai probabilitas tiap entitas
    '''
    def categorize(self, teks):
        # split token by spasi (ieu keur entitas mh useless sih da per-token si teks nu di kategorikeun na)
        tokens = teks.split(" ")
        # inisiasi
        prior = 0
        maksProb = 0
        peluangEntitas = []

        for e in self.daftarEntitas:
            # prior probability
            prior = self.prior(e["entitas"])
            
            # inisiasi peluang posterior
            # sarua jeung => P(c|w) = P(c)
            hitungPeluangEntitas = prior

            # loop token/word nu di data test
            for token in tokens:

                # likelihood
                hitungPeluangEntitas *= self.likelihood(token, e["entitas"])

                # print("%f / %f = %f" % (math.log(tokenProbability), prior, math.log(tokenProbability)*prior) )

                # posterior probability
                # P(c|w) = ( P(w│c) * P(c) ) / ( P(w) )
                if self.debug:
                    v = len(self.vocabulary) # |V|
                    nTokAll = len(e["tokens"]) # count(c) itung jumlah keseluruhan kata di kelas c
                    nTok = e["tokens"].count(token) # count(w,c) itung jumlah kata w di dalem kelas c

                    if self.smoothing:
                        print("P(%s | %s) = P(%s|%s)*P(%s)/P(%s) = %d/%d * %d/%d = %d/%d (%f) [posterior probability]" % (str(e["entitas"]), str(token), str(token), str(e["entitas"]), str(e["entitas"]), str(token), nTok+1, nTokAll+v, self.docFrequencyCount[e["entitas"]], self.totalNumberOfDocuments, nTok+1*self.docFrequencyCount[e["entitas"]], (nTokAll+v)*self.totalNumberOfDocuments, (nTok+1*self.docFrequencyCount[e["entitas"]])/((nTokAll+v)*self.totalNumberOfDocuments)) )
                    else:
                        print("P(%s | %s) = P(%s|%s)*P(%s)/P(%s) = %d/%d * %d/%d = %d/%d (%f) [posterior probability]" % (str(e["entitas"]), str(token), str(token), str(e["entitas"]), str(e["entitas"]), str(token), nTok, nTokAll, self.docFrequencyCount[e["entitas"]], self.totalNumberOfDocuments, nTok*self.docFrequencyCount[e["entitas"]], (nTokAll)*self.totalNumberOfDocuments, (nTok*self.docFrequencyCount[e["entitas"]])/((nTokAll)*self.totalNumberOfDocuments)) )
            
            # masukin peluang
            peluangEntitas.append({
                "entitas" : e["entitas"],
                "probabilitas" : hitungPeluangEntitas
            })

        indexEntitas = 0
        # cari maksimal kemungkinan dari entitas
        for i, pe in enumerate(peluangEntitas):
            if pe["probabilitas"] > maksProb:
                maksProb = pe["probabilitas"]
                indexEntitas = i
        
        entitas = peluangEntitas[indexEntitas]["entitas"]

        return {
            "entitas" : entitas,
            "probabilitas" : peluangEntitas[indexEntitas]["probabilitas"],
            "probabilitasEntitas" : peluangEntitas
        }