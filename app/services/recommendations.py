def generate_recommendations(user_data):
    # Rule-based example
    recs = []
    if user_data["total_spending"] > user_data["income"]:
        recs.append("You're spending more than you earn. Consider setting up a strict monthly budget.")
    if user_data["category_spending"]["entertainment"] > 0.15 * user_data["income"]:
        recs.append("Cut back on entertainment to improve savings.")
    return recs
