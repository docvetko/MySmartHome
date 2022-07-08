import requests
import xmltodict
import datetime as dt


def formatted_date():

    today = dt.datetime.now()

    return today.strftime('%A, %d %B %Y')
    
def formatted_time():

    now_time = dt.datetime.now()

    return now_time.strftime('%H : %M : %S')


#url = "https://vrijeme.hr/hrvatska_n.xml"

#response = requests.get(url)

#data = xmltodict.parse(response.content)


class Prognoza:

    def __init__(self):
        self.url = "https://vrijeme.hr/hrvatska_n.xml"
        self.data = None
        self.send_request()

    def send_request(self):
        response = requests.get(self.url)

        self.data = xmltodict.parse(response.content)

    def get_formated_weather_data(self):
        return {
            'location': self.data['Hrvatska']['Grad'][44]['GradIme'],
            'current_temperature': self.data['Hrvatska']['Grad'][44]['Podatci']['Temp'],
            'humidity': self.data ['Hrvatska']['Grad'][44]['Podatci']['Vlaga'],
            'pressure': self.data ['Hrvatska']['Grad'][44]['Podatci']['Tlak'],
            'last_refrersh': f'{formatted_date()} {formatted_time()}'
        }
vrijeme = Prognoza()

print(vrijeme.get_formated_weather_data())

