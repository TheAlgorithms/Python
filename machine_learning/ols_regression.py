import pandas
!wget https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/graphing.py
!wget https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/doggy-boot-harness.csv

# Dictionary of boot sizes
data = {
    "boot_size":[39, 38, 37, 39, 38, 35, 37, 36, 35, 40, 
                    40, 36, 38, 39, 42, 42, 36, 36, 35, 41, 
                    42, 38, 37, 35, 40, 36, 35, 39, 41, 37, 
                    35, 41, 39, 41, 42, 42, 36, 37, 37, 39,
                    42, 35, 36, 41, 41, 41, 39, 39, 35, 39],
    
    "harness_size":[58, 58, 52, 58, 57, 52, 55, 53, 49, 54,
                59, 56, 53, 58, 57, 58, 56, 51, 50, 59,
                59, 59, 55, 50, 55, 52, 53, 54, 61, 56,
                55, 60, 57, 56, 61, 58, 53, 57, 57, 55,
                60, 51, 52, 56, 55, 57, 58, 57, 51, 59]
}

import pandas as pd
df = pd.DataFrame(data)
df


# Selecting a model
import statsmodels.formula.api as smf

formula = "boot_size ~ harness_size"

# Create the model without training it 
model = smf.ols(formula = formula, data = df)

# We have created our model but it lacks internal parameters
if not hasattr(model, "params"):
    print("Model selected but lacks internal parameters. We need to train it")
 


# Model Training
import graphing

# Train the model so that it creates a line that fits our data 
fitted_model = model.fit()

print("The following model parameters have been found:\n" +
      f"Line slope:{fitted_model.params[1]}\n" +
      f"Line intercept: {fitted_model.params[0]}"
     )




# Show a graph of the result
graphing.scatter_2D(df, label_x = "harness_size",
                        label_y = "boot_size",
                        trendline = lambda x: fitted_model.params[1]*x + fitted_model.params[0]
                   )




# Model in production
harness_size = {"harness_size":[52.5]}

# Use the model to predict what size of boots the dog will fit
approximate_boot_size = fitted_model.predict(harness_size)

# Print the result
print("Estimated approximate_boot_size:")
print(approximate_boot_size[0])
