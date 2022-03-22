"""Row-oriented vs. Column-oriented Data Structure Compositions."""

row_data: list[dict[str, str]] = [
    {"name": "UNC", "city": "Chapel Hill"}, 
    {"name": "Duke", "city": "Durham"}
]

col_data: dict[str, list[str]] = {
    "name": ["UNC", "Duke"],
    "city": ["Chapel Hill", "Durham"]
}

print(col_data["city"][1])