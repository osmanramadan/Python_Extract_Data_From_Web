import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import TimeoutException


   


def get_post_contact(links):
 
    chrome_options = Options()
    

    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:

        driver.get('https://haraj.com.sa/register.php')
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )

        username = ""
        password = ""

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys(username)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="auth_submit_username"]'))
        ).click()

        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        ).send_keys(password)

        # time.sleep(1)
        # WebDriverWait(driver, 10).until(
        #  EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="auth_submit_login"]'))
        # ).click()

        # time.sleep(3)
        # # Wait until the user menu button appears before proceeding
        # WebDriverWait(driver, 15).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="user-menu-button"]'))
        # )


        # script = """
        # try {
        #     localStorage.setItem('login', JSON.stringify({
        #         "state":{
        #             "accessToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjIxODU4MTI5IiwidCI6ImEiLCJleHAiOjE3MjQ3ODM3MzYsInVsIjoxLCJpZGVyIjoiU1M6XzAwYmY3MWU5NGU3ZDhhMWUyYmY4ZTA1OGZhZGFiMGViMmMyNjZiYTAzYjNhNSIsInRjIjoyMDI0MDgxN30.bQdu017Nd0rXe0SId7D8zEXvkasAc8RMELhgdOeQ6AI", "ATvalidUntil": 1724347695,
        #             "refreshToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjIxODU4MTI5IiwidCI6InIiLCJleHAiOjE4MTcyMzE3MzYsInVsIjoxLCJpZGVyIjoiU1M6XzAwYmY3MWU5NGU3ZDhhMWUyYmY4ZTA1OGZhZGFiMGViMmMyNjZiYTAzYjNhNSIsInRjIjoyMDI0MDgxN30.D3KTQ4KBig0JFxgfxyFpeGawsdMXr8FcNwrCb6qzZDE","RTvalidUntil": 1816795695,
        #             "ul": 1,
        #             "status": 200,
        #             "username": "النجاح السهل",
        #             "countMessages": 0,
        #             "countNotes": 0,
        #             "message": "",
        #             "isRecaptchaNeeded": false,
        #             "oldRefreshToken": ""
        #         }
        #     }));
        #     return true;
        # } catch (e) {
        #     return false;
        # }
        # """
        
        script = """
        try {
            localStorage.setItem('login', JSON.stringify({
                "state":{
                    "accessToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjE5NTc1NDA1IiwidCI6ImEiLCJleHAiOjE3MjQzNDc2OTUsInVsIjoxLCJpZGVyIjoiU1M6X2M4Mzk2NTRhMWE4YTFkZmUzNGUzNDk1MzgwNjc0NzhkNWExMmE2OWEyMTczOCIsInRjIjoyMDI0MDgxMn0.87U-EEQjNQR3ld5PS3jkEmkXNvYEZR6gzqX3TN7oVsY", "ATvalidUntil": 1724347695,
                    "refreshToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjE5NTc1NDA1IiwidCI6ImEiLCJleHAiOjE3MjQzNDc2OTUsInVsIjoxLCJpZGVyIjoiU1M6X2M4Mzk2NTRhMWE4YTFkZmUzNGUzNDk1MzgwNjc0NzhkNWExMmE2OWEyMTczOCIsInRjIjoyMDI0MDgxMn0.87U-EEQjNQR3ld5PS3jkEmkXNvYEZR6gzqX3TN7oVsY","RTvalidUntil": 1816795695,
                    "ul": 1,
                    "status": 200,
                    "username": "النجاح السهل",
                    "countMessages": 0,
                    "countNotes": 0,
                    "message": "",
                    "isRecaptchaNeeded": false,
                    "oldRefreshToken": ""
                }
            }));
            return true;
        } catch (e) {
            return false;
        }
        """
        driver.execute_script(script) 
        print("Loading...")

        contacts=[]

        for link in links:


            driver.get(link)
            time.sleep(1)

            WebDriverWait(driver, 25).until(
              EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="post-contact"]'))
            )

            time.sleep(1)
            
            
            button = driver.find_element(By.CSS_SELECTOR, '[data-testid="post-contact"]')
            button.click()

            time.sleep(1)

            WebDriverWait(driver, 25).until(
              EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="contact_mobile"]'))
            )

            time.sleep(2)

            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            contact_mobile_element = soup.find(attrs={"data-testid": "contact_mobile"})
            

            time.sleep(2)
            if contact_mobile_element:
                contacts.append(contact_mobile_element.text.strip())
            else:
              print("Phone Not Found")
              contacts.append('')
            # return False
        
        return contacts

    except TimeoutException as e:
            print(f"Timeout while processing : {e}")





