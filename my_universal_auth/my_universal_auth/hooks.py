app_name = "test app"
app_title = "My Universal Auth"
app_publisher = "Your Name"
app_description = "Universal OAuth for Multiple Sites"
app_email = "yash@yopmail.com"
app_license = "MIT"

# Ye sabse important part hai: fixtures
# Jab bhi app install hoga, ye OAuth Client record create kar dega
fixtures = [
    {
        "dt": "OAuth Client",
        "filters": [["app_name", "=", "test app"]]
    }
]