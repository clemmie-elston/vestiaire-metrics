import psycopg2

# Database connection parameters
DATABASE_URL = "postgres://wkuxgxgf:tytC8ie5i09kjsJ6PgPK_auU5mtQh-l9@ruby.db.elephantsql.com/wkuxgxgf"

# List of your SQL query files with absolute paths
query_files = [
    "/Users/clementine.elston-green/Documents/vestiaire-metrics/sql/analysis/exercise_analysis/a_total_listings_per_customer.sql",
    "/Users/clementine.elston-green/Documents/vestiaire-metrics/sql/analysis/exercise_analysis/b_items_listed_by_category_per_customer.sql",
    "/Users/clementine.elston-green/Documents/vestiaire-metrics/sql/analysis/exercise_analysis/c_seller_listing_dates_and_actions.sql",
    "/Users/clementine.elston-green/Documents/vestiaire-metrics/sql/analysis/exercise_analysis/d_median_clicks_per_product.sql",
    "/Users/clementine.elston-green/Documents/vestiaire-metrics/sql/analysis/exercise_analysis/e_last_action_for_unsubmitted_products.sql"
]

def run_queries(database_url, query_files):
    # Connect to the database
    conn = psycopg2.connect(database_url)
    cur = conn.cursor()
    
    for query_file in query_files:
        with open(query_file, 'r') as file:
            query = file.read()
            print(f"Executing query from {query_file}...")
            cur.execute(query)
            # Depending on your queries, you may need to fetch results
            try:
                results = cur.fetchall()
                for row in results:
                    print(row)
            except psycopg2.ProgrammingError:
                # This handles the case where there's no data to fetch (e.g., INSERT/UPDATE statements)
                conn.commit()  # Commit any changes made by the query
            print("\n")  # Add spacing between query results for readability
    
    # Clean up
    cur.close()
    conn.close()

# Run the queries
run_queries(DATABASE_URL, query_files)

