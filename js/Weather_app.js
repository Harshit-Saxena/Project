const timeEl = document.getElementById('time');
const dateEl = document.getElementById('date');
const currentWeatherItemsEl = document.getElementById('current-weather-items');
const timezone = document.getElementById('time-zone');
const countryEl = document.getElementById('country');
const weatherforecastEl = document.getElementById('weather-forecast');
const currenttempEl = document.getElementById('current-temp');

const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thruday', 'Friday', 'Saturday', 'Sunday'];

const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

const API_KEY = '2d6bd0592bdfecd4b393b15b9fbed391'

setInterval(() => {
    const time = new Date();
    const month = time.getMonth();
    const date = time.getDate();
    const day = time.getDay();
    const hour = time.getHours();
    const hoursIn12HrsFormat = hour >= 13 ? hour % 12 : hour
    const minutes = time.getMinutes();
    const minute = minutes < 10 ? '0'+minutes : minutes;
    const ampm = hour >= 12 ? 'PM' : 'AM'

    timeEl.innerHTML = (hoursIn12HrsFormat < 10 ? '0'+hoursIn12HrsFormat : hoursIn12HrsFormat) + ':' + minute + ' ' + `<span id="am-pm">${ampm}</span>`

    dateEl.innerHTML = days[day] + ', ' + date + ' ' + months[month] 

}, 1000);


function getWeatherData() {
    navigator.geolocation.getCurrentPosition((success) => {
        let { latitude, longitude } = success.coords;
        fetch(`https://api.openweathermap.org/data/2.5/onecall?lat=${latitude}&lon=${longitude}&exclude=hourly,minutely&units=metric&appid=${API_KEY}`).then(res => res.json()).then(data => {
        console.log(data)
        showWeatherData(data)
    }
    )
        })
    }
getWeatherData()

function showWeatherData(data) {
    let { humidity, pressure, sunrise, sunset, wind_speed, wind_deg, temp, uvi } = data.current;

    currentWeatherItemsEl.innerHTML =
    `<div class="weather-items">
        <div>Humidity</div>
        <div>${humidity}%</div>
    </div>
    <div class="weather-items">
        <div>Pressure</div>
        <div>${pressure}</div>
    </div>
    <div class="weather-items">
        <div>UVI</div>
        <div>${uvi}</div>
    </div>
    <div class="weather-items">
        <div>Wind Speed</div>
        <div>${wind_speed}</div>
    </div>
    <div class="weather-items">
        <div>Wind Degree</div>
        <div>${wind_deg}</div>
    </div>
    <div class="weather-items">
        <div>Sunrise</div>
        <div>${window.moment(sunrise*1000).format("HH:mm a")}</div>
    </div>
    <div class="weather-items">
        <div>Sunset</div>
        <div>${window.moment(sunset*1000).format("HH:mm a")}</div>
    </div>
    <div class="weather-items">
        <div>Temp</div>
        <div>${temp} &#176;C</div>
    </div>
    `;
    let otherDayForecast = ''
    data.daily.forEach((day, idx) => {

        if (idx == 0) {
            currenttempEl.innerHTML =
            `
            <img src="http://openweathermap.org/img/wn/${day.weather[0].icon}@4x.png" alt="weather-icon" class="w-icon">
            <div class="others">
                <div class="day">${window.moment(day.dt*1000).format('ddd')}</div>
                <div class="temp">Night - ${day.temp.night}&#176; C</div>
                <div class="temp">Day - ${day.temp.day}&#176; C</div>
            </div>
            `
        }
        else {
            otherDayForecast +=
            `
            <div class="weather-forecast-item">
            <div class="day">${window.moment(day.dt*1000).format('ddd')}</div>
            <img src="http://openweathermap.org/img/wn/${day.weather[0].icon}@2x.png" alt="weather-icon" class="w-icon">
            <div class="temp">Night - ${day.temp.night}&#176; C</div>
            <div class="temp">Day - ${day.temp.day}&#176; C</div>
        </div>
        `
        }
    })

    weatherforecastEl.innerHTML = otherDayForecast;
   
}