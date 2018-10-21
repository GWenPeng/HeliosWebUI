class DriverURL():

   def driverURL(self,drivername):


      if(drivername=='Chrome') :
       ChromeDriverURL='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'
       DriverURL=ChromeDriverURL
      elif(drivername=='IE-32'):
        DriverURL='C:\\Program Files\\internet explorer\\IEDriverServer-32x.exe'
      elif(drivername=='IE-64'):
        DriverURL = 'C:\\Program Files\\internet explorer\\IEDriverServer_64x.exe'
      elif (drivername == 'Edge'):
          DriverURL = 'C:\\Program Files\\internet explorer\\MicrosoftWebDriver .exe'
      else: print("drivername is error!")

      return DriverURL