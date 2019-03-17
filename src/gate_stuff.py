class LogicGate:

    def __init__(self,n):
        self.name = n
        self.output = None

    def getLabel(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

    @staticmethod
    def performGateLogic(a, b):
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)
        self.a = None
        self.b = None

    def performGateLogic(self):
        self.a = self.getPinA()
        self.b = self.getPinB()
        if self.a ==1 or self.b==1:
            return 1
        else:
            return 0

    @staticmethod
    def performGateLogic(a, b):
        if a ==1 or b==1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1

"""Create a two new gate classes, one called NorGate the other called NandGate.
   NandGates work like AndGates that have a Not attached to the output. NorGates
   work lake OrGates that have a Not attached to the output."""

class NorGate(OrGate):

    def __init__(self,n):
        OrGate.__init__(self,n)

    def performGateLogic(self):
        return not OrGate.performGateLogic(self)

class XorGate(OrGate):

    def __init__(self,n):
        OrGate.__init__(self,n)

    def performGateLogic(self):
        OrTrue = OrGate.performGateLogic(self)
        AndTrue = AndGate.performGateLogic(self.a, self.b)
        if OrTrue and not AndTrue:
            return True
        return False

    @staticmethod
    def performGateLogic(a, b):
        OrTrue = OrGate.performGateLogic(a, b)
        AndTrue = AndGate.performGateLogic(a, b)
        if OrTrue and not AndTrue:
            return True
        return False

class NandGate(AndGate):

    def __init__(self,n):
        AndGate.__init__(self,n)

    def performGateLogic(self):
        return not AndGate.performGateLogic(self)

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

class halfAdder:

    def __init__(self):
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter Circuit Input A " + "-->"))

    def getPinB(self):
        return int(input("Enter Circuit Input B " + "-->"))

    def getOutput(self):
        self.pinA = self.getPinA()
        self.pinB = self.getPinB()
        sum_toReturn = XorGate.performGateLogic(self.pinA, self.pinB)
        carry_toReturn = AndGate.performGateLogic(self.pinA, self.pinB)
        sum_toReturn = 0 if not sum_toReturn else 1
        carry_toReturn = 0 if not carry_toReturn else 1
        return sum_toReturn,carry_toReturn

    # Now extend that circuit and implement an 8 bit full-adder.
class fullAdder(halfAdder):

    def __init__(self):
        # TODO: find out what the difference is between calling super() and calling init method of parent class
        halfAdder.__init__(self)
        self.pinC = None

    def getPinC(self):
        # Pin C is the carry input
        return int(input("Enter Circuit Input C " + "-->"))

    def getOutput(self, pinA=None, pinB = None, pinC = None):
        if pinA is None:
            self.pinA = self.getPinA()
            self.pinB = self.getPinB()
            self.pinC = self.getPinC()
        else:
            self.pinA = pinA
            self.pinB = pinB
            self.pinC = pinC
        # calculate sum S=(A XOR B) XOR Cin
        sum_toReturn = XorGate.performGateLogic(XorGate.performGateLogic(self.pinA, self.pinB), self.pinC)
        #print('Sum to return: ' + str(sum_toReturn))
        #print('Carry to return:' + str(carry_toReturn))
        # Cout=(A AND B) OR (Cin AND (A XOR B))
        carry_toReturn = OrGate.performGateLogic(AndGate.performGateLogic(self.pinA, self.pinB), AndGate.performGateLogic(self.pinC, XorGate.performGateLogic(self.pinA, self.pinB)))
        sum_toReturn = 0 if not sum_toReturn else 1
        carry_toReturn = 0 if not carry_toReturn else 1
        return sum_toReturn,carry_toReturn

class eightBitFullAdder:
    def __init__(self):
        self.Anum = None
        self.Bnum = None

    def getFirst8bitNum(self):
        return int(input("Enter first 8 bit number " + "-->"))

    def getSecond8bitNum(self):
        return int(input("Enter second 8 bit number " + "-->"))

    def getOutput(self):
        self.Anum = self.getFirst8bitNum()
        self.Bnum = self.getSecond8bitNum()
        # convert Anum and Bnum into lists of bit numbers
        Anums = [int(x) for x in str(self.Anum)]
        Bnums = [int(x) for x in str(self.Bnum)]
        Anums = Anums[::-1]
        Bnums = Bnums[::-1]
        i = 0
        curr_carry = 0
        theSum = []
        my_full_adder = fullAdder()
        while(i < 8):
            # input current A num, B num, and Carry into full adder
            curr_sum, curr_carry = my_full_adder.getOutput(Anums[i],Bnums[i],curr_carry)
            theSum.append(curr_sum)
            i += 1
        if curr_carry == 1:
            theSum.append(curr_carry)
        # convert sum from list of ints into one integer
        sumInCorrectOrder = theSum[::-1]
        sumStrings = map(str, sumInCorrectOrder)  # ['1','2','3']
        sumString = ''.join(sumStrings)  # '123'
        sumAsInt = int(sumString)  # 123
        return sumAsInt


def main():
   # The circuit simulation shown in this chapter works in a backward direction. In other words,
   # given a circuit, the output is produced by working back through the input values, which in
   # turn cause other outputs to be queried. This continues until external input lines are found,
   # at which point the user is asked for values. Modify the implementation so that the action is
   # in the forward direction; upon receiving inputs the circuit produces an output.

   # g1 = AndGate("G1")
   # g2 = AndGate("G2")
   # g3 = OrGate("G3")
   # g4 = NotGate("G4")
   # c1 = Connector(g1,g3)
   # c2 = Connector(g2,g3)
   # c3 = Connector(g3,g4)
   # print(g4.getOutput())
   #
   # """Create a series of gates that prove the following equality NOT (( A and B) or (C and D))
   # is that same as NOT( A and B ) and NOT (C and D). Make sure to use some of your new
   # gates in the simulation."""
   #
   # g3 = NorGate("G3")
   # g4 = NandGate("G4")
   # g5 = NandGate("G5")
   # g6 = AndGate("G6")
   # c1 = Connector(g1,g3)
   # c2 = Connector(g2,g3)
   # c3 = Connector(g4,g6)
   # c4 = Connector(g5,g6)
   # print(g3.getOutput() == g6.getOutput())
   #
   # # Test Xor Gate
   # xor_gate = XorGate('Akon')
   # print(xor_gate.getOutput())

   # Test Half Adder
   # my_half_adder = halfAdder()
   # my_sum,my_carry = my_half_adder.getOutput()
   # print('Half Adder results: Sum = ' + str(my_sum) + ' Carry = ' + str(my_carry))

   # Test Full Adder
   # my_full_adder = fullAdder()
   # my_sum,my_carry = my_full_adder.getOutput()
   # print('Full Adder results: Sum = ' + str(my_sum) + ' Carry = ' + str(my_carry))

   # Test 8 bit full Adder
   my_8bit_adder = eightBitFullAdder()
   my_sum = my_8bit_adder.getOutput()
   print('8 bit Full Adder results: Sum = ' + str(my_sum))

if __name__ == '__main__':
    main()
