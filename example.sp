*title: delay meas.
.option brief nopage nomod post=1 ingold=2 autostop
.inc '../rohmlib/model_rohm180.sp'
.inc '../rohmlib/ROHM18INVP010.sp'
.temp 25.0
.param _vdd = 1.8
.param _vss = 0.0
.param _vnw = 1.8
.param _vpw = 0.0
.param cap = 10f 
.param slew = 100p 
.param _tslew = slew
.param _tstart = slew
.param _tend = '_tstart + _tslew'
.param _tsimend = '_tslew * 20 * 1' 
.param _Energy_meas_end_extent = 10.0
 
VDD_DYN VDD_DYN 0 DC '_vdd' 
VSS_DYN VSS_DYN 0 DC '_vss' 
VNW_DYN VNW_DYN 0 DC '_vnw' 
VPW_DYN VPW_DYN 0 DC '_vpw' 
* output load calculation
VOCAP VOUT WOUT DC 0
 
.tran 0.01ns '_tsimend'
 
VIN VIN 0 PWL(1p '_vss' '_tstart' '_vss' '_tend' '_vdd' '_tsimend' '_vdd') 
VHIGH VHIGH 0 DC '_vdd' 
VLOW VLOW 0 DC '_vss' 
** Delay 
* Prop delay 
.measure Tran PROP_IN_OUT trig v(VIN) val='0.9*1' rise=1 
+ targ v(VOUT) val='0.9*1' fall=1 
* Trans delay 
.measure Tran TRANS_OUT trig v(VOUT) val='1.4400000000000002*1' fall=1
+ targ v(VOUT) val='0.36000000000000004*1' fall=1 
.param ENERGY_START = 1.68333e-10
.param ENERGY_END = 3.39815e-10
* 
** In/Out Q, Capacitance 
* 
.measure Tran Q_IN_DYN integ i(VIN) from='ENERGY_START' to='ENERGY_END'  
.measure Tran Q_OUT_DYN integ i(VOCAP) from='ENERGY_START' to='ENERGY_END*_Energy_meas_end_extent' 
 
* 
** Energy 
*  (Total charge, Short-Circuit Charge) 
.measure Tran Q_VDD_DYN integ i(VDD_DYN) from='ENERGY_START' to='ENERGY_END*_Energy_meas_end_extent'  
.measure Tran Q_VSS_DYN integ i(VSS_DYN) from='ENERGY_START' to='ENERGY_END*_Energy_meas_end_extent'  
 
* Leakage current 
.measure Tran I_VDD_LEAK avg i(VDD_DYN) from='_tstart*0.1' to='_tstart'  
.measure Tran I_VSS_LEAK avg i(VSS_DYN) from='_tstart*0.1' to='_tstart'  
 
* Gate leak current 
.measure Tran I_IN_LEAK avg i(VIN) from='_tstart*0.1' to='_tstart'  
*comment out .control for ngspice batch mode 
*.control 
*run 
.print tran V(VIN) V(VOUT) 
*.endc 
XINV VIN VOUT VHIGH VLOW VDD_DYN VSS_DYN VNW_DYN VPW_DYN DUT 
C0 WOUT VSS_DYN 'cap'
 
.SUBCKT DUT IN OUT HIGH LOW VDD VSS VNW VPW 
XDUT IN OUT VDD VSS VNW VPW ROHM18INVP010
.ends 
 
.param cap =1e-14
.param slew =1.6666666666666666e-10
.end 
