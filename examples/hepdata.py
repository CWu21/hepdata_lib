from __future__ import print_function
from hepdata_lib import Submission
import ROOT
import math

submission = Submission()

# submission.read_abstract("example_inputs/abstract.txt")
# submission.add_link("Webpage with all figures and tables", "https://cms-results.web.cern.ch/cms-results/public-results/publications/B2G-16-029/")
# submission.add_link("arXiv", "http://arxiv.org/abs/arXiv:1802.09407")
# submission.add_record_id(1657397, "inspire")
# submission.add_additional_resource("Original abstract file", "example_inputs/abstract.txt", copy_file=True) 



PNGName = ["_higgs_m", "_higgs_pT", "_Z_pT", "_jetpt", "_NTracks_", "_GhostTracks_deltaRLeadTrack_", 
                                "_GhostTracks_leadTrackPtRatio_", "_GhostTracks_tau2_", "_GhostTracks_angularity_2_",
                                "_GhostTracks_M2_0p3_", "_GhostTracks_U1_0p7_", "_Reg", "_Clas"]

HistoName = ["_higgs_m", "_higgs_pT", "_Z_pT", "_jet pt", "_NTracks_", "_GhostTracks_deltaRLeadTrack_", 
                                "_GhostTracks_leadTrackPtRatio_", "_GhostTracks_tau2_", "_GhostTracks_angularity_2_",
                                "_GhostTracks_M2_0p3_", "_GhostTracks_U1_0p7_", "_Reg", "_Clas"]

x_axis = ["$m_{llj}$", "pT_{H}", "pT_Z", "p_T^{jet}", "number of tracks", "#Delta R_{leading jet}", "p_{T, leading track}/p_{T, tracks}", 
            "#tau_{2, tracks}", "angularity_{tracks}(0.2)", "M_{2, tracks}(0.3)", "U_{1, tracks}(0.7)",
            "RegMLP output", "ClasMLP output"]

x_unit = ["GeV", "GeV","GeV","GeV", "", "","","","","","","",""]


from hepdata_lib import Table

from hepdata_lib import RootFileReader     

from hepdata_lib import Variable, Uncertainty
from hepdata_lib import Uncertainty

#####  figure 1 ###########

reader = RootFileReader("input/Plot_test.root")

i=0

#####  figure 1a ###########

table_1a = Table("Figure 1a")   # 1a:0, 5:1, 6:3, 7:8, 8:5, 9:9, 10:4, 11:6, 12:7, 13:10
table_1a.description = ""
table_1a.location = "Data from Figure 1a (left), located on page 5."
table_1a.keywords["observables"] = ["N"]
table_1a.add_image("input/postRWTotal"+PNGName[i]+"ComBkg_hdbs3.png")

#####  figure 1b ###########

table_1b = Table("Figure 1b")
table_1b.description = ""
table_1b.location = "Data from Figure 1b (right), located on page 5."
table_1b.keywords["observables"] = ["N"]
table_1b.add_image("input/postRWnnSR"+PNGName[i]+"ComBkg_hdbs3.png")


fig1 = (0, 1)
Histtype = ["Total", "nnSR"]

