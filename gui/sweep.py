import numpy as np
from scipy import signal

class Simulator(object):

    """Simulates multiple sweeps and extracts movement. """

    def __init__(self, sfreqs, vfreqs, sintens, vintens, sweeps=None, noise=25, samples=500):
        """Initialize parameters."""
        self.sfreqs = sfreqs
        self.vfreqs = vfreqs
        self.sintens = sintens
        self.vintens = vintens
        self.noise = noise
        self.samples = samples
        self._set_static()

    def _set_static(self):
        x = np.linspace(-np.pi, np.pi, self.samples)
        self.static = np.zeros(self.samples)
        
        for i,f in zip(self.sintens, self.sfreqs):
            self.static += i*np.sin(f*x)
        
        noise = np.random.normal(0, 1, self.samples)
        self.static += 25 * noise

    def simulate_mixer(self):
        x = np.linspace(-np.pi, np.pi, self.samples)
        self.basebands = [self.static + (self.vintens * np.sin(f*x)) for f in self.vfreqs]  
        return self.basebands
    
    def _add_diffs(self):
        ffts = [np.abs(np.fft.rfft(b)) for b in self.basebands]
        diffs = np.zeros(len(ffts[0]))

        for i in range(0, len(ffts) - 1):
            diffs += np.abs(ffts[i+1] - ffts[i])
        
        return diffs
       
    def extract_movement(self):
        self.simulate_mixer()
        return self._add_diffs()

#fmcw = Simulator([20, 30, 40, 45], [15, 18, 22, 24, 27], [85, 35, 25, 20], 40)
#baseband = fmcw.extract_movement()

#from matplotlib import pyplot as plt
#plt.plot(baseband)
#plt.show()
