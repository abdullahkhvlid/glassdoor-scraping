from bs4 import BeautifulSoup
import os
import pandas as pd


dl = {"title":[], "link": [], "salary": []}


for i in os.listdir("data"):
    try:    
        with open(f"data/{i}" , "r") as f:
            r = f.read()

        soup = BeautifulSoup(r, "html.parser")
        pretty = soup.prettify()



        with open(f"data/{i}" , "w") as f:
             p =  f.write(pretty)


        t = soup.find("a")
        if t:
            title = t.get_text()

        else:
            title = "None"

        
        s = soup.find("div", class_="JobCard_salaryEstimate__QpbTW")
        if s :
            salary = s.find(text= True, recursive=False)
        else:
            salary = "None"

        
        l = soup.find('a', class_="JobCard_jobTitle__GLyJ1")
        if l:
           link = l.get("href")
        else:
            link = "None"

            

        dl["title"].append(title)
        dl["salary"].append(salary)
        dl["link"].append(link)

        
    except ValueError as e:
        print(e)


df = pd.DataFrame(dl)
df.to_csv("jobs_Data.csv")
