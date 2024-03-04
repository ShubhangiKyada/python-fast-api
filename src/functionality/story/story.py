from database.database import Sessionlocal
from src.resource.story.model import Story
from fastapi.responses import JSONResponse


db = Sessionlocal()

def create_story(story_details,user_data):
    
    story_info = Story(
        photo = story_details.get("Photo"),
        user_id=user_data,
    )
    db.add(story_info)
    db.commit()
    db.close()

    return JSONResponse({"Message":"Story created"},status_code=201)


