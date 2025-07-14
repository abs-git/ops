import os
import mlflow

def main():

    user = 'donghyun'
    pw = 'donghyun'

    mlflow.set_tracking_uri(f"http://{user}:{pw}@localhost:8080")




if __name__=='__main__':
    main()