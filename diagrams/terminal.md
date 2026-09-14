# Terminal diagrams

## 1. Input to QPU to display

```
 WORLD  camera / LiDAR / IMU / GPS / 5G / mic
   |    analog voltages  (Maxwell / huge-occupation photon field)
   v
  ADC   Nyquist samples  ->  classical bits
   |
   v
 HOST   CPU / GPU / FPGA compiler   (DFS/BFS/A*, CNN, transformer)
   |    circuit  ->  pulse schedule
   v
  DAC + IQ mixer + LO   4-10 GHz envelopes
   |
   v   attenuators @ 50K / 4K / 100mK
+--------------------------------------------------+
|  QPU  ~10 mK                                     |
|    |psi> in (C^2)^n                              |
|    U(t) = T exp(-i integral H(t) dt / hbar)      |
|    superposition = ONE vector a|0> + b|1>        |
|    NOT two voltages on one wire                  |
+--------------------------------------------------+
   |
   v   dispersive readout -> HEMT/JPA
  ADC   I/Q blobs  ->  state discrimination
   |
   v
 HOST   shot histogram ~ Born PDF
   |
   v
 DISPLAY  framebuffer DAC  ->  photons to eye
```

## 2. Why you cannot stream 0 and 1 at once

```
 classical bit line     5V -------- 0V -------- 5V
                        [  1  ]     [  0  ]     [  1  ]

 qubit state            |psi> = a|0> + b|1>     in  C^2
                        measurement  ->  ONE bit
                        P(0)=|a|^2   P(1)=|b|^2
```

## 3. Generator pattern (Ch 12-14)

```
 transformation     unitary group                 Hermitian generator
 time t             U(t) = exp(-i H t / hbar)     H   energy
 space a            T(a) = exp(-i p a / hbar)     p   momentum = -i hbar d/dx
 angle theta        R(th)= exp(-i L th / hbar)    L   angular momentum
```

## 4. Chapter chain

```
 Ch1 LA -> Ch2 kets/psi -> Ch3 H -> Ch4 inner product -> Ch5 delta -> Ch6 bras
    -> Ch7 A-hat -> Ch8 |c|^2 -> Ch9 Hermitian -> Ch10 [A,B] -> Ch11 U
    -> Ch12 generators -> Ch13 i hbar dt = H -> Ch14 p = -i hbar d/dx
                         \                \
                          \                -> QPU pulses
                           -> Born readout -> classical display
```
