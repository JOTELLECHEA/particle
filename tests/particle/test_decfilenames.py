# -*- encoding: utf-8 -*-
# Copyright (c) 2018-2020, Eduardo Rodrigues and Henry Schreiner.
#
# Distributed under the 3-clause BSD license, see accompanying file LICENSE
# or https://github.com/scikit-hep/particle for details.

from __future__ import absolute_import, division, print_function

import pytest

from particle.particle import Particle, ParticleNotFound


# All particle names found in DECAY.DEC
dec_names = [
    "B'_1+",
    "B'_1-",
    "B'_10",
    "B'_c1+",
    "B'_c1-",
    "B'_s10",
    "B*+",
    "B*-",
    "B*0",
    "B+",
    "B-",
    "B0",
    "B_0*+",
    "B_0*-",
    "B_0*0",
    "B_1+",
    "B_1-",
    "B_10",
    "B_2*+",
    "B_2*-",
    "B_2*0",
    "B_c*+",
    "B_c*-",
    "B_c+",
    "B_c-",
    "B_c0*+",
    "B_c0*-",
    "B_c1+",
    "B_c1-",
    "B_c2*+",
    "B_c2*-",
    "B_s*0",
    "B_s0",
    "B_s0*0",
    "B_s10",
    "B_s2*0",
    "D'_1+",
    "D'_1-",
    "D'_10",
    "D'_s1+",
    "D'_s1-",
    "D(2S)+",
    "D(2S)-",
    "D(2S)0",
    "D*(2S)+",
    "D*(2S)-",
    "D*(2S)0",
    "D*+",
    "D*-",
    "D*0",
    "D+",
    "D-",
    "D0",
    "D_0*+",
    "D_0*-",
    "D_0*0",
    "D_1+",
    "D_1-",
    "D_10",
    "D_2*+",
    "D_2*-",
    "D_2*0",
    "D_s*+",
    "D_s*-",
    "D_s+",
    "D_s-",
    "D_s0*+",
    "D_s0*-",
    "D_s1+",
    "D_s1-",
    "D_s2*+",
    "D_s2*-",
    "Delta(1600)+",
    "Delta(1600)++",
    "Delta(1600)-",
    "Delta(1600)0",
    "Delta(1620)+",
    "Delta(1620)++",
    "Delta(1620)-",
    "Delta(1620)0",
    "Delta(1700)+",
    "Delta(1700)++",
    "Delta(1700)-",
    "Delta(1700)0",
    "Delta(1900)+",
    "Delta(1900)++",
    "Delta(1900)-",
    "Delta(1900)0",
    "Delta(1905)+",
    "Delta(1905)++",
    "Delta(1905)-",
    "Delta(1905)0",
    "Delta(1910)+",
    "Delta(1910)++",
    "Delta(1910)-",
    "Delta(1910)0",
    "Delta(1920)+",
    "Delta(1920)++",
    "Delta(1920)-",
    "Delta(1920)0",
    "Delta(1930)+",
    "Delta(1930)++",
    "Delta(1930)-",
    "Delta(1930)0",
    "Delta(1950)+",
    "Delta(1950)++",
    "Delta(1950)-",
    "Delta(1950)0",
    "Delta+",
    "Delta++",
    "Delta-",
    "Delta0",
    "J/psi",
    "K''*+",
    "K''*-",
    "K''*0",
    "K'*+",
    "K'*-",
    "K'*0",
    "K'_1+",
    "K'_1-",
    "K'_10",
    "K*+",
    "K*-",
    "K*0",
    "K*0R",
    "K*0T",
    "K*BL",
    "K*BR",
    "K*BS",
    "K*L",
    "K*S",
    "K+",
    "K-",
    "K0",
    "K_0*+",
    "K_0*-",
    "K_0*0",
    "K_0*0N",
    "K_1+",
    "K_1-",
    "K_10",
    "K_2*+",
    "K_2*-",
    "K_2*0",
    "K_L0",
    "K_S0",
    "Lambda(1405)0",
    "Lambda(1520)0",
    "Lambda(1600)0",
    "Lambda(1670)0",
    "Lambda(1690)0",
    "Lambda(1800)0",
    "Lambda(1810)0",
    "Lambda(1820)0",
    "Lambda(1830)0",
    "Lambda(1890)0",
    "Lambda0",
    "Lambda_b0",
    "Lambda_c(2593)+",
    "Lambda_c(2625)+",
    "Lambda_c+",
    "N(1440)+",
    "N(1440)0",
    "N(1520)+",
    "N(1520)0",
    "N(1535)+",
    "N(1535)0",
    "N(1650)+",
    "N(1650)0",
    "N(1675)+",
    "N(1675)0",
    "N(1680)+",
    "N(1680)0",
    "N(1700)+",
    "N(1700)0",
    "N(1710)+",
    "N(1710)0",
    "N(1720)+",
    "N(1720)0",
    "N(1900)+",
    "N(1900)0",
    "N(1990)+",
    "N(1990)0",
    "N(2090)+",
    "N(2090)0",
    "N(2190)+",
    "N(2190)0",
    "Omega-",
    "Omega_b*-",
    "Omega_b-",
    "Omega_c*0",
    "Omega_c0",
    "Omega_cc*+",
    "Omega_cc+",
    "Sigma(1660)0",
    "Sigma(1670)0",
    "Sigma(1750)+",
    "Sigma(1750)-",
    "Sigma(1750)0",
    "Sigma(1775)+",
    "Sigma(1775)-",
    "Sigma(1775)0",
    "Sigma(1915)+",
    "Sigma(1915)-",
    "Sigma(1915)0",
    "Sigma(1940)+",
    "Sigma(1940)-",
    "Sigma(1940)0",
    "Sigma*+",
    "Sigma*-",
    "Sigma*0",
    "Sigma+",
    "Sigma-",
    "Sigma0",
    "Sigma_b*+",
    "Sigma_b*-",
    "Sigma_b*0",
    "Sigma_b+",
    "Sigma_b-",
    "Sigma_b0",
    "Sigma_c*+",
    "Sigma_c*++",
    "Sigma_c*0",
    "Sigma_c+",
    "Sigma_c++",
    "Sigma_c0",
    "Upsilon",
    "Upsilon(2S)",
    "Upsilon(3S)",
    "Upsilon(4S)",
    "Upsilon(5S)",
    "Upsilon_1(1D)",
    "Upsilon_1(2D)",
    "Upsilon_2(1D)",
    "Upsilon_2(2D)",
    "Upsilon_3(1D)",
    "Upsilon_3(2D)",
    "X_1(3872)",
    "Xi'_b-",
    "Xi'_b0",
    "Xi'_c+",
    "Xi'_c0",
    "Xi*-",
    "Xi*0",
    "Xi-",
    "Xi0",
    "Xi_b*-",
    "Xi_b*0",
    "Xi_b-",
    "Xi_b0",
    "Xi_bc+",
    "Xi_bc0",
    "Xi_c*+",
    "Xi_c*0",
    "Xi_c+",
    "Xi_c0",
    "Xi_cc*+",
    "Xi_cc*++",
    "Xi_cc+",
    "Xi_cc++",
    "Xsd",
    "Xss",
    "Xsu",
    "Xu+",
    "Xu-",
    "Xu0",
    "a_0+",
    "a_0-",
    "a_00",
    "a_1+",
    "a_1-",
    "a_10",
    "a_2+",
    "a_2-",
    "a_20",
    "anti-B'_10",
    "anti-B'_s10",
    "anti-B*0",
    "anti-B0",
    "anti-B_0*0",
    "anti-B_10",
    "anti-B_2*0",
    "anti-B_s*0",
    "anti-B_s0",
    "anti-B_s0*0",
    "anti-B_s10",
    "anti-B_s2*0",
    "anti-D'_10",
    "anti-D(2S)0",
    "anti-D*(2S)0",
    "anti-D*0",
    "anti-D0",
    "anti-D_0*0",
    "anti-D_10",
    "anti-D_2*0",
    "anti-Delta(1600)-",
    "anti-Delta(1600)--",
    "anti-Delta(1600)+",
    "anti-Delta(1600)0",
    "anti-Delta(1620)-",
    "anti-Delta(1620)--",
    "anti-Delta(1620)+",
    "anti-Delta(1620)0",
    "anti-Delta(1700)-",
    "anti-Delta(1700)--",
    "anti-Delta(1700)+",
    "anti-Delta(1700)0",
    "anti-Delta(1900)-",
    "anti-Delta(1900)--",
    "anti-Delta(1900)+",
    "anti-Delta(1900)0",
    "anti-Delta(1905)-",
    "anti-Delta(1905)--",
    "anti-Delta(1905)+",
    "anti-Delta(1905)0",
    "anti-Delta(1910)-",
    "anti-Delta(1910)--",
    "anti-Delta(1910)+",
    "anti-Delta(1910)0",
    "anti-Delta(1920)-",
    "anti-Delta(1920)--",
    "anti-Delta(1920)+",
    "anti-Delta(1920)0",
    "anti-Delta(1930)-",
    "anti-Delta(1930)--",
    "anti-Delta(1930)+",
    "anti-Delta(1930)0",
    "anti-Delta(1950)-",
    "anti-Delta(1950)--",
    "anti-Delta(1950)+",
    "anti-Delta(1950)0",
    "anti-Delta-",
    "anti-Delta--",
    "anti-Delta+",
    "anti-Delta0",
    "anti-K''*0",
    "anti-K'*0",
    "anti-K'_10",
    "anti-K*0",
    "anti-K*0T",
    "anti-K0",
    "anti-K_0*0",
    "anti-K_0*0N",
    "anti-K_10",
    "anti-K_2*0",
    "anti-Lambda(1405)0",
    "anti-Lambda(1520)0",
    "anti-Lambda(1600)0",
    "anti-Lambda(1670)0",
    "anti-Lambda(1690)0",
    "anti-Lambda(1800)0",
    "anti-Lambda(1810)0",
    "anti-Lambda(1820)0",
    "anti-Lambda(1830)0",
    "anti-Lambda(1890)0",
    "anti-Lambda0",
    "anti-Lambda_b0",
    "anti-Lambda_c(2593)-",
    "anti-Lambda_c(2625)-",
    "anti-Lambda_c-",
    "anti-N(1440)-",
    "anti-N(1440)0",
    "anti-N(1520)-",
    "anti-N(1520)0",
    "anti-N(1535)-",
    "anti-N(1535)0",
    "anti-N(1650)-",
    "anti-N(1650)0",
    "anti-N(1675)-",
    "anti-N(1675)0",
    "anti-N(1680)-",
    "anti-N(1680)0",
    "anti-N(1700)-",
    "anti-N(1700)0",
    "anti-N(1710)-",
    "anti-N(1710)0",
    "anti-N(1720)-",
    "anti-N(1720)0",
    "anti-N(1900)-",
    "anti-N(1900)0",
    "anti-N(1990)-",
    "anti-N(1990)0",
    "anti-N(2090)-",
    "anti-N(2090)0",
    "anti-N(2190)-",
    "anti-N(2190)0",
    "anti-Omega+",
    "anti-Omega_b*+",
    "anti-Omega_b+",
    "anti-Omega_c*0",
    "anti-Omega_c0",
    "anti-Omega_cc*-",
    "anti-Omega_cc-",
    "anti-Sigma(1660)0",
    "anti-Sigma(1670)0",
    "anti-Sigma(1750)-",
    "anti-Sigma(1750)+",
    "anti-Sigma(1750)0",
    "anti-Sigma(1775)-",
    "anti-Sigma(1775)+",
    "anti-Sigma(1775)0",
    "anti-Sigma*+",
    "anti-Sigma*-",
    "anti-Sigma*0",
    "anti-Sigma+",
    "anti-Sigma-",
    "anti-Sigma0",
    "anti-Sigma_b*+",
    "anti-Sigma_b*-",
    "anti-Sigma_b*0",
    "anti-Sigma_b+",
    "anti-Sigma_b-",
    "anti-Sigma_b0",
    "anti-Sigma_c*-",
    "anti-Sigma_c*--",
    "anti-Sigma_c*0",
    "anti-Sigma_c-",
    "anti-Sigma_c--",
    "anti-Sigma_c0",
    "anti-Xi'_b+",
    "anti-Xi'_b0",
    "anti-Xi'_c-",
    "anti-Xi'_c0",
    "anti-Xi*+",
    "anti-Xi*0",
    "anti-Xi+",
    "anti-Xi0",
    "anti-Xi_b*+",
    "anti-Xi_b*0",
    "anti-Xi_b+",
    "anti-Xi_b0",
    "anti-Xi_bc-",
    "anti-Xi_bc0",
    "anti-Xi_c-",
    "anti-Xi_c0",
    "anti-Xi_cc*-",
    "anti-Xi_cc*--",
    "anti-Xi_cc-",
    "anti-Xi_cc--",
    "anti-Xsd",
    "anti-Xss",
    "anti-Xsu",
    "anti-b",
    "anti-c",
    "anti-cc_1",
    "anti-cd_0",
    "anti-cd_1",
    "anti-cs_0",
    "anti-cs_1",
    "anti-cu_0",
    "anti-cu_1",
    "anti-d",
    "anti-n0",
    "anti-nu_e",
    "anti-nu_mu",
    "anti-nu_tau",
    "anti-p-",
    "anti-rndmflav",
    "anti-s",
    "anti-su_0",
    "anti-u",
    "anti-ud_0",
    "anti-ud_1",
    "anti-uu_1",
    "b",
    "b_1+",
    "b_1-",
    "b_10",
    "c",
    "c-hadron",
    "cc_1",
    "cd_0",
    "cd_1",
    "chi_b0",
    "chi_b0(2P)",
    "chi_b0(3P)",
    "chi_b1",
    "chi_b1(2P)",
    "chi_b1(3P)",
    "chi_b2",
    "chi_b2(2P)",
    "chi_b2(3P)",
    "chi_c0",
    "chi_c1",
    "chi_c2",
    "cs_0",
    "cs_1",
    "cu_0",
    "cu_1",
    "d",
    "e+",
    "e-",
    "eta",
    "eta'",
    "eta_b",
    "eta_b2(1D)",
    "eta_b2(2D)",
    "eta_c",
    "eta_c(2S)",
    "f'_0",
    "f'_1",
    "f'_2",
    "f_0",
    "f_0(1500)",
    "f_1",
    "f_2",
    "g",
    "gamma",
    "h'_1",
    "h_1",
    "h_b",
    "h_b(2P)",
    "h_b(3P)",
    "h_c",
    "mu+",
    "mu-",
    "n0",
    "nu_e",
    "nu_mu",
    "nu_tau",
    "omega",
    "omega(1650)",
    "omega(2S)",
    "p+",
    "phi",
    "phi(1680)",
    "pi+",
    "pi-",
    "pi0",
    "psi(2S)",
    "psi(3770)",
    "psi(4040)",
    "psi(4160)",
    "psi(4415)",
    "rho(2S)+",
    "rho(2S)-",
    "rho(2S)0",
    "rho(3S)+",
    "rho(3S)-",
    "rho(3S)0",
    "rho+",
    "rho-",
    "rho0",
    "rndmflav",
    "s",
    "specflav",
    "su_0",
    "su_1",
    "tau+",
    "tau-",
    "u",
    "ud_0",
    "ud_1",
    "uu_1",
]