def fetch_posts(url, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


def extract_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    posts_list_div = soup.find('div', {"id": "postsList"})
    if posts_list_div:
        for link in posts_list_div.find_all("a", {"data-testid": "post-title-link"}):
            href = link.get('href')
            if href:
                links.append("https://haraj.com.sa" + href)
    return links

def extract_cats(html):
    soup = BeautifulSoup(html, 'html.parser')
    cats = []
    posts_cats = soup.find('ul', {"data-testid": "ul_tags_0"})
    
    if posts_cats:
        print("0. All posts")
        for i, cat in enumerate(posts_cats.find_all('li')):
            cat_name = cat.text
            cats.append(cat_name)
            
            print(f"{i + 1}. {cat_name}")
    return cats


def extract_cities(html):
    soup = BeautifulSoup(html, 'html.parser')
    cities = []
    search_cities = soup.find("select", {"id": "cities"})
    
    if search_cities:
        print("Available cities:")
        for i, option in enumerate(search_cities.find_all("option")):
            city_name = option.text
            cities.append(city_name)
            print(f"{i}. {city_name}")
    return cities


def fetch_link_content(link):
    response = requests.get(link)
    response.raise_for_status()
    return response.text

def extract_data_from_content(html, post_link):

    soup = BeautifulSoup(html, 'html.parser')
    data = {}
    
    title = soup.find('h1').text if soup.find('h1') else 'No title'
    desc = soup.find("article").text if soup.find("article") else 'No description'
    city = soup.find("span", {"class": "city"}).text if soup.find("span", {"class": "city"}) else 'No city'
    author = "https://haraj.com.sa" + soup.find("a", {"data-testid": "post-author"}).get("href") if soup.find("a", {"data-testid": "post-author"}) else 'No author'

    post_time_span = soup.find("span", {"id": "post_time"})
    if post_time_span:
        post_time_subspan = post_time_span.find("span", {"data-testid": "post-time"})
        if post_time_subspan:
            time = post_time_subspan.text
        else:
            time = 'No time info'
    else:
        time = 'No time info'
    
    images_len = 0
    images_links = []
    for span in soup.find_all("span"):
        data_testid = span.get("data-testid")
        if data_testid and data_testid.startswith("post-image-"):
            img_tag = span.find("img")
            if img_tag and img_tag.get("srcset"):
                srcset = img_tag.get("srcset")
                src = srcset.split(',')[0].split(' ')[0]
                images_links.append(src)
                images_len += 1

    data['title'] = title
    data['description'] = desc
    data['city'] = city
    data['time'] = time
    # data['phone'] =''
    data['post_link'] = post_link
    data['contact_link'] = author
    data['images_len'] = images_len
    data['image_links'] = ', '.join(images_links)

    return data

def main():


    base_url = 'https://haraj.com.sa/tags'
    params = {}  

    html = fetch_posts(base_url, params)
    cats = extract_cats(html)
    cat_urls = {}  

    cat_urls[0] = base_url  
    for i, cat in enumerate(cats):
        cat_name = cat.lower().replace(" ", "-")
        cat_urls[i + 1] = f'https://haraj.com.sa/tags/{cat_name}'

    while True:

        user_input = input("Enter the number of pages to fetch (or 'q' to quit): ")
        if user_input.lower() == 'q':
            print("Exiting...")
            break
        
        try:
            num_pages = int(user_input)
            if num_pages < 1:
                raise ValueError("Number of pages must be at least 1.")
        except ValueError as e:
            print(f"Invalid input:Enter valid num")
            continue

       
        print("Available categories:")
        for num, cat in cat_urls.items():
            if num == 0:
                print("0. All posts")
            else:
                print(f"{num}. {cats[num - 1]}")

        print("Enter 's' to search by keyword.")
        choice = input("Enter the number of the category you want to fetch posts from or 's' to search: ")

        if choice.lower() == 's':

            search_term = input("Enter the search term: ").strip()
            if not search_term:
                print("Search term cannot be empty. Exiting...")
                continue
            

            cities_html = fetch_posts('https://haraj.com.sa/search/cities')
            cities = extract_cities(cities_html)

            while True:
                city_choice_input = input("Enter the number of the city you want to search in: ").strip()
                
                try:
                    city_choice = int(city_choice_input)
                    
                    if 0 <= city_choice < len(cities):
                        if city_choice == 0:
                            city_name = ''
                            base_url = f'https://haraj.com.sa/search/{search_term}'
                        else:
                            city_name = cities[city_choice].lower().replace(" ", "-")
                            base_url = f'https://haraj.com.sa/search/{search_term}/city/{city_name}'
                        break  # Exit the loop if valid input is provided
                    
                    else:
                        print("Invalid city choice. Please enter a valid number.")
                
                except ValueError:
                    print("Invalid input. Please enter a number.")
        
        else:
            try:
                cat_choice = int(choice)
                if cat_choice not in cat_urls:
                    raise ValueError("Invalid category number.")
                base_url = cat_urls[cat_choice]
            except ValueError as e:
                print(f"Invalid input: Enter valid number")
                continue

        posts = []
        html = fetch_posts(base_url, params)
        posts.extend(extract_links(html))

      
        for page in range(1, num_pages + 1):
            params.update({'page': page}) 
            html = fetch_posts(base_url, params)
            posts.extend(extract_links(html))

       
        all_data = []
        print("Extracting data ...........")
        print("Loading....................")
        for post_link in posts:
            content = fetch_link_content(post_link)
            data = extract_data_from_content(content,post_link)
            all_data.append(data)
        links=[]

        for i in all_data:
            links.append(i['post_link'])
        

        contacts=get_post_contact(links)
        print(contacts)
        for i in range(len(all_data)):
           all_data[i]['phone'] = contacts[i]


        columns = ['title', 'description', 'city', 'time', 'phone', 'post_link', 'contact_link', 'images_len', 'image_links']
        df = pd.DataFrame(all_data,columns=columns)
        df.to_excel('posts_data.xlsx', index=False)

        print("Posts_data has been saved to posts_data.xlsx.")

if __name__ == "__main__":
  main()


