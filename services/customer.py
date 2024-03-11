from fastapi import HTTPException,status


from schema.customer import customers, CustomerCreate, Customer

#Dependency class injected into customer creation
class CustomerService:
# Create a dependency that checks that a username is not in the system when creating a customer. (Usernames should be unique)
    @staticmethod
    def is_username_unique(payload : CustomerCreate):
        # return all(customer.username != username for customer in customers)
        for customer in customers:
            if  customer.username == payload.username:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Customer with username {payload.username} already exists")
        return payload
   
            
        
customer_service = CustomerService()
         



            
           