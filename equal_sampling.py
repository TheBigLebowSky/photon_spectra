import cherenkov_la_palma
import cherenkov_cta_chile
import hamamatsu_r11920_100_05
import hamamatsu_s10362_33_050c
import nsb_la_palma_2002_hoffmann
import nsb_la_palma_2013_benn
import veritas_nsb_filter_2015
import cta_mirrors
import numpy as np

wavelength = np.linspace(240e-9, 700e-9, 460)

cherenkov_histogram_on_ground = np.interp(
    x=wavelength,
    xp=cherenkov_la_palma.cherenkov_histogram_on_ground[:, 0],
    fp=cherenkov_la_palma.cherenkov_histogram_on_ground[:, 1],)

cherenkov_la_palma_zd_70deg = np.interp(
    x=wavelength,
    xp=cherenkov_la_palma.cherenkov_histogram_on_ground_zenith_distance_70deg[:, 0],
    fp=cherenkov_la_palma.cherenkov_histogram_on_ground_zenith_distance_70deg[:, 1],)

cherenkov_gamma_below_5gev_5000m_asl = np.interp(
    x=wavelength,
    xp=cherenkov_cta_chile.cherenkov_gamma_below_5gev_5000m_asl[:, 0],
    fp=cherenkov_cta_chile.cherenkov_gamma_below_5gev_5000m_asl[:, 1],)

hamamatsu_s10362_33_050c = np.interp(
    x=wavelength,
    xp=hamamatsu_s10362_33_050c.hamamatsu_s10362_33_050c[:, 0],
    fp=hamamatsu_s10362_33_050c.hamamatsu_s10362_33_050c[:, 1],)

hamamatsu_r11920_100_05 = np.interp(
    x=wavelength,
    xp=hamamatsu_r11920_100_05.hamamatsu_r11920_100_05[:, 0],
    fp=hamamatsu_r11920_100_05.hamamatsu_r11920_100_05[:, 1],)

nsb_diff_la_palma_2002_hoffmann = np.interp(
    x=wavelength,
    xp=nsb_la_palma_2002_hoffmann.la_palma_2002_hoffmann[:, 0],
    fp=nsb_la_palma_2002_hoffmann.la_palma_2002_hoffmann[:, 1],)
nsb_diff_la_palma_2002_hoffmann[wavelength < 362e-9] = np.nan
nsb_diff_la_palma_2002_hoffmann[wavelength > 550e-9] = np.nan

nsb_diff_la_palma_benn = np.interp(
    x=wavelength,
    xp=nsb_la_palma_2013_benn.la_palma_2013_benn[:, 0],
    fp=nsb_la_palma_2013_benn.la_palma_2013_benn[:, 1],)

veritas_nsb_filter_2015 = np.interp(
    x=wavelength,
    xp=veritas_nsb_filter_2015.veritas_nsb_filter_2015[:, 0],
    fp=veritas_nsb_filter_2015.veritas_nsb_filter_2015[:, 1],)

mst_dielectric = np.interp(
    x=wavelength,
    xp=cta_mirrors.mst_dielectric[:, 0],
    fp=cta_mirrors.mst_dielectric[:, 1],)

mst_Al_SiO2_before = np.interp(
    x=wavelength,
    xp=cta_mirrors.mst_Al_SiO2_before[:, 0],
    fp=cta_mirrors.mst_Al_SiO2_before[:, 1],)

mst_Al_SiO2_HfO2_SiO2_before = np.interp(
    x=wavelength,
    xp=cta_mirrors.mst_Al_SiO2_HfO2_SiO2_before[:, 0],
    fp=cta_mirrors.mst_Al_SiO2_HfO2_SiO2_before[:, 1],)

astri_SiO2_mixed_multilayer_yellow = np.interp(
    x=wavelength,
    xp=cta_mirrors.astri_SiO2_mixed_multilayer_yellow[:, 0],
    fp=cta_mirrors.astri_SiO2_mixed_multilayer_yellow[:, 1],)

astri_SiO2_TiO2_mulitlayer = np.interp(
    x=wavelength,
    xp=cta_mirrors.astri_SiO2_TiO2_mulitlayer[:, 0],
    fp=cta_mirrors.astri_SiO2_TiO2_mulitlayer[:, 1],)

astri_SiO2_mixed_multilayer_orange = np.interp(
    x=wavelength,
    xp=cta_mirrors.astri_SiO2_mixed_multilayer_orange[:, 0],
    fp=cta_mirrors.astri_SiO2_mixed_multilayer_orange[:, 1],)

astri_Al_SiO2 = np.interp(
    x=wavelength,
    xp=cta_mirrors.astri_Al_SiO2[:, 0],
    fp=cta_mirrors.astri_Al_SiO2[:, 1],)