# Sub-list of .dec particle names unkown to the PDG data table (the .mcd and our .csv files)
list_dec_but_not_in_pdt = [
    "B'_1+",
    "B'_1-",
    "B'_10",
    "B'_c1+",
    "B'_c1-",
    "B'_s10",
    "B_0*+",
    "B_0*-",
    "B_0*0",
    "B_1+",
    "B_1-",
    "B_10",
    "B_c*+",
    "B_c*-",
    "B_c0*+",
    "B_c0*-",
    "B_c1+",
    "B_c1-",
    "B_c2*+",
    "B_c2*-",
    "B_s0*0",
    "B_s10",
    "D'_1+",
    "D'_1-",
    "D'_10",
    "D(2S)+",
    "D(2S)-",
    "D(2S)0",
    "D*(2S)+",
    "D*(2S)-",
    "D*(2S)0",
    "D_1+",
    "D_1-",
    "D_10",
    "N(1900)+",
    "N(1900)0",
    "N(1990)+",
    "N(1990)0",
    "N(2090)+",
    "N(2090)0",
    "Omega_b*-",
    "Omega_cc*+",
    "Omega_cc+",
    "Sigma_b*0",
    "Sigma_b0",
    "Upsilon_1(1D)",
    "Upsilon_1(2D)",
    "Upsilon_2(1D)",
    "Upsilon_2(2D)",
    "Upsilon_3(1D)",
    "Upsilon_3(2D)",
    "X_1(3872)",
    "Xi'_b-",
    "Xi'_b0",
    "Xi_b*-",
    "Xi_b*0",
    "Xi_bc+",
    "Xi_bc0",
    "Xi_cc*+",
    "Xi_cc*++",
    "Xi_cc+",
    "Xi_cc++",
    "anti-B'_10",
    "anti-B'_s10",
    "anti-B_0*0",
    "anti-B_10",
    "anti-B_s0*0",
    "anti-B_s10",
    "anti-D'_10",
    "anti-D(2S)0",
    "anti-D*(2S)0",
    "anti-N(1900)-",
    "anti-N(1900)0",
    "anti-N(1990)-",
    "anti-N(1990)0",
    "anti-N(2090)-",
    "anti-N(2090)0",
    "anti-Omega_b*+",
    "anti-Omega_c*0",
    "anti-Omega_cc*-",
    "anti-Omega_cc-",
    "anti-Sigma_b*0",
    "anti-Sigma_b0",
    "anti-Xi'_b0",
    "anti-Xi'_b+",
    "anti-Xi_b*+",
    "anti-Xi_b*0",
    "anti-Xi_bc-",
    "anti-Xi_bc0",
    "anti-Xi_cc*-",
    "anti-Xi_cc*--",
    "anti-Xi_cc-",
    "anti-Xi_cc--",
    "chi_b0(3P)",
    "chi_b1(3P)",
    "chi_b2(3P)",
    "eta_b",
    "eta_b2(1D)",
    "eta_b2(2D)",
    "h_b(2P)",
    "h_b(3P)",
    "omega(2S)",
    "rho(3S)+",
    "rho(3S)-",
    "rho(3S)0",
]


