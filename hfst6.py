from quatern import Quaternion, QuaternionTable

def _multiply(q1:Quaternion, q2:Quaternion, msg):
    print(f'{msg}: {q1*q2}')
    print(QuaternionTable(q1,q2).table)

def opgave3():
    _multiply(Quaternion(0, 2,-4,5), Quaternion(7,2,1,0), 'opgave 3')
def opgave4():
    _multiply(Quaternion(-16, -2, 3,2), Quaternion(-1,4,0,2), 'opgave 4')
def hfst6():
    opgave3()
    opgave4()

if __name__=='__main__':
    hfst6()