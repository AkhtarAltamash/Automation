# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time

# url = "https://sportslumo.com/cricket/players/country/pakistan/#google_vignette"

# # Initialize the Selenium webdriver (you need to download chromedriver and provide its path)
# driver = webdriver.Chrome("path/to/chromedriver")

# # Load the webpage
# driver.get(url)

# # Allow some time for dynamic content to load (you might need to adjust this)
# time.sleep(5)

# # Get the HTML content after the page has loaded
# html_content = driver.page_source

# # Close the browser
# driver.quit()

# # Parse the HTML content with BeautifulSoup
# soup = BeautifulSoup(html_content, "html.parser")

# players_list = []

# # Assuming player details are within a specific class or tag, modify this based on the actual HTML structure
# player_elements = soup.find_all("div", class_="player-card")

# for player_element in player_elements:
#     player_details = {}

#     # Extracting data based on the HTML structure
#     player_details["Name"] = player_element.find("div", class_="player-info").find("h3").text.strip()
#     player_details["Country"] = "Pakistan"  # Since we're scraping Pakistan players
#     player_details["Date of Birth"] = player_element.find("div", class_="player-info").find("div", text="Date of Birth:").find_next_sibling("div").text.strip()
#     player_details["Batting Style"] = player_element.find("div", class_="player-info").find("div", text="Batting Style:").find_next_sibling("div").text.strip()
#     player_details["Bowling Arm"] = player_element.find("div", class_="player-info").find("div", text="Bowling Arm:").find_next_sibling("div").text.strip()
#     player_details["Bowling Style"] = player_element.find("div", class_="player-info").find("div", text="Bowling Style:").find_next_sibling("div").text.strip()
#     player_details["Team"] = player_element.find("div", class_="team").text.strip()
#     player_details["ICC Ranking"] = player_element.find("div", class_="player-info").find("div", text="ICC Ranking:").find_next_sibling("div").text.strip()

#     players_list.append(player_details)

# # Print or further process the extracted data
# for player in players_list:
#     print(player)

# _______________________

# import requests
# from bs4 import BeautifulSoup

# url = 'https://sportslumo.com/cricket/players/country/pakistan/#google_vignette'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')

# players = soup.select('.player-card')

# for player in players:
#     name = player.select_one('.player-name').text
#     country = player.select_one('.player-country').text
#     dob = player.select_one('.player-dob').text
#     bat_style = player.select_one('.player-bat-style').text
#     bowl_arm = player.select_one('.player-bowl-arm').text
#     bowl_style = player.select_one('.player-bowl-style').text
#     team = player.select_one('.player-team').text
#     icc_ranking = player.select_one('.player-icc-ranking').text

#     print(f'Name: {name}')
#     print(f'Country: {country}')
#     print(f'Date of Birth: {dob}')
#     print(f'Batting Style: {bat_style}')
#     print(f'Bowling Arm: {bowl_arm}')
#     print(f'Bowling Style: {bowl_style}')
#     print(f'Team: {team}')
#     print(f'ICC Ranking: {icc_ranking}')
#     print()



# _____________________


# from selenium import webdriver

# # Set up the web driver
# driver = webdriver.Chrome()  # Use the appropriate driver for your preferred browser

# # Navigate to the webpage
# driver.get('https://sportslumo.com/cricket/players/country/pakistan/')  # Replace with your desired URL

# # Extract the title of the webpage
# page_title = driver.title
# print("Page Title:", page_title)

# # Extract other data using appropriate Selenium commands (e.g., find_element_by_xpath, find_element_by_id, etc.)

# # Close the web driver
# driver.quit()


# _____________________
# ____________BEST_____________

# import requests
# from bs4 import BeautifulSoup

# url = "https://sportslumo.com/cricket/players/country/pakistan/"
# response = requests.get(url)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # Find all divs with class "col-md-10"
#     divs = soup.find_all('div', class_='col-md-10')
    
#     for div in divs:
#         # Extract and print the details from each div
#         details = div.get_text(strip=True)
#         print(details)
# else:
#     print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# ______________________ANOTHER BEST____________________
# import requests
# from bs4 import BeautifulSoup

# url = "https://sportslumo.com/cricket/players/country/pakistan/"
# response = requests.get(url)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     divs = soup.find_all('div', class_='col-md-10')
    
