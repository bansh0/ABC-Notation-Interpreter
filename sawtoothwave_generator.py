import numpy as np
from scipy import signal as sg
from pysinewave import SineWaveGenerator
from pysinewave import utilities

class SawtoothWaveGenerator(SineWaveGenerator):
    #Modified from sinewave_generator from pysinewave by daviddavini

    def next_data(self, frames):
        '''Get the next pressure array for the given number of frames'''

        # Convert frame information to time information
        time_array = utilities.frames_to_time_array(0, frames, self.samplerate)
        delta_time = time_array[1] - time_array[0]

        # Calculate the frequencies of this batch of data
        new_frequency_array = self.new_frequency_array(time_array)

        # Calculate the phases
        new_phase_array = self.new_phase_array(new_frequency_array, delta_time)

        # Calculate the amplitudes
        new_amplitude_array = self.new_amplitude_array(time_array)

        # Create the sawtoothwave array
        sawtoothwave_array = new_amplitude_array * sg.sawtooth(2*np.pi*new_phase_array)
        
        # Update frequency and amplitude
        self.frequency = new_frequency_array[-1]
        self.amplitude = new_amplitude_array[-1]

        # Update phase (getting rid of extra cycles, so we don't eventually have an overflow error)
        self.phase = new_phase_array[-1] % 1

        #print('Frequency: {0} Phase: {1} Amplitude: {2}'.format(self.frequency, self.phase, self.amplitude))

        return sawtoothwave_array