import numpy as np

_archambault2017gamma = "".join([
    "@article{archambault2017gamma,"
    "title={Gamma-ray observations under bright moonlight with VERITAS},"
    "author={Archambault, S and Archer, A and Benbow, W and Bird, R and "
    "Bourbeau, E and Bouvier, A and Buchovecky, M and Bugaev, V and "
    "Cardenzana, JV and Cerruti, M and others},"
    "journal={Astroparticle Physics},"
    "volume={91},"
    "pages={34--43},"
    "year={2017},"
    "publisher={Elsevier}"
    "}"
])

_veritas_nsb_filter_2015 = np.array([
    # wavelength/m, efficiency/1
    [200, -0.0],
    [251.45091130912675, 0.0],
    [257.3269595854213, 0.0066541199654472916],
    [261.8675423443762, 0.02637663064857132],
    [265.07265958599146, 0.04980782936522399],
    [266.942311310267, 0.07120845691017053],
    [268.8119630345425, 0.09422408530124105],
    [270.36110303465654, 0.11918368697581339],
    [271.53631268991546, 0.14329871039587894],
    [273.03203406933585, 0.16864103492119709],
    [274.1538251039012, 0.19491528212274511],
    [275.22219751777294, 0.2184597050897812],
    [276.29056993164465, 0.2404625363400621],
    [277.3589423455164, 0.2611440032616956],
    [278.4273147593882, 0.28160524279522137],
    [279.4956871732599, 0.3029473918811785],
    [280.5640595871316, 0.3247299957433516],
    [281.685850621697, 0.34730442282468754],
    [283.1815720011174, 0.3710611101556285],
    [284.30336303568276, 0.3951330834760982],
    [285.425154070248, 0.4168266010050026],
    [286.9208754496685, 0.4412880159778889],
    [288.0426664842338, 0.46399457949208966],
    [289.16445751879917, 0.48511550581191365],
    [290.90437830710454, 0.5092451755086381],
    [292.36957476041437, 0.5313916255882903],
    [293.91871476052836, 0.5532974074810999],
    [296.05545958827184, 0.5757207859470896],
    [298.19220441601533, 0.5959418905320004],
    [301.9315078645664, 0.6273647305696527],
    [304.6024388992457, 0.6475024722449408],
    [308.34174234779687, 0.6675468972303528],
    [312.88232510675175, 0.6878700280628617],
    [318.22418717611043, 0.7039204987215714],
    [324.10023545240495, 0.7142217563947921],
    [329.9762837286995, 0.7209993758582868],
    [335.8523320049941, 0.7180069075584501],
    [341.72838028128865, 0.7066057571672216],
    [347.0702423506474, 0.6895820782664575],
    [351.3437320061343, 0.6700804897970113],
    [354.54884924774956, 0.6489796132345549],
    [356.95268717896096, 0.6289822198608406],
    [358.6887923515025, 0.6082484955928763],
    [360.63857200681844, 0.5861453800065418],
    [362.0274561448517, 0.5640673977153473],
    [363.41634028288496, 0.5409910512647303],
    [364.9120616623054, 0.5185880780482603],
    [366.0338526968707, 0.4964563453436971],
    [367.10222511074244, 0.4739732441961867],
    [368.0103416625334, 0.44876230957021457],
    [368.65136511085643, 0.42743235386506784],
    [369.7731561454218, 0.40212934677175116],
    [370.8415285592936, 0.37568215263829896],
    [371.9099009731653, 0.34615177507133643],
    [372.978273387037, 0.3166213975043738],
    [374.0466458009088, 0.28591647386750263],
    [375.1150182147805, 0.25315609460829125],
    [376.1833906286522, 0.21922116927917124],
    [377.19834442183037, 0.18678478556721],
    [377.91949580119376, 0.1645724272425937],
    [378.8543216633316, 0.13739363026051188],
    [379.86927545650974, 0.10851024841002466],
    [380.9910664910751, 0.08567378806351611],
    [382.0594389049468, 0.062309777363574126],
    [383.18122993951215, 0.04114704516668555],
    [385.15008767364714, 0.020346061783580005],
    [389.80513890551686, 0.0005017788796930489],
    [395.6811871818114, 0],
    [700.0, 0.0],
])

_veritas_nsb_filter_2015[:, 0] *= 1e-9

transmission = {
    "wavelength_vs_value": _veritas_nsb_filter_2015,
    "units": ["m", "1"],
    "reference": _archambault2017gamma
}