for f in fig1:

    pre = reader.read_hist_1d("preRW"+Histtype[f]+HistoName[i]+"ComBkg_hdbs3")

    post = reader.read_hist_1d("postRW"+Histtype[f]+HistoName[i]+"ComBkg_hdbs3")

    data = reader.read_hist_1d("postRW"+Histtype[f]+HistoName[i]+"Data_hdbs3")

    sig_05 = reader.read_hist_1d("postRW"+Histtype[f]+HistoName[i]+"Sig_hdbs3_05")
    sig_20 = reader.read_hist_1d("postRW"+Histtype[f]+HistoName[i]+"Sig_hdbs3_20")
    sig_40 = reader.read_hist_1d("postRW"+Histtype[f]+HistoName[i]+"Sig_hdbs3_40")

    data.keys()

    # x-axis: 
    x = Variable(x_axis[i], is_independent=True, is_binned=False, units=x_unit[i])
    x.values = pre["x"]

    # y-axis: N events

    bkg_pre = Variable("Number of pre-reweighting background events", is_independent=False, is_binned=False, units="")
    bkg_pre.values = pre["y"]


    bkg_post = Variable("Number of post-reweighting background events", is_independent=False, is_binned=False, units="")
    bkg_post.values = post["y"]


    Ndata = Variable("Number of data events", is_independent=False, is_binned=False, units="")
    Ndata.values = data["y"]

    sig05 = Variable("Number of 0.5 GeV signal events", is_independent=False, is_binned=False, units="")
    sig05.values = sig_05["y"]


    sig20 = Variable("Number of 2.0 GeV signal events", is_independent=False, is_binned=False, units="")
    sig20.values = sig_20["y"]


    sig40 = Variable("Number of 4.0 GeV signal events", is_independent=False, is_binned=False, units="")
    sig40.values = sig_40["y"]



    unc_pre = Uncertainty("pre-reweighting background statistical uncertainty", is_symmetric=True)
    unc_pre.values = pre["dy"]


    unc_post = Uncertainty("post-reweighting background statistical uncertainty", is_symmetric=True)
    unc_post.values = post["dy"]


    unc_data = Uncertainty("Poisson errors", is_symmetric=True)
    unc_data.values = data["dy"]

    bkg_pre.add_uncertainty(unc_pre)
    bkg_post.add_uncertainty(unc_post)
    Ndata.add_uncertainty(unc_data)

    if f == 0:
        table_1a.add_variable(x)
        table_1a.add_variable(bkg_pre)
        table_1a.add_variable(bkg_post)
        table_1a.add_variable(Ndata)
        table_1a.add_variable(sig05)
        table_1a.add_variable(sig20)
        table_1a.add_variable(sig40)


        # table.add_additional_resource("Background ROOT file", "example_inputs/mlfit_lm_1000.root", copy_file=False)  # optional
        # table.add_additional_resource("Data ROOT file", "example_inputs/Data_cat0_singleH.root", copy_file=False)  # optional
        # table.add_additional_resource("Signal ROOT file", "example_inputs/BprimeBToHB1000_cat0_singleH.root", copy_file=False)  # optional

        submission.add_table(table_1a)

    if f == 1:
        table_1b.add_variable(x)
        table_1b.add_variable(bkg_pre)
        table_1b.add_variable(bkg_post)
        table_1b.add_variable(Ndata)
        table_1b.add_variable(sig05)
        table_1b.add_variable(sig20)
        table_1b.add_variable(sig40)

        submission.add_table(table_1b)

########################################################

#####  figure 2 ###########


#####  figure 2a ###########
table_2a = Table("Figure 2a")  
table_2a.description = ""
table_2a.location = "Data from Figure 2a"
table_2a.keywords["observables"] = ["N"]
table_2a.add_image("input/postRWmSR"+PNGName[11]+"ComBkg_hdbs3.png")


#####  figure 2b ###########

table_2b = Table("Figure 2b") 
table_2b.description = ""
table_2b.location = "Data from Figure 2b"
table_2b.keywords["observables"] = ["N"]
table_2b.add_image("input/postRWmSR"+PNGName[12]+"ComBkg_hdbs3.png")


