from agents.customer_agent import CustomerAgent
from agents.product_agent import ProductAgent
from agents.recommendation_agent import RecommendationAgent

user_id = "user_1"

customer = CustomerAgent(user_id)
product = ProductAgent()
recommender = RecommendationAgent()

prefs = customer.get_preferences()
print(f"[Main] Current preferences: {prefs}")

recommendations = recommender.get_recommendations(user_id)
print(f"[Main] Final Recommendations: {recommendations}")