#     for div in divs:
#         # Extracting specific details from each div
#         name = div.find('div', class_='player-name').get_text(strip=True)

#         # Extracting country information from the div with class 'col-md-6 pl-0'
#         country_div = div.find('div', class_='col-md-6 pl-0')
#         country = country_div.find('td', class_='dark-text-val').get_text(strip=True) if country_div else "N/A"
        
#         age_div = div.find('div', class_='col-md-6 pl-0')
#         age_info = age_div.find('td', class_='dark-text-val').get_text(strip=True) if age_div else "N/A"
#         age = age_info.split('(')[0].strip() if age_info else "N/A"

#         bat_style_div = div.find('div', class_='col-md-6 pl-0')
#         bat_style = bat_style_div.find('td', class_='dark-text-val').get_text(strip=True) if bat_style_div else "N/A"


#         bowling_style_div = div.find('div', class_='col-md-6')
#         bowling_style = bowling_style_div.find('td', class_='dark-text-val').get_text(strip=True) if bowling_style_div else "N/A"
        
#         team_div = div.find('div', class_='col-md-6')
#         team = team_div.find('td', class_='dark-text-val').get_text(strip=True) if team_div else "N/A"

#         icc_ranking_div = div.find('div', class_='col-md-6')
#         icc_ranking = icc_ranking_div.find('td', class_='dark-text-val').get_text(strip=True) if icc_ranking_div else "N/A"
        
#         # Print or store the extracted details
#         print(f"Name: {name}")
#         print(f"Country: {country}")
#         print(f"Age: {age}")
#         print(f"Bat Style: {bat_style}")
#         print(f"Bowling Style: {bowling_style}")
#         print(f"Team: {team}")
#         print(f"ICC Ranking: {icc_ranking}")
#         print("\n")
# else:
#     print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# _______________________


# import requests
# from bs4 import BeautifulSoup

# url = "https://sportslumo.com/cricket/players/country/pakistan/"
# response = requests.get(url)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     divs = soup.find_all('div', class_='col-md-10')
    
#     for div in divs:
#         # Extracting specific details from each div
#         name = div.find('div', class_='player-name').get_text(strip=True)

#         # Extracting country information from the div with class 'col-md-6 pl-0'
#         country_div = div.find('div', class_='col-md-6 pl-0')
#         country = country_div.find('td', class_='dark-text-val').get_text(strip=True) if country_div else "N/A"
        
#         age_div = div.find('div', class_='col-md-6 pl-0')
#         age_info = age_div.find('td', class_='dark-text-val').get_text(strip=True) if age_div else "N/A"
#         age = age_info.split('(')[0].strip() if age_info else "N/A"

#         bat_style_div = div.find('div', class_='col-md-6 pl-0')
#         bat_style = bat_style_div.find('td', class_='dark-text-val').get_text(strip=True) if bat_style_div else "N/A"


#         bowling_style_div = div.find('div', class_='col-md-6')
#         bowling_style = bowling_style_div.find('td', class_='dark-text-val').get_text(strip=True) if bowling_style_div else "N/A"
        
#         team_div = div.find('div', class_='col-md-6')
#         team = team_div.find('td', class_='dark-text-val').get_text(strip=True) if team_div else "N/A"

#         icc_ranking_div = div.find('div', class_='col-md-6')
#         icc_ranking = icc_ranking_div.find('td', class_='dark-text-val').get_text(strip=True) if icc_ranking_div else "N/A"
        
#         # Print or store the extracted details
#         print(f"Name: {name}")
#         print(f"Country: {country}")
#         print(f"Age: {age}")
#         print(f"Bat Style: {bat_style}")
#         print(f"Bowling Style: {bowling_style}")
#         print(f"Team: {team}")
#         print(f"ICC Ranking: {icc_ranking}")
#         print("\n")
# else:
#     print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
# _________________________________________

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# url = "https://sportslumo.com/cricket/players/country/pakistan/"
# response = requests.get(url)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')

#     divs = soup.find_all('div', class_='player-box')

#     data = []

#     for div in divs:
#         name = div.find('div', class_='player-name').get_text(strip=True)

