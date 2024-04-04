# AirBnB MongoDB Analysis
## Data Set Details
### Origin & Format
The origin of my data set is [AirBnB listings data](http://insideairbnb.com/get-the-data.html), a web page that records global AirBnB data. For this assignment, I chose AirBnB data from San Francisco, California, United States. It is a list of AirBnB in San Francisco area with information such as their host name, locations, and rating. The original data file was in **CVS** format.  

### Raw Data Example
Here is a display of the first 10 rows of my data.
|id      |listing_url                          |scrape_id|last_scraped|source         |name                                        |description                                                                                                                                                                          |neighborhood_overview                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |picture_url                                                              |host_id |host_url                                  |host_name|host_since|host_location       |host_about                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |host_response_time|host_response_rate|host_acceptance_rate|host_is_superhost|host_thumbnail_url                                                                                        |host_picture_url                                                                                             |host_neighbourhood|host_listings_count|host_total_listings_count|host_verifications              |host_has_profile_pic|host_identity_verified|neighbourhood                           |neighbourhood_cleansed|neighbourhood_group_cleansed|latitude|longitude |property_type       |room_type      |accommodates|bathrooms|bathrooms_text|bedrooms|beds|amenities                                                                                                                                                        |price   |minimum_nights|maximum_nights|minimum_minimum_nights|maximum_minimum_nights|minimum_maximum_nights|maximum_maximum_nights|minimum_nights_avg_ntm|maximum_nights_avg_ntm|calendar_updated|has_availability|availability_30|availability_60|availability_90|availability_365|calendar_last_scraped|number_of_reviews|number_of_reviews_ltm|number_of_reviews_l30d|first_review|last_review|review_scores_rating|review_scores_accuracy|review_scores_cleanliness|review_scores_checkin|review_scores_communication|review_scores_location|review_scores_value|license       |instant_bookable|calculated_host_listings_count|calculated_host_listings_count_entire_homes|calculated_host_listings_count_private_rooms|calculated_host_listings_count_shared_rooms|reviews_per_month|
|--------|-------------------------------------|---------|------------|---------------|--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|--------|------------------------------------------|---------|----------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|------------------|--------------------|-----------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|------------------|-------------------|-------------------------|--------------------------------|--------------------|----------------------|----------------------------------------|----------------------|----------------------------|--------|----------|--------------------|---------------|------------|---------|--------------|--------|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------|--------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------|----------------|---------------|---------------|---------------|----------------|---------------------|-----------------|---------------------|----------------------|------------|-----------|--------------------|----------------------|-------------------------|---------------------|---------------------------|----------------------|-------------------|--------------|----------------|------------------------------|-------------------------------------------|--------------------------------------------|-------------------------------------------|-----------------|
|1094764 |https://www.airbnb.com/rooms/1094764 |2.02E+13 |3/7/2024    |city scrape    |San Francisco Presidio Paradise!            |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |https://a0.muscache.com/pictures/16468522/12924599_original.jpg          |172460  |https://www.airbnb.com/users/show/172460  |Leila    |7/19/2010 |Raleigh, NC         |We are from the San Francisco Bay Area and still consider it home, though we now live on the east coast.  I teach nineteenth-century British literature at NC State University, my husband writes philosophy textbooks, and we spend summers in southwest France.  We eventually plan to move back to the Bay Area, which we miss terribly, though there are certainly worse places to live than Raleigh and the Research Triangle.  We love to travel, eating at good restaurants, hanging out with friends, and going to movies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |within a day      |100%              |50%                 |f                |https://a0.muscache.com/im/pictures/user/85a6a3ac-5160-40c1-a217-c6814194bbee.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/85a6a3ac-5160-40c1-a217-c6814194bbee.jpg?aki_policy=profile_x_medium|Richmond District |2                  |6                        |['email', 'phone']              |t                   |t                     |                                        |Inner Richmond        |                            |37.78814|-122.46547|Entire rental unit  |Entire home/apt|2           |         |              |1       |1   |[]                                                                                                                                                               |$150.00 |30            |180           |30                    |30                    |180                   |180                   |30                    |180                   |                |t               |30             |60             |90             |365             |3/7/2024             |1                |0                    |0                     |10/31/2021  |10/31/2021 |5                   |5                     |5                        |5                    |5                          |5                     |5                  |              |f               |2                             |2                                          |0                                           |0                                          |0.03             |
|38047206|https://www.airbnb.com/rooms/38047206|2.02E+13 |3/7/2024    |previous scrape|52 Vesta home                               |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |https://a0.muscache.com/pictures/6726f7cf-73aa-40fa-aef5-6ef42404a1bc.jpg|92965890|https://www.airbnb.com/users/show/92965890|å”±      |9/1/2016  |Bridgeport, CT      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |N/A               |N/A               |N/A                 |f                |https://a0.muscache.com/im/pictures/user/adf55172-c98a-4600-8027-efc1ced6b071.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/adf55172-c98a-4600-8027-efc1ced6b071.jpg?aki_policy=profile_x_medium|                  |1                  |3                        |['email', 'phone']              |t                   |f                     |                                        |Bayview               |                            |37.7298 |-122.40096|Private room in home|Private room   |1           |         |1 shared bath |        |    |["Smoke alarm", "Hangers", "Air conditioning", "Carbon monoxide alarm", "Essentials", "Wifi"]                                                                    |        |90            |1125          |90                    |90                    |1125                  |1125                  |90                    |1125                  |                |                |0              |0              |0              |0               |3/7/2024             |0                |0                    |0                     |            |           |                    |                      |                         |                     |                           |                      |                   |              |f               |1                             |0                                          |1                                           |0                                          |                 |
|43475468|https://www.airbnb.com/rooms/43475468|2.02E+13 |3/7/2024    |previous scrape|Beautiful Mission District Home and Backyard|Beautiful entire first floor of home with backyard in the sunny Mission District. Large studio, living room, and kitchen, washer and dryer included. Five minute walk to restaurants.|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |https://a0.muscache.com/pictures/f196cbea-2500-47c5-985a-85684497c990.jpg|65136730|https://www.airbnb.com/users/show/65136730|Ryan     |3/30/2016 |Badamsha, Kazakhstan|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |N/A               |N/A               |N/A                 |f                |https://a0.muscache.com/im/pictures/user/c463f9ef-b352-4b01-8363-55be52e23731.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/c463f9ef-b352-4b01-8363-55be52e23731.jpg?aki_policy=profile_x_medium|Mission District  |1                  |3                        |['email', 'phone', 'work_email']|t                   |t                     |                                        |Mission               |                            |37.75721|-122.41245|Entire home         |Entire home/apt|5           |         |1.5 baths     |2       |    |["TV", "Smoke alarm", "Carbon monoxide alarm", "Private entrance", "Security cameras on property", "Essentials", "Washer", "Heating", "Kitchen", "Dryer", "Wifi"]|        |30            |1125          |30                    |30                    |1125                  |1125                  |30                    |1125                  |                |                |0              |0              |0              |0               |3/7/2024             |0                |0                    |0                     |            |           |                    |                      |                         |                     |                           |                      |                   |              |f               |1                             |1                                          |0                                           |0                                          |                 |
|6.49E+17|https://www.airbnb.com/rooms/648549709021440854|2.02E+13 |3/7/2024    |city scrape    |LuxoStays &#124; ! Quiet Rm #Private Bathrm & VIEW|This house is well-maintained, and has upgraded furnishings!<br /> <br />Conveniently located, this spacious apartment is only a couple of blocks from restaurants of different cuisines, grocery stores, farmers' markets and other stores that you'll need! <br /> <br />The nearest bus stop is 10 minutes away from the property and will take you. John McLaren Park is just a 5-minutes drive from our home.<br /> <br />Longer inquiries are very welcome. Inquire even if the calendar is blocked off.|The neighborhood is on a quiet street with families, children, and other working professionals. There are many great restaurants within a 1-mile radius. Itâ€™s located close to many transportation options and is a few minutes from several commercial areas with shops and restaurants.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |https://a0.muscache.com/pictures/miso/Hosting-648549709021440854/original/a09fcb9b-b75a-440f-9246-8a29c9e05b96.jpeg|226555948|https://www.airbnb.com/users/show/226555948|Gi'Angelo|11/19/2018|San Francisco, CA   |Our company is called Luxo Stays based in the Bay Area and we provide property management for furnished short-term and medium term rentals. We also manage shared-living/co-living properties. I was born and raised in San Francisco and the Peninsula.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |within an hour    |100%              |98%                 |f                |https://a0.muscache.com/im/pictures/user/16771cc9-a065-4a2b-a3c4-6060315e0eb8.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/16771cc9-a065-4a2b-a3c4-6060315e0eb8.jpg?aki_policy=profile_x_medium|Burlingame        |69                 |103                      |['email', 'phone']              |t                   |t                     |San Francisco, California, United States|Excelsior             |                            |37.7267606|-122.4085215|Private room in home|Private room   |2           |2.5      |2.5 shared baths|1       |1   |["Hot water kettle", "Bathtub", "Iron", "Keypad", "Coffee", "Refrigerator", "Fire extinguisher", "Stainless steel gas stove", "Coffee maker", "Smoke alarm", "First aid kit", "Bed linens", "Clothing storage: closet", "Cleaning products", "Hot water", "Conditioner", "Security cameras on property", "Oven", "Hair dryer", "Paid washer \u2013 In building", "Dedicated workspace", "Dishwasher", "Self check-in", "TV", "Long term stays allowed", "Hangers", "Lock on bedroom door", "Body soap", "Carbon monoxide alarm", "Microwave", "Cooking basics", "Essentials", "Shampoo", "Dining table", "Dishes and silverware", "Kitchen", "Free street parking", "Wifi", "Paid dryer \u2013 In building"]|$69.00  |30            |1125          |30                    |30                    |1125                  |1125                  |30                    |1125                  |                |t               |0              |0              |0              |216             |3/7/2024             |6                |3                    |0                     |9/4/2022    |1/13/2024  |5                   |4.83                  |4.5                      |5                    |5                          |5                     |5                  |2022-003280STR|f               |13                            |2                                          |11                                          |0                                          |0.33             |
|47918229|https://www.airbnb.com/rooms/47918229|2.02E+13 |3/7/2024    |city scrape    |Blueground &#124; Marina District, w/d, nr parks |Feel at home wherever you choose to live with Blueground. Youâ€™ll love this stylish Marina District furnished two-bedroom apartment with its modern decor, fully equipped kitchen, and pretty living room. Ideally located, youâ€™re close to all the best that San Francisco has to offer! (ID #SFO434)|This furnished apartment is located in the dreamy Marina neighborhood of San Francisco's northern shore. Sitting on the edge of the bay, it entices many shoppers and diners. The hilly green space is also ideal for picnicking or just relaxing. The Palace of Fine Arts (POFA) is a monumental structure originally built in 1915 that has since become a Marina landmark. Between hosting exhibitions and being the backdrop for photo shoots, itâ€™s not to be missed. Offering spectacular views of the Golden Gate Bridge and numerous bars, this trendy area is usually filled with people both day and night. Using public transport, Fishermanâ€™s Wharf is 20 minutes away. Without traffic, the SFO airport is 35 minutes away by cab.|https://a0.muscache.com/pictures/prohost-api/Hosting-47918229/original/990b35ec-12c1-4064-bf80-316775f5774f.jpeg|107434423|https://www.airbnb.com/users/show/107434423|Blueground|12/16/2016|New York, NY        |Weâ€™re Blueground, a global proptech company with several thousand move-in-ready apartments in a growing number of major cities around the world. With flexible terms and homes in vibrant, centrally based neighborhoods, youâ€™ll feel at home and free to roam for as long as you want â€” a month, a year, or longer.   Each apartment is thoughtfully designed with exclusive furnishings, fully equipped kitchens, and incredible amenities â€“ making every day a five-star experience. From day one, youâ€™ll enjoy high-speed Wi-Fi, premium linens, and smart home entertainment. Plus, access to pools, gyms, and outdoor spaces in select buildings.  Why stress over your apartment? We provide a hassle-free alternative â€” a consistent, quality guest experience that starts even before you arrive. Because we let you book our most up-to-date apartment listings online, confirm with a click, pay securely, and check in easily.   Even better? You can enhance your stay with car rentals, grocery delivery, laundry services, and more through our special partnerships.   During your stay Upon arrival, youâ€™ll either be greeted personally by a Blueground team member or given self-check-in instructions. The entire apartment is yours! Youâ€™ll enjoy reliable support via email, phone, and our Guest App, where you can request everything from a home cleaning to extra towels.   Weâ€™ll share all details upon confirmation of your stay.|within an hour    |99%               |97%                 |f                |https://a0.muscache.com/im/pictures/user/d0ad9599-6fc0-4be6-865e-ffe99142517c.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/d0ad9599-6fc0-4be6-865e-ffe99142517c.jpg?aki_policy=profile_x_medium|Cambridge         |5040               |5316                     |['email', 'phone', 'work_email']|t                   |t                     |San Francisco, California, United States|Marina                |                            |37.80366|-122.44518|Entire rental unit  |Entire home/apt|4           |1        |1 bath        |2       |2   |["Private entrance", "Bathtub", "Iron", "Refrigerator", "Coffee maker", "Dryer", "Smoke alarm", "Bed linens", "Hot water", "Oven", "Hair dryer", "Heating", "Dishwasher", "Self check-in", "TV", "Fast wifi \u2013 80 Mbps", "Hangers", "Long term stays allowed", "Microwave", "Carbon monoxide alarm", "Paid parking on premises", "Essentials", "Washer", "Shampoo", "Pets allowed", "Lockbox", "Kitchen"]|$246.00 |31            |1125          |31                    |365                   |1125                  |1125                  |36.4                  |1125                  |                |t               |6              |36             |66             |341             |3/7/2024             |0                |0                    |0                     |            |           |                    |                      |                         |                     |                           |                      |                   |              |f               |183                           |183                                        |0                                           |0                                          |                 |
|9.38E+17|https://www.airbnb.com/rooms/938317240177880784|2.02E+13 |3/7/2024    |city scrape    |Presidio Heights Condo - 2bdrm/2 bath       |Relax in very well appointed two bedroom/two bath condo with incredible views in safe, quiet Presidio Heights neighborhood, conveniently located near Laurel Village shopping center and top rated restaurants.|Quiet neighborhood with everything you need within a few blocks; Peet's, Starbucks, groceries, hardware, several boutique clothing retailers, top rated restaurants, art house movie theatre and more.  Close proximity to historic Presidio with endless hiking trails, museums, golf course and easy access to the Golden Gate Bridge.                                                                                                                                                                                                                                                                                                                                                                                                          |https://a0.muscache.com/pictures/miso/Hosting-938317240177880784/original/355ba39e-fe2f-47c0-aa1d-0999729311d8.jpeg|51769509|https://www.airbnb.com/users/show/51769509|Turner   |12/19/2015|San Francisco, CA   |Single, early riser, very clean                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |within a few hours|90%               |89%                 |t                |https://a0.muscache.com/im/pictures/user/565d1421-a3cd-4178-ae20-ff96b0d56993.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/565d1421-a3cd-4178-ae20-ff96b0d56993.jpg?aki_policy=profile_x_medium|Presidio Heights  |1                  |1                        |['email', 'phone']              |t                   |t                     |San Francisco, California, United States|Presidio Heights      |                            |37.78986|-122.45094|Entire condo        |Entire home/apt|4           |2        |2 baths       |2       |2   |["Thermador stainless steel single oven", "Central heating", "Free dryer \u2013 In unit", "Private entrance", "Bathtub", "Outdoor playground", "Coffee", "Barbecue utensils", "Sub-Zero refrigerator", "Toaster", "Mountain view", "Courtyard view", "Smoke alarm", "Board games", "First aid kit", "Park view", "Bed linens", "Clothing storage: closet and dresser", "Wolf gas stove", "Cleaning products", "Hot water", "Security cameras on property", "Portable fans", "60\" HDTV with Amazon Prime Video, Apple TV, Chromecast, Disney+, HBO Max, Netflix", "Smart lock", "Private patio or balcony", "Dedicated workspace", "Dishwasher", "Coffee maker: espresso machine, Keurig coffee machine", "Record player", "Self check-in", "Ocean view", "Hangers", "Microwave", "Bay view", "Garden view", "Cooking basics", "BBQ grill", "Essentials", "Wine glasses", "Washer", "Freezer", "Baking sheet", "Blender", "Dining table", "McIntosh sound system with aux", "Pets allowed", "Dishes and silverware", "Extra pillows and blankets", "Books and reading material", "Kitchen", "Free street parking", "Wifi"]|$328.00 |5             |365           |5                     |5                     |365                   |365                   |5                     |365                   |                |t               |1              |5              |23             |277             |3/7/2024             |12               |12                   |1                     |7/30/2023   |2/29/2024  |4.83                |4.83                  |4.67                     |5                    |4.75                       |5                     |4.83               |2023-006462STR|f               |1                             |1                                          |0                                           |0                                          |1.62             |
|24823466|https://www.airbnb.com/rooms/24823466|2.02E+13 |3/7/2024    |city scrape    |Live like a local in the heart of the City  |Stay and live in our home in Duboce Triangle while we are away this Summer. <br />Perfect place for someone who wants to relocate wants to explore the city or needs to find a permanent place in the Bay Area.|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |https://a0.muscache.com/pictures/airflow/Hosting-24823466/original/9c267454-8652-4754-8864-78c3e951bd08.jpg|10729940|https://www.airbnb.com/users/show/10729940|Claudia  |12/20/2013|San Francisco, CA   |Hello, Iâ€™m from Germany and Iâ€™m primarily a mother, wife, designer, yogi and part time instructor at the Academy of Art University. My husband JB is a designer from Switzerland and we have lived in San Francisco for more than 15 years. Stay with us in our live and work space and become part of our busy and creative household for a couple of days, weekends or even for a longer stretch of time to explore the city, to transition to a new home or simply getting to know the hidden gems of San Francisco. Get in touch - we love to share our place with you!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |within an hour    |100%              |100%                |f                |https://a0.muscache.com/im/pictures/user/7549e8f6-538a-4ce7-a303-b55be515d070.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/7549e8f6-538a-4ce7-a303-b55be515d070.jpg?aki_policy=profile_x_medium|Duboce Triangle   |2                  |4                        |['email', 'phone']              |t                   |t                     |                                        |Castro/Upper Market   |                            |37.766  |-122.43498|Private room in rental unit|Private room   |2           |1        |1 bath        |1       |1   |["Smoke alarm", "Hangers", "Lock on bedroom door", "Carbon monoxide alarm", "Private entrance", "Essentials", "Iron", "Washer", "Hair dryer", "Heating", "Shampoo", "Refrigerator", "Fire extinguisher", "Dedicated workspace", "Coffee maker", "Kitchen", "Dryer", "Wifi"]|$135.00 |30            |75            |30                    |30                    |75                    |75                    |30                    |75                    |                |t               |0              |0              |4              |172             |3/7/2024             |7                |2                    |0                     |7/16/2018   |8/8/2023   |5                   |5                     |4.57                     |4.86                 |5                          |4.86                  |4.71               |              |f               |2                             |0                                          |2                                           |0                                          |0.1              |
|53849558|https://www.airbnb.com/rooms/53849558|2.02E+13 |3/7/2024    |city scrape    |Stunning 1-Bedroom Loft in Clock Tower Building|Live like a local while residing in an iconic San Francisco landmark! Anyone who has driven across the Bay Bridge from SF to Oakland has seen the Cityâ€™s most visible and historic Clock Tower building off to the right; a building that once housed the largest printing company on the West coast.|NEIGHBORHOOD <br />Beyond conveniently located in the heart of SOMA in the South Beach neighborhood â€“ basically at the center of SFâ€™s tech universe. Walk just a few blocks to access fine dining, ample shopping, art galleries, Giants baseball stadium, financial district, Ferry building shops/dining, waterfront exercise/activities along the Embarcadero, entertainment venues, and many transit routes. Access wine country, the East Bay, Marin, or the South Bay easily via freeway access, which is only blocks away as well. Many tech bus routes to/from Silicone Valley also have stops in this neighborhood.                                                                                                                  |https://a0.muscache.com/pictures/445a165e-de89-4593-a8d9-671f7193bc37.jpg|3793516 |https://www.airbnb.com/users/show/3793516 |Audrey   |10/7/2012 |Oakland, CA         |I am a lover of design, travel and making a difference as an individual, as a means to create change in our ever evolving world.  I am an artist, property manager and designer, entrepreneur, lover of good food and good people.  I come from the hills of Pennsylvania followed by 20 years in New York City, before coming  west to find a more balanced, creative and authentic lifestyle in the San Francisco Bay area.  I enjoy refurbishing my 100-plus-year old triplex in Oakland with my partner and dogs, immersing myself in other cultures and countries, good food, small company performances, film festivals, architecture, art, fashion, sunny days, and social responsibility.   Let me know what else I can tell you.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |within an hour    |100%              |98%                 |t                |https://a0.muscache.com/im/pictures/user/779e7801-39cc-4747-a3b8-295004a3b3c4.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/779e7801-39cc-4747-a3b8-295004a3b3c4.jpg?aki_policy=profile_x_medium|Mosswood          |9                  |20                       |['email', 'phone', 'work_email']|t                   |t                     |San Francisco, California, United States|South of Market       |                            |37.78425|-122.39254|Entire condo        |Entire home/apt|2           |1        |1 bath        |1       |1   |["3n1 Everyone for Every Body Soap shampoo", "Central heating", "Free dryer \u2013 In unit", "Private entrance", "Hot water kettle", "Iron", "Elevator", "Coffee", "Refrigerator", "Host greets you", "Smoke alarm", "Luggage dropoff allowed", "First aid kit", "Bed linens", "Cleaning available during stay", "Outdoor furniture", "Outdoor dining area", "3n1 Everyone for Every Body Soap body soap", "Paid parking lot on premises \u2013 1 space", "Free washer \u2013 In unit", "Clothing storage: closet", "Cleaning products", "Stainless steel electric stove", "Hot water", "Shower gel", "Security cameras on property", "Hair dryer", "Laundromat nearby", "Dedicated workspace", "Dishwasher", "Free parking on premises", "Stainless steel oven", "Coffee maker: french press, Keurig coffee machine", "TV", "Long term stays allowed", "Hangers", "3n1 Everyone for Every Body Soap conditioner", "Microwave", "Carbon monoxide alarm", "Room-darkening shades", "Cooking basics", "Shared backyard \u2013 Fully fenced", "Essentials", "Wine glasses", "City skyline view", "Freezer", "Baking sheet", "Ceiling fan", "Dining table", "Dishes and silverware", "Extra pillows and blankets", "Books and reading material", "Kitchen", "Wifi"]|$175.00 |30            |1125          |30                    |30                    |1125                  |1125                  |30                    |1125                  |                |t               |0              |5              |35             |153             |3/7/2024             |7                |1                    |0                     |2/4/2022    |5/9/2023   |4.86                |5                     |5                        |5                    |5                          |4.71                  |4.71               |              |f               |2                             |2                                          |0                                           |0                                          |0.28             |
|20077154|https://www.airbnb.com/rooms/20077154|2.02E+13 |3/7/2024    |city scrape    |SF private room r                           |Small room in a quiet house with own lock and key.<br /><br />Share common area, kitchen and bathroom with Airbnb guest. Host does not use them.<br /><br />This an old 1900's house with uneven heights. If you are on the taller side, please reconsider a different location. <br /><br />Bathroom is small; if you are large or tall please reconsider. <br /><br />The neighborhood is quiet with the occasional dog walkers. <br /><br />Next to the spacious Balboa Park and police station. <br /><br />Next to bus J,K,M to downtown. 29, 49, BART.|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |https://a0.muscache.com/pictures/35ba3ce0-36ae-487c-8ba6-62aeda8da17b.jpg|66385869|https://www.airbnb.com/users/show/66385869|Bobby    |4/8/2016  |San Francisco, CA   |Welcome! I do animation and modeling. I speak English, ä¸­æ–‡, and gradually Espanol.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |within an hour    |100%              |93%                 |f                |https://a0.muscache.com/im/pictures/user/8db7ea04-47c6-43bc-9a62-23e2a8499da3.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/8db7ea04-47c6-43bc-9a62-23e2a8499da3.jpg?aki_policy=profile_x_medium|Mission Terrace   |5                  |12                       |['email', 'phone']              |t                   |t                     |                                        |Outer Mission         |                            |37.7249 |-122.43979|Private room in home|Private room   |1           |1        |1 shared bath |1       |1   |["Lock on bedroom door", "Essentials", "Hair dryer", "Heating", "Shampoo", "Kitchen", "Free street parking", "Wifi"]                                             |$60.00  |30            |1125          |30                    |30                    |1125                  |1125                  |30                    |1125                  |                |t               |29             |59             |89             |179             |3/7/2024             |7                |2                    |1                     |8/10/2018   |2/15/2024  |4.86                |4.86                  |4.29                     |4.86                 |4.86                       |4.86                  |4.86               |STR-0001337   |f               |2                             |0                                          |2                                           |0                                          |0.1              |
|30774802|https://www.airbnb.com/rooms/30774802|2.02E+13 |3/7/2024    |city scrape    |Modern New place & furnished  for Long term stay|Modern, high-end remodeled entire guest house in law in the warmest neighborhood in San Francisco city.  Few minutes get attractions spot/medical/schools.  Bedroom C will be available on 10/8/2023<br />With very low rate you can peremptorily own your comforting place.  High ceiling; comfortable living. Kitchen-stove, microwave, refrigerator.  Easy free street parking.  Very safe residential neighborhood. Amenity limitation Laundry and washer, fee$5. Please email me confirm room availability-booking.|5 Minutes walk to the John McLaren park.  Within 8 minutes to downtown SF or airport close to highway 101 and 280.   2 Block away from bus stop of 44, 54 .  Restaurants for breakfast/lunch /dinner just 10 minutes walk.  Generally this is a very safe area and the warm climate if you don't like cold weather all the time.                                                                                                                                                                                                                                                                                                                                                                                                                  |https://a0.muscache.com/pictures/airflow/Hosting-30774802/original/9fcb1730-ab09-4ddd-9827-b1d2f7c802ed.jpg|230265204|https://www.airbnb.com/users/show/230265204|Athena   |12/11/2018|San Francisco, CA   |I am people person and live in San Francisco for over 20 years. I enjoy reading books and traveling and of course good conversation.   I enjoy neighborhood hiking likes John McLaren park /trails, walk down to get fresh food in walking distance, and local restaurants . I am sure you choose the right place to stay in San Francisco which it is an amazing city.  You will love it!!  I will make sure you will have a good stay in my place and enjoy here                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |within an hour    |100%              |100%                |t                |https://a0.muscache.com/im/pictures/user/a3858200-b3fd-46c4-8f92-c894437e21a0.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/a3858200-b3fd-46c4-8f92-c894437e21a0.jpg?aki_policy=profile_x_medium|Excelsior         |4                  |4                        |['email', 'phone']              |t                   |t                     |San Francisco, California, United States|Excelsior             |                            |37.72682|-122.42159|Private room in guest suite|Private room   |1           |2        |2 shared baths|3       |3   |["Single level home", "Trash compactor", "Private entrance", "Hot water kettle", "Bathtub", "Iron", "Keypad", "Refrigerator", "Coffee maker", "Clothing storage", "Dryer", "Toaster", "Smoke alarm", "Safe", "Air conditioning", "First aid kit", "Bed linens", "TV with standard cable", "Hot water", "Security cameras on property", "Oven", "Hair dryer", "Heating", "Patio or balcony", "Pocket wifi", "Stove", "Self check-in", "Long term stays allowed", "Hangers", "Microwave", "Carbon monoxide alarm", "Room-darkening shades", "Cooking basics", "Essentials", "Washer", "Shampoo", "Freezer", "Dining table", "Dishes and silverware", "Extra pillows and blankets", "Kitchen", "Children\u2019s books and toys", "Free street parking", "Wifi"]|$40.00  |30            |180           |30                    |30                    |1125                  |1125                  |30                    |1125                  |                |t               |13             |43             |49             |265             |3/7/2024             |48               |0                    |0                     |1/19/2019   |9/11/2022  |4.85                |4.92                  |4.94                     |5                    |4.9                        |4.71                  |4.71               |1096490       |t               |4                             |0                                          |4                                           |0                                          |0.77             |


### Data Srubbing
I used a python code to select several columns that are relevent for this assignment and delete those that are irrelevant. The python code can be found here at [data_scrubbing](/data_scrubbing.py). 

After the first step, the data only includes **'id','name','host_id','host_name','host_is_superhost','neighbourhood','neighbourhood_group_cleansed','price','beds','review_scores_rating'**. 


## Data Analysis
1. show exactly two documents from the `listings` collection in any order. I showed the first two documents from the 'listings' collection. Here are the input and the output.
```
db.listings.find().limit(2)
```
```
[
  {
    _id: ObjectId('660e0bf4b6515eb2057989a0'),
    id: 24823466,
    name: 'Live like a local in the heart of the City',
    host_id: 10729940,
    host_name: 'Claudia',
    host_is_superhost: 'f',
    neighbourhood: '',
    neighbourhood_group_cleansed: '',
    price: '$135.00',
    beds: 1,
    review_scores_rating: 5
  },
  {
    _id: ObjectId('660e0bf4b6515eb2057989a1'),
    id: 53849558,
    name: 'Stunning 1-Bedroom Loft in Clock Tower Building',
    host_id: 3793516,
    host_name: 'Audrey',
    host_is_superhost: 't',
    neighbourhood: 'San Francisco, California, United States',
    neighbourhood_group_cleansed: '',
    price: '$175.00',
    beds: 1,
    review_scores_rating: 4.86
  }
]
```

2. show exactly 10 documents in any order, but "prettyprint" in easier to read format, using the `pretty()` function.
```
db.listings.find().limit(10).pretty()
```
```
[
  {
    _id: ObjectId('660e0bf4b6515eb2057989a0'),
    id: 24823466,
    name: 'Live like a local in the heart of the City',
    host_id: 10729940,
    host_name: 'Claudia',
    host_is_superhost: 'f',
    neighbourhood: '',
    neighbourhood_group_cleansed: '',
    price: '$135.00',
    beds: 1,
    review_scores_rating: 5
  },
  {
    _id: ObjectId('660e0bf4b6515eb2057989a1'),
    id: 53849558,
    name: 'Stunning 1-Bedroom Loft in Clock Tower Building',
    host_id: 3793516,
    host_name: 'Audrey',
    host_is_superhost: 't',
    neighbourhood: 'San Francisco, California, United States',
    neighbourhood_group_cleansed: '',
    price: '$175.00',
    beds: 1,
    review_scores_rating: 4.86
  },
  {
    _id: ObjectId('660e0bf4b6515eb2057989a2'),
    id: 20077154,
    name: 'SF private room r',
    host_id: 66385869,
    host_name: 'Bobby',
    host_is_superhost: 'f',
    neighbourhood: '',
    neighbourhood_group_cleansed: '',
    price: '$60.00',
    beds: 1,
    review_scores_rating: 4.86
  },
  {
    _id: ObjectId('660e0bf4b6515eb2057989a3'),
    id: 30774802,
    name: 'Modern New place & furnished  for Long term stay',
    host_id: 230265204,
    host_name: 'Athena',
    host_is_superhost: 't',
    neighbourhood: 'San Francisco, California, United States',
    neighbourhood_group_cleansed: '',
    price: '$40.00',
    beds: 3,
    review_scores_rating: 4.85
  },
  {
    _id: ObjectId('660e0bf4b6515eb2057989a4'),
    id: 415498,
    name: 'Prime Location - Studio Apartment',
    host_id: 216682,
    host_name: 'Jay',
    host_is_superhost: 'f',
    neighbourhood: '',
    neighbourhood_group_cleansed: '',
    price: '$80.00',
    beds: 1,
    review_scores_rating: 4.79
  },
  {
    _id: ObjectId('660e0bf4b6515eb2057989a5'),
    id: Long('725479609346985276'),
    name: '546D - Large Master Bedroom w/ Private Bath Fits 4',
    host_id: 122429357,
    host_name: 'Irene',
    host_is_superhost: 'f',
    neighbourhood: '',
    neighbourhood_group_cleansed: '',
    price: '$61.00',
    beds: 2,
    review_scores_rating: 4.75
  },
  {
    _id: ObjectId('660e0bf4b6515eb2057989a6'),
    id: 3442439,
    name: 'Spacious Bernal Heights In-law with private entry.',
    host_id: 17349647,
    host_name: 'Candace And Joshua',
    host_is_superhost: 't',
    neighbourhood: 'San Francisco, California, United States',
    neighbourhood_group_cleansed: '',
    price: '$125.00',
    beds: 1,
    review_scores_rating: 4.96
  },
  {
    _id: ObjectId('660e0bf4b6515eb2057989a7'),
    id: 2802480,
    name: 'Marina Modern 2BR (30 day min)',
    host_id: 14333760,
    host_name: 'Alessandra',
    host_is_superhost: 'f',
    neighbourhood: 'San Francisco, California, United States',
    neighbourhood_group_cleansed: '',
    price: '$285.00',
    beds: 2,
    review_scores_rating: 4.76
  },
  {
    _id: ObjectId('660e0bf4b6515eb2057989a8'),
    id: Long('648549709021440854'),
    name: 'LuxoStays | ! Quiet Rm #Private Bathrm & VIEW',
    host_id: 226555948,
    host_name: "Gi'Angelo",
    host_is_superhost: 'f',
    neighbourhood: 'San Francisco, California, United States',
    neighbourhood_group_cleansed: '',
    price: '$69.00',
    beds: 1,
    review_scores_rating: 5
  },
  {
    _id: ObjectId('660e0bf4b6515eb2057989a9'),
    id: 25376401,
    name: 'Cheerful Suite w/ Garden, Steps from Dolores Park',
    host_id: 113405017,
    host_name: 'Russell',
    host_is_superhost: 't',
    neighbourhood: 'San Francisco, California, United States',
    neighbourhood_group_cleansed: '',
    price: '$208.00',
    beds: 1,
    review_scores_rating: 4.95
  }
]
```

3. choose two hosts (by reffering to their `host_id` values) who are superhosts (available in the `host_is_superhost` field), and show all of the listings offered by both of the two hosts
   - only show the `name`, `price`, `neighbourhood`, `host_name`, and `host_is_superhost` for each result
```
db.listings.find({ "host_is_superhost": "t" }, { "host_id": 1 }).limit(2)
```
```
[
  { _id: ObjectId('660e0bf4b6515eb2057989a1'), host_id: 3793516 },
  { _id: ObjectId('660e0bf4b6515eb2057989a3'), host_id: 230265204 }
]
```
```
db.listings.find({host_is_superhost:"t", "host_id": { $in: [3793516, 230265204] }},{"name": 1, "price": 1, "neighbourhood": 1, "host_name": 1, "host_is_superhost": 1, "_id": 0})
```
```
[
  {
    name: 'Stunning 1-Bedroom Loft in Clock Tower Building',
    host_name: 'Audrey',
    host_is_superhost: 't',
    neighbourhood: 'San Francisco, California, United States',
    price: '$175.00'
  },
  {
    name: 'Modern New place & furnished  for Long term stay',
    host_name: 'Athena',
    host_is_superhost: 't',
    neighbourhood: 'San Francisco, California, United States',
    price: '$40.00'
  },
  {
    name: 'Brand New High end private room for long term stay',
    host_name: 'Athena',
    host_is_superhost: 't',
    neighbourhood: 'San Francisco, California, United States',
    price: '$45.00'
  },
  {
    name: 'Modern Room A with/private bath in San Francisco',
    host_name: 'Athena',
    host_is_superhost: 't',
    neighbourhood: 'San Francisco, California, United States',
    price: '$55.00'
  },
  {
    name: 'Modern Oasis Brand New Guest Suite',
    host_name: 'Athena',
    host_is_superhost: 't',
    neighbourhood: 'San Francisco, California, United States',
    price: '$106.00'
  }
]
```

4. find all the unique `host_name` values (see [the docs](https://docs.mongodb.com/manual/reference/method/db.collection.distinct/))
```
db.listings.distinct("host_name")
```
```
[
  '1906 Mission',     'A',                     'AC And Linda',
  'Aabid',            'Aaron',                 'Abel',
  'Abhay',            'Abhi',                  'Abla',
  'Abrasha & Maria',  'Ac',                    'Ada',
  'Adam',             'Adam N Alex',           'Adam&Roz',
  'Adamjake',         'Adell',                 'Aditi',
  'Adrian',           'Adriana',               'Afshin',
  'Ahmad',            'Ahmed',                 'Aida',
  'Aidan',            'Aiden',                 'Aileen',
  'Aimee',            'Air Concierge',         'Aisling',
  'Aj',               'Aja',                   'Ajay',
  'Akshay',           'Al',                    'Alan',
  'Albert',           'Albina',                'Ale',
  'Alejandro',        'Alejandro (Alex)',      'Alek',
  'Alekhya',          'Aleksandra',            'Alene',
  'Alessandra',       'Alex',                  'Alex & Daniel',
  'Alex & Lina',      'Alexander And Heather', 'Alexandra',
  'Alexia',           'Alice',                 'Alice & Ahmed',
  'Alice/Peter',      'Alireza',               'Alison',
  'Alissa',           'Aljosha',               'Allen',
  'Allen Palomino &', 'Allison',               'Alok',
  'Alvaro',           'Alyssa',                'Amal',
  'Amanda',           'Amber',                 'Ambrish',
  'Ame',              'Amelie',                'Amina And Olivier',
  'Amir',             'Amir Hossein',          'Amit',
  'Amol',             'Amsi',                  'Amy',
  'Amy& Michael',     'An Elegant Hotel',      'Ana',
  'Andi',             'Andre',                 'Andrea',
  'Andrea & Luong',   'Andreas',               'Andrew',
  'Andrews Hotel',    'Andy',                  'Angela',
  'Angelica',         'Angeline',              'Angella',
  'Angelo',           'Angie',                 'Ani',
  'Aniket',           'Anil',                  'Anirudh',
  'Anita',
  ... 1810 more items
]
```
5. find all of the places that have more than 2 `beds` in a neighborhood of your choice (referred to as either the `neighborhood` or `neighbourhood_group_cleansed` fields in the data file), ordered by `review_scores_rating` descending
   - only show the `name`, `beds`, `review_scores_rating`, and `price`
   - if your data set only has blanks for all the neighborhood-related fields, or only one neighborhood value in all documents, you may pick another field to filter by - include an explanation and justification for this in your report.
   - if you run out of memory for this query, try filtering `review_scores_rating` that aren't empty (`$ne`); and lastly, if there's still an issue, you can set the `beds` to match exactly 2.
```
db.listings.distinct("neighbourhood")
```
```
[
  '',
  'Noe Valley - San Francisco, California, United States',
  'San Francisco, California, United States',
  'San Francisco, Hayes Valley, California, United States',
  'san francisco, California, United States'
]
```
```
db.listings.countDocuments({neighbourhood:"San Francisco, California, United States"})
```
```
4502
```
```
db.listings.find({neighbourhood:"San Francisco, California, United States",beds:{$gt:2}},{_id:0,name:1,beds:1,review_scores_rating:1,price:1}).sort({review_scores_rating:-1})
```
```
[
  {
    name: 'Gorgeous Seaside View Home w Deck, Piano',
    price: '$294.00',
    beds: 3,
    review_scores_rating: 5
  },
  {
    name: 'Chic Urban Oasis with Views near Bernal Peak',
    price: '$327.00',
    beds: 7,
    review_scores_rating: 5
  },
  {
    name: 'Spacious Luxury 2BD Loft in Downtown San Francisco',
    price: '$250.00',
    beds: 3,
    review_scores_rating: 5
  },
  {
    name: '2+BR Noe Valley Home w/ Garden',
    price: '$140.00',
    beds: 3,
    review_scores_rating: 5
  },
  {
    name: 'Wyndham Canterbury Resort | 2BR/1BA Queen Suite',
    price: '$262.00',
    beds: 3,
    review_scores_rating: 5
  },
  {
    name: 'Wyndham Canterbury Resort | 2BR/1BA Queen Suite',
    price: '$262.00',
    beds: 3,
    review_scores_rating: 5
  },
  {
    name: '3BR Family Home in Cole Valley',
    price: '$395.00',
    beds: 3,
    review_scores_rating: 5
  },
  {
    name: 'Telegraph Hill Shangri-La',
    price: '$697.00',
    beds: 3,
    review_scores_rating: 5
  },
  {
    name: '3bd Close to BART & Glen Park',
    price: '$160.00',
    beds: 3,
    review_scores_rating: 5
  },
  {
    name: 'Luxurious and Modern Mission District Stunner!',
    price: '$199.00',
    beds: 3,
    review_scores_rating: 5
  },
  {
    name: 'Awesome View San Francisco !',
    price: '$395.00',
    beds: 3,
    review_scores_rating: 5
  },
  {
    name: '"Market Street Hideaway: Ferry & SoMa Gateway"',
    price: '$186.00',
    beds: 5,
    review_scores_rating: 5
  },
  {
    name: 'Historic 1924 Getaway in the Heart of Russian Hill',
    price: '$245.00',
    beds: 3,
    review_scores_rating: 5
  },
  {
    name: "Welcome To *The Suites at Fisherman's Wharf* 2B#2",
    price: '$249.00',
    beds: 3,
    review_scores_rating: 5
  },
  {
    name: 'Spacious, family friendly apartment near park',
    price: '$300.00',
    beds: 3,
    review_scores_rating: 5
  },
  {
    name: 'GoldenGatePrk-2 miles, Nr Ocean, Zoo, SFSU &SGrove',
    price: '$199.00',
    beds: 3,
    review_scores_rating: 5
  },
  {
    name: 'Stunning Noe Family Friendly House - Enhanced Cleaning',
    price: '$1,095.00',
    beds: 4,
    review_scores_rating: 5
  },
  {
    name: 'Penthouse on the Crest of Buena Vista Park-2bd/2ba',
    price: '$245.00',
    beds: 3,
    review_scores_rating: 5
  },
  {
    name: 'Sunnyside Cinema: King bed + 2 twin, 2 desks, yard',
    price: '$160.00',
    beds: 3,
    review_scores_rating: 5
  },
  {
    name: 'Luxurious Modern - Perfect for Discerning Traveler',
    price: '$324.00',
    beds: 3,
    review_scores_rating: 5
  }
]
Type "it" for more
```
6. show the number of listings per host
```
db.listings.aggregate({$group:{_id:"$host_id",listingCount:{$sum:1}}})
```
```
[
  { _id: 863303, listingCount: 1 },
  { _id: 331649, listingCount: 1 },
  { _id: 209073328, listingCount: 1 },
  { _id: 4338310, listingCount: 1 },
  { _id: 529515158, listingCount: 1 },
  { _id: 200818212, listingCount: 1 },
  { _id: 1932164, listingCount: 1 },
  { _id: 278593931, listingCount: 1 },
  { _id: 99291678, listingCount: 1 },
  { _id: 40993834, listingCount: 1 },
  { _id: 21226960, listingCount: 1 },
  { _id: 48785800, listingCount: 1 },
  { _id: 286153436, listingCount: 1 },
  { _id: 29123496, listingCount: 1 },
  { _id: 10255173, listingCount: 1 },
  { _id: 174792040, listingCount: 9 },
  { _id: 4587045, listingCount: 1 },
  { _id: 395372745, listingCount: 1 },
  { _id: 16266881, listingCount: 1 },
  { _id: 4769424, listingCount: 1 }
]
Type "it" for more
```
7. find the average `review_scores_rating` per neighborhood, and only show those that are `4` or above, sorted in descending order of rating (see [the docs](https://docs.mongodb.com/manual/reference/operator/aggregation/sort/))
   - if your data set only has blanks in the neighborhood-related fields, or only one neighborhood value in all documents, you may pick another field to break down the listings by - include an explanation and justification for this in your report.
- use bed count because there is only one big neighbourhood in SF.
```
jw6441> db.listings.countDocuments({})
6198
jw6441> db.listings.countDocuments({neighbourhood:"San Francisco, California, United States"})
4502
jw6441> db.listings.countDocuments({neighbourhood:"san francisco, California, United States"})
1
jw6441> db.listings.countDocuments({neighbourhood:"Noe Valley - San Francisco, California, United States"})
1
jw6441> db.listings.countDocuments({neighbourhood:"San Francisco, Hayes Valley, California, United States"})
1
jw6441> db.listings.countDocuments({neighbourhood:""})
1693

```
```
db.listings.aggregate([
  {
      review_scores_rating: { $exists: true },
    $match: {
      review_scores_rating: { $exists: true },
      beds: { $exists: true, $gt: 0 }
    }
  },
  {
    $group: {
      _id: "$beds",
      averageRating: { $avg: "$review_scores_rating" }
    }
  },
  {
    $match: {
      averageRating: { $gte: 4 }
    }
  },
  {
    $sort: { averageRating: -1 }
  }
])

```
```
[
  { _id: 12, averageRating: 4.993333333333333 },
  { _id: 10, averageRating: 4.963333333333334 },
  { _id: 6, averageRating: 4.877857142857143 },
  { _id: 9, averageRating: 4.875 },
  { _id: 7, averageRating: 4.865882352941177 },
  { _id: 4, averageRating: 4.861180811808119 },
  { _id: 8, averageRating: 4.846 },
  { _id: 3, averageRating: 4.844020979020979 },
  { _id: 2, averageRating: 4.837755261106781 },
  { _id: 5, averageRating: 4.8221978021978025 },
  { _id: 1, averageRating: 4.69306309751434 }
]
```

We can see that the more beds in an AirBnB, the more likely it is going to have a higher rating. This is probably due to the fact that more beds means a bigger house and probably also have a better quality. 
AirBnB with one bed have the lower ratings, probably due to the limited space of the room and it's possible that people have to share a common space with other consumers for those rooms. 