from flask import Flask

app=Flask(__name__)

@app.route('/fact/<int:number>')
def factor(number):
    factt=1
    if number==0:
        return '1'
    elif number<0:
        return "sorry"
    else:
        for i in range(1,number+1):
            factt=factt*i
        return f'{factt}'       
  


if __name__=='__main__':
    app.run(debug=True)