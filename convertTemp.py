def convertTemp(fromUnit,toUnit,value):
    '''
    Temperature Converter is converting a given temperature from given unit to another.
    convertTemp(fromUnit,toUnit,value)
    fromUnit is the temperature unit that need to be convert from
    toUnit is the temperature unit that need to br convert to
    vaule is the temperature value that need to be convert
    '''
    convert_temp=Temp(fromUnit,toUnit,value)
    if fromUnit=='Celsius' and toUnit=='Fahrenheit':
        convert_temp.convertCelsiusToFahrenheit()
    elif fromUnit=='Celsius' and toUnit=='Kelvin':
        convert_temp.convertCelsiusToKelvin()
    elif fromUnit=='Fahrenheit' and toUnit=='Celsius':
        convert_temp.convertFahrenheitToCelsius()
    elif fromUnit=='Fahrenheit' and toUnit=='Kelvin':
        convert_temp.convertFahrenheitToKelvin()
    elif fromUnit=='Kelvin' and toUnit=='Celsius':
        convert_temp.convertKelvinToCelsius()
    elif fromUnit=='Kelvin' and toUnit=='Fahrenheit':
        convert_temp.convertKelvinToFahrenheit()
    return print(convert_temp)




class Temp():
    
    def __init__(self,fromUnit, toUnit, value):
        self.fromUnit=fromUnit
        self.toUnit=toUnit
        self.value=value
        self.result=None
    def __str__(self):
        return (f'{self.value} {self.fromUnit} is equal to {self.result} {self.toUnit}')
        
    def convertCelsiusToFahrenheit(self):  #convert Celsius To Fahrenheit
        self.result=(self.value*9/5)+32
        return self.result
    def convertFahrenheitToCelsius(self):  #convert Fahrenheit To Celsius
        self.result=(self.value-32)*5/9
        return self.result
    def convertCelsiusToKelvin(self):      #convert Celsius To Kelvin
        self.result=self.value+273.15
        return self.result
    def convertKelvinToCelsius(self):      #convert Kelvin To Celsius
        self.result=self.value-273.15
        return self.result
    def convertFahrenheitToKelvin(self):   #convert Fahrenheit To Kelvin
        temp=self.value
        self.value=self.convertFahrenheitToCelsius()
        self.result=self.convertCelsiusToKelvin()
        self.value=temp
        return self.result    
    def convertKelvinToFahrenheit(self):   #convert Kelvin To Fahrenheit
        temp=self.value
        self.value=self.convertKelvinToCelsius()
        self.result=self.convertCelsiusToFahrenheit()
        self.value=temp
        return self.result
    
    
    

    