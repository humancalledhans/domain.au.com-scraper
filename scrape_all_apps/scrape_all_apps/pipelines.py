# pushed to docker on aws.
# python3 launcher.py works. data saved in db.

from .items import AffinityAppMediator, App, AppHighlight, AppHighlightMediator
from .db_secrets import get_db_password
import mysql.connector
from datetime import datetime


class ScrapeAllAppsPipeline:

    def __init__(self):
        # self.cnx = mysql.connector.connect(user='admin', password=get_db_password(),
        #    host='shopify-aso-free-tier.c200z18i1oar.us-east-1.rds.amazonaws.com', database='db_shopify_aso')
        self.app = []
        self.affinity_app_mediator = []
        self.app_highlight = []
        self.app_highlight_mediator = []

    def close_spider(self, spider):
        print("Closing Spider. Writing to DB.")
        # cnx = mysql.connector.connect(user='admin', password=get_db_password(),
        #                                    host='shopify-aso-free-tier.c200z18i1oar.us-east-1.rds.amazonaws.com', database='db_shopify_aso')

        # # cnx = mysql.connector.connect(user='admin', password=get_db_password(),
        # #                               host='shopify-aso-memory-max.c200z18i1oar.us-east-1.rds.amazonaws.com', database='db_shopify_aso')

        # cursor = cnx.cursor()

        # for item in self.app:
        #     self.upload_to_db(item, cnx, cursor)

        # # cnx.commit()

        # for item in self.affinity_app_mediator:
        #     self.upload_affinity_app_mediator_to_db(item, cnx, cursor)

        # # cnx.commit()

        # for item in self.app_highlight:
        #     self.upload_to_apphighlight_table(item, cnx, cursor)

        # # cnx.commit()

        # for item in self.app_highlight_mediator:
        #     self.upload_to_apphighlight_mediator_table(item, cnx, cursor)

        # # cnx.commit()

        # cursor.close()
        # cnx.close()

    # def process_item(self, item, spider):
    #     if isinstance(item, App):
    #         # self.upload_to_db(item, self.cnx)
    #         self.app.append(item)
    #         # return "Apps are now stored in CSV File."
    #         return item
    #     elif isinstance(item, AffinityAppMediator):
    #         # self.upload_affinity_app_mediator_to_db(item)
    #         self.affinity_app_mediator.append(item)
    #         return item
    #     elif isinstance(item, AppHighlight):
    #         # self.upload_to_apphighlight_table(item)
    #         self.app_highlight.append(item)
    #         return item
    #     elif isinstance(item, AppHighlightMediator):
    #         # self.upload_to_apphighlight_mediator_table(item)
    #         self.app_highlight_mediator.append(item)
    #         return item

    # def upload_to_apphighlight_table(self, highlight_data, cnx, cursor):

    #     create_table_statement = """
    #     CREATE TABLE IF NOT EXISTS db_shopify_aso.app_highlights(
    #         id INT PRIMARY KEY AUTO_INCREMENT,
    #         highlight_text VARCHAR(500) NOT NULL,
    #         scraped_date_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    #     );"""

    #     columns = 'AaT3C~*~GA@PQT'.join(str(x) for x in highlight_data.keys())
    #     values = 'AaT7C~*~GA@PQT'.join(str(x) for x in highlight_data.values())

    #     columns = tuple(map(str, columns.split('AaT3C~*~GA@PQT')))
    #     values = tuple(map(str, values.split('AaT7C~*~GA@PQT')))

    #     highlight_text = values[columns.index('highlight_text')]
    #     highlight_values = (highlight_text,)

    #     cursor.execute(create_table_statement)

    #     check_if_exists_stmt = """SELECT EXISTS(SELECT * FROM db_shopify_aso.app_highlights WHERE highlight_text = %s);"""
    #     cursor.execute(check_if_exists_stmt, highlight_values)
    #     exists = cursor.fetchone()[0]

    #     insert_stmt = """
    #     INSERT INTO app_highlights ( highlight_text ) VALUES ( %s )"""

    #     if not exists:
    #         print("Inserting new highlight")
    #         cursor.execute(insert_stmt, highlight_values)
    #         cnx.commit()

    # def upload_to_apphighlight_mediator_table(self, highlight_mediator_data, cnx, cursor):
    #     cnx = mysql.connector.connect(user='admin', password=get_db_password(),
    #                                   host='shopify-aso-free-tier.c200z18i1oar.us-east-1.rds.amazonaws.com', database='db_shopify_aso')
    #     # cnx = mysql.connector.connect(user='admin', password=get_db_password(),
    #     #                               host='shopify-aso-memory-max.c200z18i1oar.us-east-1.rds.amazonaws.com', database='db_shopify_aso')

    #     create_table_statement = """
    #     CREATE TABLE IF NOT EXISTS db_shopify_aso.app_highlights_mediator(
    #         id INT PRIMARY KEY AUTO_INCREMENT,
    #         app_id VARCHAR(50) NOT NULL,
    #         app_highlight_id VARCHAR(50) NOT NULL,
    #         scraped_date_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP

    #     );"""

    #     columns = 'AaT3C~*~GA@PQT'.join(str(x)
    #                                     for x in highlight_mediator_data.keys())
    #     values = 'AaT7C~*~GA@PQT'.join(str(x)
    #                                    for x in highlight_mediator_data.values())

    #     columns = tuple(map(str, columns.split('AaT3C~*~GA@PQT')))
    #     values = tuple(map(str, values.split('AaT7C~*~GA@PQT')))

    #     app_id = values[columns.index('app_id')]
    #     highlight_text = values[columns.index('highlight_text')]

    #     cursor.execute(create_table_statement)

    #     # find the app_highlight_id-s. for each value, add one entry into the table.
    #     get_id_from_table_stmt = "SELECT id FROM db_shopify_aso.app_highlights WHERE highlight_text = %s;"
    #     cursor.execute(get_id_from_table_stmt, (highlight_text,))
    #     app_highlight_id = cursor.fetchone()[0]

    #     apphighlight_mediator_values = (app_id, app_highlight_id)

    #     check_if_exists_stmt = """SELECT EXISTS(SELECT * FROM db_shopify_aso.app_highlights_mediator WHERE app_id = %s AND app_highlight_id = %s);"""
    #     cursor.execute(check_if_exists_stmt, apphighlight_mediator_values)
    #     exists = cursor.fetchone()[0]

    #     insert_stmt = """
    #     INSERT INTO app_highlights_mediator ( app_id, app_highlight_id ) VALUES ( %s, %s )"""

    #     if not exists:
    #         print("Inserting new app highlight mediator")
    #         cursor.execute(insert_stmt, apphighlight_mediator_values)
    #         cnx.commit()

    # def upload_to_db(self, app_data, cnx, cursor):
    #     cnx = mysql.connector.connect(user='admin', password=get_db_password(),
    #                                   host='shopify-aso-free-tier.c200z18i1oar.us-east-1.rds.amazonaws.com', database='db_shopify_aso')
    #     # cnx = mysql.connector.connect(user='admin', password=get_db_password(),
    #     #                               host='shopify-aso-memory-max.c200z18i1oar.us-east-1.rds.amazonaws.com', database='db_shopify_aso')

    #     create_table_statement = """
    #     CREATE TABLE IF NOT EXISTS db_shopify_aso.app(
    #         app_id VARCHAR(255) PRIMARY KEY,
    #         app_logo VARCHAR(65535) NOT NULL,
    #         app_title VARCHAR(65535),
    #         app_intro_vid_url VARCHAR(65535),
    #         app_developer_link VARCHAR(65535) NOT NULL,
    #         app_illustration_image VARCHAR(65535),
    #         app_brief_description VARCHAR(65535),
    #         app_full_description VARCHAR(65535),
    #         app_rating VARCHAR(65535),
    #         app_num_of_reviews VARCHAR(65535),
    #         app_pricing_hint VARCHAR(65535),
    #         app_url VARCHAR(65535),
    #         app_published_date DATE NOT NULL,
    #         dev_id VARCHAR(255) NOT NULL,
    #         scraped_date_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    #     );"""

    #     columns = 'AaT3C~*~GA@PQT'.join(str(x)
    #                                     for x in app_data.keys())
    #     values = 'AaT7C~*~GA@PQT'.join(str(x)
    #                                    for x in app_data.values())

    #     columns = tuple(map(str, columns.split('AaT3C~*~GA@PQT')))
    #     values = tuple(map(str, values.split('AaT7C~*~GA@PQT')))
    #     # print("COLUMNS AFTER MAPPING ", columns)
    #     # print("VALUES AFTER MAPPING", values)

    #     app_id_index = columns.index('app_id')
    #     app_id = values[app_id_index]

    #     app_logo_index = columns.index('app_logo')
    #     app_logo = values[app_logo_index]

    #     app_title_index = columns.index('app_title')
    #     app_title = values[app_title_index]

    #     app_intro_vid_url_index = columns.index('app_intro_vid_url')
    #     app_intro_vid_url = values[app_intro_vid_url_index]
    #     if app_intro_vid_url == 'None':
    #         app_intro_vid_url = None

    #     app_developer_link_index = columns.index('app_developer_link')
    #     app_developer_link = values[app_developer_link_index]

    #     app_illustration_image_index = columns.index('app_illustration_image')
    #     app_illustration_image = values[app_illustration_image_index]

    #     app_brief_description_index = columns.index('app_brief_description')
    #     app_brief_description = values[app_brief_description_index]

    #     app_full_description_index = columns.index('app_full_description')
    #     app_full_description = values[app_full_description_index]

    #     app_rating_index = columns.index('app_rating')
    #     app_rating = values[app_rating_index]

    #     app_num_of_reviews_index = columns.index('app_num_of_reviews')
    #     app_num_of_reviews = values[app_num_of_reviews_index]

    #     app_pricing_hint_index = columns.index('app_pricing_hint')
    #     app_pricing_hint = values[app_pricing_hint_index]

    #     app_url_index = columns.index('app_url')
    #     app_url = values[app_url_index]

    #     app_published_date_index = columns.index('app_published_date')
    #     date_string = values[app_published_date_index]
    #     app_published_date = datetime.strptime(date_string, "%B %d, %Y")

    #     app_dev_id_index = columns.index('dev_id')
    #     dev_id = values[app_dev_id_index]

    #     app_values = (app_id, app_logo, app_title, app_intro_vid_url, app_developer_link, app_illustration_image, app_brief_description,
    #                   app_full_description, app_rating, app_num_of_reviews, app_pricing_hint, app_url, app_published_date, dev_id)

    #     check_if_exists_stmt = """SELECT EXISTS(SELECT * FROM db_shopify_aso.app WHERE app_id = %s AND app_logo = %s AND app_title = %s AND app_intro_vid_url = %s AND app_developer_link = %s AND app_illustration_image = %s AND app_brief_description = %s AND app_full_description = %s AND app_rating = %s AND app_num_of_reviews = %s AND app_pricing_hint = %s AND app_url = %s AND app_published_date = %s AND dev_id = %s);"""

    #     cursor.execute(create_table_statement)

    #     cursor.execute(check_if_exists_stmt, app_values)
    #     exists = cursor.fetchone()[0]

    #     insert_stmt = """
    #         INSERT INTO app ( app_id, app_logo, app_title, app_intro_vid_url, app_developer_link, app_illustration_image, app_brief_description, app_full_description, app_rating, app_num_of_reviews, app_pricing_hint, app_url, app_published_date, dev_id )
    #         VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )
    #         """
    #     if not exists:
    #         print("Inserting new app")
    #         cursor.execute(insert_stmt, app_values)
    #         cnx.commit()

    #     # print("LEN_OF_COLUMNS", len(columns))
    #     # print("LEN_OF_VALUES", len(values))

    # def upload_affinity_app_mediator_to_db(self, mediator_data, cnx, cursor):

    #     create_table_statement = """
    #     CREATE TABLE IF NOT EXISTS db_shopify_aso.affinity_apps_mediator(
    #         id INT PRIMARY KEY AUTO_INCREMENT,
    #         parent_app_id VARCHAR(50) NOT NULL,
    #         affinity_app_id VARCHAR(50) NOT NULL
    #     );"""

    #     columns = 'AaT3C~*~GA@PQT'.join(str(x)
    #                                     for x in mediator_data.keys())
    #     values = 'AaT7C~*~GA@PQT'.join(str(x)
    #                                    for x in mediator_data.values())

    #     columns = tuple(map(str, columns.split('AaT3C~*~GA@PQT')))
    #     values = tuple(map(str, values.split('AaT7C~*~GA@PQT')))

    #     app_id_index = columns.index('app_id')
    #     app_id = values[app_id_index]

    #     affinity_app_id_index = columns.index('affinity_app_id')
    #     affinity_app_id = values[affinity_app_id_index]

    #     values = (app_id, affinity_app_id)

    #     cursor.execute(create_table_statement)

    #     check_if_exists_stmt = """SELECT EXISTS(SELECT * FROM db_shopify_aso.affinity_apps_mediator WHERE parent_app_id = %s AND affinity_app_id = %s);"""
    #     cursor.execute(check_if_exists_stmt, values)
    #     exists = cursor.fetchone()[0]

    #     insert_stmt = """
    #     INSERT INTO affinity_apps_mediator ( parent_app_id, affinity_app_id ) VALUES ( %s, %s )
    #     """

    #     if not exists:
    #         print("Inserting new affinity apps mediator")
    #         cursor.execute(insert_stmt, values)  # closing the connection.
    #         cnx.commit()
