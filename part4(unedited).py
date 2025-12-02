tsunami_deviation = 2.0 # ft
sigma_deviations = tsunami_deviation / std_dev

print("\n" + "="*30)
print(f"Tsunami Analysis:")
print(f"A {tsunami_deviation} ft deviation represents a {sigma_deviations:.2f} sigma event.")
print("="*30 + "\n")

residuals_with_outlier = np.append(residuals, tsunami_deviation)

plt.figure(figsize=(8, 6))
plt.hist(residuals_with_outlier, bins=20, edgecolor='black', alpha=0.7, color='green', label='Residuals + Tsunami')
plt.xlabel('Residuals (ft)')
plt.ylabel('Frequency')
plt.title('Residuals Histogram with Tsunami Outlier')
plt.annotate('Tsunami Outlier', xy=(2.0, 1), xytext=(0.5, 5),
             arrowprops=dict(facecolor='red', shrink=0.05))
plt.legend()
plt.savefig('residuals_histogram with tsunami outlier.png')
plt.show()
