months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

seasons = (
    tuple([months[11], months[0], months[1]]),  
    tuple(months[2:5]), 
    tuple(months[5:8]),  
    tuple(months[8:11]) 
)

print(seasons)