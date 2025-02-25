import pandas as pd

# Load data from CSV files
bills_df = pd.read_csv("bills.csv")  # DataFrame containing bill information
legislators_df = pd.read_csv("legislators.csv")  # DataFrame containing legislator information
votes_df = pd.read_csv("votes.csv")  # DataFrame containing vote information
vote_results_df = pd.read_csv("vote_results.csv")  # DataFrame containing vote results

# Create dictionaries for mapping IDs to names and bill IDs
legislators_dict = legislators_df.set_index("id")["name"].to_dict()  # Maps legislator ID to name
votes_dict = votes_df.set_index("id")["bill_id"].to_dict()  # Maps vote ID to bill ID

# Calculate support/oppose counts for legislators
legislator_support_oppose = vote_results_df.groupby(["legislator_id", "vote_type"]).size().unstack(fill_value=0)
# Rename columns based on vote type (2 = oppose, other = support)
legislator_support_oppose.columns = ["num_opposed_bills" if col == 2 else "num_supported_bills" for col in legislator_support_oppose.columns]
legislator_support_oppose["id"] = legislator_support_oppose.index # add legislator ID as a column.
legislator_support_oppose["name"] = legislator_support_oppose["id"].map(legislators_dict) # Maps legislator ID to name.
# Reorder columns for better readability
legislator_support_oppose = legislator_support_oppose[["id", "name", "num_supported_bills", "num_opposed_bills"]]

# Map bill IDs to vote results
vote_results_df["bill_id"] = vote_results_df["vote_id"].map(votes_dict)

# Calculate support/oppose counts for bills
bills_support_oppose = vote_results_df.groupby(["bill_id", "vote_type"]).size().unstack(fill_value=0)
# Rename columns based on vote type (2 = oppose, other = support)
bills_support_oppose.columns = ["opposer_count" if col == 2 else "supporter_count" for col in bills_support_oppose.columns]
bills_support_oppose["id"] = bills_support_oppose.index # add bill ID as a column.
# Merge bill details with support/oppose counts
bills_support_oppose = bills_support_oppose.merge(bills_df, on="id", how="left")
# Map sponsor ID to sponsor name, fill missing values with "Unknown"
bills_support_oppose["primary_sponsor"] = bills_support_oppose["sponsor_id"].map(legislators_dict).fillna("Unknown")
# Reorder columns for better readability
bills_support_oppose = bills_support_oppose[["id", "title", "supporter_count", "opposer_count", "primary_sponsor"]]

# Define output file paths
legislators_output_path = "legislators-support-oppose-count.csv"
bills_output_path_corrected = "bills-support-oppose-count.csv"

# Save DataFrames to CSV files
legislator_support_oppose.to_csv(legislators_output_path, index=False)
bills_support_oppose.to_csv(bills_output_path_corrected, index=False)