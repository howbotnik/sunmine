# How to configure Sunmine
## Below is the default config file: *sunmine.cfg*
### Usage for each section is suggested in italics.

`[Location]`<br>
`# for local weather information`<br><br>
*# Country code in relation to ISO3166 Alpha-2 standards* <br> 
`country_code = GB`

*# Nearest town/city. Postal codes not tested but may work.* <br>
`location = London`

`# for the sunrise / sunset api`<br>
`latitude = 51.5074`<br>
`longitude = 0.1278`

`[Tokens]`<br>
*# API keys are available here: https://openweathermap.org/*
`open_weather = **OpenweatherAPIKey**`

`[Communication]`<br>
`# Emails user when turning mining on or off`

*# Where you want the emails to be sent*<br>
`recipient_email = test@test.com`

*# The account you want to send from*<br>
`sender_email = test@test.com`

*# I recommend generating an 'app specific' password from your email provider*<br>
`password = yourpassword`

`smtp_server_address = smtp.gmail.com`<br>
`smtp_port = 587`

`[Miner]`
<br>
*# This will require you to have a fully set up miner executable.  Make sure this works first, then put the full path to the executable here* <br>
`program_location = **path to your executable miner**`


`
