import kinematika as kin

_F, _m = map(float, input("Upišite iznos sile[N] i mase[kg] razdvojene razmakom: ").split(" "))

kin.jednoliko_gibanje(_F, _m)
