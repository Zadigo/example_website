overviews = [
    {
        "highlight_value": "1 lift|24 hour business centre|24 hour coffee shop|24 hour reception|24 hour room service|24 hour security|24 hours front desk|24-hour business center|24-Hour Front Desk|24-hr Coffee Shop|24/7 Power|Activities desk|Activity centre|Airport Transfer Available With Charges Rs.200/- Per Trip|Arrangements Of Kitty Parties & Birthday Party|Auditorium|Ballroom|Banqueting|Bar|Board Room|Boardroom|Breakfast buffet|Children's Playground|Doctor on Call|Dry Cleaning|Dry Cleaning Service|Dry cleaning/laundry service|Free garage parking|Free Parking|Free Wi-Fi|Free Wi-Fi Icon|Handicap Facilities|Hot tub|In-room safe (some rooms)|Laundry Service|Newspaper|Non-smoking rooms|Room Service|Room service (24 hours)|Room Service (24 Hours)(after 11:00pm.round The Clock Menu)|Room Service 24 Hrs|Room Service 6 Am - 12 Night|Room Service 7 Am To 9 Pm|Room Service 7am-11:30pm|Room Service, 24 Hour Reception|Room Service, 24 Hour Reception And Laundry Service|Room Services 7 Am To 9 Pm|Wake up call|Wheelchair access"
    }
]

# for overview in overviews:
#     for values in overview.values():
#         if '|' in values: 
#             elements = values.split('|')
#             print(elements)

elements = [
    values.split('|') 
        for my_value in overviews 
            for values in my_value.values() if '|' in values
]
print(elements)
