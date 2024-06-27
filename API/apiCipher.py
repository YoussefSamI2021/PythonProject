from flask import Flask, request, jsonify
import json
from cipherCe import CaesarCipher as ca
    
    
app = Flask(__name__)



self_key ={"a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g": "j",
"h": "k","i": "l", "j": "m", "k": "n", "l": "o", "m": "p", "n": "q", "o":
"r", "p": "s","q": "t", "r": "u", "s": "v", "t": "w", "u": "x", "v": "y",
"w": "z", "x": "a","y": "b", "z": "c", " ":" "}

@app.route('/', methods=['GET'])
def cipher():
        data=request.args.to_dict()["params"]
        data_dict=json.loads(data)
        string=data_dict["string"]
        encrypt = data_dict["encrypt"]
        if "key" in data_dict:
                return jsonify(ca.get_cipher(string , data_dict["key"] , encrypt=encrypt))
        
        else:
                return jsonify(ca.get_cipher(string , self_key , encrypt=encrypt))


app.run()



