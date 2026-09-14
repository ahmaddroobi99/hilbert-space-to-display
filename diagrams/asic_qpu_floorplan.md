# ASIC-style fridge floorplan

```
 300 K   HOST CPU/GPU     RFSoC / FPGA AWG          display / DAC
         compiler         14-bit DAC @ ~2 GSps      framebuffer
              |                   |
              |            IQ mixers + LO 4-10 GHz
              |
  50 K   ----------------------------------------------------------
              |           attenuators / IR filters
   4 K   ----------------------------------------------------------
              |           HEMT amp (readout going UP)
              |           optional cryo-CMOS DAC (control going DOWN)
 100 mK  ----------------------------------------------------------
              |           more attenuation
  10 mK  ==========================================================
              |           magnetic shield
              +-- transmon / spin / ion chip
                    XY drive line per qubit
                    Z / flux bias
                    readout resonator (freq multiplexed)
                    couplers
              THIS PLANE IS THE QPU
  10 mK  ==========================================================
```

Control ASICs at 3-4 K are still CMOS transistors.
The quantum processor is the isolated two-level modes at ~10 mK.
