def serializer_for_getpost(post_data,comment_data,like_data):
    if not isinstance(post_data, list):
        post_data = [post_data]

    if not isinstance(like_data,list):
        like_data = [like_data]
        
    if not isinstance(comment_data,list):
        comment_data = [comment_data]
       
    filter_data=[]


    
    for record in post_data:
        post_info={
            "photo": record.photo,
            "user_id": record.user_id,
            "description": record.description,
            "locations": record.location,
            "likes": 0,
            "comments": [],
        }

        for comment in comment_data:
            if comment.post_id==record.id:
                post_info["comments"].append(comment.comment)

        for like in like_data:
            if  like.post_id == record.id :
                post_info['likes'].append(like.count)

            
    return filter_data












