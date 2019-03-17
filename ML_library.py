class mlSkies:
   

    def train_test_split(a,b,split_index=0.2):
        a_train=[]
        b_train=[]
        a_test=[]
        b_test=[]
        a_train=a[0:int((len(a)*(1-split_index)))]
        b_train=b[0:int((len(b)*(1-split_index)))]
        a_test=a[len(a_train):len(a)]
        b_test=b[len(b_train):len(b)]
        return a_train,a_test,b_train,b_test
    
    def linear_regression(X_train,y_train):
        from statistics import mean
        a=X_train
        b=y_train
        m=( ( (mean(a))*mean(b)) - (mean(a*b))) / (
                (mean(a)**2)-(mean(a*a)))
        b= mean(b)-m*mean(a)
        return m, b

    def plot_regression_line(X_train,y_train,slope,intercept):
        import matplotlib.pyplot as plt
        regression_line=[(slope*i)+intercept for i in X_train]
        plt.plot(X_train, regression_line)
        plt.scatter(X_train,y_train)    
        plt.show()

    def linear_regression_predict(Value_of_independent_variable_to_be_predicted , slope,intercept):
        return (slope*Value_of_independent_variable_to_be_predicted) + intercept


    def train_test_split(X,y,split_index=0.2):
        a=X
        b=y
        a_train=[]
        b_train=[]
        a_test=[]
        b_test=[]
        a_train=a[0:int((len(a)*(1-split_index)))]
        b_train=b[0:int((len(b)*(1-split_index)))]
        a_test=a[len(a_train):len(a)]
        b_test=b[len(b_train):len(b)]
        return a_train,a_test,b_train,b_test

    def standard_scaler(c):
        sum_1=0
        for i in range(0,len(c)):
            sum_1=sum_1+c[i]
        avg=sum_1/len(c)
        for j in range(0,len(c)):
            c[j]=c[j]/avg
        return avg
    
        
    