# Sub-list of particle names specific to .dec files
list_dec_specific = [
    "K*0R",
    "K*0T",
    "K*BL",
    "K*BR",
    "K*BS",
    "K*L",
    "K*S",
    "K_0*0N",
    "Xsd",
    "Xss",
    "Xsu",
    "Xu+",
    "Xu-",
    "Xu0",
    "anti-K*0T",
    "anti-K_0*0N",
    "anti-rndmflav",
    "anti-cc_1",
    "anti-cd_0",
    "anti-cd_1",
    "anti-cs_0",
    "anti-cs_1",
    "anti-cu_0",
    "anti-cu_1",
    "anti-su_0",
    "anti-ud_0",
    "anti-ud_1",
    "anti-uu_1",
    "anti-Xsd",
    "anti-Xss",
    "anti-Xsu",
    "c-hadron",
    "cc_1",
    "cd_0",
    "cd_1",
    "cs_0",
    "cs_1",
    "cu_0",
    "cu_1",
    "su_0",
    "su_1",
    "ud_0",
    "ud_1",
    "uu_1",
    "rndmflav",
    "specflav",
]

for elm in list_dec_but_not_in_pdt + list_dec_specific:
    dec_names.remove(elm)


def test_decfile_style_names_valid():
    failures = set()
    for name in dec_names:
        try:
            assert Particle.from_evtgen_name(name).pdgid != 0
        except ParticleNotFound:
            failures.add(name)

    assert failures == set()
