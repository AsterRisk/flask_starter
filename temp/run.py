#! /usr/bin/env python
from app.views import app

if __name__ == "__main__":
    print ("hello from views")
    app.run(debug=True,host="localhost",port=5000)