## 11 for 2a, 12 for 2b
for j in 11, 12:

    post = reader.read_hist_1d("postRWmSR"+HistoName[j]+"ComBkg_hdbs3")

    data = reader.read_hist_1d("postRWmSR"+HistoName[j]+"Data_hdbs3")

    sig_05 = reader.read_hist_1d("postRWmSR"+HistoName[j]+"Sig_hdbs3_05")
    sig_20 = reader.read_hist_1d("postRWmSR"+HistoName[j]+"Sig_hdbs3_20")
    sig_40 = reader.read_hist_1d("postRWmSR"+HistoName[j]+"Sig_hdbs3_40")

    data.keys()

    # x-axis: 
    x = Variable(x_axis[j], is_independent=True, is_binned=False, units=x_unit[j])
    x.values = data["x"]

    # y-axis: N events


    bkg_post = Variable("Number of post-reweighting background events", is_independent=False, is_binned=False, units="")
    bkg_post.values = post["y"]


    Ndata = Variable("Number of data events", is_independent=False, is_binned=False, units="")
    Ndata.values = data["y"]

    sig05 = Variable("Number of 0.5 GeV signal events", is_independent=False, is_binned=False, units="")
    sig05.values = sig_05["y"]


    sig20 = Variable("Number of 2.0 GeV signal events", is_independent=False, is_binned=False, units="")
    sig20.values = sig_20["y"]


    sig40 = Variable("Number of 4.0 GeV signal events", is_independent=False, is_binned=False, units="")
    sig40.values = sig_40["y"]

    unc_post = Uncertainty("post-reweighting background statistical uncertainty", is_symmetric=True)
    unc_post.values = post["dy"]


    unc_data = Uncertainty("Poisson errors", is_symmetric=True)
    unc_data.values = data["dy"]


    bkg_post.add_uncertainty(unc_post)
    Ndata.add_uncertainty(unc_data)

    if j == 11:
        table_2a.add_variable(x)

        table_2a.add_variable(bkg_post)
        table_2a.add_variable(Ndata)
        table_2a.add_variable(sig05)
        table_2a.add_variable(sig20)
        table_2a.add_variable(sig40)

        submission.add_table(table_2a)

    if j == 12:
        table_2b.add_variable(x)

        table_2b.add_variable(bkg_post)
        table_2b.add_variable(Ndata)
        table_2b.add_variable(sig05)
        table_2b.add_variable(sig20)
        table_2b.add_variable(sig40)

        submission.add_table(table_2b)

#################################


#####  figure 3 ###########

#####  figure 3a ###########
table_3a = Table("Figure 3a")   # change this
table_3a.description = ""
table_3a.location = "Data from Figure 3a."
table_3a.keywords["observables"] = ["N"]
# table.add_image("input/xxxx.png")

#####  figure 3b ###########
table_3b = Table("Figure 3b")   # change this
table_3b.description = ""
table_3b.location = "Data from Figure 3b."
table_3b.keywords["observables"] = ["N"]
# table.add_image("input/xxxx.png")


for i in 1, 2:

    if i == 1:
        reader = RootFileReader("input/Plot_gg.root")  # Plot_gg.root for 3a, Plot_qq.root for 3b
    if i == 2:
        reader = RootFileReader("input/Plot_qq.root")  # Plot_gg.root for 3a, Plot_qq.root for 3b


    sig = reader.read_hist_1d("h_L_x_signal_SignalRegion_overallSyst_x_HistSyst")
    bkg = reader.read_hist_1d("h_L_x_combined_bg_SignalRegion_overallSyst_x_StatUncert")
    fit = reader.read_hist_1d("h_SignalRegion_Total")

    fit_unc = reader.read_graph("Graph")
    data = reader.read_graph("DataSample")

    data.keys()

    # x-axis: 
    x = Variable("m_{llj}", is_independent=True, is_binned=False, units="GeV")
    x.values = fit["x"]

    # y-axis: N events

    Ndata = Variable("Number of data events", is_independent=False, is_binned=False, units="")
    Ndata.values = data["y"]

    Nbkg = Variable("Number of background events", is_independent=False, is_binned=False, units="")
    Nbkg.values = bkg["y"]

    Nsig= Variable("Number of signal events", is_independent=False, is_binned=False, units="")
    Nsig.values = sig["y"]

    Nfit= Variable("Number of total events after fit", is_independent=False, is_binned=False, units="")
    Nfit.values = fit["y"]

    unc_fit = Uncertainty("Fit uncertainty", is_symmetric=True)
    unc_fit.values = fit["dy"]


    unc_data = Uncertainty("Poisson errors", is_symmetric=True)
    # unc_data.values = data["dy"]
    unc_data.values = [math.sqrt(x) for x in data["y"]]


    Nfit.add_uncertainty(unc_fit)
    Ndata.add_uncertainty(unc_data)

    if i == 1:
        table_3a.add_variable(x)

        table_3a.add_variable(Nbkg)
        table_3a.add_variable(Ndata)
        table_3a.add_variable(Nsig)
        table_3a.add_variable(Nfit)

        submission.add_table(table_3a)

    if i == 2:
        table_3b.add_variable(x)

        table_3b.add_variable(Nbkg)
        table_3b.add_variable(Ndata)
        table_3b.add_variable(Nsig)
        table_3b.add_variable(Nfit)

        submission.add_table(table_3b)


