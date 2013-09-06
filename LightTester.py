''' Script for testing  the activity of each port on the raspberyy pi '''
import RPi.GPIO as GPIO , time
import pprint, os
pp = pprint.PrettyPrinter(indent=4).pprint

class TestStatus:
    AllChans =[8,10,12,16,18,22,24,26,3,5,7,11,13,15,19,21,23,25]
    AllChans.sort()
    #http://elinux.org/RPi_Low-level_peripherals#Introduction

    InputChans =[]
    OutputChans = {} 

    def LoadForOut(self):
        ''' initialises channels for testing '''
        GPIO.setmode(GPIO.BCM)
        for  Chan in self.AllChans:
                GPIO.setup(Chan,GPIO.OUT)
                GPIO.output(Chan,True)
                self.OutputChans[Chan] = True # signify that it is off

    def ValidateChans(self):
      ''' Makes sure that  Input and output are  disjoint '''
      for i in  self.InputChans:
          if i in  self.OutputChans:
                self.InputChans.remove(i)

    def PrintState(self):
       ''' Prints the status of each channel '''
       On =  "\033[93m"
       Off = "\033[92m"
       os.system('clear')

       for Chan in self.OutputChans:
           State = self.OutputChans[Chan]

           if (State == True):
               print ("%s Channel %d is off" % (Off,Chan))
           else:
               print ("%s Channel %d is on" % (On, Chan, ))

    def ChangeChanState(self,Chan):
       OldState = self.OutputChans[Chan]
       if (OldState == True):
           NewState = False
       else:
           NewState = True
       self.OutputChans[Chan] = NewState
       GPIO.output(Chan,NewState)

    def GetInput(self):
       Choice =0
       while (Choice != 'q' and Choice != 'Q'):
               if Choice in self.OutputChans:
                   self.ChangeChanState(Choice)
               self.PrintState()
               Choice = int(raw_input("What To Change or Q to exit " ))



if __name__ == "__main__":
    TestInstance = TestStatus()
    TestInstance.LoadForOut()
    TestInstance.ValidateChans()
    TestInstance.GetInput()





