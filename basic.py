import sys #import 모듈을 이용하여, sys.py 파일 안에 있는 코드를 사용할 수 있도록 함

class Main(QMainWindow): #부모클래스로 QMainWindow를 상속받는 Main 클래스를 정의
    def __init__(self): #Main 클래스를 생성할 때 무조건 실행되는 초기화 함수
        super().__init__() #부모 클래스인 QMainWindow 클래스를 초기화하는 함수
        self.setGeometry(100,150,500,350) #화면에 보여질 MainWindow의 x좌표,y좌표,폭,높이 설정

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

    