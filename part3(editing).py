y_model_at_data = oscillatory_function(x_data, *params)
residuals = y_data - y_model_at_data

std_dev = np.std(residuals)
print(f"Standard Deviation of Residuals: {std_dev:.4f} ft")

if std_dev > y_err:
    intrinsic_scatter = np.sqrt(std_dev**2 - y_err**2)
    print(f"Intrinsic Scatter: {intrinsic_scatter:.4f} ft")
else:
    print("Intrinsic Scatter: 0 (Data scatter is consistent with measurement error)")

plt.figure(figsize=(8, 6))
plt.hist(residuals, bins=15, edgecolor='black', alpha=0.7, density=True, label='Residuals')
plt.xlabel('Residuals (ft)')
plt.ylabel('Probability Density')
plt.title('Histogram of Tidal Residuals')
plt.legend()
plt.savefig('residuals_histogram.png')
plt.show()
