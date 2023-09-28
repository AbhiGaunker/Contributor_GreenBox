import logging
import time
logging.basicConfig(filename="main.log" , level=logging.INFO)


if __name__=="__main__":
    logging.info(f'last ran time: {time.strftime("%H:%M:%S")}\n')
