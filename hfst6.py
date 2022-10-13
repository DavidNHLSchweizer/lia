from quaternion import PointQuaternion, Quaternion, QuaternionTable, RotationQuaternion

def _multiply(q1:Quaternion, q2:Quaternion, msg):
    print(f'{msg}: {q1*q2}')
    print(QuaternionTable(q1,q2).table)

def _opgave1_2(msg, point, angle, vector):
    p = PointQuaternion(point)
    q = RotationQuaternion(angle, vector)
    print(f'{msg}:\n\tpuntquaterion is {p}\n\trotatiequaternion(geconjugeerd) is {q.conjugate()}')

def opgave1():
    _opgave1_2('Opgave 1', [-2,2,9], 84,[-4,0,3])
def opgave2():
    _opgave1_2('Opgave 2', [23,-15,7], 42,[6,-6,7])


def opgave3():
    _multiply(Quaternion(0, 2,-4,5), Quaternion(7,2,1,0), 'opgave 3')
def opgave4():
    _multiply(Quaternion(-16, -2, 3,2), Quaternion(-1,4,0,2), 'opgave 4')
def hfst6():
    opgave1()
    opgave2()
    opgave3()
    opgave4()

if __name__=='__main__':
    hfst6()