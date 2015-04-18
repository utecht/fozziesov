from database import session, Stratop, Battle, ControlNode, CorpStatus, Event, System, SystemCorps
from flask import Flask, request, make_response
import json

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
    ret = {
        'battles': [{
            'sysname': 'GE-8JV',
            'structname': 'Station',
            'nodes': [{'name': 'NODE A', 'control': 'BRAVE'},
                      {'name': 'NODE B', 'control': None},
                      {'name': 'NODE C', 'control': 'TEST'}
                     ]
            }],
        'status': {
            'corps':  [{'name': 'TEST Alliance Please Ignore', 'num': 584},
                       {'name': 'Brave Collective', 'num': 947} 
                      ],
            'events': [{'text': 'Cyno in SV-5'},
                       {'text': 'Brave fleet moving to SV-5'}
                        
                      ]},
        'systems': [
               {'name': 'GE-8JV',
                'corps': [{'name': 'TEST Alliance Please Ignore', 'num': 84},
                          {'name': 'Brave Collective', 'num': 124} 
                          ],
                'events': [{'time': '21:43', 'text': 'dscan paste'},
                           {'time': '21:38', 'text': 'dscan paste'},
                           {'time': '20:23', 'text': 'dscan paste'}
                           ]
                }
        ]}

    return json.dumps(ret)

@app.route('/setuser')
def setuser():
    # session.query(Stratop).filter_by(
    resp = make_response("eh?")
    resp.set_cookie('stratop', '1')
    return resp

@app.route('/removeuser')
def removeuser():
    resp = make_response("eh?")
    resp.set_cookie('stratop', '')
    return resp



@app.route('/update', methods=['POST', 'GET'])
def update():
    op_id = request.cookies.get('stratop')
    if not op_id:
        return json.dumps({'error': 'User not logged in!'})

    op = session.query(Stratop).filter_by(id=op_id).first()
    # ret = {
    return "User: {}".format(op.constellation)
    


@app.route('/publish', methods=['POST'])
def publish():
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
