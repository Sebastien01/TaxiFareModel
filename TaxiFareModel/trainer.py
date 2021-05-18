from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from TaxiFareModel.encoders import DistanceTransformer,TimeFeaturesEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
import numpy as np
from TaxiFareModel.data import *
from sklearn.model_selection import train_test_split

class Trainer():
    def __init__(self, X, y):
        """
            X: pandas DataFrame
            y: pandas Series
        """
        self.pipe = None
        self.X = X
        self.y = y

    def set_pipeline(self):
        """defines the pipeline as a class attribute"""
        # create distance pipeline
        self.dist_pipe = Pipeline([
            ('dist_trans', DistanceTransformer()),
            ('stdscaler', StandardScaler())])
        
        # create time pipeline
        self.time_pipe = Pipeline([
            ('time_enc', TimeFeaturesEncoder('pickup_datetime')),
            ('ohe', OneHotEncoder(handle_unknown='ignore'))])

        # create preprocessing pipeline
        self.preproc_pipe = ColumnTransformer([
            ('distance', self.dist_pipe, ["pickup_latitude", "pickup_longitude", 'dropoff_latitude', 'dropoff_longitude']),
            ('time', self.time_pipe, ['pickup_datetime'])], remainder="drop")
        
        self.pipe = Pipeline([
            ('preproc', self.preproc_pipe),
            ('linear_model', LinearRegression())])
        return self
        
    def run(self):
        """set and train the pipeline"""
        self.set_pipeline()
        self.pipe.fit(self.X,self.y)

    def evaluate(self, X_test, y_test):
        """evaluates the pipeline on df_test and return the RMSE"""
        self.y_pred = self.pipe.predict(X_test)
        self.score = np.sqrt(((self.y_pred - y_test)**2).mean())
        return self.score


if __name__ == "__main__":
    
    data = get_data() # get data
    
    data = clean_data(data) # clean data
    
    y = data.pop("fare_amount") # set X and y
    X = data 
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) # hold out
    
    model = Trainer(X_train,y_train) # train
    model.run()
    
    model.evaluate(X_test,y_test) # evaluate
    print(f'Model score RMSE : {model.score}')
    print('Done')
