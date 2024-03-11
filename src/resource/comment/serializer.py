
def view_commnet_serializer(comment_data):
    if not isinstance(comment_data,list):
        comment_data=[comment_data]

    extra_data=[]

    for record in comment_data:
        extra_data.append(
            {
                "id":record.id,
                "post_id":record.post_id,
                "comment" :record.comment,
                
                
            }
        )
        
    return extra_data

