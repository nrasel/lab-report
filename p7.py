import numpy as np
from scipy import stats


def calculate_statistics(data):
    mean = np.mean(data)
    median = np.median(data)
    mode = stats.mode(data).mode[0]
    std_dev = np.std(data)
    skewness = stats.skew(data)
    kurtosis = stats.kurtosis(data)
    
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Skewness: {skewness}")
    print(f"Kurtosis: {kurtosis}")


data = np.arange(1, 51)
calculate_statistics(data)












# Using R

# Load necessary library
# install.packages("e1071")
# library(e1071)

# # Function to calculate statistical measures
# calculate_statistics <- function(data) {
#   mean_val <- mean(data)
#   median_val <- median(data)
#   mode_val <- as.numeric(names(sort(-table(data)))[1])
#   std_dev_val <- sd(data)
#   skewness_val <- skewness(data)
#   kurtosis_val <- kurtosis(data)
  
#   cat("Mean:", mean_val, "\n")
#   cat("Median:", median_val, "\n")
#   cat("Mode:", mode_val, "\n")
#   cat("Standard Deviation:", std_dev_val, "\n")
#   cat("Skewness:", skewness_val, "\n")
#   cat("Kurtosis:", kurtosis_val, "\n")
# }

# # Applying the function to the first 50 natural numbers
# data <- 1:50
# calculate_statistics(data)