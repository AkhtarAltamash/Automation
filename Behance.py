# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# import pandas as pd
# import time

# # Replace these lines with the path to your ChromeDriver executable
# chromedriver_path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
# chrome_profile_name = 'Profile 4'
# user_data_path = r'C:\Users\ABC\AppData\Local\Google\Chrome\User Data'

# # Create a ChromeOptions object and set the user data directory
# # chrome_options = Options()
# # chrome_options.add_argument(f'--user-data-dir={user_data_path}')
# # chrome_options.add_argument(f'--profile-directory={chrome_profile_name}')

# # Create a new instance of the Chrome webdriver with options
# driver = webdriver.Chrome()

# # Maximize the browser window
# driver.maximize_window()

# # Open Behance login page
# driver.get("https://www.behance.net/")

# # Wait for the page to load
# time.sleep(5)
# search_query = input("Enter your search query: ")

# # Find the search input field and enter your search query
# search_input = driver.find_element(By.NAME, "search")
# search_input.send_keys(search_query)
# search_input.send_keys(Keys.RETURN)

# # Scrolling down to load more content
# while True:
#     # Scroll down to load more content
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)
    
#     # Get the current page source
#     page_source = driver.page_source
    
#     # Parse the HTML with BeautifulSoup
#     soup = BeautifulSoup(page_source, 'html.parser')
    
#     # Check if there is a "Load More" button, exit if not found
#     load_more_button = driver.find_elements(By.XPATH, '//div[@class="LoadMore-module-loadMore-2pk"]')
#     if not load_more_button:
#         break

# # Extract names, titles, and main profile links
# data_list = []

# # Iterate over all project containers
# project_containers = soup.select('.ProjectCover-root-X6u')
# for container in project_containers:
#     title_element = container.select_one('.ProjectCover-details-ute .TitleOwner-limitHeight-_cX .Title-title-lpJ.e2e-Title-owner.Title-mediumTitle-OeE.TitleOwner-title-H7y')
#     name_element = container.select_one('.ProjectCover-details-ute .TitleOwner-limitHeight-_cX .Owners-root-qU7.Owners-dark-BYv.Owners-overflowText-C9U.TitleOwner-owner-I52.TitleOwner-mediumOwner-eDx .Owners-miniprofileActivatorContainer-k0t .Owners-owner-EEG.e2e-Owner-user-link')

#     if title_element and name_element:
#         title_text = title_element.get_text(strip=True)
#         name_text = name_element.get_text(strip=True)
#         main_profile_link = name_element['href']  # Extracting href attribute

#         data_list.append({
#             'Name': name_text,
#             'Title': title_text,
#             'MainProfileLink': main_profile_link
#         })

# # Create a DataFrame from the list
# df = pd.DataFrame(data_list)

# # Save the DataFrame to a CSV file
# try:
#     df.to_csv(r'output_all_data.csv', index=False)
#     print("CSV file created successfully.")
# except Exception as e:
#     print(f"An error occurred while saving the CSV file: {e}")

# # Close the browser window
# driver.quit()


# ________________________


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# import pandas as pd
# import time

# # Read the CSV file containing names and main profile links
# input_file = 'output_all_data.csv'
# df_input = pd.read_csv(input_file)

# # Create a new instance of the Chrome webdriver
# driver = webdriver.Chrome()

# # Maximize the browser window
# driver.maximize_window()

# # Extract names, main profile links, and phone numbers
# data_list = []

# for index, row in df_input.iterrows():
#     # Open the main profile link
#     driver.get(row['MainProfileLink'])
#     time.sleep(3)  # Add a delay to allow the page to load (adjust as needed)
    
#     # Get the current page source
#     page_source = driver.page_source
    
#     # Parse the HTML with BeautifulSoup
#     soup = BeautifulSoup(page_source, 'html.parser')
    
#     # Check for phone numbers in different locations
#     job_title_element = soup.select_one('.ProfileCard-line-fVO.e2e-Profile-occupation')
#     if not job_title_element:
#         job_title_element = soup.select_one('.UserInfo-infoBlockRow-jf1 .UserInfo-bio-OZA')
    
#     job_title = job_title_element.get_text(strip=True) if job_title_element else None

#     data_list.append({
#         'Name': row['Name'],
#         'job Title': job_title
#     })

# # Create a DataFrame from the list
# df_output = pd.DataFrame(data_list)

# # Save the DataFrame to a new CSV file
# output_file = 'output_name_and_phone.csv'
# try:
#     df_output.to_csv(output_file, index=False)
#     print(f"CSV file '{output_file}' created successfully.")
# except Exception as e:
#     print(f"An error occurred while saving the CSV file: {e}")

# # Close the browser window
# driver.quit()

# ______________________

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

# Read the CSV file containing names, main profile links, and job titles
input_file = 'output_all_data.csv'
df_input = pd.read_csv(input_file)

# Create a new instance of the Chrome webdriver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Extract names, main profile links, job titles, and phone numbers
data_list = []

for index, row in df_input.iterrows():
    # Open the main profile link
    driver.get(row['MainProfileLink'])
    time.sleep(3)  # Add a delay to allow the page to load (adjust as needed)
    
    # Get the current page source
    page_source = driver.page_source
    
    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    
    # Extract job title
    job_title_element = soup.select_one('.ProfileCard-line-fVO.e2e-Profile-occupation')
    job_title_text = job_title_element.get_text(strip=True) if job_title_element else "Not Available"
    
    data_list.append({
        'Name': row['Name'],
        'JobTitle': job_title_text,
    })

# Create a DataFrame from the list
df_output = pd.DataFrame(data_list)

# Save the DataFrame to a new CSV file
output_file = 'output_name_job_and_phone2.csv'
try:
    df_output.to_csv(output_file, index=False)
    print(f"CSV file '{output_file}' created successfully.")
except Exception as e:
    print(f"An error occurred while saving the CSV file: {e}")

# Close the browser window
driver.quit()
