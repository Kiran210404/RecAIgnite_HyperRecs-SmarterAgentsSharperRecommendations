from models.collaborative_filter import recommend_collaborative
from models.content_filter import recommend_content

class RecommendationAgent:
    def __init__(self):
        pass

    def get_recommendations(self, user_id, method="hybrid"):
        if method == "collaborative":
            return recommend_collaborative(user_id)
        elif method == "content":
            return recommend_content(user_id)
        else:
            collab = recommend_collaborative(user_id)
            content = recommend_content(user_id)
            return list(set(collab + content))
