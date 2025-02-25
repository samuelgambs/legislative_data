# Coding Challenge - Legislative Data

This project implements a Python script to process legislative data provided in CSV files. It generates two reports:
1. **legislators-support-oppose-count.csv** – Count of bills each legislator supported or opposed.
2. **bills-support-oppose-count.csv** – Count of votes for and against each bill, along with the primary sponsor.

## 📂 Project Structure
```
📁 quorum-legislative-challenge
│️글 main.py                   # Main script for data processing
│️글 requirements.txt          # Project dependencies
│️글 bills.csv                 # Bills dataset
│️글 legislators.csv           # Legislators dataset
│️글 votes.csv                 # Votes dataset
│️글 vote_results.csv          # Vote results dataset
│️글 legislators-support-oppose-count.csv  # Output file
│️글 bills-support-oppose-count.csv        # Output file
│️글 README.md                 # Project documentation
```

---

## 🚀 How to Run the Project
### 1⃣ Create a Virtual Environment
It is recommended to use `uv` for a faster and more efficient Python environment:
```sh
uv venv .venv && source .venv/bin/activate
```
Alternatively, using `venv`:
```sh
python -m venv .venv && source .venv/bin/activate
```
On Windows:
```sh
.venv\Scripts\activate
```

### 2⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3⃣ Run the Script
```sh
python main.py
```
The output files will be generated in the root directory.

---

## 📊 Implementation Details
The script follows these steps:
1. **Loads the CSV files**: `bills.csv`, `legislators.csv`, `votes.csv`, and `vote_results.csv`.
2. **Processes legislators' votes**:
   - Counts how many bills each legislator supported (`yea`) or opposed (`nay`).
   - Generates the `legislators-support-oppose-count.csv` file.
3. **Processes votes for each bill**:
   - Counts how many legislators voted for or against each bill.
   - Associates the bill with its primary sponsor.
   - Generates the `bills-support-oppose-count.csv` file.

---

## ⏳ Complexity & Technical Decisions
- **Efficient data processing** using Pandas, leveraging `groupby()` and `merge()`.
- **Time Complexity**:
  - **Loading CSVs**: O(n), where n is the total number of rows across all CSV files.
  - **Creating dictionaries**: O(m), where m is the number of legislators or votes.
  - **Grouping and unstacking**: Generally efficient, approaching O(n) in the worst case, where n is the number of rows in `vote_results.csv`.
  - **Merging dataframes**: O(n + m), where n and m are the sizes of the dataframes.
  - **Mapping columns**: O(n), where n is the number of rows in the dataframe.
- **Scalability**: The code can be easily modified to include new fields such as "vote date" or "co-sponsors".
- **Error Handling**: The script includes checks to prevent `KeyError` and handle missing columns.

---

## 🛠️ Possible Improvements
- Implement automated tests to validate CSV outputs.
- Add logging for better debugging and tracking.
- Create a web interface for file uploads and report generation.

---

