import os
import json

def process_data(file_name, save_dir):
    asin_rating_data = {}
    with open(file_name) as f:
        next(f)
        for line in f:
            line = line.strip("\n").split(",")
            asin = line[1]
            rating = line[3]
            if len(asin) <=0 or not rating.isnumeric():
                continue
            rating = int(rating)
            if asin not in asin_rating_data.keys():
                asin_rating_data[asin] = []
            asin_rating_data[asin].append(rating)
    asin_rating_data = [[key, asin_rating_data[key]] for key in asin_rating_data.keys()]
    # Top 20 rated products
    asin_rating_data.sort(key=lambda x: len(x[1]), reverse=True)
    most_rated_products = asin_rating_data[:20]
    with open(os.path.join(save_dir, "Top_20_rated_products.json"), "w") as f:
        for d in most_rated_products:
            f.write( json.dumps( {"asin":d[0], "rating":d[1]} ) +"\n")
    # Top 20 average rating products
    asin_rating_data.sort(key=lambda x: (sum(x[1]) * 1.0 / len(x[1]), len(x[1])), reverse=True)
    average_rating_products = asin_rating_data[:20]
    with open(os.path.join(save_dir, "Top_20_avg_rating_products.json"), "w") as f:
        for d in average_rating_products:
            f.write( json.dumps( {"asin":d[0], "rating":d[1]} )  + '\n')

if __name__ == '__main__':
    process_data(
        file_name= "./merged.csv",
        save_dir="./"
    )