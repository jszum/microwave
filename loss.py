import matplotlib.pyplot as plt

frequencies = [100, 900, 2500, 5000, 10000, 20000]
distances = [500, 20000, 37000, 400000]

loss500    = [126, 145, 154, 160, 166, 172]
loss20000  = [158, 177, 186, 192, 196, 204]
loss37000  = [163, 182, 191, 197, 203, 209]
loss400000 = [184, 203, 212, 218, 224, 230]

fig = plt.figure()
fig.suptitle('Free-space losses')
ax = fig.add_subplot(111)

frequencies = [x / 1000.0 for x in frequencies]

ax.plot(frequencies, loss500,"ro-", label="500km", )
ax.plot(frequencies, loss20000,"bo-", label="20 000km", )
ax.plot(frequencies, loss37000,"go-", label="37 000km", )
ax.plot(frequencies, loss400000,"ko-", label="400 000km", )


ax.set_xlabel('Frequency [GHz]')
ax.set_ylabel('Losses [dB]')

ax.legend()
plt.show()