#################################


#####  figure 4 ###########

#####  figure 4a ###########

table_4a = Table("Figure 4a")  
table_4a.description = ""
table_4a.location = "Data from Figure 4q"
table_4a.keywords["observables"] = ["CLS"]
table_4a.keywords["reactions"] = ["p p ---> H ---> Z a"] 
# table_4a.add_image("input/xxx.pdf")
# table_4a.add_additional_resource("Original data file", "input/gglimits.txt", copy_file=True)

#####  figure 4b ###########

table_4b = Table("Figure 4b")  
table_4b.description = ""
table_4b.location = "Data from Figure 4b"
table_4b.keywords["observables"] = ["CLS"]
table_4b.keywords["reactions"] = ["p p ---> H ---> Z a"] 
# table_4b.add_image("input/xxx.pdf")
# table_4b.add_additional_resource("Original data file", "input/qqlimits.txt", copy_file=True)


import numpy as np

for i in 1, 2:

    if i == 1:
        data = np.loadtxt("input/gglimits.txt", skiprows=2) # 4a is gglimits.txt, 4b is qqlimits.txt
    if i == 2:
        data = np.loadtxt("input/qqlimits.txt", skiprows=2) # 4a is gglimits.txt, 4b is qqlimits.txt

    print(data)

    d = Variable("Resonance mass", is_independent=True, is_binned=False, units="GeV")
    d.values = data[:,0]

    obs = Variable("Observed limits", is_independent=False, is_binned=False, units="")
    obs.values = data[:,1]
    # obs.add_qualifier("Efficiency times acceptance", "Bulk graviton --> WW")
    # obs.add_qualifier("SQRT(S)", 13, "TeV")

    exp = Variable("Expected limits", is_independent=False, is_binned=False, units="")
    exp.values = data[:,2]

    p1s = Variable("+1 sigma", is_independent=False, is_binned=False, units="")
    p1s.values = data[:,3]

    m1s = Variable("-1 sigma", is_independent=False, is_binned=False, units="")
    m1s.values = data[:,4]

    p2s = Variable("+2 sigma", is_independent=False, is_binned=False, units="")
    p2s.values = data[:,5]

    m2s = Variable("-2 sigma", is_independent=False, is_binned=False, units="")
    m2s.values = data[:,6]

    if i == 1:
        table_4a.add_variable(d)
        table_4a.add_variable(obs)
        table_4a.add_variable(exp)
        table_4a.add_variable(p1s)
        table_4a.add_variable(m1s)
        table_4a.add_variable(p2s)
        table_4a.add_variable(m2s)

        submission.add_table(table_4a)

    if i == 2:
        table_4b.add_variable(d)
        table_4b.add_variable(obs)
        table_4b.add_variable(exp)
        table_4b.add_variable(p1s)
        table_4b.add_variable(m1s)
        table_4b.add_variable(p2s)
        table_4b.add_variable(m2s)

        submission.add_table(table_4b)


submission.create_files("output",remove_old=True) #  