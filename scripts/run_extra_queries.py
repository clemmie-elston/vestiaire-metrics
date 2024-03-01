import psycopg2

# Database connection parameters
DATABASE_URL = "postgres://wkuxgxgf:tytC8ie5i09kjsJ6PgPK_auU5mtQh-l9@ruby.db.elephantsql.com/wkuxgxgf"

# List of your SQL query files with absolute paths
query_files = [
    "/Users/clementine.elston-green/Documents/vestiaire-metrics/sql/analysis/extra_analysis/popular_brands.sql",
    "/Users/clementine.elston-green/Documents/vestiaire-metrics/sql/analysis/extra_analysis/popular_categories.sql",
    "/Users/clementine.elston-green/Documents/vestiaire-metrics/sql/analysis/extra_analysis/time_spent_listings.sql",
    "/Users/clementine.elston-green/Documents/vestiaire-metrics/sql/analysis/extra_analysis/frequent_usage_customers.sql",
    "/Users/clementine.elston-green/Documents/vestiaire-metrics/sql/analysis/extra_analysis/listing_success_by_brand.sql",
    "/Users/clementine.elston-green/Documents/vestiaire-metrics/sql/analysis/extra_analysis/customer_engagement_by_category.sql",
    "/Users/clementine.elston-green/Documents/vestiaire-metrics/sql/analysis/extra_analysis/conversion_by_category.sql"
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
            try:
                # Attempt to fetch results if available
                results = cur.fetchall()
                for row in results:
                    print(row)
            except psycopg2.ProgrammingError as e:
                # Handle case where there's no data to fetch
                print("No data to fetch or commit needed.")
                conn.commit()
            print("\n")  # Add spacing between query results for readability
    
    # Clean up
    cur.close()
    conn.close()

# Run the queries
run_queries(DATABASE_URL, query_files)
