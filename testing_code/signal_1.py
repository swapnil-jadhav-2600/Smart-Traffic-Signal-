class SmartTraffic_DEMO :
    S1 = 0
    S2 = 0
    S3 = 0
    S4 = 0
    R1 = 90
    R2 = 90
    R3 = 90
    R4 = 90

    G1 = 30
    G2 = 30
    G3 = 30
    G4 = 30

    @staticmethod
    def  compare( S2,  S3) :
        ans = [0] * (4)
        diff = 0
        Ga = 30
        Gb = 30
        Ra = 90
        Rb = 90
        diff = S2 - S3
        if (diff < -10) :
            Gb += 10
            Rb -= 10
            Ga -= 10
            Ra += 10
        if (diff > 10) :
            Ga += 10
            Ra -= 10
            Gb -= 10
            Rb += 10
        ans[0] = Ga
        ans[1] = Ra
        ans[2] = Gb
        ans[3] = Rb
        return ans
    
    def SetGreen(self) :
        @staticmethod
        def main(args) :
            ans = [0] * (4)
        sc =  "Python-inputs"
        print("Enter value of Vehicle count at S2 & S3: ")
        SmartTraffic_DEMO.S2 = int(input())
        SmartTraffic_DEMO.S3 = int(input())
        ans = SmartTraffic_DEMO.compare(SmartTraffic_DEMO.S2, SmartTraffic_DEMO.S3)
        print(str(ans[0]) + " " + str(ans[2]))
        SmartTraffic_DEMO.G2 = 30
        SmartTraffic_DEMO.R2 = 90
        print("Enter value of Vehicle count at S3 & S4: ")
        SmartTraffic_DEMO.S3 = int(input())
        SmartTraffic_DEMO.S4 = int(input())
        ans = SmartTraffic_DEMO.compare(SmartTraffic_DEMO.S3, SmartTraffic_DEMO.S4)
        print(str(ans[0]) + " " + str(ans[2]))
        SmartTraffic_DEMO.G3 = 30
        SmartTraffic_DEMO.R3 = 90


if __name__=="__main__":
    std = SmartTraffic_DEMO()
    std.SetGreen()
