from src.finance import read_finance_csv_operation, read_finance_excel_operation

if __name__ == "__main__":
    csv_data = read_finance_csv_operation("data/transactions.csv")
    excel_data = read_finance_excel_operation("data/transactions_excel.xlsx")
    print(csv_data)
    print(excel_data)
