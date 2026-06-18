import os 
from dotenv import load_dotenv
from data.data import get_df

load_dotenv()
train_url = os.getenv('TRAINING_DATA_URL')
def main():

    df = get_df(train_url)

    print(df)

if __name__ == "__main__":
    main()