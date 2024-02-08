
def serializer_use(users_data):
    if not isinstance(users_data,list):
        users_data=[users_data]


    extra_data=[]


    for record in users_data:
        extra_data.append(
            {
                "fname":record.first_name,
                "lname" :record.last_name,
                "name":record.name,
                "email":record.email,
                "phone_no":record.phone_no,
                "active":record.is_active,
                "verify":record.is_verify,
                
            }
        )
        
    return extra_data