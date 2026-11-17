"""Task 1: Robust hostel mess-bill file processor."""
from pathlib import Path
import csv

def process_mess_file(filename):
    """Read CSV-like register,name,amount records and return total and rejected rows."""
    total = 0.0
    accepted = []
    rejected = []

    try:
        with open(filename, "r", encoding="utf-8", newline="") as source:
            for line_number, raw_line in enumerate(source, start=1):
                if not raw_line.strip():
                    continue
                try:
                    fields = next(csv.reader([raw_line]))
                    if len(fields) != 3:
                        raise ValueError(f"expected 3 fields, found {len(fields)}")
                    register, name, amount_text = (field.strip() for field in fields)
                    if not register or not name:
                        raise ValueError("register number and name must not be empty")
                    amount = float(amount_text)
                    if amount < 0:
                        raise ValueError("amount cannot be negative")
                    total += amount
                    accepted.append((register, name, amount))
                except (ValueError, csv.Error) as error:
                    rejected.append((line_number, raw_line.rstrip("\n"), str(error)))
    except FileNotFoundError:
        raise
    except PermissionError:
        raise

    report_lines = ["Register Number | Name | Amount"]
    report_lines.extend(f"{reg} | {name} | {amount:.2f}" for reg, name, amount in accepted)
    report_lines.append(f"TOTAL | | {total:.2f}")
    report_lines.append(f"Rejected records: {len(rejected)}")
    return total, accepted, rejected, "\n".join(report_lines) + "\n"

def main():
    input_file = Path(__file__).with_name("mess_oct.txt")
    try:
        total, accepted, rejected, report = process_mess_file(input_file)
        output_file = Path(__file__).with_name("mess_report.txt")
        output_file.write_text(report, encoding="utf-8")
        print(report, end="")
        if rejected:
            print("Rejected rows:")
            for line_no, line, reason in rejected:
                print(f"Line {line_no}: {line!r} — {reason}")
    except FileNotFoundError:
        print(f"ERROR: input file not found: {input_file}")
    except PermissionError:
        print(f"ERROR: permission denied while reading {input_file}")

if __name__ == "__main__":
    main()
