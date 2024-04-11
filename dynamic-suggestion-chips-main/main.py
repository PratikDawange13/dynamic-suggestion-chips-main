from flask import Flask,request
from pprint import pprint
from sentencesep import separator
from chipgenrator import chipgenerator
app=Flask(__name__)

@app.route('/')
def add():
    return "this is webhook for suggetion "

@app.route('/city')
def add2():
    return "This is pratik web hook response"

@app.route('/city',methods=['POST'])
def hook():
    req=request.get_json(force=True)
    sessionInfo=req['sessionInfo']
    destination=req['sessionInfo']['parameters']['destination']
    session_name=req.get('sessionInfo').get('session')
    chip_list=(chipgenerator(destination))
    chip1,chip2,chip3=separator(chip_list)

    manydestination=   {
        "fulfillment_response":
            {
                "messages": [
                    
                    {
                        "payload": {
                        "botcopy": [
                            {
                            "suggestions": [
                                {
                                "action": {
                                    "message": {
                                    "command": "",
                                    "type": "training"
                                    }
                                },
                                "title": f'{chip1}'
                                },
                                {
                                "action": {
                                    "message": {
                                    "command": "",
                                    "type": "training"
                                    }
                                },
                                "title": f'{chip2}'
                                },
                                {
                                "action": {
                                    "message": {
                                    "command": "",
                                    "type": "training"
                                    }
                                },
                                "title": f'{chip3}'
                                }
                                #// Add more options as needed
                            ]
                            }
                        ]
                        }
                    }
                    ]
                },
                "session_info": {
                    "session": "session_name",
                    "parameters": {
                    "destination": None
                    }
                }
                }


    return manydestination


    """no_destination={
        "fulfillment_response":
            {
                "messages": [
                    {
                        "text": {
                            "text": [
                                f"This is your suggestion list {destination_list}, Please select one of the above."
                            ]
                        }
                    }
                ]
            },
        "session_info": {
            "session": session_name,
            "parameters": {
                "destination": None
            }
        },
       # "target_page": req.get('pageInfo').get("currentPage")  # Maintain current page
    }

    return no_destination"""

if __name__=="__main__":
    app.run(debug=True, port=3000)