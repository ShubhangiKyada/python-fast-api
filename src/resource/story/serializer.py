def serializer_for_getstory(story_data,):
    if not isinstance(story_data, list):
        story_data = [story_data]
    
    filter_data=[]
    
    for record in story_data:
        filter_data.append(
            {
                "photo": record.photo,
                "user_id": record.user_id,
            }
        )
    return filter_data