# Indoor RF Signal Simulation

This repository attempts to simulate the environment of the following research paper:

Adib et al., (2015). Multi-Person Localization via RF Body Reflections. _12th USENIX Symposium on Networked Systems
Design and Implementation (NSDI ’15)_. Available [here](https://www.usenix.org/system/files/conference/nsdi15/nsdi15-paper-adib.pdf)

In specific, we assume that the transmitter antennas generate a wide-band sweep and the received signals are mixed with the reference
signal to generate baseband. The baseband signal is then analyzed to localize objects in 3-d space.
