import numpy as np

_heraeus2018quarz = "".join([
     "@article{heraeus2018quarz,"
     "title={{Quarzglas fuer die Optik, Daten und "
     "Eigenschaften, Suprasil 311, 312, 313}},"
     "author={{Heraeus Quarzglas GmbH und Co. KG, Optics, "
     "Quarzstr. 8, 63450 Hanau, Germany}},"
     "year={2018},"
     "volume={HQS-MO 02.6 D04.2018}"
     "}"
])

_heraeus_silica_glass_suprasil_311_312_313_transmission = np.array([
    [1.56782211e-07, 6.10762223e-03],
    [1.59245971e-07, 1.85546330e-02],
    [1.61093792e-07, 3.36193299e-02],
    [1.62448860e-07, 4.84704514e-02],
    [1.63619146e-07, 6.52551934e-02],
    [1.64321318e-07, 8.03237041e-02],
    [1.64912621e-07, 9.82068342e-02],
    [1.65454648e-07, 1.20414867e-01],
    [1.65898125e-07, 1.42313978e-01],
    [1.66292326e-07, 1.66684463e-01],
    [1.66514065e-07, 1.93892450e-01],
    [1.66932904e-07, 2.31214759e-01],
    [1.67191599e-07, 2.55928490e-01],
    [1.67437975e-07, 2.74978657e-01],
    [1.67770583e-07, 2.95745056e-01],
    [1.67869133e-07, 3.13136200e-01],
    [1.68263335e-07, 3.31991861e-01],
    [1.68485073e-07, 3.51350950e-01],
    [1.68608261e-07, 3.65767293e-01],
    [1.68977826e-07, 3.86018822e-01],
    [1.69101014e-07, 4.00549580e-01],
    [1.69347390e-07, 4.17483062e-01],
    [1.69593766e-07, 4.34416544e-01],
    [1.69840142e-07, 4.51350026e-01],
    [1.70086518e-07, 4.68283508e-01],
    [1.70332894e-07, 4.85216991e-01],
    [1.70579270e-07, 5.01921642e-01],
    [1.70825646e-07, 5.18397462e-01],
    [1.71072022e-07, 5.34873283e-01],
    [1.71318398e-07, 5.51349103e-01],
    [1.71564774e-07, 5.67824923e-01],
    [1.71811150e-07, 5.84071913e-01],
    [1.72057526e-07, 6.00090072e-01],
    [1.72303902e-07, 6.15879400e-01],
    [1.72550278e-07, 6.32126389e-01],
    [1.72796654e-07, 6.48144548e-01],
    [1.73043031e-07, 6.63705045e-01],
    [1.73289407e-07, 6.79494373e-01],
    [1.73658971e-07, 6.95970193e-01],
    [1.73782159e-07, 7.09700044e-01],
    [1.74090129e-07, 7.28063718e-01],
    [1.74336505e-07, 7.45397654e-01],
    [1.74890851e-07, 7.70225800e-01],
    [1.75506791e-07, 7.90362914e-01],
    [1.76245919e-07, 8.06724319e-01],
    [1.77108236e-07, 8.21598324e-01],
    [1.78340116e-07, 8.37387652e-01],
    [1.79941560e-07, 8.53176980e-01],
    [1.81912569e-07, 8.68127261e-01],
    [1.84376329e-07, 8.80574272e-01],
    [1.87086466e-07, 8.88749774e-01],
    [1.89796603e-07, 8.94116897e-01],
    [1.92506739e-07, 8.98235852e-01],
    [1.95216876e-07, 9.00170513e-01],
    [1.97927013e-07, 9.01106639e-01],
    [1.99651645e-07, 9.02146779e-01],
    [2.99680326e-07, 9.30064141e-01],
    [4.29626388e-07, 9.31223510e-01],
    [4.78467291e-07, 9.31655018e-01],
    [5.27312743e-07, 9.32772781e-01],
    [5.76148270e-07, 9.32393261e-01],
    [6.24986691e-07, 9.32450449e-01],
    [6.73825113e-07, 9.32507637e-01],
    [7.22663535e-07, 9.32564825e-01],
    [7.71501956e-07, 9.32622013e-01],
    [8.20343273e-07, 9.33115908e-01],
    [8.69187484e-07, 9.34046510e-01],
    [9.18025492e-07, 9.34041311e-01],
    [9.66856884e-07, 9.33037924e-01],
    [9.97927057e-07, 9.31743400e-01],
    [1.05178646e-06, 9.38203873e-01],
    [1.12612490e-06, 9.39452376e-01],
    [1.20046334e-06, 9.40700879e-01],
    [1.27481026e-06, 9.40263903e-01],
    [1.34242032e-06, 9.35498783e-01],
    [1.41007410e-06, 9.22035758e-01],
    [1.48434413e-06, 9.36892945e-01],
    [1.55868477e-06, 9.37704472e-01],
    [1.63302792e-06, 9.38016598e-01],
    [1.70737107e-06, 9.38328723e-01],
    [1.78171045e-06, 9.39389951e-01],
    [1.85605517e-06, 9.39389951e-01],
    [1.93039518e-06, 9.40326328e-01],
    [2.00473927e-06, 9.40451179e-01],
    [2.07908869e-06, 9.39514801e-01],
    [2.13655649e-06, 9.35613229e-01],
    [2.16537551e-06, 9.16729620e-01],
    [2.17391188e-06, 8.99203016e-01],
    [2.18302856e-06, 8.78275726e-01],
    [2.20571892e-06, 8.46116368e-01],
    [2.22704755e-06, 8.60765471e-01],
    [2.27542937e-06, 8.71683630e-01],
    [2.30914649e-06, 8.86790517e-01],
    [2.34623911e-06, 9.02652748e-01],
    [2.40360461e-06, 9.19101776e-01],
    [2.47792015e-06, 9.24907315e-01],
    [2.53203843e-06, 9.15081596e-01],
    [2.56252932e-06, 8.99734373e-01],
    [2.58627162e-06, 8.82395786e-01],
    [2.60663835e-06, 8.64313300e-01],
    [2.61684932e-06, 8.49778644e-01],
    [2.62705685e-06, 8.35930664e-01],
    [2.64067101e-06, 8.16646494e-01],
    [2.64753174e-06, 7.96332309e-01],
    [2.65438930e-06, 7.76647577e-01],
    [2.65673997e-06, 7.57191738e-01],
    [2.65709551e-06, 2.38293057e-01],
    [2.65729341e-06, 1.98923594e-01],
    [2.65776400e-06, 1.05306672e-01],
    [2.66138954e-06, 5.63237356e-02],
    [2.66485859e-06, 3.84701418e-02],
    [2.69000000e-06, 1.50000000e-02],
    [2.71909787e-06, 4.57328366e-03],
    [2.79344196e-06, 4.69813397e-03],
    [2.83700986e-06, 7.69240361e-02],
    [2.84010267e-06, 1.33918201e-01],
    [2.84328177e-06, 1.73745448e-01],
    [2.84851468e-06, 2.53171052e-01],
    [2.84917398e-06, 3.46101296e-01],
    [2.85240371e-06, 3.75857286e-01],
    [2.85366591e-06, 3.93665101e-01],
    [2.85542863e-06, 4.46356092e-01],
    [2.85984209e-06, 5.09530347e-01],
    [2.86153140e-06, 5.76824662e-01],
    [2.86699443e-06, 6.10471819e-01],
    [2.86795518e-06, 6.43432300e-01],
    [2.87123180e-06, 6.63860932e-01],
    [2.87786442e-06, 6.88924631e-01],
    [2.89127463e-06, 7.10211608e-01],
    [2.90470901e-06, 7.26691848e-01],
    [2.91815029e-06, 7.41798735e-01],
    [2.93157978e-06, 7.59251768e-01],
    [2.97203901e-06, 7.77639443e-01],
    [3.03956233e-06, 7.90131410e-01],
    [3.11388163e-06, 7.95187847e-01],
    [3.18820846e-06, 7.98746081e-01],
    [3.26252368e-06, 8.04614045e-01],
    [3.33683921e-06, 8.10419585e-01],
    [3.40610999e-06, 8.11410584e-01],
    [3.45855581e-06, 7.98163446e-01],
    [3.47440990e-06, 7.81454314e-01],
    [3.48443367e-06, 7.59343324e-01],
    [3.49267276e-06, 7.33730284e-01],
    [3.50290732e-06, 7.14503337e-01],
    [3.50974360e-06, 6.99053112e-01],
    [3.51998852e-06, 6.77766134e-01],
    [3.53388889e-06, 6.01545023e-01],
    [3.54413554e-06, 5.79914707e-01],
    [3.55437528e-06, 5.59657745e-01],
    [3.56122364e-06, 5.41804151e-01],
    [3.56807085e-06, 5.24179449e-01],
    [3.57491805e-06, 5.06554748e-01],
    [3.58176986e-06, 4.88014477e-01],
    [3.58861937e-06, 4.69931991e-01],
    [3.59546773e-06, 4.52078398e-01],
    [3.60231609e-06, 4.34224804e-01],
    [3.60916444e-06, 4.16371210e-01],
    [3.61600935e-06, 3.99204293e-01],
    [3.62285540e-06, 3.81808484e-01],
    [3.62969916e-06, 3.64870459e-01],
    [3.63654406e-06, 3.47703542e-01],
    [3.64338782e-06, 3.30765517e-01],
    [3.65022812e-06, 3.14514169e-01],
    [3.65706612e-06, 2.98720605e-01],
    [3.66390413e-06, 2.82927041e-01],
    [3.67074213e-06, 2.67133478e-01],
    [3.67757668e-06, 2.52026590e-01],
    [3.68442158e-06, 2.34859673e-01],
    [3.69804150e-06, 2.14431042e-01],
    [3.71168643e-06, 1.89024005e-01],
    [3.72531066e-06, 1.67737028e-01],
    [3.77269146e-06, 1.53706974e-01],
    [3.84701108e-06, 1.58700987e-01],
    [3.92136489e-06, 1.56890657e-01],
    [3.97888772e-06, 1.42043875e-01],
    [4.01613544e-06, 1.27051434e-01],
    [4.04663030e-06, 1.10914532e-01],
    [4.07036771e-06, 9.45487376e-02],
    [4.09073444e-06, 7.64662516e-02],
    [4.11785702e-06, 5.89331070e-02],
    [4.16186108e-06, 4.43927282e-02],
    [4.25319548e-06, 2.58602609e-02],
    [4.32758601e-06, 1.67461885e-02],
    [4.40195803e-06, 1.13152002e-02],
    [4.47632252e-06, 7.38241555e-03],
    [4.55067822e-06, 5.19753519e-03],
    [4.60136968e-06, 4.82298427e-03],
    [4.76696945e-06, 2.07627754e-03],
    [4.84131416e-06, 2.07627754e-03],
    [4.90664280e-06, 2.99184645e-03],
    [4.96633552e-06, 4.65131510e-03]
])

