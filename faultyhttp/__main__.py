import argparse
import random
import time
from flask import Flask
app = Flask(__name__)


@app.route('/bad/timeout/<n>')
def timeout(n):
    """
    Wait n seconds before returning ok
    :param rid:
    :return:
    """
    time.sleep(int(n))
    return 'ok', 200


@app.route('/bad/http/<rid>')
def hello_world(rid):
    flip = random.random() < app.config['args'].probability
    if flip:
        print("FAIL: {}".format(rid))
        return 'Error', app.config['args'].code

    print("OK  : {}".format(rid))
    return 'ok', 200


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--code', help="Code to return randomly", default=500, type=int)
    parser.add_argument('-n', '--probability', help="", default=0.1, type=float)

    args = parser.parse_args()
    app.config['args'] = args

    app.run()