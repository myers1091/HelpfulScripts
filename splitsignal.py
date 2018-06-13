#!/usr/bin/env python

import ROOT
from ROOT import TFile, TTree, TEventList

indir = "/scratch/jmyers10/dihiggs/WHad_studies_v2/Boosted_WHad_2/"
outdir = "/scratch/jmyers10/dihiggs/WHad_studies_v2/Boosted_WHad_2/"
signalsamples = [
        ("342053","SM","125"),
        ("343764","Xhh260","260"),
        ("343766","Xhh300","300"),
        ("343769","Xhh400","400","2231.82659689"),
        ("343771","Xhh500","500","10464.9159167"),
        ("343772","Xhh600","600","9054.77398903"),
        ("343773","Xhh700","700","11563.0511329"),
        ("343774","Xhh750","750","11107.6739305"),
        ("343775","Xhh800","800","7829.5318623"),
        ("343776","Xhh900","900","7720.01648464"),
        ("343777","Xhh1000","1000","5844.94817928"),
        ("343778","Xhh1100","1100","5434.35833551"),
        ("343779","Xhh1200","1200","6156.84857874"),
        ("343780","Xhh1300","1300","6623.01477691"),
        ("343781","Xhh1400","1400","6516.45023616"),
        ("343782","Xhh1500","1500","6398.26497685"),
        ("343783","Xhh1600","1600","7150.73206994"),
        ("343784","Xhh1800","1800","6910.06879412"),
        ("343785","Xhh2000","2000","8029.06466319"),
        ("343786","Xhh2250","2250","8271.77568202"),
        ("343787","Xhh2500","2500","7560.55086198"),
        ("343788","Xhh2750","2750","8122.2700812"),
        ("343789","Xhh3000","3000","6922.51956576")
        ]



def makeList(sample):
	f1 = TFile.Open(indir+"signal.root")
	t1 = f1.Get("Nominal")
	t1.Draw(">>elist","mchannelnumber == "+sample) 
	elist = TEventList() 
	elist = ROOT.gDirectory.Get("elist")
	ef = TFile(outdir+"elist.root","recreate")
	elist.Write()
	return True
def makeSmall(filename):
	f = TFile.Open(indir+"elist.root")
	elist = f.Get("elist")
	f1 = TFile.Open(indir+"signal.root")
	Nominal = f1.Get("Nominal")
	Nominal.SetEventList(elist)
	f2 = TFile(outdir+"MVATree_"+filename+".root","recreate")
	small = Nominal.CopyTree("")
	small.Write()
	#small.Print()
	return True
for masspoint in signalsamples:
	sample = masspoint[0]
	filename = masspoint[1]
	print filename
	makeList(sample)
	makeSmall(filename)
