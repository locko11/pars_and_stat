import pandas
import csv


PARSED_DATA_PATH = 'spiders/quotes7.csv'
CAT_STAT_FILE_PAHT = 'statistic_cat.csv'
WHL_STAT_FILE_PAHT = 'statistic_whl.csv'

# def stat_to_categories(df):
#     cat_total_count = df.groupby(["category"])['title'].count()
#     cat_availability = df[df['availability'] == True].groupby(["category"])['availability'].count()
#     cat_markdown_count = df[df['price_regular'] != 'None'].groupby(["category"])['price_regular'].count()
#     cat_median_price = df[df['price'] != 'None'].groupby(["category"])["price"].median()
#
#     mask =df[df['price_regular'] != 'None']
#     mask["discount_percentage"] = 100 * (mask["price_regular"].astype(float) - mask["price"].astype(float))/mask["price_regular"].astype(float)
#     cat_median_markdown_percent = mask.groupby(["category"])['discount_percentage'].median()
#
#
#     main = pandas.concat([cat_total_count, cat_availability, cat_markdown_count, cat_median_price, cat_median_markdown_percent], axis=1)
#     main_csv = main.rename(columns={'title': 'total_count', 'availability': 'available_count', 'price_regular':'markdown_count',  \
#                                                         'price':'median_price', 'discount_percentage':'median_markdown_percent'})
#     main_csv.to_csv('statistic.csv')


def get_stat():
    df = pandas.read_csv(PARSED_DATA_PATH)

    availability_mask = df[df['availability'] == True]
    price_regular_mask = df[df['price_regular'] != 'None']
    price_mask = df[df['price'] != 'None']

    markdown_percent_mask = price_regular_mask.copy()
    markdown_percent_mask["discount_percentage"] = 100 * (price_regular_mask["price_regular"].astype(float) - \
                                                                price_regular_mask["price"].astype(float)) / \
                                                                price_regular_mask["price_regular"].astype(float)
    def get_cut_stat():
        cat_total_count = df.groupby(["category"])['title'].count()
        cat_availability = availability_mask.groupby(["category"])['availability'].count()
        cat_markdown_count = price_regular_mask.groupby(["category"])['price_regular'].count()
        cat_median_price = price_mask.groupby(["category"])["price"].median()
        cat_median_markdown_percent = markdown_percent_mask.groupby(["category"])['discount_percentage'].median()

        main_cat = pandas.concat(
            [cat_total_count, cat_availability, cat_markdown_count, cat_median_price, cat_median_markdown_percent], axis=1)
        main_cat_csv = main_cat.rename(
            columns={'title': 'total_count', 'availability': 'available_count', 'price_regular': 'markdown_count', \
                     'price': 'median_price', 'discount_percentage': 'median_markdown_percent'
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

    #
    # main_whl_csv = main_whl.rename(
    #     columns={'title': 'total_count', 'availability': 'available_count', 'price_regular': 'markdown_count', \
    #              'price': 'median_price', 'discount_percentage': 'median_markdown_percent'
    #              })
    # main_whl_csv.to_csv('statistic_whl.csv')
# print(df.loc[df['price_regular']])
# print(df.loc[df['price_regular'] != None].count())

# col = df['price'] != 'None'
#
# print(cate3)
#
# mask = df['price_regular'] != 'None'
# new_df = df[mask]
# new = round(100* (new_df["price_regular"].astype(float) - new_df["price"].astype(float))/new_df["price_regular"].astype(float))
# print(new.median())
#
# with open('statistic.csv', 'w') as file_to_write:
#     fieldnames = ['total_count', 'available_count', 'markdown_count', 'median_price', 'median_markdown_percent']
#     writer = csv.DictWriter(file_to_write, delimiter=',', quotechar='|')
#     writer.writer(main_csv)

if __name__ == '__main__':
    get_stat()
