import matplotlib.pyplot as plt

range = list(range(1, 11))
x_ticks = ["08:00 AM", "09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "01:00 PM", "02:00 PM", "03:00 PM", "04:00 PM", "05:00 PM"]
xbar = [204.8, 206.4, 206.8, 204.4, 205.2, 204.4, 203.6, 204.0, 205.4, 206.2]
R = [4, 4, 3, 4, 8, 9, 7, 10, 10, 7]

mean_xbar = 205.1
mean_R = 6.6

ucl_xbar = 208.91
lcl_xbar = 201.29

ucl_R = 13.95
lcl_R = 0

plt.plot(range, xbar, "bo-", label=r"$\bar{x}$")
plt.plot(range, [mean_xbar]*10, "r-", label=r"$\bar{\bar{x}}$")
plt.plot(range, [ucl_xbar]*10, "r--", label=r"UCL")
plt.plot(range, [lcl_xbar]*10, "g--", label=r"LCL")
plt.xticks(range, x_ticks)
plt.xlabel("Time")
plt.ylabel(r"$\bar{x}$")
plt.title(r"$\bar{x}$ Chart")
plt.legend()

plt.show()

plt.plot(range, R, "bo-", label=r"$R$")
plt.plot(range, [mean_R]*10, "r-", label=r"$\bar{R}$")
plt.plot(range, [ucl_R]*10, "r--", label=r"UCL")
plt.plot(range, [lcl_R]*10, "g--", label=r"LCL")
plt.xticks(range, x_ticks)
plt.xlabel("Time")
plt.ylabel(r"$R$")
plt.title(r"$R$ Chart")
plt.legend()

plt.show()
