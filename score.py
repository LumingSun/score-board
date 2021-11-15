from sklearn.metrics import mean_squared_log_error
import numpy as np
def scoring(csv_file,label_file='/home/slm/web/label_result.csv'):
    try:
        test = np.loadtxt(csv_file, delimiter=",", skiprows=1)
        label = np.loadtxt(label_file, delimiter=",", skiprows=1)
        test_data = test[:,1].reshape(2000,1)
        label_data = label[:,1].reshape(2000,1)
        score = np.sqrt(mean_squared_log_error(test_data, label_data))
        if(score==0):
            return "Warning"
        else:
            return score
    except:
        return False
# if __name__=='__main__':
#     print(scoring('./label_result.csv','./label_result.csv'))