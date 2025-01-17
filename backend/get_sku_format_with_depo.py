# This program helps in comparing sku in the sku dimesnion file to 
# the sku gotten in the km tracker . It first extracts data from km tracker checks if 
# its in sku dimension folder

import pandas as pd
import shutil
import math
##KM tracker is imported and cols are selected 

def get_format_from_dim_km(nameofkm,nameofdim):
        km_tracker = pd.read_excel(nameofkm,sheet_name= "MAIN DATA",skiprows=4,usecols=[0,1,2,3,4,5,13,16,51,52,57,58,59,60,130,131])
        km_tracker = km_tracker[km_tracker["PC"] == "PULP"]
        km_tracker = km_tracker[km_tracker["Validity"]=="Valid"]
        km_tracker = km_tracker[km_tracker["Balance Dispatch"]=="Dispatch"]
        km_tracker["L2 Indent"] = km_tracker["INDENT KG"] - km_tracker["L1 Indent"]

        sku_dimension = pd.read_excel(nameofdim,sheet_name="SKU dimensions",skiprows=25,usecols=[2,4,5,6,10,11,12])
        sku_dimension = sku_dimension[sku_dimension["Select your PC & Blank before Updating"] == "PULP" ]
        sku_dimension["volume"] = sku_dimension.apply(lambda row: row["CASE (Length)"]*row["CASE (Breadth)"]*row["CASE (Height)"],axis=1)
        flag = 0

        sku_dimension.rename(columns={"SKU CODE":"MATERIAL"},inplace=True)
        sku_dimension["MATERIAL"] = sku_dimension["MATERIAL"].str.upper()
        km_tracker["MATERIAL"] = km_tracker["MATERIAL"].str.upper()

        sku_dimension.drop("Select your PC & Blank before Updating",axis=1)


        dimension_name = list(sku_dimension["MATERIAL"])
        km_tracker_name = list(km_tracker["MATERIAL"].unique())
        missing = []
        for name in km_tracker_name:
                if(name not in dimension_name):
                        flag+=1
                        missing.append(name)
                        print(name)
        


        final_pre = pd.merge(km_tracker, sku_dimension,left_on='MATERIAL',right_on="MATERIAL")
        final_pre["8th cases"] = final_pre["8th.4"] / final_pre["NET WT./CASE"]
        final_pre["16th cases"] = final_pre["16th.3"] / final_pre["NET WT./CASE"]
        final_pre["24th cases"] = final_pre["24th.3"] / final_pre["NET WT./CASE"]
        final_pre["30th cases"] = final_pre["30th.3"] / final_pre["NET WT./CASE"]

        final_pre["16th cases"]  = (final_pre["16th cases"].astype(float))
        final_pre["24th cases"]  = (final_pre["24th cases"].astype(float))
        final_pre["30th cases"]  = (final_pre["30th cases"].astype(float))
        final_pre["8th cases"]  =  (final_pre["8th cases"].astype(float))

        final_pre["16th cases"] = final_pre["16th cases"].apply(lambda x:math.ceil(x))
        final_pre["24th cases"] = final_pre["24th cases"].apply(lambda x:math.ceil(x))
        final_pre["30th cases"] = final_pre["30th cases"].apply(lambda x:math.ceil(x))
        final_pre["8th cases"] = final_pre["8th cases"].apply(lambda x:math.ceil(x))


        final_pre["8th volume"] = final_pre["8th cases"] * final_pre["volume"]
        final_pre["16th volume"] = final_pre["16th cases"] * final_pre["volume"]
        final_pre["24th volume"] = final_pre["24th cases"] * final_pre["volume"]
        final_pre["30th volume"] = final_pre["30th cases"] * final_pre["volume"]

        final_pre["L1 cases"] = final_pre["L1 Indent"] / final_pre["NET WT./CASE"]
        final_pre["L1 cases"] = final_pre["L1 cases"].astype(float)
        final_pre["L1 cases"] = final_pre["L1 cases"].apply(lambda x:math.ceil(x))
        final_pre["L1 volume "] = final_pre["L1 cases"] * final_pre["volume"]
        final_pre["L1 Gross weight"] = final_pre["L1 cases"] * final_pre["GROSS WT./CASE"]
        final_pre.drop("Select your PC & Blank before Updating",axis=1)
        final_pre["L2 cases"] = final_pre["L2 Indent"] / final_pre["NET WT./CASE"]
        final_pre["L2 cases"] = final_pre["L2 cases"].astype(float)
        final_pre["L2 cases"] = final_pre["L2 cases"].apply(lambda x:math.ceil(x))
        final_pre["L2 volume "] = final_pre["L2 cases"] * final_pre["volume"]
        final_pre["L2 Gross weight"] = final_pre["L2 cases"] * final_pre["GROSS WT./CASE"]
        output_from_km_dimension = "output_from_km_dimension.xlsx"

        del final_pre["Select your PC & Blank before Updating"]
        del final_pre["PC"]
        del final_pre["PC-Depot"]
        del final_pre["DEPO-MATERIAL"]
        del final_pre["PC-DEPO-MATERIAL"]
        del final_pre["Validity"]
        del final_pre["Balance Dispatch"]
        del final_pre["CASE (Length)"]
        del final_pre["CASE (Breadth)"]
        del final_pre["CASE (Height)"]

        final_pre.to_excel(output_from_km_dimension,sheet_name=output_from_km_dimension)
        km_tracker.to_excel("h.xlsx")
        return missing
#get_format_from_dim_km('/home/aravind/Desktop/schedulerui/backend/Output of KM Tracker as on 04th Jul 2019.xlsx','/home/aravind/Desktop/schedulerui/backend/SKU dimensions.xlsx')
