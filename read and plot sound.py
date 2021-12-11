from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# read audio samples
input_data = read("D:\jest\MSU\BSECE 3RD YEAR\ECE120-E16-3 Digital Signal Processing\python work\music files\Moonshining.wav")
audio = input_data[1]

# plot the first 1024 samples
plt.plot(audio[0:124])

# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time")
# set the title  
#plt.title(" basta")
# display the plot
plt.show()