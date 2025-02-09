from flask import Flask, request
from message_parser import MessageReceived
from message_sender import Send

app = Flask(__name__)

@app.route("/messages-upsert", methods=['POST'])
def webhook():

    try:
        data = request.get_json()        
        msg = MessageReceived(data) 
        print(msg.text_message)        
                            
        #send = Send()
        #send.textMessage(number=msg.phone,msg=msg.text_message)

    except:
        print("Erro")
    
        
    return ""
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



