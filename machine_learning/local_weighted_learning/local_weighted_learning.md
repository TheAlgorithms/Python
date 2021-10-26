# Locally Weighted Linear Regression
It is a non-parametric ML algorithm that does not learn on a fixed set of parameters such as **linear regression**. \
So, here comes a question of what is *linear regression*? \
**Linear regression** is a supervised learning algorithm used for computing linear relationships between input (X) and output (Y). \

### Terminology Involved

number_of_features(i) = Number of features involved. \
number_of_training_examples(m) = Number of training examples. \
output_sequence(y) = Output Sequence. \
$\theta$ $^T$ x = predicted point. \
J($\theta$) = COst function of point.

The steps involved in ordinary linear regression are:

Training phase: Compute \theta to minimize the cost. \
J($\theta$) = $\sum_{i=1}^m$ (($\theta$)$^T$ $x^i$ - $y^i$)$^2$

Predict output: for given query point x, \
 return:  ($\theta$)$^T$ x

<img src="https://miro.medium.com/max/700/1*FZsLp8yTULf77qrp0Qd91g.png" alt="Linear Regression">

This training phase is possible when data points are linear, but there again comes a question can we predict non-linear relationship between x and y ? as shown below

<img src="https://miro.medium.com/max/700/1*DHYvJg55uN-Kj8jHaxDKvQ.png" alt="Non-linear Data">
<br />
<br />
So, here comes the role of non-parametric algorithm which doesn't compute predictions based on fixed set of params. Rather parameters $\theta$ are computed individually for each query point/data point x.
<br />
<br />
While Computing $\theta$ , a higher "preferance" is given to points in the vicinity of x than points farther from x.

Cost Function J($\theta$) = $\sum_{i=1}^m$ $w^i$ (($\theta$)$^T$ $x^i$ - $y^i$)$^2$

$w^i$ is non-negative weight associated to training point $x^i$. \
$w^i$ is large fr $x^i$'s lying closer to query point $x_i$. \
$w^i$ is small for $x^i$'s lying farther to query point $x_i$.

A Typical weight can be computed using \

$w^i$ = $\exp$(-$\frac{(x^i-x)(x^i-x)^T}{2\tau^2}$)

Where $\tau$ is the bandwidth parameter that controls $w^i$ distance from x.

Let's look at a example :

Suppose, we had a query point x=5.0 and training points $x^1$=4.9 and $x^2$=5.0 than we can calculate weights as :

$w^i$ = $\exp$(-$\frac{(x^i-x)(x^i-x)^T}{2\tau^2}$) with $\tau$=0.5

$w^1$ = $\exp$(-$\frac{(4.9-5)^2}{2(0.5)^2}$) = 0.9802

$w^2$ = $\exp$(-$\frac{(3-5)^2}{2(0.5)^2}$) = 0.000335

So, J($\theta$) = 0.9802*($\theta$ $^T$ $x^1$ - $y^1$) + 0.000335*($\theta$ $^T$ $x^2$ - $y^2$)

So, here by we can conclude that the weight fall exponentially as the distance between x & $x^i$ increases and So, does the contribution of error in prediction for $x^i$ to the cost.

Steps involved in LWL are : \
Compute \theta to minimize the cost.
J($\theta$) = $\sum_{i=1}^m$ $w^i$ (($\theta$)$^T$ $x^i$ - $y^i$)$^2$ \
Predict Output: for given query point x, \
return : $\theta$ $^T$ x

<img src="https://miro.medium.com/max/700/1*H3QS05Q1GJtY-tiBL00iug.png" alt="LWL">