_fresnell_reflection_losses = np.array([
    [1.7449681457350678e-7, 0.8972997258929201],
    [1.7720424651300534e-7, 0.8960515576805043],
    [1.7991167845250393e-7, 0.8963635997336082],
    [1.8261911039200248e-7, 0.8974245427141616],
    [1.8532654233150104e-7, 0.8981110352309902],
    [1.880339742709996e-7, 0.8995048230681878],
    [1.9074140621049816e-7, 0.9014394837974321],
    [1.9344883814999675e-7, 0.9039358202222635],
    [1.961562700894953e-7, 0.9059120865585883],
    [1.988637020289939e-7, 0.9068482127179002],
    [2.0157113396849245e-7, 0.9074098884134871],
    [2.04278565907991e-7, 0.9080339725196951],
    [2.0698599784748956e-7, 0.9087828734471445],
    [2.0969342978698812e-7, 0.9097189996064563],
    [2.124008617264867e-7, 0.9102806753020434],
    [2.1510829366598527e-7, 0.9112792098719759],
    [2.1781572560548385e-7, 0.9117784771569422],
    [2.205231575449824e-7, 0.9126938005127136],
    [2.2323058948448097e-7, 0.9128186173339552],
    [2.2593802142397953e-7, 0.9141291939569918],
    [2.2864545336347809e-7, 0.9150861229198437],
    [2.3135288530297667e-7, 0.9157102070260517],
    [2.3406031724247523e-7, 0.9171456004703297],
    [2.3664468409381478e-7, 0.9170894329007709],
    [2.390813728393635e-7, 0.919080261199574],
    [2.4218261306097093e-7, 0.9177072761659167],
    [2.4710521658733196e-7, 0.919080261199574],
    [2.516586248492159e-7, 0.9204532462332313],
    [2.554736425821457e-7, 0.9218262312668886],
    [2.582056875392761e-7, 0.9226500222870829],
    [2.608885064611429e-7, 0.9231992163005458],
    [2.635959384006414e-7, 0.9244473845129615],
    [2.6630337034014e-7, 0.9248218349766862],
    [2.6901080227963855e-7, 0.9259451863678604],
    [2.717182342191371e-7, 0.9265068620634475],
    [2.7442566615863567e-7, 0.9273181714015176],
    [2.7713309809813423e-7, 0.928067072328967],
    [2.7984053003763284e-7, 0.928691156435175],
    [2.8254796197713135e-7, 0.9295648741838659],
    [2.8525539391662996e-7, 0.9300641414688322],
    [2.880448692482345e-7, 0.9309794648246037],
    [2.906702577956271e-7, 0.9314371265024894],
    [2.9370586330354974e-7, 0.9323524498582609],
    [2.959620565864652e-7, 0.9328101115361467],
    [2.99777074319395e-7, 0.9325812806972038],

    [3.2053475132087895e-7, 0.9307544653980183],
    [3.686419425605928e-7, 0.9311230303979564],
    [4.1674293668968834e-7, 0.9326778994305652],
    [4.6484914943825196e-7, 0.9332337755935567],
    [5.129527528770816e-7, 0.9342891481913568],
    [5.610635319176798e-7, 0.933970905593433],
    [6.091723539759775e-7, 0.9340272853216156],
    [6.572811760342752e-7, 0.9340836650497983],
    [7.05389998092573e-7, 0.9341400447779811],
    [7.534988201508707e-7, 0.9341964245061638],
    [8.016053590631511e-7, 0.9346898636148041],
    [8.497096148294142e-7, 0.935620362103902],
    [8.978187630514287e-7, 0.9356143047777337],
    [9.45933456056628e-7, 0.9345468175275967],
    [9.765547929983916e-7, 0.9333131420979681],

    [0.0000010112391898986123, 0.9373299209414978],
    [0.0000020385549135623935, 0.935956567573797],
    [0.0000020993824094880534, 0.935956567573797],
    [0.0000021940029587057474, 0.935956567573797],
    [0.000002268347675948221, 0.935956567573797],
    [0.0000023426923931906945, 0.935956567573797],
    [0.000002417037110433168, 0.935956567573797],
    [0.0000024913852794686236, 0.9352698908899466],
    [0.0000025657274863162014, 0.935769292114565],
    [0.000002640073458756123, 0.9355195915022558],
    [0.0000027144194311960446, 0.9352698908899466],
    [0.000002788764148438518, 0.9352698908899466],
    [0.000002863108238082268, 0.9353947411961012],
    [0.0000029374501311304836, 0.935956567573797],
    [0.000003011794848372957, 0.935956567573797],
    [0.0000030861392518160686, 0.9360189927268743],
    [0.0000031604808310649226, 0.9366432442576473],
    [0.000003234825548307396, 0.9366432442576473],
    [0.000003309167755154974, 0.9371426454822659],
    [0.0000033835115309993616, 0.9373299209414978],
    [0.0000034578537378469395, 0.9378293221661163],
    [0.0000035321968860926033, 0.9381414479315028],
    [0.000003606538779140819, 0.9387032743091985],
    [0.0000036808806721890344, 0.9392651006868943],
    [0.00000375522256523725, 0.93982692706459],
    [0.000003829564144486105, 0.9404511785953631],
    [0.000003903905096136234, 0.9412002804322908],
    [0.00000397824542018764, 0.942074232575373],
])

