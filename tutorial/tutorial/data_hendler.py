import pandas
import csv


PARSED_DATA_PATH = 'spiders/new_data_offers.csv'
CAT_STAT_FILE_PAHT = 'new_statistic_cat_ith_offers.csv'
WHL_STAT_FILE_PAHT = 'new_statistic_whl.csv'


def get_stat():
    df = pandas.read_csv(PARSED_DATA_PATH)

    availability_mask = df[df['availability'] == True]
    price_regular_mask = df[df['price_regular'] != 'None']
    price_mask = df[df['price'] != 'None']

    markdown_percent_mask = price_regular_mask.copy()
    markdown_percent_mask["discount_percentage"] = round(100 * (price_regular_mask["price_regular"].astype(float) - \
                                                                price_regular_mask["price"].astype(float)) / \
                                                                price_regular_mask["price_regular"].astype(float))
    def get_cut_stat():
        cat_total_count = df.groupby(["category"])['title'].count()
        cat_availability = availability_mask.groupby(["category"])['availability'].count()
        cat_markdown_count = price_regular_mask.groupby(["category"])['price_regular'].count()
        cat_median_price = price_mask.groupby(["category"])["price"].median()
        cat_median_markdown_percent = markdown_percent_mask.groupby(["category"])['discount_percentage'].median()
        cat_uniue_offers = df.groupby(['category'])['offers'].unique() #I did no understand this part of task, so Idid it as I understood

        main_cat = pandas.concat(
            [cat_total_count, cat_availability, cat_markdown_count, cat_median_price, cat_median_markdown_percent, cat_uniue_offers], axis=1)
        main_cat_csv = main_cat.rename(
            columns={'title': 'total_count', 'availability': 'available_count', 'price_regular': 'markdown_count', \
                     'price': 'median_price', 'discount_percentage': 'median_markdown_percent', 'offers': 'unique_special_offers'
                     })
        main_cat_csv.to_csv(CAT_STAT_FILE_PAHT)

    def whl_stat():
        whl_total_count = df['title'].count()
        whl_availability = availability_mask['availability'].count()
        whl_markdown_count = price_regular_mask['price_regular'].count()
        whl_median_price = price_mask["price"].median()
        whl_median_markdown_percent = markdown_percent_mask['discount_percentage'].median()

        with open(WHL_STAT_FILE_PAHT, 'w') as file_to_write:
            fieldnames = ['total_count', 'available_count', 'markdown_count', 'median_price', 'median_markdown_percent']
            writer = csv.DictWriter(file_to_write, delimiter=',', quotechar='|', fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'total_count': whl_total_count, 'available_count': whl_availability,
                             'markdown_count': whl_markdown_count, 'median_price': whl_median_price,
                             'median_markdown_percent': whl_median_markdown_percent
                             })

    get_cut_stat()
    whl_stat()


if __name__ == '__main__':
    get_stat()
