import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import time
import requests

class scraping:
    header={"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
    }
    def response(self):
        Model=[]
        Price_in_euro=[]
        Range=[]
        Efficiency=[]
        Weight=[]
        Aceleration_time=[]
        stop_range=[]
        Battery=[]
        Fastcharge=[]
        Towing=[]
        Cargo_vol=[]
        Price_range_per_km=[]
        


        for i in range(1,5):
            start=time.time()
            url=f"https://ev-database.org/#group=vehicle-group&rs-pr=10000_100000&rs-er=0_1000&rs-ld=0_1000&rs-ac=2_23&rs-dcfc=0_400&rs-ub=10_200&rs-tw=0_3000&rs-ef=100_350&rs-sa=-1_5&rs-w=1000_3500&rs-c=0_5000&rs-y=2010_2030&s=1&p=0-{i}"
            res=requests.get(url,headers=self.header)
            soup=BeautifulSoup(res.text, "html.parser")
            boxes=soup.find_all("div",class_="item-data")
        
            for box in boxes:
                models=box.find("a",class_="title")
                car_price=box.find("span",class_="pricesort hidden")
                ranges=box.find("span",class_="erange_real")
                efficiencies=box.find("span",class_="efficiency")
                weights=box.find("span",class_="weight_p")
                acceleartion_timings=box.find("span",class_="acceleration_p")
                stop_ranges=box.find("span",class_="long_distance_total")
                batteries = box.find("span", class_="battery_p")
                fastcharges = box.find("span", class_="fastcharge_speed_print")
                towings = box.find("span", class_="towweight_p")
                cargo = box.find("span", class_="cargo")
                prices = box.find("span", class_="priceperrange hidden")


            
                Model.append(models.text if models else np.nan)
                Price_in_euro.append(car_price.text if car_price else np.nan)
                Range.append(ranges.text if ranges else np.nan)
                Efficiency.append(efficiencies.text if efficiencies else np.nan)
                Weight.append(weights.text if weights else np.nan)
                Aceleration_time.append(acceleartion_timings.text if acceleartion_timings else np.nan)
                stop_range.append(stop_ranges.text if stop_ranges else np.nan)
                Battery.append(batteries.text if batteries else np.nan)
                Fastcharge.append(fastcharges.text if fastcharges else np.nan)
                Towing.append(towings.text if towings else np.nan)
                Cargo_vol.append(cargo.text if cargo else np.nan)
                Price_range_per_km.append(prices.text if prices else np.nan)    

            

        
            time.sleep(3)
            end = time.time()
            print(f"Page {i} completed in {round(end - start, 2)} seconds ✅")
        
        df = pd.DataFrame({
                    "Model": Model,
                    "Price_in_euro":Price_in_euro,
                    "Range": Range,
                    "Efficiency": Efficiency,
                    "Weight": Weight,
                    "Aceleration_time": Aceleration_time,
                    "Stop_range": stop_range,
                    "Battery": Battery,
                    "Fastcharge": Fastcharge,
                    "Towing": Towing,
                    "Cargo_volume": Cargo_vol,
                    "Price_range_per_km": Price_range_per_km
                    
        })

        return df


















     