_suprasil_refractive_index = np.array([
    [190, 1.5657],
    [193.4, 1.5601],
    [200, 1.5505],
    [220, 1.5285],
    [240, 1.5133],
    [248.4, 1.5083],
    [260, 1.5024],
    [266, 1.4997],
    [274.87, 1.4961],
    [280, 1.4942],
    [300, 1.4878],
    [308, 1.4856],
    [320, 1.4827],
    [325, 1.4816],
    [337, 1.4792],
    [340, 1.4787],
    [360, 1.4753],
    [365.48, 1.4745],
    [380.0, 1.4725],
    [400.0, 1.4701],
    [404.65, 1.4696],
    [435.83, 1.4667],
    [441.6, 1.4662],
    [447.1, 1.4658],
    [486.13, 1.4631],
    [488.0, 1.463],
    [514.5, 1.4616],
    [532, 1.4607],
    [546.07, 1.4601],
    [587.56, 1.4585],
    [632.8, 1.457],
    [656.27, 1.4564],
    [694.3, 1.4554],
    [752.5, 1.4542],
    [800, 1.4533],
    [850, 1.4525],
    [900, 1.4518],
    [905, 1.4517],
    [1000, 1.4504],
    [1064, 1.4496],
    [1153, 1.4486],
    [1200, 1.4481],
    [1319, 1.4467],
    [1400, 1.4458],
    [1600, 1.4434],
    [1800, 1.4409],
    [2000, 1.4381],
    [2200, 1.435],
    [2400, 1.4316],
    [2600, 1.4279],
    [2800, 1.4238],
    [3000, 1.4193],
    [3200, 1.4143],
    [3400, 1.4088],
])

_suprasil_refractive_index[:, 0] *= 1e-9

refraction = {
    "wavelength_vs_value": _suprasil_refractive_index,
    "units": ["m", "1"],
    "reference": _heraeus2018quarz
}

transmission = {
    "wavelength_vs_value": _heraeus_silica_glass_suprasil_311_312_313_transmission,
    "units": ["m", "1"],
    "reference": _heraeus2018quarz
}

fresnell_reflection_losses = {
    "wavelength_vs_value": _fresnell_reflection_losses,
    "units": ["m", "1"],
    "reference": _heraeus2018quarz
}