#         # Extracting information from the div's text content
#         country = div.find('td', text='Country:').find_next('td').get_text(strip=True) if div.find('td', text='Country:') else "N/A"
#         age = div.find('td', text='Age:').find_next('td').get_text(strip=True) if div.find('td', text='Age:') else "N/A"
#         bat_style = div.find('td', text='Bat Style:').find_next('td').get_text(strip=True) if div.find('td', text='Bat Style:') else "N/A"
#         bowling_style = div.find('td', text='Bowling Style:').find_next('td').get_text(strip=True) if div.find('td', text='Bowling Style:') else "N/A"
#         team = div.find('td', text='Team:').find_next('td').get_text(strip=True) if div.find('td', text='Team:') else "N/A"
#         icc_ranking = div.find('td', text='ICC Ranking:').find_next('td').get_text(strip=True) if div.find('td', text='ICC Ranking:') else "N/A"

#         data.append((name, country, age, bat_style, bowling_style, team, icc_ranking))

#     # Creating a pandas DataFrame from the extracted data using zip
#     df = pd.DataFrame(list(zip(*data)), columns=["Name", "Country", "Age", "Bat Style", "Bowling Style", "Team", "ICC Ranking"])

#     # Saving the DataFrame to an Excel file
#     df.to_excel("C:/Users/H A Computer/Desktop/pak_team.xlsx", index=False)

#     print("Excel file created successfully.")
# else:
#     print(f"Failed to retrieve the webpage. Status code: {response.status_code}")


# ________________________________ BEST ____________


# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# base_url = "https://sportslumo.com/cricket/players/country/pakistan/page/"
# excel_path = "C:/Users/H A Computer/Desktop/pak_team.xlsx"

# data = []

# for page_number in range(1, 6):  # Assuming there are 5 pages, adjust as needed
#     url = f"{base_url}{page_number}/"
#     response = requests.get(url)

#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         divs = soup.find_all('div', class_='col-md-10')

#         for div in divs:
#             # Extracting specific details from each div
#             name = div.find('div', class_='player-name').get_text(strip=True)
#             country_div = div.find('div', class_='col-md-6 pl-0')
#             country = country_div.find('td', class_='dark-text-val').get_text(strip=True) if country_div else "N/A"
#             age_container = div.find('td', class_='light-text-para', string='Age')
#             age_value = age_container.find_next('td', class_='dark-text-val').get_text(strip=True) if age_container else "N/A"
#             bat_style_container = div.find('td', class_='light-text-para', string='Bat Style')
#             bat_style = bat_style_container.find_next('td', class_='dark-text-val').get_text(strip=True) if bat_style_container else "N/A"
#             bowling_style_container = div.find('td', class_='light-text-para', string='Bowl Style')
#             bowling_style = bowling_style_container.find_next('td', class_='dark-text-val').get_text(strip=True) if bowling_style_container else "N/A"
#             team_container = div.find('td', class_='light-text-para', string='Team')
#             team = team_container.find_next('td', class_='dark-text-val').get_text(strip=True) if team_container else "N/A"
#             icc_ranking_container = div.find('td', class_='light-text-para', string='ICC Ranking')
#             icc_ranking = icc_ranking_container.find_next('td', class_='dark-text-val').get_text(strip=True) if icc_ranking_container else "N/A"

#             # Store the extracted details in a dictionary
#             player_data = {
#                 "Name": name,
#                 "Country": country,
#                 "Age": age_value,
#                 "Bat Style": bat_style,
#                 "Bowling Style": bowling_style,
#                 "Team": team,
#                 "ICC Ranking": icc_ranking
#             }

#             data.append(player_data)

#         print(f"Page {page_number} data extracted.")
#     else:
#         print(f"Failed to retrieve the webpage for page {page_number}. Status code: {response.status_code}")

# # Create a DataFrame from the list of dictionaries
# df = pd.DataFrame(data)

# # Export the DataFrame to an Excel file
# df.to_excel(excel_path, index=False)

# print(f"Data exported to {excel_path}")


# __________________________

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime

base_url = "https://sportslumo.com/cricket/players/country/pakistan/page/"
excel_path = "C:/Users/H A Computer/Desktop/pak_team.xlsx"

data = []

