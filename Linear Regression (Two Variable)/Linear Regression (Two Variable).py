## Linear Regression for one Varible

import matplotlib.pyplot as plt


## Hypothesis function
def h(x,i,m):
    return m*x[i][1]+b


## Cost Function
def cost(j,m):
    prediction=[]
    sum=0
    
    for i in range(n):
        temp=h(x,i,m)
        prediction.append(temp)
        sum=sum+(temp-y[i])*x[i][j];
    avg=sum/n
    
    return avg,prediction

#GradientDecent
def gradient(m,b,alpha,iteration):
    Prediction=[0,0,0,0]
    x2=[5,10,15,20]
    
    for i in range(iteration):
        
        #plots for visualizing how our Best line improved
        plt.scatter(x2,y)               ## actual data
        plt.plot(x2,Prediction)         ## our prediction line
        plt.show()
        
        t0,Prediction=cost(0,m)         
        t1,Prediction=cost(1,m)
        
        b=b-alpha*t0
        m=m-alpha*t1

## This function will call GradientDecent
def fit(m,b,alpha,iteration):
    gradient(m,b,alpha,iteration)


##  (Training examples), 
    
x=[[1,5],[1,10],[1,15],[1,20]]  ## x is our input
y=[10,20,30,40]                 ## y is our label

n=len(x)                        ## n is our total training examples

m=0                             ## m is our parameter (theta1)
b=0                             ## b is our y intercept (theta0)
alpha=0.01                      ## alpha is our learning rate
iteration=50                    ## total iteration for gradient decent. increase the number for long dataset


#calling fit method to train our model
fit(m,b,alpha,iteration)