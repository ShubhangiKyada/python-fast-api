from database.database import Sessionlocal
from src.resource.story.model import Story
from fastapi.responses import JSONResponse
from datetime import datetime,timedelta
from src.resource.story.serializer import serializer_for_getstory
from fastapi import HTTPException
import uuid

db = Sessionlocal()


def create_story(story_details, user_data):
    id=uuid.uuid4()
    story_info = Story(
        id=id,
        photo=story_details.get("photo"),
        user_id=user_data,
    )
    db.add(story_info)
    db.commit()
    db.close()

    return JSONResponse({"Message": "Story created"})


def view_story(user_id):
    current_time = datetime.utcnow()
    story_data = db.query(Story).filter_by(user_id=user_id).all()
    story_list=[]
    if story_data:
        for story in  story_data:
            if current_time <= (story.created_at + timedelta(hours=24)):
                filter_data = serializer_for_getstory(story)
                story_list.append(filter_data)
            return JSONResponse({"Story": filter_data})
        else:
            raise HTTPException(status_code=404, detail="Story is now unavailable")
    else:
        raise HTTPException(status_code=404, detail="Story not found")