for page_number in range(1, 6):  # Assuming there are 5 pages, adjust as needed
    url = f"{base_url}{page_number}/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        divs = soup.find_all('div', class_='col-md-10')

        for div in divs:
            # Extracting specific details from each div
            name = div.find('div', class_='player-name').get_text(strip=True)
            country_div = div.find('div', class_='col-md-6 pl-0')
            country = country_div.find('td', class_='dark-text-val').get_text(strip=True) if country_div else "N/A"

            age_container = div.find('td', class_='light-text-para', string='Age')
            age_td = age_container.find_next('td', class_='dark-text-val') if age_container else None
            age_value = age_td.get_text(strip=True) if age_td else "N/A"

            # Extracting the date in DD/MM/YYYY format
            date_str = age_value.split("(")[1].split(")")[0]
            date_object = datetime.strptime(date_str, "%d %b, %Y")
            formatted_date = date_object.strftime("%d/%m/%Y")

            # Check if age_value is not "N/A" and not None before formatting
            formatted_age = formatted_date if age_value != "N/A" and age_value is not None else "N/A"

            bat_style_container = div.find('td', class_='light-text-para', string='Bat Style')
            bat_style = bat_style_container.find_next('td', class_='dark-text-val').get_text(strip=True) if bat_style_container else "N/A"

            

            
            # Extracting the batting hand preference and dropping "bat"
            hand_preferences = [style.split(" bat")[0].split()[-1] for style in bat_style.split(",")]

            # Join the hand preferences into a single string
            hand_preference_string = ', '.join(hand_preferences)

            # print(hand_preference_string)

            bowling_style_container = div.find('td', class_='light-text-para', string='Bowl Style')
            bowling_style = bowling_style_container.find_next('td', class_='dark-text-val').get_text(strip=True) if bowling_style_container else "N/A"
            bowling_arm =""
            if "right-arm" in bowling_style:
                bowling_arm = 'Right'
            elif "left-arm" in bowling_style:
                bowling_arm = 'Left'
            else:
                bowling_arm = "Unknown"


            if "fast" in bowling_style or "medium" in bowling_style:
                bowling_style = 'Pace' 
            elif "orthodox" in bowling_style or "offbreak" in bowling_style or "legbreak" in bowling_style or "wrist-spin" in bowling_style:
                bowling_style ='Spin'

                
            team_container = div.find('td', class_='light-text-para', string='Team')
            team = team_container.find_next('td', class_='dark-text-val').get_text(strip=True) if team_container else "N/A"
            psl_teams = ["Karachi Kings", "Islamabad United", "Lahore Qalandars", "Multan Sultans", "Peshawar Zalmi", "Quetta Gladiators"]

            team = re.findall(r'\b(?:' + '|'.join(psl_teams) + r')\b', team)

            icc_ranking_container = div.find('td', class_='light-text-para', string='ICC Ranking')
            icc_ranking_text = icc_ranking_container.find_next('td', class_='dark-text-val').get_text(strip=True) if icc_ranking_container else "N/A"

            # Extract numeric values from ICC ranking text using regular expression
            icc_ranking_values = [int(value) for value in re.findall(r'\d+', icc_ranking_text)]

            # Create a dictionary with the required format
            icc_ranking_dict = {
                'T20 Bat': icc_ranking_values[0] if len(icc_ranking_values) > 0 else None,
                'ODI Bat': icc_ranking_values[1] if len(icc_ranking_values) > 1 else None,
                'Test Bat': icc_ranking_values[2] if len(icc_ranking_values) > 2 else None,
                'Test Bowl': icc_ranking_values[3] if len(icc_ranking_values) > 3 else None,
                'All Rounder': icc_ranking_values[4] if len(icc_ranking_values) > 4 else None
            }

            # Store the extracted details in a dictionary
            player_data = {
                "Name": name,
                "Country": country,
                "Age": formatted_age,
                "Bat Style": bat_style,
                "Bowling Arm" :bowling_arm,
                "Bowling Style": bowling_style,
                "Team": team,
                "ICC_Ranking": icc_ranking_dict
            }

            data.append(player_data)

        print(f"Page {page_number} data extracted.")
    else:
        print(f"Failed to retrieve the webpage for page {page_number}. Status code: {response.status_code}")

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Export the DataFrame to an Excel file
df.to_excel(excel_path, index=False)

print(f"Data exported to {excel_path}")
