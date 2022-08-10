from flask import Flask,request,render_template
import argparse

def parse_opt():
    #创建解析对象
    parser = argparse.ArgumentParser()
    #填入解析参数
    parser.add_argument("--port",help="输入端口号",default=2500,type=int)
    #对输入进行解析
    args = parser.parse_args()
    return args


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")


if __name__ == "__main__":
# app.register_blueprint(yolo_bp)
    opt = parse_opt()
    print(opt.port)
    app.run("0.0.0.0", port=opt.port)




