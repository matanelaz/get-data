
def convert_to_csv(df):
    rows = []
    for record in df.values.tolist():
        row = ",".join(record)
        rows.append(row)
    return rows


