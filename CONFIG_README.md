# How to configure Sunmine
## Below is the default config file: *sunmine.cfg*
### Usage for each section is suggested in italics.

`[Location]`<br>
`# for local weather information`<br><br>
*Country code in relation to ISO3166 Alpha-2 standards* <br> 
`country_code = GB`

*Nearest town/city. Postal codes not tested but may work.* <br>
`location = London`

`# for the sunrise / sunset api`

`latitude = 51.5074`

`longitude = 0.1278`

`[Tokens]`
`open_weather = **OpenweatherAPIKey**`

`[Communication]`

`# Emails user when turning mining on or off`

`recipient_email = test@test.com`

`sender_email = test@test.com`

`password = yourpassword`

`smtp_server_address = smtp.gmail.com`

`smtp_port = 587`

`[Miner]`

`# read the documentation for best practice`

`program_location = **path to your executable miner**`


`
