﻿Caesar Cipher 

Overview 

T he Caesar cipher is a simple encryption technique t hat was used by J ulius Caesar to send 
secret messages to his allies. 

Your j ob would be to construct a Caesar Cipher package that would be implemented into 
an A PI to call 

steps 

This proj ect would be divided into two main steps; building the package and the A PI 

NOTE: You can use any logic you see suits, I only provide you with some 
helpful steps, what matters to me is to build the package as OOP, install 
it and then use it’s function as input to the A PI route 
﻿First; the package: 

Implement Caesar Cipher in OOP paradigm as follows; 

Your class should contain the following methods and attributes: 

    1.  Constructor that takes the key that maps the input to the output: 
            a.  Self.key: a dictionary mapping each letter to another letter in the vocab. 
            b.  Self.antikey: a dict with a swapped values/keys of self.key 

                For example key={“a”: “l”, …} then antikey={“l”: “a”, …} 

                Where key would be used to encry pt and antikey would be used to decy pt 

    2.  encry pt_string(string): Method that takes the the message you want to encry pt and 
        returns it as encry pted 

                for example; caesar.encry pt_string(‘ Hi”) ⇒ ul where h=u and i=l and so on 
                based on your key 

    3.  decry pt_string(string): Method that takes an encry pted string and tries to decry pt it 

                for example; caesar.decry pt_string(‘ul”) ⇒ hi where h=u and i=l and so on 
                based on your key 

    4.  check_input(string): method that checks for input text validity if it contains only 
        alphabets and spaces or not, so for example if string has “@” sign it would raise a 
        ValueError telling that it’s not valid input, only alphabets and spaces allowed. 

In another module in the same package, call the CaeserCipher class and wrap all the logic 
into a function to be used directly in the api; so this function should look like this: 

get_cipher(string, key=None, encrypt=True), where: 

String: is the string that you want either to encry pt or decry pt 

Key: the key dictionary that maps between letters, it has default value of None so if the 
user didn’t provide an explicit key you can use the default key; 

{"a" :  "d",   "b" :  "e",   "c" :  "f",   "d" : "g",   "e" :  "h",   "f" :  "i",  "g" :  "j", 

"h" :  "k","i" :   "l",   "j" :  "m",   "k" :  "n",  "l" :  "o",   "m" :  "p",   "n" :  "q",  "o" : 

"r",   "p" :  "s","q" :   "t",   "r" :  "u",   "s" : "v",   "t" :  "w",   "u" :  "x",   "v" : "y", 

"w" :  "z",   "x" :  "a","y" :   "b",   "z" :  "c",  "  " :"  "} 

encrypt: boolean ﬂag to direct the function; if True then encry pt this text; if False then 
decry pt this text 

Using all this build a package that only uses this get_cipher function and does all the magic 
﻿Second the A PI: 

Build a simple GET api that takes the pay load from the user with the parameters as a 
dictionary and returns the result; 

So the ﬁnal requirement of this proj ect is as follows: 

     1)  The user sends a request to the api with the data required and get his results 
    2)   Here are 4 examples of how I used the api as a ﬁnal result: 

         ahmed_elbaqary@A hmed-Elbaqary:~$ curl -G "http://127.0.0.1:5000/" 
         --data-urlencode 'params={"string":"Hello Data Engineers","encry pt":true}' 

         { 

          "result": "khoor gdwd hqj lqhhuv" 

         } 

         ============================================================== 

         ahmed_elbaqary@A hmed-Elbaqary:~$ curl -G "http://127.0.0.1:5000/" 
         --data-urlencode 'params={"string":"khoor gdwd hqj lqhhuv","encry pt":false}' 

         { 

          "result": "hello data engineers" 

         } 

         ============================================================== 

         ahmed_elbaqary@A hmed-Elbaqary:~$ curl -G "http://127.0.0.1:5000/" 
         --data-urlencode 'params={"string":"Hello Data Engineers this is if you want to use a 
         key I deﬁned it manually for test","encry pt":true, "key": {"a": "d", "b": "e", "c": "f", "d": 
         "g", "e": "h", "f": "i", "g": "j ", "h": "k", 

                    "i": "l", "j ": "m", "k": "n", "l": "o", "m": "p", "n": "q", "o": "r", "p": "s", 

                    "q": "t", "r": "u", "s": "v", "t": "w", "u": "x", "v": "y", "w": "z", "x": "a", 

                    "y": "b", "z": "c", " ":" "}}' 

         { 

          "result": "khoor gdwd hqj lqhhuv wklv lv li brx zdqw wr xv h d nhb l ghilqhg lw 
         pdqxdoob iru whvw" 

         } 

         ============================================================== 

         ahmed_elbaqary@A hmed-Elbaqary:~$ curl -G "http://127.0.0.1:5000/" 
         --data-urlencode 'params={"string":"khoor gdwd hqj lqhhuv wklv lv li brx zdqw wr xv h 
         d nhb l ghilqhg lw pdqxdoob iru whvw","encry pt":false, "key": {"a": "d", "b": "e", "c": 
         "f", "d": "g", "e": "h", "f": "i", "g": "j ", "h": "k", 
﻿                    "i": "l", "j ": "m", "k": "n", "l": "o", "m": "p", "n": "q", "o": "r", "p": "s", 

                    "q": "t", "r": "u", "s": "v", "t": "w", "u": "x", "v": "y", "w": "z", "x": "a", 

                    "y": "b", "z": "c", " ":" "}}' 

         { 

          "result": "hello data engineers this is if you want to use a key i deﬁned it manually 
         for test" 

         } 

Notes 

The proj ect would go like this: 

     1)  You build a Caesar Cipher package that can be installed in the python env as known, 
         the package has two modules, one for the Class itself with all its methods/attributes, 
         and another module with a function that wraps up all the logic the A PI needs to use 
     2)  Build an A PI that can call this package functions and the user can call with data and 
         this would be the ﬁnal result 
