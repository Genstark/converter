def spectogram_librosa(wav_file):
    import librosa
    import pylab
    import numpy as np

    (sig, rate) = librosa.load(wav_file, sr=32000, mono=True,  duration=1, dtype=np.float32)
    name = pylab.specgram(sig, Fs=rate)
    pylab.savefig('spectrogram.jpg')

spectogram_librosa("car.wav")