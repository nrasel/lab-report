

def sum_of_cubes(n):
    sum = 0
    for i in range(1, n + 1):
        # print(i)

        sum += i * i*i
        
    return sum



print(sum_of_cubes(99))

# (1/1)^3*(1/3)^3*.....+(1/9)^3*




def product_of_series():
    product = 1  
    for i in range(1, 7, 2):  
        print(i)
        product *= (1 / i) ** 3  
    return product


result = product_of_series()
print(f"Product of the series: {result}")



# Using R programming
# Function to calculate the sum of cubes
# sum_of_cubes <- function(n) {
#   sum <- 0
#   for (i in 1:n) {
#     sum <- sum + (i^3)
#   }
#   return(sum)
# }

# # Driver function
# print(sum_of_cubes(99))


# # Function to calculate the product of the series
# product_of_series <- function() {
#   product <- 1  # Start with product = 1
#   for (i in seq(1, 7, by = 2)) {  # Iterate over odd numbers from 1 to 7
#     product <- product * (1 / i)^3  # Multiply by (1/i)^3
#   }
#   return(product)
# }

# # Calculate the result
# result <- product_of_series()
# cat("Product of the series:", result, "\n")