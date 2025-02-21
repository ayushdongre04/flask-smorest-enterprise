# This file contains utility functions (e.g., formatting API responses).
def format_response(data, status_code=200, message="Success"):
    """Helper function to format API responses."""
    return {"status": status_code, "message": message, "data": data}, status_code
