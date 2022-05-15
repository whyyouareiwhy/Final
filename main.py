import numpy as np
import scipy.io.wavfile as wav
from pedalboard import Pedalboard, Chorus, Reverb
from pedalboard.io import AudioFile
import simpleaudio as sa

# TO DO
# 1 - record audio input
# 2 - guitar tuner
# 3 - add other effects
# 4 - web app


# take in audio signal, add reverb, write to "reverb_audio.wav"
def reverb(signal):
    echo_dur = 0.2  # can modify as arg parameter later
    delay_amp = 0.5  # can modify as arg parameter later

    fs, audio = wav.read(signal)

    delay_samples = round(echo_dur * fs)
    zero_padding = np.zeros(delay_samples)

    delay_padding = np.concatenate((zero_padding, audio))
    delayed_audio = np.concatenate((audio, zero_padding))
    reverb_audio = delayed_audio + delay_amp * delay_padding

    wav.write("reverb_audio.wav", fs, reverb_audio.astype(np.int16))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("Playing original...")
    wave_obj = sa.WaveObject.from_wave_file("gc.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

    reverb('gc.wav')

    print("Playing modified...")
    wave_obj = sa.WaveObject.from_wave_file("reverb_audio.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

    # Read in a whole audio file:
    # with AudioFile('gc.wav', 'r') as f:
    #     audio = f.read(f.frames)
    #     samplerate = f.samplerate

    # Make a Pedalboard object, containing multiple plugins:
    # board = Pedalboard([Chorus(), Reverb(room_size=0.15)])

    # Run the audio through this pedalboard!
    # effected = board(audio, samplerate)

    # Write the audio back as a wav file:
    # with AudioFile('processed-output.wav', 'w', samplerate, effected.shape[0]) as f:
    #     f.write(effected)

    # wave_obj = sa.WaveObject.from_wave_file('processed-output.wav')
    # play_obj = wave_obj.play()
    # play_obj.wait_done()
