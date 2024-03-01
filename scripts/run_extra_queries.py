import psycopg2
import csv
import os


DATABASE_URL = "postgres://wkuxgxgf:tytC8ie5i09kjsJ6PgPK_auU5mtQh-l9@ruby.db.elephantsql.com/wkuxgxgf"


results_directory = "/Users/clementine.elston-green/Documents/vestiaire-metrics/data/results_csv/extra_results_csv"


query_files = [
    "/Users/clementine.elston-green/Documents/vestiaire-metrics/sql/analysis/extra_analysis/popular_brands.sql",
    "/Users/clementine.elston-green/Documents/vestiaire-metrics/sql/analysis/extra_analysis/popular_categories.sql",
    "/Users/clementine.elston-green/Documents/vestiaire-metrics/sql/analysis/extra_analysis/time_spent_listings.sql",
    "/Users/clementine.elston-green/Documents/vestiaire-metrics/sql/analysis/extra_analysis/frequent_usage_customers.sql",
    "/Users/clementine.elston-green/Documents/vestiaire-metrics/sql/analysis/extra_analysis/listing_success_by_brand.sql",
    "/Users/clementine.elston-green/Documents/vestiaire-metrics/sql/analysis/extra_analysis/customer_engagement_by_category.sql",
    "/Users/clementine.elston-green/Documents/vestiaire-metrics/sql/analysis/extra_analysis/conversion_by_category.sql",
     "/Users/clementine.elston-green/Documents/vestiaire-metrics/sql/analysis/extra_analysis/listing_success_rate.sql"
]


def run_queries_and_export_to_csv(database_url, query_files, results_directory):

    conn = psycopg2.connect(database_url)
    cur = conn.cursor()
    
    for query_file in query_files:
        with open(query_file, 'r') as file:
            query = file.read()
            print(f"Executing query from {query_file}...")
            cur.execute(query)
            try:
            
                results = cur.fetchall()
     
                headers = [desc[0] for desc in cur.description]
         
                csv_file_path = os.path.join(
                    results_directory,
                    f"{os.path.splitext(os.path.basename(query_file))[0]}.csv"
                )
          
                with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(headers)  
                    csv_writer.writerows(results)  
                print(f"Results from {query_file} written to {csv_file_path}")
            except psycopg2.ProgrammingError as e:
   
                print("No data to fetch or commit needed.", e)
                conn.commit()
            print("\n")  
    

    cur.close()
    conn.close()


run_queries_and_export_to_csv(DATABASE_URL, query_files, results_directory)
