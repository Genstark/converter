import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 2  # Duration of recording

myrecording = sd.rec(int(fs * seconds), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished

# Save the recording to a WAV file
write("recorded.wav", fs, myrecording)